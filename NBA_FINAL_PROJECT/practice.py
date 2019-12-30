# Prior Matchups this season (Try/Except)
import pandas as pd


url = 'https://www.basketball-reference.com/teams/LAL/2020/gamelog/'

dfs = pd.read_html(url, header = 1)
df = pd.DataFrame(dfs[0])
df['Unnamed: 3'].fillna('Home', inplace=True)
df['Unnamed: 3'].replace('@','Away',inplace=True)

opp = 'LAC'

df_filter = df.loc[df['Opp'].isin([opp])]

df_filter_col = df_filter[['Date', 'G', 'Unnamed: 3', 'W/L', 'Tm', 'Opp.1']]

df_filter_col.columns = ['Date', 'Game', 'Home/Away', 'W/L', 'LAL Score', 'LAC Score']

df_filter_col.set_index(['Date'], inplace=True)

print(df_filter_col)



