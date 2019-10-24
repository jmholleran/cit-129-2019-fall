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

def main():
    
    # Use panda to read html table from url
    dfs = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019_ratings.html', header=1)[0]   
    
    # Create excel file from the html table; remove default row index
    dfs.to_excel('panda_team_stats.xlsx', index = False)
    
    # Create DataFrame using the table read from HTML
    nbaTeamStatsTable = pd.DataFrame(dfs)
    
    # Print DataFrame without default row index
    print(nbaTeamStatsTable.to_string(index=False))
    
if __name__=='__main__':
    main()