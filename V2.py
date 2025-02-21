import math

def is_factorial(x):
    """Check if x is a factorial of any number."""
    if x <= 0:
        return None
    n = 1
    factorial = 1
    while factorial < x:
        n += 1
        factorial *= n
    return n if factorial == x else None

def brocard_problem_solver(start, end):
    """Solve Brocard's problem for numbers in a given range."""
    for number in range(start, end + 1):
        x = number**2 - 1
        result = is_factorial(x)
        if result is not None:
            print(f"{number} is a solution to Brocard's problem! (n! = {x}, n = {result})")

# Define the range to search for solutions
brocard_problem_solver(2, 1000)
