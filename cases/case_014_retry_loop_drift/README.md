# Case 014 — Retry Loop Drift

The system repeatedly retries a failed task without proving that anything has changed.

The failure is not the first error.

The failure is continuing to retry when the system cannot demonstrate state change, verification improvement, or progress.

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
  "verification_delta": 0,
  "progress_delta": 0,
  "last_error": "tool_timeout",
  "elapsed_minutes": 35
}
Detection Logic

Retry Loop Drift is detected when:

* retries increase
* state does not change
* verification does not improve
* progress remains absent

## Example Output

Execution:

```bash
python cases/case_014_retry_loop_drift/governor.py
```

Output:

```json
{
  "signal_score": 85,
  "action": "STOP",
  "reasons": [
    "repeated_retry_without_state_change",
    "verification_stagnation",
    "progress_absent",
    "retry_loop_duration_exceeded"
  ]
}
```
Interpretation

The system is not failing because the first attempt failed.

It is failing because it continues retrying without evidence that the next attempt has a better chance of succeeding.

Governor blocks the loop and requires review before further retries.