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



<svg width="100%" viewBox="0 0 680 680" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
<mask id="imagine-text-gaps-wqe5u7" maskUnits="userSpaceOnUse"><rect x="0" y="0" width="680" height="680" fill="white"/><rect x="289.6455993652344" y="31.31915283203125" width="100.70877838134766" height="21.36170196533203" fill="black" rx="2"/><rect x="298.96319580078125" y="111.31915283203125" width="82.07357788085938" height="21.3616943359375" fill="black" rx="2"/><rect x="252.47695922851562" y="132.5248260498047" width="174.94715881347656" height="18.95035457611084" fill="black" rx="2"/><rect x="72" y="212.5248260498047" width="126.11835479736328" height="18.95035457611084" fill="black" rx="2"/><rect x="106.89384460449219" y="253.3191680908203" width="114.24662780761719" height="21.36170196533203" fill="black" rx="2"/><rect x="116.05696105957031" y="274.52484130859375" width="95.88607788085938" height="18.95035457611084" fill="black" rx="2"/><rect x="123.33245086669922" y="290.5248107910156" width="81.52540588378906" height="18.95035457611084" fill="black" rx="2"/><rect x="286.2420349121094" y="253.3191680908203" width="115.54818725585938" height="21.36170196533203" fill="black" rx="2"/><rect x="310.1482849121094" y="274.52484130859375" width="67.98376846313477" height="18.95035457611084" fill="black" rx="2"/><rect x="290.0662536621094" y="290.5248107910156" width="107.86746215820312" height="18.95035457611084" fill="black" rx="2"/><rect x="470.4731750488281" y="253.3191680908203" width="107.08795166015625" height="21.36170196533203" fill="black" rx="2"/><rect x="484.11236572265625" y="274.52484130859375" width="79.7752685546875" height="18.95035457611084" fill="black" rx="2"/><rect x="486.8025207519531" y="290.5248107910156" width="74.39494323730469" height="18.95035457611084" fill="black" rx="2"/><rect x="296.6648864746094" y="411.31915283203125" width="86.70355987548828" height="21.36170196533203" fill="black" rx="2"/><rect x="301.9510192871094" y="432.52484130859375" width="76.3769760131836" height="18.95035457611084" fill="black" rx="2"/><rect x="304.5733642578125" y="511.3192138671875" width="70.88168334960938" height="21.36170196533203" fill="black" rx="2"/><rect x="296.9700622558594" y="532.5248413085938" width="86.0598373413086" height="18.95035457611084" fill="black" rx="2"/><rect x="261.23870849609375" y="577.9432373046875" width="33.522605895996094" height="18.95035457611084" fill="black" rx="2"/><rect x="297.2978820800781" y="631.3191528320312" width="85.40425109863281" height="21.36170196533203" fill="black" rx="2"/><rect x="432.3357849121094" y="557.9432373046875" width="163.32846069335938" height="18.95035457611084" fill="black" rx="2"/><rect x="524.9064331054688" y="245.94326782226562" width="91.0935287475586" height="18.95035457611084" fill="black" rx="2"/></mask></defs>

<!-- User Question -->
<g style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
  <rect x="240" y="20" width="200" height="44" rx="8" stroke-width="0.5" style="fill:rgb(68, 68, 65);stroke:rgb(180, 178, 169);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="340" y="42" text-anchor="middle" dominant-baseline="central" style="fill:rgb(211, 209, 199);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">User question</text>
</g>

<!-- Arrow: User → Main Agent -->
<line x1="340" y1="64" x2="340" y2="104" marker-end="url(#arrow)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

<!-- Main Agent -->
<g style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
  <rect x="200" y="104" width="280" height="56" rx="8" stroke-width="0.5" style="fill:rgb(60, 52, 137);stroke:rgb(175, 169, 236);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="340" y="122" text-anchor="middle" dominant-baseline="central" style="fill:rgb(206, 203, 246);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Main agent</text>
  <text x="340" y="142" text-anchor="middle" dominant-baseline="central" style="fill:rgb(175, 169, 236);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Task decomposition &amp; routing</text>
</g>

<!-- Arrow: Main Agent → Subagents -->
<line x1="340" y1="160" x2="340" y2="204" marker-end="url(#arrow)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

<!-- Subagents container -->
<rect x="60" y="204" width="560" height="156" rx="12" fill="none" stroke="var(--color-border-secondary)" stroke-width="1" stroke-dasharray="5 4" style="fill:none;stroke:rgba(222, 220, 209, 0.3);color:rgb(255, 255, 255);stroke-width:1px;stroke-dasharray:5px, 4px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
<text x="76" y="222" dominant-baseline="central" style="fill:var(--color-text-secondary);fill:rgb(194, 192, 182);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:start;dominant-baseline:central">Subagents — parallel</text>

<!-- Web Researcher -->
<g style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
  <rect x="84" y="232" width="160" height="104" rx="8" stroke-width="0.5" style="fill:rgb(8, 80, 65);stroke:rgb(93, 202, 165);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="164" y="264" text-anchor="middle" dominant-baseline="central" style="fill:rgb(159, 225, 203);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Web researcher</text>
  <text x="164" y="284" text-anchor="middle" dominant-baseline="central" style="fill:rgb(93, 202, 165);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Websites, news</text>
  <text x="164" y="300" text-anchor="middle" dominant-baseline="central" style="fill:rgb(93, 202, 165);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Funding data</text>
</g>

<!-- Review Analyzer -->
<g style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
  <rect x="264" y="232" width="160" height="104" rx="8" stroke-width="0.5" style="fill:rgb(8, 80, 65);stroke:rgb(93, 202, 165);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="344" y="264" text-anchor="middle" dominant-baseline="central" style="fill:rgb(159, 225, 203);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Review analyzer</text>
  <text x="344" y="284" text-anchor="middle" dominant-baseline="central" style="fill:rgb(93, 202, 165);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">G2, Reddit</text>
  <text x="344" y="300" text-anchor="middle" dominant-baseline="central" style="fill:rgb(93, 202, 165);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Sentiment signals</text>
</g>

<!-- Hiring Analyzer -->
<g style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
  <rect x="444" y="232" width="160" height="104" rx="8" stroke-width="0.5" style="fill:rgb(8, 80, 65);stroke:rgb(93, 202, 165);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="524" y="264" text-anchor="middle" dominant-baseline="central" style="fill:rgb(159, 225, 203);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Hiring analyzer</text>
  <text x="524" y="284" text-anchor="middle" dominant-baseline="central" style="fill:rgb(93, 202, 165);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Job postings</text>
  <text x="524" y="300" text-anchor="middle" dominant-baseline="central" style="fill:rgb(93, 202, 165);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Role signals</text>
</g>

<!-- Arrow: Subagents → Synthesizer -->
<line x1="340" y1="360" x2="340" y2="404" marker-end="url(#arrow)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

<!-- Synthesizer -->
<g style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
  <rect x="200" y="404" width="280" height="56" rx="8" stroke-width="0.5" style="fill:rgb(113, 43, 19);stroke:rgb(240, 153, 123);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="340" y="422" text-anchor="middle" dominant-baseline="central" style="fill:rgb(245, 196, 179);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Synthesizer</text>
  <text x="340" y="442" text-anchor="middle" dominant-baseline="central" style="fill:rgb(240, 153, 123);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Draft report</text>
</g>

<!-- Arrow: Synthesizer → Evaluator -->
<line x1="340" y1="460" x2="340" y2="504" marker-end="url(#arrow)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

<!-- Evaluator -->
<g style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
  <rect x="200" y="504" width="280" height="56" rx="8" stroke-width="0.5" style="fill:rgb(99, 56, 6);stroke:rgb(239, 159, 39);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="340" y="522" text-anchor="middle" dominant-baseline="central" style="fill:rgb(250, 199, 117);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Evaluator</text>
  <text x="340" y="542" text-anchor="middle" dominant-baseline="central" style="fill:rgb(239, 159, 39);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Quality check</text>
</g>

<!-- PASS arrow → Final Report -->
<line x1="290" y1="560" x2="290" y2="620" marker-end="url(#arrow)" mask="url(#imagine-text-gaps-wqe5u7)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
<text x="278" y="592" text-anchor="middle" style="fill:var(--color-text-success);fill:rgb(122, 185, 72);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">Pass</text>

<!-- Final Report -->
<g style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
  <rect x="200" y="620" width="280" height="44" rx="8" stroke-width="0.5" style="fill:rgb(68, 68, 65);stroke:rgb(180, 178, 169);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="340" y="642" text-anchor="middle" dominant-baseline="central" style="fill:rgb(211, 209, 199);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Final report</text>
</g>

<!-- FAIL loop back to subagents -->
<path d="M 390 560 L 390 580 L 620 580 L 620 280 L 608 280" fill="none" stroke="var(--color-border-primary)" stroke-width="1" marker-end="url(#arrow)" style="fill:none;stroke:rgba(222, 220, 209, 0.4);color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
<text x="514" y="572" text-anchor="middle" style="fill:var(--color-text-danger);fill:rgb(238, 136, 132);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">Fail — re-research (max 3×)</text>
<text x="612" y="260" text-anchor="end" style="fill:var(--color-text-secondary);fill:rgb(194, 192, 182);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:end;dominant-baseline:auto">Identifies gaps</text>

</svg>
```
User Question
      │
      ▼
┌─────────────┐
│ Main Agent  │  Task decomposition & routing
└──────┬──────┘
       │
       ▼
┌──────────────────────────────────┐
│       Subagents (parallel)       │
├──────────────────────────────────┤
│ • Web Researcher — websites,    │
│   news, funding                 │
│ • Review Analyzer — G2, Reddit  │
│ • Hiring Analyzer — job posts   │
└──────────┬───────────────────────┘
           │
           ▼
    ┌─────────────┐
    │ Synthesizer │  Draft report
    └──────┬──────┘
           │
           ▼
    ┌─────────────┐
    │  Evaluator  │  Quality check
    └──────┬──────┘
           │
     PASS ─┼─ FAIL → identifies gaps → re-research (max 3x)
           │
           ▼
     Final Report
```

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
git clone https://github.com/[your-username]/competitive-analysis-agent.git
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

## About Me

[LinkedIn](https://www.linkedin.com/in/lyuhuan-y/)

 
