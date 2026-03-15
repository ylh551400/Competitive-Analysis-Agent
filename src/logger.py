"""Structured markdown logger for agent execution tracking."""

import threading
from datetime import datetime
from pathlib import Path


class MarkdownLogger:
    """Writes structured execution logs to a markdown file."""

    def __init__(self, log_path: str = "logs/execution_log.md"):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._init_log()

    def _init_log(self):
        with self._lock:
            with open(self.log_path, "w", encoding="utf-8") as f:
                f.write("# Execution Log\n\n")
                f.write(f"Started: {self._timestamp()}\n\n---\n\n")

    def _timestamp(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _append(self, text: str):
        with self._lock:
            with open(self.log_path, "a", encoding="utf-8") as f:
                f.write(text)

    def log_agent_start(self, agent_name: str, task: str, context: str = ""):
        entry = (
            f"## [{agent_name}] @ {self._timestamp()}\n\n"
            f"### Input\n"
            f"- Task: {task}\n"
        )
        if context:
            entry += f"- Context: {context}\n"
        entry += "\n"
        self._append(entry)

    def log_agent_action(self, agent_name: str, understanding: str, action: str):
        entry = (
            f"### Execution — {agent_name}\n"
            f"- Understanding: {understanding}\n"
            f"- Action: {action}\n\n"
        )
        self._append(entry)

    def log_agent_result(
        self,
        agent_name: str,
        result: str,
        confidence: str = "Medium",
        issues: str = "",
    ):
        entry = (
            f"### Output — {agent_name}\n"
            f"- Result: {result}\n"
            f"- Confidence: {confidence}\n"
        )
        if issues:
            entry += f"- Issues/Gaps: {issues}\n"
        entry += "\n---\n\n"
        self._append(entry)

    def log_evaluation(self, attempt: int, passed: bool, gaps: str = ""):
        status = "PASS" if passed else "FAIL"
        entry = (
            f"## [Evaluator] Attempt {attempt} @ {self._timestamp()}\n\n"
            f"- Result: {status}\n"
        )
        if gaps:
            entry += f"- Missing information: {gaps}\n"
        entry += "\n---\n\n"
        self._append(entry)

    def log_final(self, message: str):
        entry = (
            f"## Final Result @ {self._timestamp()}\n\n"
            f"{message}\n\n"
            f"---\n"
        )
        self._append(entry)
