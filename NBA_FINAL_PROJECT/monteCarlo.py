# Monte Carlo Simulation
# Simulation Code & Monte Carlo Concepts from two sources:
# MIT 6.0002 Introduction to Computational Thinking and Data Science, Fall 2016 by John Guttag: https://www.youtube.com/watch?v=OgO1gpXSUzU
# "How to Simulate NBA Games in Python" by Ken Jee: https://www.youtube.com/watch?v=irjTWNV0eAY
# Code was changed to reflect Score Differential then apply to the Score instead of averaging as in Ken Jee video as it yields 3-4% differences

import numpy as np

def gameSim(homePts_mu, homePts_std, homeOpp_mu, homeOpp_std, awayPts_mu, awayPts_std, awayOpp_mu, awayOpp_std):
    
    while True:
    
        homeScoreDiff = (np.random.normal(homePts_mu, homePts_std)) - (np.random.normal(awayOpp_mu, awayOpp_std))
        awayScoreDiff = (np.random.normal(awayPts_mu, awayPts_std)) - (np.random.normal(homeOpp_mu, homeOpp_std))
        
        homeScore = ((np.random.normal(homePts_mu, homePts_std)) + homeScoreDiff)
        awayScore = ((np.random.normal(awayPts_mu, awayPts_std)) + awayScoreDiff)
        
        if int(round(homeScore)) > int(round(awayScore)):
            return 1
            break
        elif int(round(homeScore)) < int(round(awayScore)):
            return -1
            break
        else:
            continue
    
def gamesSimulator(n, homePts_mu, homePts_std, homeOpp_mu, homeOpp_std, awayPts_mu, awayPts_std, awayOpp_mu, awayOpp_std):
    
    homeTeamWins = 0
    awayTeamWins = 0
    
    for game in range(n):
        
        one_sim = gameSim(homePts_mu, homePts_std, homeOpp_mu, homeOpp_std, awayPts_mu, awayPts_std, awayOpp_mu, awayOpp_std)

        if one_sim == 1:
            homeTeamWins += 1
        elif one_sim == -1:
            awayTeamWins += 1
            
    homeTeamSimProb = (homeTeamWins / (awayTeamWins + homeTeamWins))
    awayTeamSimProb = (awayTeamWins / (awayTeamWins + homeTeamWins))
    
    return homeTeamSimProb, awayTeamSimProb
    


            

    