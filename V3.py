import math

class Solution:
    def solve(self, a):
        i, num = 0, 1
        L = []
        while i < a:
            i = math.factorial(num)
            L.append(i)
            num += 1
        if a in L:
            return L.index(a) + 1
        else:
            return -1

def brocard_problem_solver(start, end):
    """Solve Brocard's problem for numbers in a given range."""
    ob = Solution()
    for number in range(start, end + 1):
        x = number**2 - 1
        result = ob.solve(x)
        if result != -1:
            print(f"{number} is a solution to Brocard's problem! (n! = {x}, n = {result})")

# Define the range to search for solutions
brocard_problem_solver(2, 100)
