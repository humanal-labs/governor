import json
import time

with open("case_010.log", "r") as file:
    log = json.load(file)

print("\n=== Governor Runtime Check ===\n")

time.sleep(1)

print(f"[{log['timestamp']}]")
print(f"Health Endpoint      : {log['health_endpoint']}")
print(f"Execution Throughput : {log['execution_throughput']}")
print(f"Task Queue State     : {log['task_queue_state']}")
print(f"Self Recovery        : {log['self_recovery']}")

time.sleep(1)

if (
    log["health_endpoint"] == "HEALTHY"
    and log["execution_throughput"] == 0
):
    print("\nGovernor:")
    print("Health illusion detected.")
    print("Action: STOP")

else:
    print("\nGovernor:")
    print("No drift detected.")
