 # Governor Drift Taxonomy v0.2

Governor is not a hierarchy of failures.

It is a set of observational lenses for detecting divergence between operational health and actual trustworthiness in autonomous systems.

A drift may appear in any lens first.

A drift may remain isolated.

A drift may propagate across lenses.

---

## Research Question

Can a system remain operationally healthy while becoming progressively less trustworthy?

---

## Core Principle

```text
Observable Health
≠
Actual Trustworthiness
 Operational health is not a truth signal.

It is only a set of observable indicators suggesting that a system is functioning as expected.

⸻

Observational Lenses

Execution Lens

Mismatch:
 Health ≠ Execution

The system appears alive, but work is not being executed.

Related case:
Case 010 — Health Illusion
State & Behavioral Lens

Mismatch:
State inconsistency
or
stalled progress
The system is active, but state is unclear, stale, inconsistent, or behavior is no longer producing progress.

Related cases:
Case 011 — State Desync
Case 012 — Silent Stall
Case 014 — Retry Loop Drift

Judgment Lens

Mismatch:
Decision confidence
≠
Decision quality
 The system continues making decisions, but the quality of judgment degrades.

Related case:
Case 013 — Judgment Drift
Trust / Provenance Lens

Mismatch:
 Trust > Provenance
 The output appears trustworthy, but the evidence chain supporting that trust is weak, missing, or unverifiable.

Related case:
 Case 015 — Trust Inheritance Drift
 Behavioral Trust Lens

Mismatch:
 Healthy appearance
+
progressive untrustworthiness
 The system remains operationally healthy while becoming less trustworthy over time.

Status:
 Research hypothesis.
 Detection remains incomplete.
 Propagation Rules

Rule 1 — Persistence Amplifies Risk

Persistent execution or state drift increases the risk of judgment drift.
 Execution / State Drift
→
Judgment Risk ↑
 Rule 2 — Unexplained Divergence Escalates

Unexplained divergence between observable signals and expected trustworthiness increases behavioral trust risk.
 Unexplained Divergence
→
Behavioral Trust Risk ↑
 Rule 3 — Cross-Layer Inconsistency Triggers REVIEW

When different lenses disagree, Governor should not assume the system is safe.
 Health = Green
Progress = Zero
 Trust = High
Evidence = Weak
 Execution = Good
Judgment = Poor
 These patterns trigger REVIEW.

⸻

REVIEW Logic

Governor may issue REVIEW when:
 Confidence > Evidence
 Or
 Cross-layer inconsistency exists
 Or
 Divergence persists without explanation
 REVIEW does not assume failure.

 REVIEW assumes uncertainty.

⸻
Case Mapping
Case 010 → Execution Lens
Case 011 → State & Behavioral Lens
Case 012 → State & Behavioral Lens
Case 013 → Judgment Lens
Case 014 → State & Behavioral Lens
Case 015 → Trust / Provenance Lens

 Current Status

Draft v0.2.

This taxonomy is exploratory.

The lenses may change as new cases are studied