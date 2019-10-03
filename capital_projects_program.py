# -*- coding: utf-8 -*-
"""
Joe Holleran
10/02/2019
Capital Projects Program
Python 2
"""
# Filtering and print of capital projects in PGH

import csv

PROJECT_CSV = 'capitalprojects.csv'
LOG_FILE = 'malformedProjects.txt'
SEARCH_CRIT = 'capitalprojects.json'

def readAndProcessProjects():
    with open(PROJECT_CSV, 'r') as projFile:
        reader = csv.DictReader(projFile)
    # for json:
    # json.load()
    
        for proj in reader:
            # check project for integrity
            if checkProjectIntegrity(proj):
                applyProjectFilter(proj)
                # send well-formed projects to search filter

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
        
def logMalformedProject(projid):
    with open(LOG_FILE, 'a') as outfile:
        outfile.write(str(projid))
        
def applyProjectFilter(proj):
    
    # function to open json file for search criteria
    # function to check on dates - split on dash and check for length
    # function to check query for blanks
    # function key[value] to check if list and compare the keys/values in both
    # function to apply project filter
    # function to record output
    
    with open(SEARCH_CRIT, 'r') as searchFile:
        search = json.load(searchFile)
    
    
        
    # implement filter logic here
    # if filter outputs project, record
    recordOutputProject(proj)
    
def recordOutputProject(proj):
    printProjectToConsole(proj)
    

readAndProcessProjects()
    
    
    
    