# -*- coding: utf-8 -*-
"""
Practice Functions for Final Project
"""
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    dfs = pd.read_html('https://www.basketball-reference.com/teams/PHI/2020/gamelog/', header = 1)
    df = pd.DataFrame(dfs[0])
    
    """
    df_1 = df.loc[df['Unnamed: 3'].isnull()]
    """
    
    df_2 = df['Tm']
    
    df_3 = df['Opp.1']
    
    df_4 = df['G']
    
    name = 'Philadelphia 76ers'
    
    tm_pts = pd.to_numeric(df_2, errors='coerce')
    tm_pts = tm_pts.dropna()
    opp_pts = pd.to_numeric(df_3, errors='coerce')
    opp_pts = opp_pts.dropna()
    gm_num = pd.to_numeric(df_4, errors='coerce')
    gm_num = gm_num.dropna()    

    
    plt.plot(gm_num, tm_pts, color='blue', label=name + ' Points')
    plt.plot(gm_num, opp_pts, color='red', label='Opponent Points')
    plt.xticks(range(0, (len(gm_num) + 2), 2))
    plt.title(name + ' Previous ' + str(len(gm_num)) + ' Games')
    plt.legend()
    plt.show()

    
    """
    plt.plot(year,price, label="S&P 500", color = "blue")
    plt.xlabel("Year")
    plt.ylabel("S&P 500 Price")
    plt.title("S&P 500 from 1928 to 2018")
    plt.xticks(range(1928, 2019, 10))
    plt.legend()
    plt.show()
    """
    

    # SATURDAY/SUNDAY
    # 1 HOUR
    # Ask User to Enter Home Team Moneyline
    # Ask User to Enter Away Team Moneyline
    # Convert Home Team Moneyline to Decimal Odds
    # Convert Away Team Moneyline to Decimal Odds
    # Convert Home Team Moneyline to Implied Probability
    # Convert Away Team Moneyline to Implied Probability
    
    # SUNDAY 
    # 3 HOURS
    # Monte Carlo Simulation Modules
    # Take Monte Carlo results and show probabilities
    # Show Kelly Criterion for Model
    
    # SUNDAY
    # 2 HOURS
    # Ask user to adjust probability from prior results?
    # Bayes Theorem Module
    # Output new Probability
    # Output adjusted Kelly Criterion using new Probability
    
    # SUNDAY
    # 1 HOUR
    # Packup Everything into Functions
    # Continue to Next Matchup
    
    # MONDAY
    # 3 HOURS
    # Option 3 = Analyze Particular Matchup
    # Output to Excel - given the dates and matchups are not there
    
    
    # TUESDAY
    # 4 HOURS
    # DOCUMENTATION & COMMENTS
    # BE SURE TO DOCUMENT YOUTUBE VIDEOS: MIT LECTURES & KEN'S MONTE CARLO SIM
    # SOURCES
    # README
    # SLIDES & PRESTENTATION
    # MONEYLINES FOR WEDNESDAY GAMES
    
    # IF ENOUGH TIME AFTER EVERYTHING ELSE IS COMPLETE
    # Bayes Theorem - search for probabilities in the excel file
    
    
    


    
    
    
if __name__=='__main__':
    main()