def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    print("Factorial of 5 using recursion:", factorial(5))
    print("Factorial of 5 using iteration:", factorial_iterative(5))

if __name__ == "__main__":
    main()

# This code first defines two functions: factorial() and factorial_iterative(). The factorial() function uses recursion to calculate the factorial of a number. The factorial_iterative() function uses iteration to calculate the factorial of a number.

#The main() function then calls both functions to calculate the factorial of 5. The results of both functions are then printed to the console.

#As you can see, the code for the factorial() function is recursive. The factorial_iterative() function, on the other hand, is iterative.

#The factorial() function works by calling itself to calculate the factorial of a smaller number. The factorial_iterative() function, on the other hand, works by iteratively multiplying the number by itself until it reaches 1.

#Both functions will produce the same result, but the factorial() function may be slower for larger numbers. This is because the factorial() function has to call itself multiple times, which can lead to stack overflow errors.

#The factorial_iterative() function, on the other hand, does not have this problem. This is because it does not call itself recursively.

#Which function you use will depend on the specific problem you are trying to solve. If you are trying to solve a problem that is recursive in nature, then the factorial() function may be a good choice. However, if you are trying to solve a problem that is not recursive in nature, then the factorial_iterative() function may be a better choice.
