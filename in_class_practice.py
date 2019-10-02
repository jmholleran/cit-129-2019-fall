"""
In-Class Practice
"""

import csv
import json
def main():
    
    csv_practice()
    json_practice()    
    

def csv_practice():
    # Question : Does the racial make up of the Allegheny County Jail
    # reflect the makeup of Allegheny County at large?

    # Keys available: _id	date	gender	race	agebook	agecurr

    file = open('jail.csv', newline='')

    reader = csv.DictReader(file)

    totBlack = 0
    totWhite = 0
    censusDate = '2018-01-01'

    for row in reader:
        if row['date'] == censusDate:
            if row['race'] == 'B':
                totBlack = totBlack + 1
            elif row['race'] == 'W':
                totWhite = totWhite + 1
            
    print("Date: ", censusDate)
    print("Total Black: ", totBlack)
    percent_black = totBlack / (totBlack + totWhite)
    print("Percent Black: ", percent_black)
    print("Total White: ", totWhite)
    percent_white = totWhite / (totWhite + totBlack)
    print("Percent White: ", percent_white)
            
    file.close()
    
def json_practice():

    # json dumps
    
    # Simplest example of encoding python objects in JSON and 
    # writing to file
    file = open('writeranges2.txt', 'w')
    file.write(json.dumps({'student-count':12, 'teacher-count':1}))
    file.close()
    
    # json loads
    
    # Simplest example of reading in JSON to python objects
    
    json.loads()
    
    

if __name__ == "__main__":
    main()




