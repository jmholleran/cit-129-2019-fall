# -*- coding: utf-8 -*-
"""
Practice Functions for Final Project
"""
import datetime as dt
import pandas as pd

def main():
    
    dfs = pd.read_html('https://www.basketball-reference.com/teams/BOS/2020/gamelog/', header = 1)
    df = pd.DataFrame(dfs[0])
    df_1 = df.loc[df['Unnamed: 3'].isnull()]
    
    print(df_1)
    
    
    


    
    
    
if __name__=='__main__':
    main()