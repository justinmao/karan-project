"""
Fibonacci Sequence:
Enter a number and have the program generate the Fibonacci sequence to that 
number or to the Nth number.

Concept(s): recursion, error handling
"""

def main():
    print("This program will return the Fibonacci sequence at a given "
          "position.")
    while True:
        try:
            n = int(raw_input("Enter a number: "))
            print(fibonacci(n))
        except ValueError:
            invalid_input()

def fibonacci(n):
    if isinstance(n, int) and n > 0:
        if n == 1 or n == 2:
            return 1
        elif n >= 2:
            return fibonacci(n-1) + fibonacci(n-2)
    else:
        return invalid_input()

def invalid_input():
    print("Input must be a positive integer.")
    
main()