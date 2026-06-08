snapshot = {
    "task_id": "task_014",
    "attempt_count": 12,
    "state_changed": False,
    "strategy_changed": False,
    "verification_delta": 0,
    "progress_delta": 0,
    "last_error": "tool_timeout",
    "elapsed_minutes": 35
}

score = 0
reasons = []

if snapshot["attempt_count"] > 5 and not snapshot["state_changed"]:
    score += 25
    reasons.append("repeated_retry_without_state_change")

if not snapshot["strategy_changed"]:
    score += 20
    reasons.append("no_strategy_mutation")

if snapshot["verification_delta"] == 0:
    score += 20
    reasons.append("verification_stagnation")

if snapshot["progress_delta"] == 0:
    score += 20
    reasons.append("progress_absent")

if snapshot["elapsed_minutes"] > 30:
    score += 10
    reasons.append("retry_loop_duration_exceeded")

if snapshot["last_error"] == "tool_timeout" and snapshot["attempt_count"] > 5:
    score += 10
    reasons.append("repeated_same_error")

if score >= 70:
    action = "ESCALATE"
elif score >= 40:
    action = "REVIEW"
else:
    action = "CONTINUE"

result = {
    "signal_score": score,
    "action": action,
    "reasons": reasons,
    "suggestion": "Require strategy mutation before next retry. Consider circuit breaker or exponential backoff with jitter."
}
print(result)