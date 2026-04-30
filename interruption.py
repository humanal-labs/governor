def should_stop(action, confidence, history):
    risky_keywords = ["delete", "rm", "drop", "prod", "deploy", "overwrite"]

    # 1. Riskli aksiyon + düşük confidence
    if any(k in action.lower() for k in risky_keywords):
        if confidence < 0.6:
            return True, f"Low confidence ({confidence}) on risky action"

    # 2. Tehlikeli SQL komutları
    dangerous_sql = ["delete from", "drop table", "truncate"]

    if any(sql in action.lower() for sql in dangerous_sql):
        return True, "Dangerous SQL detected"

    # 3. Loop detection
    if len(history) >= 3 and history[-1] == history[-2] == history[-3]:
        return True, "Loop detected"

    return False, ""
