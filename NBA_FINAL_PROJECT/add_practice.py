"""
Additional Final Project Practice File
"""
import pandas as pd

dfs = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2020_games-december.html')

df = pd.DataFrame(dfs[0])

df.set_index('Date', inplace=True)

date = 'Wed, Dec 4, 2019'
  
dfsearch = df.loc[[date], ['Visitor/Neutral', 'Home/Neutral']]

print(dfsearch)
        
        
        
        

