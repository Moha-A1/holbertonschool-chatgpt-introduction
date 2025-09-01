#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    The factorial of a number n is the product of all positive integers
    less than or equal to n. For example, factorial(4) = 4 * 3 * 2 * 1 = 24.
    
    Parameters:
        n (int): A non-negative integer for which to calculate the factorial.
                Must be >= 0.
    
    Returns:
        int: The factorial of the input number n.
             Returns 1 if n is 0 (by definition, 0! = 1).
    
    Raises:
        RecursionError: If n is negative, will cause infinite recursion.
        ValueError: If the input cannot be converted to an integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input from command line argument and calculate factorial
f = factorial(int(sys.argv[1]))
print(f)
