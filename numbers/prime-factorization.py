"""
Prime Factorization:
Have the user enter a number and find all Prime Factors (if there are any) and 
display them.

Concept(s): nested loops, prime numbers, exceptions
"""

def main():
    print "This program will return the prime factors of a number."
    while True:
        try:
            n = int(raw_input("Enter a number: "))
            print str(factorization(n))[1:-1]
                
        except ValueError:
            invalid_input()

def find_primes(n): # find primes up to n
    primes = []
    for i in range(2, n+1):
        divisible = False
        for prime in primes:
            if i%prime == 0:
                divisible = True
        if divisible == False:
            primes.append(i)
    return primes

def factorization(n):
    if isinstance(n, int) and n > 0:
        if n == 1: return [1]
        primes = find_primes(n) # prime numbers up to n
        factors = []
        remainder = n
        while remainder != 1:
            for prime in primes:
                if remainder%prime == 0:
                    remainder = remainder/prime
                    factors.append(prime)
        factors.sort()
        return factors
    else:
        raise ValueError
def invalid_input():
    print "Input must be a positive integer."
    
main()