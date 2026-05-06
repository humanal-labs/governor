# Real Drift Cases

Operational drift patterns observed in public systems, retry loops, and agent workflows.

Goal:
Identify moments where systems appear operationally correct locally, while drifting systemically over time.

---

## Case 001 — Infinite Retry Loop on Permanent I/O Error

Source:
conda/rattler

Issue:
`should_retry()` retries permanent I/O errors, causing infinite retry loops.

Observed Pattern:
- Local logic considers retry "safe"
- System cannot distinguish transient vs permanent failure
- Retry counter keeps execution alive indefinitely
- Operational state appears active while no forward progress exists

Potential Signals:
- repeated identical retries
- no state transition
- latency growth
- unchanged input fingerprint
- retry density spike

Governor Relevance:
System appears alive, but operationally stalled.

Possible Review Point:
Pause execution after repeated unchanged retries without state evolution.

---

## Case 002 — Retry Loop Without Backoff

Source:
ProjectHermes

Issue:
Reconnect loop retries with fixed interval and no exponential backoff.

Observed Pattern:
- failure recovery attempts become tempo-stable
- system increases infrastructure pressure during outage
- retries amplify operational noise

Potential Signals:
- constant retry interval
- rising failure frequency
- tempo rigidity
- infrastructure saturation risk

Governor Relevance:
The system optimizes persistence while degrading stability.

Possible Review Point:
Introduce interruption layer when retry tempo becomes mechanically constant under failure.

---

## Case 003 — Crash Loop Trap

Source:
FidoCanCode/home

Issue:
check=True inside retry loops creates crash-loop traps.

Observed Pattern:
- watchdog restarts preserve failure condition
- restart mechanism reinforces instability
- local recovery logic compounds systemic failure

Potential Signals:
- restart repetition
- identical crash signature
- compressed restart intervals
- repeated execution path

Governor Relevance:
Recovery mechanism becomes the drift source itself.

Possible Review Point:
Escalate to human review after repeated identical crash paths.

Add initial operational drift cases
