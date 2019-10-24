# -*- coding: utf-8 -*-
"""
Joe Holleran
10/23/2019
In-class Coding: pandas, numpy, matplotlib
"""
import pandas as pd
import numpy as np
import matplotlib as plt
from pandas import DataFrame, Series
import csv

# Numpy 
# Column = Series ; entire set of columns = DataFrame

seriesObj = Series([80000, 60000, 340666, 21000000],['Indian', 'Greek', 'Latin', 'Chili'])
print(seriesObj)
print(seriesObj.max())
  
energy_df = pd.read_csv('usaPowerSources2001-2018.csv')
print(energy_df.wind.describe())

print(energy_df.solar.plot())


    
