# Operational Drift Taxonomy

Operational drift occurs when systems appear locally functional while systemic operational integrity degrades over time.

The goal is not to detect visible failure.

The goal is to identify:
- ambiguity
- hidden non-progress
- incoherent system state
- false operational confidence

---

## 1. Silent Failure Drift
System stops progressing without explicit failure.

Example:
- active session
- no execution progress
- no terminal state

Related:
Case 012

---

## 2. Semantic Drift
Execution continues while operational meaning collapses.

Example:
- empty tool arguments
- successful execution with null outcome

Related:
Case 007

---

## 3. Governance Drift
Displayed controls diverge from actual enforcement behavior.

Example:
- rejected action still executes
- configured limits ignored

Related:
Case 006
Case 013

---

## 4. Observability Drift
Monitoring layers diverge from execution reality.

Example:
- healthy dashboard
- stalled execution layer

Related:
Case 010

---

## 5. Recursive Drift
Recovery or retry mechanisms reinforce instability.

Example:
- restart loops
- self-calling deadlocks
- retry storms

Related:
Case 001
Case 002
Case 003
Case 009

---

## 6. State Desynchronization
Different system layers report contradictory realities.

Example:
- frontend STARTING
- backend IDLE
- task READY

Related:
Case 011

---

## 7. Recovery Drift
Recovery mechanisms create secondary operational instability.

Example:
- restart succeeds
- continuity silently lost

Related:
Case 004
