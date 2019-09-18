# -*- coding: utf-8 -*-
"""
Joe Holleran
Python 2
Mini-Program: Dictionary
09/18/2019
"""

# Source for menu structure of program:  
#   Starting out with Python by Gaddis - page 456-459
# Nested Dictionaries Resources:
#   https://docs.python.org/3/tutorial/datastructures.html
#   https://www.geeksforgeeks.org/python-nested-dictionary/
# NBA Player Statistics: basketball-reference.com/players

DISPLAY = 1
NEWSTAT = 2
NEWPLAYER = 3
DELETESTATS = 4
DISPLAYALL = 5
DELETEPLAYER = 6
MODIFYSTAT = 7
QUIT = 8

def main():
    
    nba = {"LeBron James": {"PPG": "27.4", "RPG": "8.5"},
        "Stephen Curry": {"PPG": "27.3", "RPG": "5.3"},
        "James Harden": {"PPG": "36.1", "RPG": "6.6"}}
    
    choice = 0
    
    while choice != QUIT:
        
        choice = get_menu_choice()
        
        if choice == DISPLAY:
            display(nba)
        elif choice == NEWSTAT:
            newstat(nba)
        elif choice == NEWPLAYER:
            newplayer(nba)
        elif choice == DELETESTATS:
            deletestats(nba)
        elif choice == DISPLAYALL:
            displayall(nba)
        elif choice == DELETEPLAYER:
            deleteplayer(nba)
        elif choice == MODIFYSTAT:
            modifystat(nba)
            
def get_menu_choice():
    
    print("Dataset of NBA Player Statistics")
    print("** User Can Add, Modify, & Delete NBA Players & their Statistics**")
    print("---------------------------")
    print("1. Display Player Statistics")
    print("2. Add New Statistic")
    print("3. Add New Player")
    print("4. Delete Player Statistic")
    print("5. Display All Players")
    print("6. Delete Player")
    print("7. Modify Statistic")
    print("8. Quit the program")
    print()
    
    choice = int(input("Enter your choice: "))
    
    while choice < DISPLAY or choice > QUIT:
        choice = int(input("Enter a valid choice: "))
        
    return choice

def displayall(nba):
    
    print("----------------")
    print("Display All Players")
    print("")
    
    for key, value in nba.items():
        print(key)
        
    input("Press enter to continue")

def display(nba):             
    
    print("----------------")
    print("Display Player Statistics")
    print("")
    
    for key, value in nba.items():
        print(key)
    
    print("")
    select = input("Choose Player: ")

    print("")
    print(select + " statistics")
    for key, value in nba[select].items():
        print(key, value)
        
    print("\n")
        
    input("Press enter to continue")
    
     
def newstat(nba):
    
    print("----------------")
    print("Add New Stat Category to Player")
    
    print("")
    
    for key, value in nba.items():
        print(key)
    
    print("")
    
    player = input("Choose Player: ")
        
    print("\n" + player + " current statistics: ")

    for key, value in nba[player].items():
        print(key, value)
        
    new_stat = input("New Stat Category: ")
    new_value = input(new_stat + " value: ")
    
    if new_stat not in nba[player]:
        nba[player][new_stat] = new_value
    else:
        print("That entry already exists.")

    print("\n" + player + " modified statistics: ")
    
    for key, value in nba[player].items():
        print(key, value)
        
    input("Press enter to continue")
    
def newplayer(nba):
    
    print("----------------")
    print("Add New NBA Player")
    print("")
    
    player = input("Enter Player Name: ")
    
    nba[player] = {}
    
    print("")
    add_choice = input("Would you like to add statistics to " + player + "? ")
    
    if add_choice == "Y" or add_choice == "Yes" or add_choice == "y" or add_choice == "yes":
        
        print("Add statistics to " + player)
        
        new_stat = input("Enter new stat category: ")
        new_value = input("Enter " + new_stat + " value: ")
        
        nba[player] = {new_stat : new_value}
        
        print("")
        print(player + " statistics added.")
        
    input("Press enter to continue")
   
def deletestats(nba):
    
    print("----------------")
    print("Delete Stats of NBA Player")
    print("")
    
    for key, value in nba.items():
        print(key)
    
    print("")
    
    player = input("Choose Player: ")
    
    print("\n" + player + " Current Statistics.")
    for key, value in nba[player].items():
        print(key, value)
        
    delete_key = input("Select Statistic to Delete: ")
    
    if len(nba[player]) == 1:
        print("Sorry, cannot remove last key/value pair.")
    elif delete_key in nba[player]:
        del nba[player][delete_key]
    else:
        print("Stat not found.")
    
    input("Press enter to continue")
    
def deleteplayer(nba):
    
    print("----------------")
    print("Delete NBA Player from Datastat")
    print("")
    
    for key, value in nba.items():
        print(key)
    
    print("")
    
    player = input("Choose Player: ")
    
    if player in nba:
        del nba[player]
    else:
        print("Player not found.")
        
    print("")
    print(player + " has been deleted from dataset.")
        
    input("\nPress enter to continue")
    
def modifystat(nba):
    
    print("----------------")
    print("Modify Stat of NBA Player")
    print("")
    
    print("UNDER CONSTRUCTION")
    
if __name__ == "__main__":
    main()


