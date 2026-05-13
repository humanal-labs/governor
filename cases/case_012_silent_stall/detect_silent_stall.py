import json
import time

with open("case_012_silent_stall.log", "r") as file:
    log = json.load(file)

print("\n=== Governor Runtime Check ===\n")

time.sleep(1)

print(f"[{log['timestamp']}]")
print(f"Session State     : {log['session_state']}")
print(f"Message State     : {log['message_state']}")
print(f"Agent State       : {log['agent_state']}")
print(f"Output Progress   : {log['output_progression']}")
print(f"Terminal State    : {log['terminal_state']}")
print(f"Explicit Error    : {log['explicit_error']}")

time.sleep(1)

if (
    log["session_state"] == "ACTIVE"
    and log["agent_state"] == "IDLE"
    and log["output_progression"] == "NONE"
    and log["explicit_error"] is False
):
    print("\nGovernor:")
    print("Operational ambiguity detected.")
    print("Action: REVIEW")

else:
    print("\nGovernor:")
    print("No drift detected.")
