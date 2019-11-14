"""
Joe Holleran
11/13/2019
Python 2
Week 10 - PA Crash Data
"""
# Notebook for assembling and analyzing data about crashes on state highways
# provided by PennDot
# https://data.pa.gov/Public-Safety/Crash-Incident-Details-CY-1997-Current-Annual-Coun/dc5b-gebx

# Work process log

"""
1)  Download and inspect CSV file to anticipate needs in creating a database 
    table to store info
    - Convert Yes/No to boolean
    - Strip space and turn header values to all lowercase for COL names
    - Lat/Lon are in the set twice; use the iso lat/lon columns
    
2)  
    
"""   
import pandas as pd
import sqlite3 
import re

cleancols = []

with open('crashtest.csv', 'r') as ctfile:
    head = ctfile.readlines()[0]
    
    cols = head.split(',')
    
    exp_space = re.compile('\s+')
    exp_weird = re.compile('\W+')
    
    for entry in cols:
        prettycol = exp_space.sub('_', entry).lower()
        finalcol = exp_weird.sub('', prettycol)
        cleancols.append(finalcol)
               
df = pd.read_csv('crashtest.csv', skiprows=1, names=cleancols)

 # Make the connection object
dbconn = sqlite3.connect('pacrash.db')
    
# Make the cursor object
cursor = dbconn.cursor()
    
# Pandas DF to_sql
df.to_sql('penna_crash', dbconn, if_exists='replace', index=False)
    
# Query the DB - SELECT Teams with Net Rating over 3.5
cursor.execute("SELECT weather, day_of_week FROM penna_crash WHERE weather = 'Snow'")
    
# Assign the cursor object to a dataframe
display_df = pd.DataFrame(cursor.fetchall(), columns=['weather', 'day_of_week'])

print(display_df)
    
# Close the connection
dbconn.close()
    