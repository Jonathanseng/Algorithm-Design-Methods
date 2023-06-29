def factorial(n):
  """
  Calculates the factorial of a number.

  Args:
    n: The number to calculate the factorial of.

  Returns:
    The factorial of the number.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


def fibonacci(n):
  """
  Calculates the Fibonacci number of a number.

  Args:
    n: The number to calculate the Fibonacci number of.

  Returns:
    The Fibonacci number of the number.
  """

  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
  print("The factorial of 5 is:")
  print(factorial(5))

  print("The Fibonacci number of 10 is:")
  print(fibonacci(10))


if __name__ == "__main__":
  main()
#This code first defines a function called factorial(). This function takes one argument: n. n is the number to calculate the factorial of.

#The factorial() function then works by recursively calling itself until n is 0. The base case is when n is 0, in which case the function returns 1. Otherwise, the function returns n multiplied by the factorial of n - 1.

#The fibonacci() function works similarly to the factorial() function. The base case is when n is 0 or 1, in which case the function returns 0 or 1, respectively. Otherwise, the function returns the sum of the Fibonacci numbers of n - 1 and n - 2.

#The main() function then calls the factorial() function and the fibonacci() function with different arguments. The main() function then prints the results of the functions.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as recursion.py, you can run it by typing the following command into the command line:
