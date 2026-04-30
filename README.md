# Interruption Layer
Stops risky agent actions before they execute.

```bash
$ python demo.py
[EXECUTED] ls
[EXECUTED] cd /
[INTERRUPTED] Low confidence (0.4) on risky action
[INTERRUPTED] Dangerous SQL detected
Shipped May 1st, 2026. Blocked rm -rf / and DELETE FROM users;.

⸻

What is this?

Agentic systems scale decisions.
Interruption Layers scale judgment.

LLMs don’t know when they’re out of distribution.

Interruption Layer is an external approximation of that missing awareness.

Status: v0.1.1 — Proof of concept. Not production ready.

⸻

What it does

* Blocks low-confidence risky actions
* Detects destructive shell commands (rm -rf /)
* Detects dangerous SQL (DELETE FROM users;)
* Detects repeated action loops

⸻

Why this matters

Agents can act faster than humans can monitor.

Small mistakes become real actions before anyone notices.

This layer introduces a simple pause before execution.

Not smarter agents.
Safer agents.

⸻

Quick start
git clone https://github.com/humanal-labs/interruption-layer
cd interruption-layer
python demo.py
Zero dependencies. Minimal code.

⸻

Limitations

This is a brake prototype, not a complete safety system.

* Confidence scoring is naive
* Rules are hardcoded
* False positives and false negatives are possible
* No human-in-the-loop yet

Do not use in production. Use it to understand the problem.

⸻

Roadmap

* v0.1.1: Shell + SQL demo ✅
* v0.2: Aider / Continue integration
* v1.0: YAML policy rules + human approval

⸻

License

MIT. Fork it. Make it better.
