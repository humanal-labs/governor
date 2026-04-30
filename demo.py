from interruption import should_stop

history = []

def run_action(action, confidence):
    stop, reason = should_stop(action, confidence, history)

    if stop:
        print(f"[INTERRUPTED] {reason}")
    else:
        print(f"[EXECUTED] {action}")
        history.append(action)


# Demo
run_action("ls", 0.9)
run_action("cd /", 0.9)
run_action("rm -rf /", 0.4)
run_action("DELETE FROM users;", 0.9)