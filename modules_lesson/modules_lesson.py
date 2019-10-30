"""
Modules Lesson
10/30/2019
"""
from boo import happyHalloween
from netwins import win_percent
from mltodec import convertmltodec as cmd
from kelly import oneKelly, halfKelly, twoKelly


def main():
    
    #boo_example()
    #print("************\n\n")
    #netwins_example()
    #print("************\n\n")
    #mlToDecOdds_example()
    #print("************\n\n")
    #kellyCriterion_example()
    #print("************\n\n")
    #tryYourOwnModule()
    
def boo_example():

    print(happyHalloween())
    
def netwins_example():
    
    # Determine expected wins over 82-games for NBA team using Net Rating

    # Los Angeles Lakers current (10/30) Net Rating
    net_rate = 11.1

    exp_win_percent = win_percent(net_rate)
    exp_wins = exp_win_percent * 82

    print("Expected Win Percentage: ", exp_win_percent)
    print("Expected Wins: ", exp_wins)
    
def mlToDecOdds_example():

    # Convert moneyline odds to decimal odds
    # Positive moneyline is payout on $100 bet
    # Negative moneyline is amount you would need to bet to win $100
    
    # Memphis Grizzlies at Los Angeles Lakers on 10/29/2019
    away_team_ml = 575
    home_team_ml = -850
    
    global away_dec_odds
    global home_dec_odds
    
    away_dec_odds = cmd(away_team_ml)
    home_dec_odds = cmd(home_team_ml)

    print("Away Team Decimal Odds: ", away_dec_odds)
    print("Home Team Decimal Odds: ", home_dec_odds)

def kellyCriterion_example():

    # Input probability and decimal odds to return Kelly Criterion
    # Kelly Criterion negative is unfavorable bet; Kelly Criterion positive is amount of bankroll to bet

    # Away team prob = 100 / (575 + 100)
    away_team_prob = .1481
    # Home team prob = -850 / (-850 - 100)
    home_team_prob = .8947

    # oneKelly ; halfKelly ; twoKelly

    away_kelly = oneKelly(away_team_prob, away_dec_odds)
    print("Away Team Kelly Criterion: ", away_kelly)
    away_halfKelly = halfKelly(away_team_prob, away_dec_odds)
    print("Away Team 1/2 Kelly Criterion: ", away_halfKelly)
    away_twoKelly = twoKelly(away_team_prob, away_dec_odds)
    print("Away Team 2 Kelly Criterion: ", away_twoKelly)
    print("*********************************************")
    home_kelly = oneKelly(home_team_prob, home_dec_odds)
    print("Home Team Kelly Criterion: ", home_kelly)
    home_halfKelly = halfKelly(home_team_prob, home_dec_odds)
    print("Home Team 1/2 Kelly Criterion: ", home_halfKelly)
    home_twoKelly = twoKelly(home_team_prob, home_dec_odds)
    print("Home Team 2 Kelly Criterion: ", home_twoKelly)
    
def tryYourOwnModule():
    
    print("\nBuild your own module using one of the following criteria:\n")
    print("1. Create a module using code you have already written\n")
    print("2. Create a module to modify a string, such as:\n"
          "\n\ta. Take in a string and change any instance of 'you' to 'yinz'")
    print("\n3. Create a module to apply an equation or run a calculation, such as:\n"
          "\n\ta. Equations similar to previous examples (Kelly Criterion, Moneyline to Decimal Odds)\n"
          "\tb. Grade Criteria Module: Take in Average/Mean Grade and output Letter Grade"
          "\n\tc. Calculation or equation of your choosing")

if __name__=='__main__':
    main()