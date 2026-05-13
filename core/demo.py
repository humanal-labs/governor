from dataclasses import dataclass


@dataclass
class Trace:
    ts: str
    action: str
    retry: int
    latency_ms: int
    actions_per_min: float
    result: str


BASELINE = {
    "retry_p95": 1,
    "latency_median": 120,
    "tempo_median": 8.2,
}


def governor(trace: Trace):
    signals = []

    if trace.retry > BASELINE["retry_p95"] * 2:
        signals.append("retry spike")

    if trace.latency_ms > BASELINE["latency_median"] * 1.4:
        signals.append("latency drift")

    if trace.actions_per_min < BASELINE["tempo_median"] / 3:
        signals.append("tempo shift")

    if len(signals) >= 2:
        return {
            "action": "PAUSE",
            "signals": signals,
            "reason": "early drift detected",
        }

    return {
        "action": "CONTINUE",
        "signals": [],
        "reason": None,
    }


traces = [
    Trace("01:55", "weld_check", 0, 118, 8.1, "pass"),
    Trace("01:56", "weld_check", 0, 121, 8.3, "pass"),
    Trace("01:57", "weld_check", 1, 145, 7.9, "pass"),
    Trace("01:58", "weld_check", 3, 180, 2.1, "pass"),
    Trace("01:59", "weld_check", 4, 210, 1.8, "pass"),
    Trace("02:14", "weld_check", 5, 340, 1.2, "FAIL - $18k"),
]


for trace in traces:
    decision = governor(trace)

    print(
        f"{trace.ts} | retry={trace.retry} | "
        f"latency={trace.latency_ms}ms | "
        f"tempo={trace.actions_per_min}/min | "
        f"{decision['action']}"
    )

    if decision["action"] == "PAUSE":
        print(f"\n⚠️ GOVERNOR TRIGGERED at {trace.ts}")
        print(f"Signals: {', '.join(decision['signals'])}")
        print("Action: PAUSE — second-look required")
        print("Impact: paused before the 02:14 failure could compound")
        break

