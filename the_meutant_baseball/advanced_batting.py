"""
Joe Holleran
11/10/2019
FanGraphs - Advanced Stats
Daily Fantasy Analysis
"""
# Python script to move Advanced Baseball Stats to Excel Sheet

import pandas as pd

def main():
    
    # Use panda to read html table from url
    dfs = pd.read_html('https://www.baseball-reference.com/leagues/MLB/2019-advanced-batting.shtml#players_advanced_batting::none')  
        
    # Create DataFrame using the table read from HTML
    mlbBattingAdvStats = pd.DataFrame(dfs)
    
    # Create excel file from the html table; remove default row index
    mlbBattingAdvStats.to_excel('batting_advanced_stats.xlsx', index = False)
    
    # Print DataFrame without default row index
    print(mlbBattingAdvStats.to_string(index=False))
    
if __name__=='__main__':
    main()


