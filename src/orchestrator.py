"""Core orchestration logic for the competitive analysis agent."""

import io
import os
import sys
from pathlib import Path

# Allow running inside a Claude Code session (unset nesting guard)
os.environ.pop("CLAUDECODE", None)

# Ensure UTF-8 stderr for SDK subprocess output on Windows
if sys.platform == "win32" and hasattr(sys.stderr, "buffer"):
    sys.stderr = io.TextIOWrapper(
        sys.stderr.buffer, encoding="utf-8", errors="replace"
    )

from claude_agent_sdk import query, ClaudeAgentOptions, HookMatcher

from .agents import get_all_agents
from .logger import MarkdownLogger

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"
PROJECT_ROOT = Path(__file__).parent.parent


def _load_main_prompt() -> str:
    return (PROMPTS_DIR / "main_agent.md").read_text(encoding="utf-8")


async def run_analysis(user_question: str, model: str = "sonnet") -> str:
    """Run the full competitive analysis pipeline.

    Args:
        user_question: The user's business decision question.
        model: Model to use for the main orchestrator agent.

    Returns:
        Path to the generated report.
    """
    # Setup
    logger = MarkdownLogger(str(PROJECT_ROOT / "logs" / "execution_log.md"))
    agents = get_all_agents()

    # Ensure output directories exist
    (PROJECT_ROOT / "outputs").mkdir(parents=True, exist_ok=True)
    (PROJECT_ROOT / "research_notes").mkdir(parents=True, exist_ok=True)

    logger.log_agent_start(
        agent_name="Main Orchestrator",
        task=user_question,
        context="Starting competitive analysis",
    )

    # Build the orchestration prompt
    main_prompt = _load_main_prompt()
    full_prompt = f"""{main_prompt}

---

## User's Business Question

{user_question}

---

## Execution Instructions

You are now running. Follow your workflow:

1. Analyze the question and identify 2-5 competitors.
2. Delegate research to subagents (web-researcher, review-analyzer, hiring-analyzer) — run them in parallel.
   - Give each subagent a clear prompt specifying which companies to research.
   - Subagents will save findings to `research_notes/` directory.
3. After research completes, delegate to the synthesizer to create `outputs/draft_report.md`.
4. Delegate to the evaluator to check the draft.
5. If FAIL: re-delegate to fill gaps. Max 3 retries.
6. Copy/rename the final draft to `outputs/report.md`.

Start now.
"""

    report_path = str(PROJECT_ROOT / "outputs" / "report.md")

    # Run the main agent
    result_text = ""
    async for message in query(
        prompt=full_prompt,
        options=ClaudeAgentOptions(
            model=model,
            tools=[
                "Read", "Write", "Glob", "Grep",
                "WebSearch", "WebFetch", "Agent", "Bash",
            ],
            permission_mode="bypassPermissions",
            agents=agents,
            cwd=str(PROJECT_ROOT),
            max_turns=80,
            debug_stderr=sys.stderr,
        ),
    ):
        # Stream progress
        if hasattr(message, "content"):
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)
                    result_text += block.text
        if hasattr(message, "result"):
            result_text = str(message.result)
            print(f"\n{'='*60}")
            print("Analysis complete.")
            print(f"{'='*60}")

    logger.log_final(f"Report generated at: {report_path}")

    return report_path
