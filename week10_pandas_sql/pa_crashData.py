# -*- coding: utf-8 -*-
"""
Joe Holleran
PA Crash Test Data
11/17/2019
"""
import pandas as pd

df_hundred = pd.read_csv(r'C:\Users\joeyh\analytics_large_data_files\pa_crash_dataset.zip', chunksize=100000)

df_list = []

for hundred in df_hundred:
    
    df_list.append(hundred)
    
df_concat = pd.concat(df_list)




