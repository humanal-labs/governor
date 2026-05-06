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

---
## Case 007 — Tool execution continues after semantic intent collapse

### Source
Issue:
"_parse_native_tool_call drops Bedrock Converse API tool arguments — always passes empty dict"

### Drift Pattern
The system continues executing tool calls even though the original operational intent has been silently lost during argument parsing.

### Human Observation
The operator sees successful execution traces and active tool usage, but downstream results appear incomplete, inconsistent, or meaningless.

### What Created False Confidence?
Execution activity remained visible, creating the illusion that operational intent survived intact despite silent argument collapse.

### Potential Signals
- empty tool payloads
- execution traces without semantic effect
- successful tool invocation with null operational outcome
- mismatch between requested action and downstream state

### Governor Relevance
Governor could validate semantic continuity between intended action and executable payload instead of assuming successful invocation preserves operational meaning.

---
## Case 008 — Workflow silently executes twice after credentialing error

### Source
n8n issue:
"Credentialing error causing workflow to run twice"

### Drift Pattern
A credential-related fault causes workflow replay or duplicate execution while the system still appears operational.

### Human Observation
The operator may initially see successful workflow completion without realizing actions were executed multiple times. Discovery often happens later through duplicated side effects.

### What Created False Confidence?
The workflow completed successfully enough to preserve the illusion of correctness, while hidden execution duplication propagated downstream.

### Potential Signals
- duplicate execution traces
- repeated downstream side effects
- repeated external API actions
- workflow success paired with abnormal execution count

### Governor Relevance
Governor could validate execution uniqueness and replay integrity instead of assuming successful completion implies single execution consistency.
--
## Case 009 — Self-calling workflow enters recursive operational deadlock

### Source
n8n issue:
"Webhook HTTP response blocks on concurrency queue even in onReceived response mode — causes deadlock with self-calling workflows"

### Drift Pattern
The workflow recursively interacts with itself until operational concurrency locks execution into a self-sustaining deadlock state.

### Human Observation
The system appears active and partially responsive, but execution throughput silently collapses. Operators may initially interpret the issue as temporary latency rather than systemic deadlock.

### What Created False Confidence?
Surface activity and partial responsiveness concealed the fact that the workflow had become operationally self-blocking.

### Potential Signals
- growing concurrency queue
- repeated self-references in execution traces
- throughput collapse despite active processes
- increasing execution wait times
- persistent active-state workflows without forward progress

### Governor Relevance
Governor could detect recursive execution dependency patterns and identify throughput collapse before workflows become operationally self-blocking.
---
## Case 010 — System reports healthy while execution layer silently stalls

### Source
n8n issue:
"External task runner: Code nodes time out for hours while /healthz reports healthy, no self-recovery"

### Drift Pattern
Operational health indicators remain positive while the actual execution layer silently degrades into stalled or non-responsive behavior.

### Human Observation
Operators trust monitoring dashboards and health endpoints, delaying intervention because the system appears operational despite execution collapse.

### What Created False Confidence?
Health-check infrastructure validated service availability rather than operational throughput or execution integrity.

### Potential Signals
- healthy status with zero execution throughput
- long-running timeouts
- stalled task queues
- increasing execution latency despite healthy monitoring
- absence of self-recovery behavior

### Governor Relevance
Governor could compare operational throughput against health-state assumptions instead of treating service availability as proof of functional execution integrity.
--
## Case 011 — System layers disagree on operational state

### Source
OpenHands issue:
"Self-hosted UI remains stuck on 'Starting' / 'Loading...' even though app-conversation start task is READY and backend conversation is IDLE"

### Drift Pattern
Different operational layers report contradictory states simultaneously, creating fragmented system reality across the stack.

### Human Observation
Operators receive conflicting signals: the interface implies active initialization while backend systems report idle or ready states. This delays diagnosis because no single layer fully reflects operational reality.

### What Created False Confidence?
Each subsystem appeared internally valid in isolation, masking the fact that overall state synchronization had collapsed.

### Potential Signals
- contradictory subsystem states
- persistent loading indicators
- idle backend with active frontend state
- mismatched orchestration status
- stalled initialization without explicit failure

### Governor Relevance
Governor could validate cross-layer state coherence instead of assuming independently healthy subsystems reflect shared operational reality.

---

## Case 012 — Agent silently stalls without visible failure state

### Source
OpenHands issue:
"Observed Behavior: The agent remains idle. No visual feedback or error notification is shown in the interface."

### Drift Pattern
The agent stops making operational progress without surfacing explicit failure, leaving operators in an ambiguous waiting state.

### Human Observation
The operator sees an apparently active session but receives no indication whether execution is progressing, stalled, or failed.

### What Created False Confidence?
The absence of explicit failure signals preserved the illusion that the agent might still recover or continue autonomously.

### Potential Signals
- prolonged inactivity without terminal state
- no output progression
- idle execution traces
- absent failure notifications
- operator uncertainty about system state

### Governor Relevance
Governor could identify operational inactivity windows and surface ambiguity states instead of allowing silent non-progress to masquerade as temporary execution delay.

--
## Case 013 — Guardrail representation diverges from actual execution behavior

### Source
n8n issue:
"Guardrails node threshold hint contradicts actual node behavior"

### Drift Pattern
Governance or safety-layer representations no longer accurately reflect the real operational behavior of the underlying execution system.

### Human Observation
Operators trust displayed thresholds and guardrail hints, assuming execution boundaries are enforced consistently when actual runtime behavior diverges.

### What Created False Confidence?
The existence of visible governance controls created the impression of reliable enforcement even though operational execution no longer matched the represented policy layer.

### Potential Signals
- mismatch between displayed thresholds and runtime behavior
- unexpected execution despite configured limits
- inconsistent policy enforcement
- divergence between UI governance layer and execution traces

### Governor Relevance
Governor could continuously validate alignment between represented governance constraints and actual runtime execution behavior instead of assuming configuration implies enforcement.

Add human observation patterns to drift cases--

