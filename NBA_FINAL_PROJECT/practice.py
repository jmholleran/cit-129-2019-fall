# -*- coding: utf-8 -*-
"""
Practice Functions for Final Project
"""
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from mltodec import convertmltodec as cmd
import numpy as np
import random as rnd
from monteCarlo import gameSim, gamesSimulator 

def main():
    
    dfs = pd.read_html('https://www.basketball-reference.com/teams/LAL/2020/gamelog/', header = 1)
    df = pd.DataFrame(dfs[0])
      
    df_2 = df['Tm']
    
    df_3 = df['Opp.1']
    
    name = 'Los Angeles Lakers'
    
    tm_pts = pd.to_numeric(df_2, errors='coerce')
    tm_pts = tm_pts.dropna()
    tm_pts_mu = tm_pts.mean()
    tm_pts_std = tm_pts.std()
    
    opp_pts = pd.to_numeric(df_3, errors='coerce')
    opp_pts = opp_pts.dropna()
    opp_pts_mu = opp_pts.mean()
    opp_pts_std = opp_pts.std()
    
    dfs_11 = pd.read_html('https://www.basketball-reference.com/teams/BOS/2020/gamelog/', header = 1)
    df_11 = pd.DataFrame(dfs_11[0])
    
    name_1 = 'Boston Celtics'
    
    df_2_11 = df_11['Tm']
    
    df_3_11 = df_11['Opp.1']
    
    tm_pts_11 = pd.to_numeric(df_2_11, errors='coerce')
    tm_pts_11 = tm_pts_11.dropna()
    tm_pts_mu_11 = tm_pts_11.mean()
    tm_pts_std_11 = tm_pts_11.std()
  
    opp_pts_11 = pd.to_numeric(df_3_11, errors='coerce')
    opp_pts_11 = opp_pts_11.dropna()
    opp_pts_mu_11 = opp_pts_11.mean()
    opp_pts_std_11 = opp_pts_11.std()
    
    
    homeSimProb, awaySimProb = gamesSimulator(10000, tm_pts_mu, tm_pts_std, opp_pts_mu, opp_pts_std, tm_pts_mu_11, tm_pts_std_11, opp_pts_mu_11, opp_pts_std_11)

    print(name, ": ", homeSimProb)
    print(name_1, ": ", awaySimProb)
    
    
    


    
    # MONDAY
    # 1.5 HR
    # Ask user to adjust probability from prior results?
    # using.... Bayes Theorem Module
    # Output new Probability
    # Output adjusted Kelly Criterion using new Probability
    # 1 HR
    # Option 3 = Analyze Particular Matchup
    # 2 HR
    # Output to Excel - given the dates and matchups are not there
    
    
    # TUESDAY
    # 5-7PM
    # DOCUMENTATION & COMMENTS
    # BE SURE TO DOCUMENT YOUTUBE VIDEOS: MIT LECTURES & KEN'S MONTE CARLO SIM
    # 7-8PM
    # SOURCES
    # 8-9PM
    # README
    # 9-1030PM
    # SLIDES & PRESTENTATION
    # MONEYLINES FOR WEDNESDAY GAMES
    
    # IF ENOUGH TIME AFTER EVERYTHING ELSE IS COMPLETE
    # Bayes Theorem - search for probabilities in the excel file
    
    
    


    
    
    
if __name__=='__main__':
    main()