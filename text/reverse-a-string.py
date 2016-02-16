"""
Reverse a String:
Enter a string and the program will reverse it and print it out.

Concept(s): simplicity, string
"""

def main():
    print "This program will take input and print it out backwards."
    while True:
        s = raw_input("Enter a string: ")
        print(s[::-1])
        
main()