import json

with open("case_010.log", "r", encoding="utf-8") as f:
    log = json.load(f)

health_ok = log.get("health_status") == 200
no_execution = log.get("executions_per_min", 0) == 0
queue_backlog = log.get("queue", 0) >= 1000

drift_detected = health_ok and no_execution and queue_backlog

result = {
    "case_id": log.get("case_id"),
    "drift_detected": drift_detected,
    "action": "STOP" if drift_detected else "CONTINUE",
    "reason": "Dashboard green, but execution stopped and queue is growing."
}

print(json.dumps(result, indent=2))
