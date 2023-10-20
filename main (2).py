def factorial(n):
  if n == 0:
      return 1  # Base case: 0! = 1
  else:
      return n * factorial(n - 1)  # Recursive case

# Example usage:
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
