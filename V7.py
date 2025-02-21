import math

def inverse_factorial(n_factorial):
    i = 1
    fact = 1
    while fact < i
        i += 1
        fact *= i
        if fact == n_factorial:
            return i
    return None 

def solve(start, end):
    for number in range(start, end + 1):
		    m = number
        n_factorial = m**2 - 1
        n = inverse_factorial(n_factorial)
        if type(n) is int and n != -1:
            print(f"{n} is a solution to Brocard's problem!")
            
solve(2, 10)
