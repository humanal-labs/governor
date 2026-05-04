# Governor

> "You don't lose control straight away.  
> You just lose the early warning."  
> — Manufacturing principle

The missing control point for autonomous systems.

In physical systems, control doesn’t only come from formal rules.

It comes from small, informal moments:  
a second look, a hesitation, a pause before passing something on.

These aren’t designed.  
But they act as a buffer.

In manufacturing, they show up as:  
machine cycles, handover points, informal checks.

They slow things down just enough to catch drift.

Agents removed these for speed.

What remains is fast execution —  
without the moment that corrects the system.

Governor brings that moment back.

---

## The Problem

When systems speed up, informal checks disappear first.

People trust the system more.  
Or move things through to keep flow.

What remains is fast execution,  
without the moment that catches drift.

Individually correct. Systemically wrong.

Executed in sequence, each action looks reasonable.  
Executed at speed, they drift.

You don’t lose control immediately.  
You lose early warning.

---

## The Fix

We don’t add friction everywhere.

We restore the missing control point.

A lightweight governor, triggered only when signals suggest drift.

Not a blocker.  
A control point.

Quiet most of the time.  
Meaningful when it shows up.

---

## How It Works: Observable Drift

Governor moves beyond abstract signals.

It watches for observable drift:

1. **Behaviour Change**  
   The agent does something outside its normal pattern.

2. **Result Drift**  
   Cost, time, or output moves outside its baseline.

3. **Tempo Shift**  
   A step takes much longer than expected.

Governor triggers only when multiple signals line up.

This keeps it:

- Quiet most of the time  
- Trusted when it appears  

---
## Signal Design

Governor does not rely only on abstract signals.

It prioritizes observable drift:

- Execution taking longer than expected  
- Increasing retries or corrections  
- Output deviating from normal range  
- Sudden changes in behavior patterns  

These are the signals operators trust.

Quiet most of the time.  
Meaningful when triggered.
--
```python
drift_signals = {
    "execution_time_spike": current_time / baseline_time,
    "retry_count": retries,
    "output_variance": deviation_from_expected,
    "behavior_change": is_new_pattern
}
```

## Example

A single action:

```python
task = {
    "tool": "api",
    "cmd": "place_order",
    "confidence": 0.65,
    "cost": 18000
}
```

Individually, it looks correct.

Now apply the governor:

```python
def should_pause(task):
    if task["confidence"] < 0.7 and task["cost"] > 500:
        return True, "Low confidence, high cost"
    return False, None

pause, reason = should_pause(task)

if pause:
    print(f"PAUSED: {reason}")
```

Output:

```
PAUSED: Low confidence, high cost
```

---

## Demo

```bash
python demo.py
```

Simulates an agent executing actions at speed.

- Low-risk actions pass through  
- High-cost, uncertain actions trigger a pause  
- Potential drift is surfaced before execution  

Example output:

```
⚠️ GOVERNOR TRIGGERED: Cost $18,000 | Confidence 0.62
Pausing 10s. Drift risk detected.
Action requires review before execution.
```

---

## Why It Matters

At small scale, nothing looks wrong.

At scale, drift compounds.

No single action fails.  
The system drifts.

Governor restores the moment  
where the system can correct itself.
