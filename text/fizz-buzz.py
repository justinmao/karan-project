"""
Fizz Buzz:
Write a program that prints the numbers from 1 to 100. But for multiples of 
three print "Fizz" instead of the number and for the multiples of five print 
"Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

Concept(s): mod
"""

def main():
    print("This program will print out numbers from 1 to 100, replacing "
          "multiples of 3 with \"Fizz\", multiples of 5 with \"Buzz\" "
          "and multiples of both 3 and 5 with \"FizzBuzz\".")
    n = 1
    while n <= 100:
        print(fizzbuzz(n))
        n += 1

def fizzbuzz(n):
    if n%3 == 0 and n%5 == 0:
        return "FizzBuzz"
    elif n%3 == 0:
        return "Fizz"
    elif n%5 == 0:
        return "Buzz"
    else:
        return n
        
main()