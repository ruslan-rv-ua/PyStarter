var1 = "hello!"
var2 = 8
# v
def f(a: int, b: int) -> int:
    """Add 2 integers.

    Returns:
        sum of 2 integers.
    """
    sum = a + b
    return sum


sum = f(var1, var2)
print(f"{var1}+{var2}={sum}")
