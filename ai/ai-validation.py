print("AI Validation Started")

issues = []

with open("app/app.py", "r") as f:
    code = f.read()

if "print(" in code:
    issues.append("Avoid print statements in production code")

if len(code) < 10:
    issues.append("Code too small")

if issues:
    print("AI Issues Found:")
    for i in issues:
        print("-", i)
else:
    print("AI Validation Passed")

print("AI Validation Completed")
