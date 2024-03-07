def pedometer():
    steps = 0
    def step():
        nonlocal steps
        steps += 1
        return steps
    def jump():
        nonlocal steps
        steps += 2
        return steps
    return step, jump

step, jump = pedometer()

print(step())
print(jump())
print(step())
print(jump())
print(step())