import math

def solve(a):
    i, num = 0, 1
    L = []
    while i < a:
        i = math.factorial(num)
        L.append(i)
        # If 'a' was just added to L, return its 1-based index right away
        if a in L:
            return L.index(a) + 1
        num += 1
    
    # If we exit the loop without finding 'a' in L, it's not a factorial
    return -1

def brocard_problem_solver(start, end):
    for number in range(start, end + 1):
        x = number**2 - 1
        result = solve(x)
        # Check if 'solve(x)' gave a valid integer factorial index
        if type(result) is int and result != -1:
            print(f"{number} is a solution to Brocard's problem! (n! = {x}, n = {result})")

brocard_problem_solver(2, 10)
