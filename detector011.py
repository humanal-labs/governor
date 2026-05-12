def detect_case_011(log):
    signals = log.get("signals", {})

    frontend_active = signals.get("frontend_state") in ["STARTING", "LOADING"]
    ui_loading = "Loading" in signals.get("ui_status", "")
    backend_idle = signals.get("backend_conversation_state") == "IDLE"
    task_ready = signals.get("app_conversation_task") == "READY"
    no_error = signals.get("explicit_error") is False

    if frontend_active and ui_loading and backend_idle and task_ready and no_error:
        return {
            "case_id": log.get("case_id"),
            "drift_detected": True,
            "action": "STOP",
            "reason": "Frontend shows active startup while backend is idle/ready. Cross-layer state coherence failed."
        }

    return {
        "case_id": log.get("case_id"),
        "drift_detected": False,
        "action": "CONTINUE",
        "reason": "No cross-layer state desynchronization detected."
    }
