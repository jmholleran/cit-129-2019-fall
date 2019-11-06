# -*- coding: utf-8 -*-
"""
Joe Holleran
Pandas - Basketball Reference - Team Stats
10/23/2019
Python 2
"""
# Pandas DataFrame: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
# Pandas Read HTML: https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.read_html.html
# Pandas To_Excel: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html

import pandas as pd
import sqlite3 

def main():
    
    # Use panda to read html table from url
    dfs = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019_ratings.html', header=1)[0]   
    
    # Create excel file from the html table; remove default row index
    dfs.to_excel('panda_team_stats.xlsx', index = False)
    
    # Create DataFrame using the table read from HTML
    nbaTeamStats = pd.DataFrame(dfs)
    
    # Print DataFrame without default row index
    print(nbaTeamStats.to_string(index=False))
    
    # Make the connection object
    dbconn = sqlite3.connect('teamStats.db')
    
    # Make the cursor object
    cursor = dbconn.cursor()
    
    # Pandas DF to_sql
    nbaTeamStats.to_sql('team_stats', dbconn, if_exists='replace', index=False)
    
    # Query the DB - SELECT Teams with Net Rating over 3.5
    cursor.execute("SELECT Team, W, NRtg FROM team_stats WHERE NRtg > 3.5")
    
    # Assign the cursor object to a dataframe
    df = pd.DataFrame(cursor.fetchall(), columns=['Team', 'W', 'NRtg']  )
    print(df)
    
    # Close the connection
    dbconn.close()
   
if __name__=='__main__':
    main()