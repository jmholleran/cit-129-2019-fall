"""
Modules Lesson
10/31/2019
"""

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
    
    from boo import happyHalloween

    print(happyHalloween())
    
def netwins_example():
    
    # Determine expected wins over 82-games for NBA team using Net Rating

    from netwins import win_percent

    net_rate = 2.4

    exp_wins = win_percent(net_rate)

    print("Expected Wins: ", exp_wins)
    
def mlToDecOdds_example():

    # Convert moneyline odds to decimal odds
    # Positive moneyline is payout on $100 bet
    # Negative moneyline is amount to bet to win $100

    from mltodec import convertmltodec as cmd
    
    # Memphis Grizzlies at Los Angeles Lakers on 10/30/2019
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
    from kelly import oneKelly, halfKelly, twoKelly as K1, KH, K2

    # Away team prob = 100 / (575 + 100)
    away_team_prob = .1481
    # Home team prob = -850 / (-850 - 100)
    home_team_prob = .8947

    # oneKelly ; halfKelly ; twoKelly

    away_kelly = K1(away_team_prob, away_dec_odds)
    print("Away Team Kelly Criterion: ", away_kelly)
    away_halfKelly = KH(away_team_prob, away_dec_odds)
    print("Away Team 1/2 Kelly Criterion: ", away_halfKelly)
    away_twoKelly = K2(away_team_prob, away_dec_odds)
    print("Away Team 2 Kelly Criterion: ", away_twoKelly)
    print("*********************************************")
    home_kelly = K1(home_team_prob, home_dec_odds)
    print("Home Team Kelly Criterion: ", home_kelly)
    home_halfKelly = KH(home_team_prob, home_dec_odds)
    print("Home Team 1/2 Kelly Criterion: ", home_halfKelly)
    home_twoKelly = K2(home_team_prob, home_dec_odds)
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