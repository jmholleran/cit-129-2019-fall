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
    print("-------------------------")
    
    for num in range(2, 101, 2):
        print(num, end=", ")
    
    print("\n")
    
def challenge_two():
    
    print("Challenge Two")
    print("-------------------------")
    
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
    print("-------------------------")
    
    gibberish = "askaliceithinkshe'llknow"

    for letter in gibberish[::2]:
        print(letter, end=" ")
    
    print("\n")
    
def challenge_four():
    
    print("Challenge Four")
    print("-------------------------")
    
    for num in range(1,5):
        for number in range(5,8):
            mult = num * number
            print(num, "|", number, "|", mult)
    
    print("\n")
    
def challenge_five():
    
    print("Challenge Five")
    print("-------------------------")
    
    listoflists = [['mn', 'pa', 'ut'], ['b','p','c'], ['echo', 'charlie', 'tango']]
    labels = {"state":"US State Abbr: ", "element":"Chemical Element: ", "alpha": "Phonetic Call: "}

    for item in listoflists[0]:
        print(labels.get("state"), item.upper())
    
    for item in listoflists[1]:
        print(labels.get("element"), item.upper())
    
    for item in listoflists[2]:
        print(labels.get("alpha"), item.upper())
        
    print("\n")
     
if __name__ == "__main__":
    main()
