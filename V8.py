import math

def is_integer(value):
    return value > 0 and value == int(value)

def find_brocard_solutions(limit):
    solutions = []
    for m in range(2, limit):
        potential_factorial = m**2 - 1
        n = 0
        while True:
            if math.factorial(n) == potential_factorial:
                solutions.append((n, m))
                break
            elif math.factorial(n) > potential_factorial:
                break
            n += 1
    return solutions
solution_limit = 100
solutions = find_brocard_solutions(solution_limit)
print("Solutions to Brocard's Problem (n, m):")
print(solutions)
