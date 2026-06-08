# Case 014 — Retry Loop Drift

The system repeatedly retries a failed task without demonstrating that anything meaningful changed between attempts.

The failure is not the first error.

The failure is continuing to retry while state, strategy, verification, and progress remain effectively unchanged.

## Pattern

A task fails.

The agent retries.

The retry loop continues.

But the system cannot answer:

> What changed before the next attempt?

## Signal

```json
{
  "task_id": "task_014",
  "attempt_count": 12,
  "state_changed": false,
  "strategy_changed": false,
  "verification_delta": 0,
  "progress_delta": 0,
  "last_error": "tool_timeout",
  "elapsed_minutes": 35
}
```

## Drift vs Retry Policy

Retry Loop Drift is not triggered by retries alone.

A retry policy becomes drift when:

- retries continue increasing
- state remains unchanged
- strategy remains unchanged
- verification does not improve
- progress remains absent

The issue is not repetition itself.

The issue is repeated execution without evidence that success became more likely.

## Detection Logic

Governor evaluates:

- retry growth
- state change
- strategy mutation
- verification improvement
- observable progress

## Example Output

Execution:

```bash
python cases/case_014_retry_loop_drift/governor.py
```
"suggestion": "Require strategy mutation before next retry. Consider circuit breaker or exponential backoff with jitter."

Output:

```json
{
  "signal_score": 95,
  "action": "ESCALATE",
  "reasons": [
    "repeated_retry_without_state_change",
    "no_strategy_mutation",
    "verification_stagnation",
    "progress_absent",
    "retry_loop_duration_exceeded"
  ]
}
```

## Interpretation

Retry Loop Drift does not mean the system failed.

It means the system continues attempting recovery without evidence that recovery became more likely.

Governor escalates the task for review, intervention, or strategy change before resources are consumed indefinitely.