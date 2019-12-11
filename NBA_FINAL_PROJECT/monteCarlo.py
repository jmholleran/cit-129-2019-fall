# Monte Carlo Simulation
# Simulation Code & Monte Carlo Concepts from two sources:
# MIT 6.0002 Introduction to Computational Thinking and Data Science, Fall 2016 by John Guttag: https://www.youtube.com/watch?v=OgO1gpXSUzU
# "How to Simulate NBA Games in Python" by Ken Jee: https://www.youtube.com/watch?v=irjTWNV0eAY
# Code was changed to reflect Score Differential then apply to the Score instead of averaging as in Ken Jee video as it yields 3-4% differences

# Import NumPy module for random.normal
import numpy as np

# Single Game Simulation Function - Take in Home Team & Away Team Pts & Opp Mu, Std
def gameSim(homePts_mu, homePts_std, homeOpp_mu, homeOpp_std, awayPts_mu, awayPts_std, awayOpp_mu, awayOpp_std):
    
    while True:
        
        # Create variables for Home/Away Pts & Opp Pts
        # Use np.random.normal to create a random sample from normal distribution 
        # of Home/Away Pts & Opp Pts
        homePts = np.random.normal(homePts_mu, homePts_std)
        homeOpp = np.random.normal(homeOpp_mu, homeOpp_std)
        awayPts = np.random.normal(awayPts_mu, awayPts_std)
        awayOpp = np.random.normal(awayOpp_mu, awayOpp_std)
    
        # Home/Away Score Differential takes random sample of Pts Scored and
        # Opp Pts Scored and returns either a positive or negative value
        # Example: Home Team scores 115 and Opp Gives Up 125 
        # Example: The 'differential' would be 10 ; accounts for playing
        # teams with strong/weak defenses in theory
        homeScoreDiff = (homePts) - (awayOpp)
        awayScoreDiff = (awayPts) - (homeOpp)
        
        # The Final Score (Home/Away Score) takes the random sample of the
        # Home/Away Pts and applies the differential
        homeScore = (homePts) + (homeScoreDiff)
        awayScore = (awayPts) + (awayScoreDiff)
        
        # If Home Score greater than Away Score then the home team wins
        # If Away Score greater than Home Score then the away team wins
        if int(round(homeScore)) > int(round(awayScore)):
            return 1
            break
        elif int(round(homeScore)) < int(round(awayScore)):
            return -1
            break
        else:
            continue

# Monte Carlo Simulation - runs the game simulation N number of times
# 10,000 used as tested several large values and minor differences after 10,000 samples
def gamesSimulator(n, homePts_mu, homePts_std, homeOpp_mu, homeOpp_std, awayPts_mu, awayPts_std, awayOpp_mu, awayOpp_std):
    
    # Collect the Home/Away wins totals
    homeTeamWins = 0
    awayTeamWins = 0
    
    # For loop for Monte Carlo Simulation - N = number of times to simulate
    for game in range(n):
        
        # One_Sim = The result of one game simulation
        one_sim = gameSim(homePts_mu, homePts_std, homeOpp_mu, homeOpp_std, awayPts_mu, awayPts_std, awayOpp_mu, awayOpp_std)
        
        # If the Home Team Wins then add to Home Wins & vice versa for Away Team
        if one_sim == 1:
            homeTeamWins += 1
        elif one_sim == -1:
            awayTeamWins += 1
    
    # Calculate the Home/Away results from the Monte Carlo Simulation (Probability)
    # Based on 10,000 simulations of the game    
    homeTeamSimProb = (homeTeamWins) / (awayTeamWins + homeTeamWins)
    awayTeamSimProb = (awayTeamWins) / (awayTeamWins + homeTeamWins)
    
    # Return the results of the simulation - Home/Away Probability
    return homeTeamSimProb, awayTeamSimProb
    


            

    