# Competitive Analysis Agent

A multi-agent competitive analysis tool built with Claude Agent SDK. Give it a business decision question, and it automatically researches competitors, analyzes reviews, infers strategic direction from hiring data, and produces a structured report with built-in quality control.

## Why I Built This

Competitive analysis is a routine task for PMs and analysts, but doing it manually is painful: scanning websites, reading G2 reviews, checking news, analyzing job postings—half a day per company, a day and a half for three.

Existing AI tools can help with search, but output quality is inconsistent with no structured verification.

This project explores: **How can multiple AI agents collaborate with quality control to ensure reliable output?**

## What It Does

```
Your question: "We're a project management SaaS startup considering competing 
               with Asana, Monday.com, and ClickUp. Is it worth it?"

↓ Automated execution

1. Main Agent decomposes the task
2. Three Subagents research in parallel (websites, reviews, hiring)
3. Synthesizer compiles draft report
4. Evaluator checks quality (rejects and re-researches if insufficient)
5. Outputs final report
```

## Example Output

Running the question above produced a 2000+ word analysis report containing:

- **Market Overview** — Positioning, revenue scale, funding status for all three
- **Competitor Comparison** — Pricing, features, target customer comparison tables
- **User Pain Points** — Real issues extracted from G2/Capterra reviews
- **Strategic Direction** — Investment priorities inferred from hiring patterns
- **Entry Recommendation** — Focus on agency/professional services vertical, price at $18-22/user/mo

Key findings:
> "All three lack native project budgeting and resource management—a genuine gap"
> 
> "The SMB segment is being actively abandoned—all three are pricing toward enterprise"

Full report: [`outputs/report.md`](outputs/report.md)

## Architecture

<img width="600" height="700" alt="Image" src="https://github.com/user-attachments/assets/67043e10-9652-49e5-80a5-36bc20afa376" />

## Quality Control

This is the core design element of the project.

The Evaluator checks every report against:

| Check | Standard |
|-------|----------|
| Completeness | All dimensions covered for each competitor |
| Specificity | No vague claims like "targets enterprises"—concrete data required |
| Consistency | No contradictions across sections |
| Evidence | Every conclusion traces back to specific findings |

Failed checks trigger targeted re-research, up to 3 retries. After that, gaps are flagged and output continues.

## Tech Stack

- **Claude Agent SDK** — Multi-agent orchestration
- **Claude Sonnet** — Balance of quality and cost
- **Python asyncio** — Parallel subagent execution
- **Structured Logging** — Step-by-step logs for debugging

## Design Decisions

**Why multi-agent instead of one big prompt?**

Single prompts struggle with:
- Complex search tasks—longer queries yield worse results
- No quality gate—output quality is luck-dependent
- Debugging—no visibility into which step failed

**Why Claude Agent SDK instead of LangGraph?**

- Project complexity is moderate—explicit code-level routing not needed
- Structured logging addresses debugging needs

**Why is the Evaluator a separate agent?**

Separation of concerns—the writer and reviewer are different agents to avoid "grading your own homework."

## Setup

```bash
# Clone
git clone https://github.com/ylh551400/competitive-analysis-agent.git
cd competitive-analysis-agent

# Install
python -m venv .venv
source .venv/bin/activate
pip install -e .

# Configure
cp .env.example .env
# Add your ANTHROPIC_API_KEY

# Run
python -m src.main "Your business question here"
```

## Limitations & Future Work

**Current limitations:**
- Public information only—paid data sources (market share, detailed revenue) not accessible
- No persistence—re-researches from scratch each run
- English sources work better than others

**Potential extensions:**
- Follow-up questions: Ask questions about the report, trigger targeted re-research
- Verticalization: Custom analysis frameworks for SaaS, fintech, etc.
- More data sources: Crunchbase API, LinkedIn integration

 
 
