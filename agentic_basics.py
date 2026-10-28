def ispect_failure(log: str) -> str:
    if "ModuleNotFoundError:" in log:
        return "Likely dependency or import failure"

    if "AssertionError" in log:
        return "A rest assertion failed"

    if "SyntaxError" in log:
        return "Python syntax error detected"

    return "Unknown failure"

sample_log = "ModuleNotFoundError: No module named 'requests'"

result = ispect_failure(sample_log)
print(result)
