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
    return None  # If no exact n! equals x
print(inverse_factorial(150))
