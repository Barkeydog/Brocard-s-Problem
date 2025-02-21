import math

def check_factorial_properties():
    for num in range(1, 26):  # Numbers from 1 to 25
        factorial = math.factorial(num)  # Compute factorial of the number
        result = math.sqrt(factorial + 1)  # Add one and calculate square root
        if result.is_integer():  # Check if the result is an integer
            # Print only numbers that satisfy the condition
            print(f"Number: {num}, Factorial+1: {factorial + 1}, Square Root: {int(result)}")

# Run the function
if __name__ == "__main__":
    check_factorial_properties()
