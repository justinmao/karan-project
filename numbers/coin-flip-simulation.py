"""
Coin Flip Simulation:
Write some code that simulates flipping a single coin however many times the
user decides. The code should record the outcomes and count the number of tails
and heads.

Concept(s): random numbers, global variables
"""

from random import randint

heads = 0;
tails = 0;

def main():
    print("This program will flip a coin and record the outcomes.")
    while True:
        run = raw_input("Flip a coin? (y/n/reset): ")
        if run == "y":
            print(flip())
        elif run == "n":
            pass
        elif run == "reset":
            global heads
            global tails
            heads = 0;
            tails = 0;
        else: 
            print("Input invalid.")

def flip():
    value = ""
    i = randint(0,1)
    global heads
    global tails
    if i == 0:
        heads += 1;
        value = "heads"
    else:
        tails += 1;
        value = "tails"
    return ("The coin landed on "+value+", for a total of "+str(heads)+" heads "
            "and "+str(tails)+" tails.")
        
def invalid_input():
    return "Input must be a positive integer."
    
main()