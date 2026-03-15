"""CLI entry point for the competitive analysis agent."""

import argparse
import asyncio
import io
import sys

from dotenv import load_dotenv

# Fix Windows terminal encoding for emoji/unicode output
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding="utf-8", errors="replace"
    )
    sys.stderr = io.TextIOWrapper(
        sys.stderr.buffer, encoding="utf-8", errors="replace"
    )


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Competitive Analysis Agent — AI-powered competitive intelligence"
    )
    parser.add_argument(
        "question",
        nargs="?",
        help="Your business decision question (e.g., 'We are a project management SaaS, should we compete with Asana and Monday.com?')",
    )
    parser.add_argument(
        "--model",
        default="sonnet",
        choices=["sonnet", "opus", "haiku"],
        help="Model for the main orchestrator (default: sonnet)",
    )
    args = parser.parse_args()

    question = args.question
    if not question:
        print("Competitive Analysis Agent")
        print("=" * 40)
        print()
        question = input("Enter your business decision question:\n> ").strip()
        if not question:
            print("No question provided. Exiting.")
            sys.exit(1)

    print()
    print(f"Starting analysis for: {question}")
    print(f"Model: {args.model}")
    print("=" * 60)
    print()

    from .orchestrator import run_analysis

    report_path = asyncio.run(run_analysis(question, model=args.model))

    print()
    print(f"Report saved to: {report_path}")
    print(f"Execution log: logs/execution_log.md")


if __name__ == "__main__":
    main()
