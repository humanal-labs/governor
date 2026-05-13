# Case 010 — Health Illusion

## Source
n8n issue:
"External task runner: Code nodes time out for hours while /healthz reports healthy, no self-recovery"

## Drift Pattern
Operational health indicators remain positive while the execution layer silently stalls.

## Observed Behavior
- health endpoint: HEALTHY
- execution throughput: ZERO
- task queue: STALLED
- timeout duration: HOURS
- self recovery: ABSENT

## Human Problem
Operators trust monitoring dashboards and delay intervention because the system appears operational.

## Governor Interpretation
Reported health diverges from operational throughput reality.

## Action
STOP
