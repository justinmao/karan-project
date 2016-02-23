"""
Collatz Conjecture:
Start with a number n > 1. Find the number of steps it takes to reach one using
the following process: If n is even, divide it by 2. If n is odd, multiply it
by 3 and add 1.

Concept(s): linear time
"""

def main():
    print ("This program will determine the number of steps needed to reach 1 "
           "given a number according to the Collatz Conjecture.")
    while True:
        try:
            n = int(raw_input("Enter a number: "))
            print str(collatz(n)) + " steps."
        except ValueError: 
            invalid_input()

def collatz(n):
    if isinstance(n, int) and n > 0:
        steps = 0;
        while n != 1:
            if n%2 == 0:
                n = n/2
                steps += 1
            else:
                n = n*3 + 1
                steps += 1
        return steps
    else:
        raise ValueError
def invalid_input():
    print "Invalid input."
    
main()