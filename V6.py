import math

def inverse_factorial(x):
    if x == 1:  # Special case: 0! and 1! are both 1
        return 1
    n = 1
    fact = 1
    while fact < x:
        n += 1
        fact *= n
        if fact == x:
            return n
    return None  

def solve(start, end):
    for number in range(start, end + 1):
        x = number**2 - 1
        result = inverse_factorial(x)
        if type(result) is int and result != -1:
            print(f"{number} is a solution to Brocard's problem! (n! = {x}, n = {result})")

solve(2, 10)
