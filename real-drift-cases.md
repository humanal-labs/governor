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
---
## Case 004 — Session continuity silently lost after restart

### Source
OpenHands issue:
"ACP: conversations cannot be resumed after sandbox restart (session_id is not persisted)"

### Drift Pattern
The system appears operational after restart, but conversational continuity is silently broken because session identity is lost.

### Human Observation
The user likely notices only after attempting to continue work. The interface still appears alive, but historical context and continuity are gone.

### What Created False Confidence?
The restart succeeds technically, creating the illusion of recovery, while hidden conversational state was never restored.

### Potential Signals
- sudden context discontinuity
- missing session linkage
- reset conversation identity
- successful restart without continuity validation

### Governor Relevance
Governor could require continuity validation checkpoints after recovery events instead of assuming restart success equals operational recovery.

---
## Case 005 — Message silently dropped without visible failure

### Source
OpenHands issue:
"Send button silently drops attachment-only chat messages"

### Drift Pattern
The system accepts user interaction and appears functional, but the actual payload is never processed or delivered.

### Human Observation
The user believes the message was successfully sent because no visible failure occurs. The missing action is only discovered later through absence of response or workflow inconsistency.

### What Created False Confidence?
The interface preserved the illusion of successful execution by failing silently instead of surfacing uncertainty or validation errors.

### Potential Signals
- missing downstream acknowledgment
- no resulting agent activity
- interaction recorded without execution trace
- silent payload discard

### Governor Relevance
Governor could validate execution continuity between user intent and downstream system acknowledgment instead of assuming UI submission equals operational success.
---

## Case 006 — Rejected tool calls still execute despite human review

### Source
LangGraph issue:
"HumanInTheLoopMiddleware executes rejected tool calls in LangGraph's ToolNode"

### Drift Pattern
The system presents a human approval/rejection checkpoint, but rejected actions may still execute downstream, breaking the integrity of the review process.

### Human Observation
The operator believes intervention successfully stopped execution. The mismatch may only become visible later through unexpected side effects or downstream behavior.

### What Created False Confidence?
The interface and workflow implied that human rejection was authoritative, while execution state diverged internally.

### Potential Signals
- rejected actions appearing in execution logs
- mismatch between approval state and execution trace
- downstream side effects after rejection
- inconsistent review-state synchronization

### Governor Relevance
Governor could validate execution integrity after review checkpoints instead of assuming human intervention automatically propagates through operational state.

Add human observation patterns to drift cases
