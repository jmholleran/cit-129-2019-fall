"""
Python 2
Week 4 - string formatting
10/01/2019
Joe Holleran 
"""

def main():
       
    getName()
    greeting()
   
    
def getName():

    file = open('names.txt', 'r')
    
    for name in file:
        first, last = name.split()

    file.close()
    

def greeting():

    file = open('names.txt', 'r')
    
    for name in file:
        first, last = name.split()
        print("Good evening Dr. " + last + ", would you mind if I call you " + first + "?")
    
    file.close()


if __name__ == "__main__":
    main()




