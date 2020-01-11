# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 13:32:07 2020

@author: joeyh
"""
import pandas as pd

date = 'Mon, Dec 9, 2019'
home_team = 'Phoenix Suns'
away_team = 'Minnesota Timberwolves'

check_file = pd.read_csv('nbaML_2020_MASTER.csv', header=0)
df = pd.DataFrame(check_file)
date_col = df['date']
home_col = df['home_team']
away_col = df['away_team']

date_col = str(date_col)
home_col = str(home_col)
away_col = str(away_col)

df_check = pd.DataFrame({'date': [date], 'home_team': [home_team], 'away_team': [away_team]})

equals = pd.DataFrame({'date': [date], 'home_team': [home_team], 'away_team': [away_team]})


print(df_check.equals(equals))

