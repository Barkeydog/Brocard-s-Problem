def solve(a):
	i,num=0,1
  L=[]
  while i < a :
	  i=math.factorial(num)
    L.append(i)
    num+=1
    if a in L :
	    return L.index(a)+1
     else :
	     return -1

def brocard_problem_solver(start, end):
	for number in range(start, end + 1):
  x = number**2 - 1
  result = solve(x)
  if result(x) is int:
	  print(f"{number} is a solution to Brocard's problem! (n! = {x}, n = {result})")

brocard_problem_solver(2, 10)
