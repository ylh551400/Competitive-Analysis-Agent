"""Agent definitions for the competitive analysis system."""

from pathlib import Path

from claude_agent_sdk import AgentDefinition

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"


def _load_prompt(name: str) -> str:
    return (PROMPTS_DIR / f"{name}.md").read_text(encoding="utf-8")


def create_web_researcher() -> AgentDefinition:
    return AgentDefinition(
        description=(
            "Researches company websites, news, funding, pricing, "
            "and product features via web search."
        ),
        prompt=_load_prompt("web_researcher"),
        tools=["WebSearch", "WebFetch", "Read", "Write", "Glob"],
        model="sonnet",
    )


def create_review_analyzer() -> AgentDefinition:
    return AgentDefinition(
        description=(
            "Analyzes user reviews from G2, Capterra, Reddit "
            "to extract pain points and sentiment."
        ),
        prompt=_load_prompt("review_analyzer"),
        tools=["WebSearch", "WebFetch", "Read", "Write", "Glob"],
        model="sonnet",
    )


def create_hiring_analyzer() -> AgentDefinition:
    return AgentDefinition(
        description=(
            "Analyzes job postings to infer strategic direction "
            "and investment areas."
        ),
        prompt=_load_prompt("hiring_analyzer"),
        tools=["WebSearch", "WebFetch", "Read", "Write", "Glob"],
        model="sonnet",
    )


def create_synthesizer() -> AgentDefinition:
    return AgentDefinition(
        description=(
            "Synthesizes all research findings into a structured "
            "competitive analysis draft report."
        ),
        prompt=_load_prompt("synthesizer"),
        tools=["Read", "Write", "Glob", "Grep"],
        model="sonnet",
    )


def create_evaluator() -> AgentDefinition:
    return AgentDefinition(
        description=(
            "Evaluates the draft report for completeness, specificity, "
            "consistency, and evidence. Returns PASS or FAIL with specific gaps."
        ),
        prompt=_load_prompt("evaluator"),
        tools=["Read", "Glob", "Grep"],
        model="sonnet",
    )


def get_all_agents() -> dict[str, AgentDefinition]:
    """Return all subagent definitions keyed by agent name."""
    return {
        "web-researcher": create_web_researcher(),
        "review-analyzer": create_review_analyzer(),
        "hiring-analyzer": create_hiring_analyzer(),
        "synthesizer": create_synthesizer(),
        "evaluator": create_evaluator(),
    }
