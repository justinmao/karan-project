"""
Prime Factorization:
Have the user enter a number and find all Prime Factors (if there are any) and 
display them.

Concept(s): nested loop
"""

def main():
    print("This program will return the prime factors of a number.")
    while True:
        try:
            n = int(raw_input("Enter a number: "))
            find_primes(n)
        except ValueError:
            invalid_input()

def find_primes(n): # find primes up to than n
    primes = []
    for i in range(2, n+1):
        divisible = False
        for prime in primes:
            if i%prime == 0:
                divisible = True
        if divisible == False:
            primes.append(i)
    print(primes)

def invalid_input():
    print("Input must be a positive integer.")
    
main()