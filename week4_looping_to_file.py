"""
Python 2
Week 4 - looping to file
10/01/2019
Joe Holleran                                                                                 
"""
# https://www.youtube.com/watch?v=0PkIvXfP3ew

file = open('writeranges2.txt', 'w')

decrease = 1
for num in range(0, 11-decrease):
    for dat in range(0, 10-num):
        print(dat, end="")
        file.write(str(dat))
    print()
    
    
file.close()