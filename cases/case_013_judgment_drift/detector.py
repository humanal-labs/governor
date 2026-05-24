log = {
    "confidence": 0.91,
    "verification_rate": 0.32,
    "recent_reviews": 1
}

confidence = log.get("confidence", 0)
verification_rate = log.get("verification_rate", 0)
review_count = log.get("recent_reviews", 0)

judgment_drift = (
    confidence > 0.8
    and verification_rate < 0.5
    and review_count < 2
)

result = {
    "drift_detected": judgment_drift,
    "action": "REVIEW" if judgment_drift else "ALLOW",
    "reason": "High confidence masking degraded verification"
}

print(result)