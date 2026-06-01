# governor.py
# Governor v0.2 — Behavioral Signal Scoring Layer

def evaluate_signals(snapshot):
    score = 0
    reasons = []

    # Queue growing while executions drop
    if snapshot["queue_growth"] > 0.7 and snapshot["execution_drop"] > 0.6:
        score += 35
        reasons.append("queue_execution_divergence")

    # Rollback clustering
    if snapshot["rollback_cluster"]:
        score += 20
        reasons.append("rollback_cluster_detected")

    # Escalation spike
    if snapshot["escalation_spike"]:
        score += 15
        reasons.append("escalation_frequency_increase")

    # Healthy dashboard paradox
    if snapshot["health_status"] == "green" and score > 40:
        reasons.append("healthy_dashboard_behavioral_drift")

    # Decision layer
    if score >= 60:
        action = "STOP"
    elif score >= 35:
        action = "REVIEW"
    else:
        action = "CONTINUE"

    return {
        "signal_score": score,
        "action": action,
        "reasons": reasons
    }


# Example snapshot
snapshot = {
    "queue_growth": 0.82,
    "execution_drop": 0.71,
    "rollback_cluster": True,
    "escalation_spike": True,
    "health_status": "green"
}

result = evaluate_signals(snapshot)

print(result)