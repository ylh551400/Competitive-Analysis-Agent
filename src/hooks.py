"""Execution hooks for structured logging of agent activity."""

from claude_agent_sdk.types import (
    HookContext,
    PreToolUseHookInput,
    PostToolUseHookInput,
)

from .logger import MarkdownLogger


class AgentTracker:
    """Tracks agent execution and logs structured output."""

    def __init__(self, logger: MarkdownLogger):
        self.logger = logger
        self._agent_names: dict[str, str] = {}

    async def pre_tool_use(
        self,
        hook_input: PreToolUseHookInput,
        session_id: str | None,
        context: HookContext,
    ) -> dict:
        tool_name = hook_input.get("tool_name", "unknown")
        tool_params = hook_input.get("tool_input", {})
        tool_use_id = hook_input.get("tool_use_id", "")
        agent_type = hook_input.get("agent_type", "main")

        if tool_name == "Agent":
            description = tool_params.get("description", "")
            prompt_preview = tool_params.get("prompt", "")[:200]
            self._agent_names[tool_use_id] = description
            self.logger.log_agent_start(
                agent_name=description or "Subagent",
                task=description,
                context=prompt_preview,
            )
        elif tool_name in ("WebSearch", "WebFetch"):
            agent_name = self._agent_names.get(agent_type, agent_type)
            query = tool_params.get("query", tool_params.get("url", ""))
            self.logger.log_agent_action(
                agent_name=agent_name,
                understanding=f"Using {tool_name}",
                action=str(query)[:300],
            )

        return {}

    async def post_tool_use(
        self,
        hook_input: PostToolUseHookInput,
        session_id: str | None,
        context: HookContext,
    ) -> dict:
        tool_name = hook_input.get("tool_name", "unknown")
        tool_use_id = hook_input.get("tool_use_id", "")

        if tool_name == "Agent" and tool_use_id in self._agent_names:
            agent_name = self._agent_names[tool_use_id]
            result = hook_input.get("tool_response", "")
            result_preview = str(result)[:500] if result else "Completed"
            self.logger.log_agent_result(
                agent_name=agent_name,
                result=result_preview,
            )

        return {}
