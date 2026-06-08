# Case 015 — Trust Inheritance Drift

A result may look correct even when the path that produced it is no longer trustworthy.

## Definition

Trust Inheritance Drift occurs when an agent transfers confidence from the final output back onto the entire execution chain without validating the integrity of intermediate steps.

The result succeeds.

The path does not.

The system trusts both.

## Core Question

Are we trusting the result?

Or are we trusting the path that produced the result?

## Pattern

Tool A executes.

Tool B produces a weak, stale, hallucinated, or unverifiable output.

Tool C consumes that output.

A later step generates a plausible final result.

The task is marked successful.

Trust assigned to the final output is inherited by the entire execution chain.

## Signal Hypothesis

```json
{
  "task_id": "task_015",
  "trust_score": 0.95,
  "provenance_score": 0.33,
  "verified_steps": 2,
  "execution_steps": 5,
  "evidence_chain_complete": false
}
Trust Inheritance Drift may exist when:
trust_score > 0.90

provenance_score < 0.50

## Example
Tool A
  ↓
Tool B (hallucinated output)
  ↓
Tool C (partial correction)
  ↓
Final Output (appears correct)
Final output succeeds.

Intermediate trust chain remains weak.

Why It Matters

Agent systems increasingly operate through long execution chains.

A high-confidence result can hide a low-confidence path.

The failure is not visible in the output.

The failure exists in the inherited trust.

Open Questions

1. How should provenance_score be calculated?
2. How should trust decay across execution chains?
3. When should inherited trust trigger review?
4. Should Governor REVERIFY, ESCALATE, or DECAY TRUST?
5. How much missing evidence is acceptable before trust becomes unsafe?

Status

Concept Case

No runtime detector yet.

Pattern definition phase.
