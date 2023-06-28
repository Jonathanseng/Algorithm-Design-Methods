use std::collections::HashMap;

fn fibonacci(n: u32) -> u32 {
    let mut memo = HashMap::new();
    if let Some(result) = memo.get(&n) {
        return *result;
    } else {
        if n == 0 {
            result = 0;
        } else if n == 1 {
            result = 1;
        } else {
            result = fibonacci(n - 1) + fibonacci(n - 2);
        }
        memo.insert(n, result);
        return result;
    }
}

// Memoization is a technique used to store the results of function calls so that they do not have to be recomputed when the function is called again with the same inputs. This can be especially useful in dynamic programming problems, where the same subproblems may be solved multiple times.

// In Rust, memorization can be implemented using a hash map. For example, the following code shows how to implement a memoized Fibonacci function:

// The memo hash map is used to store the results of previous Fibonacci function calls. The fibonacci() function first checks if the result for the given n is already stored in the memo hash map. If it is, the function simply returns the stored result. Otherwise, the function computes the result and stores it in the memo hash map before returning it.

// Tabulation is another technique used in dynamic programming to store the results of function calls. However, unlike memorization, tabulation stores the results of all function calls in a table. This can be useful in dynamic programming problems where the order in which the subproblems are solved does not matter.

// In Rust, tabulation can be implemented using a vector. For example, the following code shows how to implement a tabulated Fibonacci function:

fn fibonacci(n: u32) -> u32 {
    let mut fib = vec![0; n + 1];
    fib[0] = 0;
    fib[1] = 1;
    for i in 2..n + 1 {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    return fib[n];
}

// The fib vector is used to store the results of all Fibonacci function calls. The fibonacci() function first initializes the fib vector with the values 0 and 1. Then, the function computes the values of fib[i] for i from 2 to n. Finally, the function returns the value of fib[n].

// Both memorization and tabulation are useful techniques for dynamic programming in Rust. The choice of which technique to use depends on the specific problem being solved.
