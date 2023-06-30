def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# This function works by first checking if the input number (n) is equal to 0. If it is, then the function returns 1. Otherwise, the function calls itself with the input number minus 1. The function continues to call itself until the input number is 0, at which point the function returns 1.

#Here is another example of a recursive function in Python:

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# This function works by first checking if the input number (n) is equal to 0 or 1. If it is, then the function returns the number. Otherwise, the function calls itself twice, once with the input number minus 1 and once with the input number minus 2. The function then returns the sum of the two results.

#These are just two examples of recursive functions in Python. There are many other recursive functions that can be written in Python.

#To run these functions, you can save them in a file and then run the file from the command line. For example, if you save the factorial function in a file called factorial.py, you can run it from the command line as follows:
