"""
Check if Palindrome:
Checks if the string entered by the user is a palindrome. That is that it 
reads the same forwards as backwards like "racecar".

Concept(s): mod
"""

def main():
    print("This program will take input and check whether it is a palindrome.")
    while True:
        s = raw_input("Enter a string: ")
        if len(s) != 0:
            print(palindrome(s))

def palindrome(s):
    length = len(s)
    if length%2 == 0 or length == 1:
        for i in range(length/2):
            if s[i] != s[-i-1]:
                return False
        return True
    else:
        return False
main()