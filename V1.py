import math

def inverse_factorial(x):
    n = 1
    factorial = 1
    while factorial < x: 
        n += 1
        factorial *= n
    return n if factorial == x else None

number = 2
end = 1000

while number < end:
    x = number**2 - 1
    result = inverse_factorial(x)

    if isinstance(x, int):
        print(f"{number} is a solution to Brocard's problem!")
    else:
        number += 1 print
