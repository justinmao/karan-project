"""
Next Prime Number:
Have the program find prime numbers until the user chooses to stop asking for 
the next one.

Concept(s): helper functions, initialization, list iteration, global variables
"""

primes = ["init"]

def main():
    global primes
    print "This program will consecutively return prime numbers."
    while True:
        s = raw_input("Find next prime? (y/reset): ")
        if s == "y":
            print next_prime(primes[-1])
        elif s == "reset":
            primes = ["init"]
            print "Program has been reset."
        else:
            invalid_input()

def next_prime(n): 
    global primes
    if n == "init":
        primes = [2]
        return 2
    else:
        while True:
            if is_prime(n):
                primes.append(n)
                return n
            else:
                n = n + 1;

def is_prime(n):
    for i in primes:
        if n % i == 0:
            return False
    return True

def invalid_input():
    print "Please input 'y' or 'reset'."
    
main()