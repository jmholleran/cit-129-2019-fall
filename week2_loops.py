# -*- coding: utf-8 -*-
"""
Joe Holleran
Python 2
09/11/2019
Week 2 - Exercises Loops!
"""
def main():

    challenge_one()
    challenge_two()
    challenge_three()
    challenge_four()
    challenge_five()
    
def challenge_one():
    
    print("Challenge One")
    
    for num in range(2, 101, 2):
        print(num, end=", ")
    
    print("\n")
    
def challenge_two():
    
    print("Challenge Two")
    
    word = "KABOOM"

    for letter in word:
        print(letter, end=" ")
        for x in letter:
            print(x, end=" ")
            for x in letter:
                print(x, end=" ")
                
    print("\n")
    
def challenge_three():
    
    print("Challenge Three") 
    
    gibberish = "askaliceithinkshe'llknow"

    for letter in gibberish[::2]:
        print(letter, end=" ")
    
    print("\n")
    
def challenge_four():
    
    print("Challenge Four")
    
    for number in range(1, 5):
        print(number)
        for num in range(5,8):
            print(num)
    
    print("\n")
    
def challenge_five():
    
    print("Challenge Five")
    
    print("\n")
    
    
    
if __name__ == "__main__":
    main()
