"""
Count Vowels:
Enter a string and the program counts the number of vowels in the text. For 
added complexity have it report a sum of each vowel found.

Concept(s): simplicity, string
"""

def main():
    print("This program will count the number of vowels in input.")
    while True:
        s = raw_input("Enter a string: ")
        n = count_vowels(s)
        print(str(n) + " vowels found.")

def count_vowels(s):
    vowels = "aeiouAEIOU"
    total = 0
    for char in s:
        if char in vowels:
            total += 1
    return total
    
main()