# -*- coding: utf-8 -*-
"""
Joe Holleran
10/02/2019
Capital Projects Program
Python 2
"""
# Filtering and print of capital projects in PGH

import csv
import json

PROJECT_CSV = 'capitalprojects.csv'
LOG_FILE = 'malformedProjects.txt'
SEARCH_CRIT = 'capitalprojects.json'
SEARCH_OUT = 'searchOutput.txt'

def readAndProcessProjects():
    with open(PROJECT_CSV, 'r') as projFile:
        reader = csv.DictReader(projFile)
    
        for proj in reader:
            # check project for integrity
            if checkProjectIntegrity(proj) and checkDateIntegrity(proj):
                applyProjectFilter(proj)
                recordOutputProject(proj)

def printProjectToConsole(proj):
    print("***Project Profile***")
    
    for key in proj:
        print(key, end=": ")
        print(proj[key])
        
def checkProjectIntegrity(proj):
    if proj['area'] == '':
        logMalformedProject(proj['id'])
        return False
    else:
        return True
    
def checkDateIntegrity(proj):
    
    check_date = proj['start_date']
    split_date = check_date.split("/")
    
    date_acc = 0
    
    for date in split_date:
        date_acc += (len(date))
        
    if date_acc != 8:
        return False
    else:
        return True
    
def logMalformedProject(projid):
    with open(LOG_FILE, 'a') as outfile:
        outfile.write(str(projid))
        
def applyProjectFilter(proj):
    
    with open(SEARCH_CRIT) as searchFile:
        search = json.load(searchFile)
 
    for key, value in search.items():
        print("project key ", proj[key])
        print("search key ", search[key])
        if value != "":
            if proj[key] == search[key]:
                return True
            else:
                return False
    
    
"""
    with open(SEARCH_CRIT) as searchFile:
        search = json.load(searchFile)
        
    crit_list = []
        
    for crit in search:
        crit_list.append(checkSearchCriteria(search[crit], proj))
        
    if all(crit_list):
        printProjectToConsole(proj)
    else:
        searchFile.close()
"""

"""
def checkSearchCriteria(crit, proj):

    
    f_list = []
    
    for i in range(0, len(crit)):
        if crit[i] in proj.values():
            f_list.append(True)
        elif crit[i] == "":
            f_list.append(True)
        else:
            f_list.append(False)
            
    if any(f_list):
        return True
    else:
        return False
"""

def recordOutputProject(proj):
    
    printProjectToConsole(proj)
    
    with open(SEARCH_OUT, 'w') as search_out:
        for key, value in proj.items():
            search_out.write(str(key + ": " + value + "\n"))
    

readAndProcessProjects()
    
    
    
    