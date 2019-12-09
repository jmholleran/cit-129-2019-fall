"""
Joe Holleran
11/28/2019
Python 2 - Final Project
Web Scrap NBA Statistics to Evaluate ML Probabilities
"""
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from mltodec import convertmltodec as cmd
from kelly import oneKelly, halfKelly, fourthKelly
from mlToImpliedProbability import convertMLtoProb as cmprob
from monteCarlo import gameSim, gamesSimulator 

teamAbbrev = {'Atlanta Hawks': 'ATL', 'Boston Celtics': 'BOS', 'Brooklyn Nets': 'BRK',
              'Charlotte Hornets': 'CHO', 'Chicago Bulls': 'CHI', 'Cleveland Cavaliers': 'CLE',
              'Dallas Mavericks': 'DAL', 'Denver Nuggets': 'DEN', 'Detroit Pistons': 'DET',
              'Golden State Warriors': 'GSW', 'Houston Rockets': 'HOU', 'Indiana Pacers': 'IND',
              'Los Angeles Clippers': 'LAC', 'Los Angeles Lakers': 'LAL', 'Memphis Grizzlies':'MEM',
              'Miami Heat': 'MIA', 'Milwaukee Bucks': 'MIL', 'Minnesota Timberwolves': 'MIN',
              'New Orleans Pelicans': 'NOP', 'New York Knicks': 'NYK', 'Oklahoma City Thunder': 'OKC',
              'Orlando Magic': 'ORL', 'Philadelphia 76ers': 'PHI', 'Phoenix Suns': 'PHO',
              'Portland Trail Blazers': 'POR', 'Sacramento Kings': 'SAC', 'San Antonio Spurs': 'SAS',
              'Toronto Raptors': 'TOR', 'Utah Jazz': 'UTA', 'Washington Wizards': 'WAS'}

def main():
    
    while True:
        
        print("*********************** MAIN MENU ***********************" + "\n")
        print("1.) NBA Matchups Tonight")
        print("2.) Analysis: NBA Matchups Tonights")
        print("X.) Analysis: Enter Your Own Matchup")
        print("3.) EXIT" + "\n")
        
        print("*********************************************************" + "\n")
        
        try:
            user_select = int(input("Please choose one of the options above: "))
        except ValueError:
            user_select = int(input("Please choose one of the options above: "))
            
        # Call functions if user selects from menu; ask again if user selects
        # option outside 1-7
        if user_select < 1 or user_select > 3:
            user_select = int(input("Please choose one of the options above: "))
            if user_select == 3:
                print("------------EXIT--------------")
                break
        elif user_select == 1:
            today_matchups = getTodayMatchups()
            printTodayMatchups(today_matchups)
        elif user_select == 2:
            today_matchups = getTodayMatchups()
            
            for home, away in today_matchups.items():
                
                print(home, " vs. ", away)
                print("--------------------------------------------------" + "\n")
                
                homeTeam = home
                awayTeam = away
                
                matchupAnalysisGraph(homeTeam, awayTeam)                
                
                # Code Needed for implied Probabilities & Kelly Criterion
                
                homeML, awayML = getMoneyLines(homeTeam, awayTeam)
                homeDecOdd = cmd(homeML)
                awayDecOdd = cmd(awayML)
                homeImpliedProb = cmprob(homeML)
                awayImpliedProb = cmprob(awayML)
                
                displayImpliedProbs(homeTeam, awayTeam, homeImpliedProb, awayImpliedProb)
                
                # Monte Carlo Simulation DataFrames and data filtered by Home/Away
                
                homeDF = getTeamStatsDataFrame(homeTeam)
                awayDF = getTeamStatsDataFrame(awayTeam)
                                
                homeDF_filter = filterHomeTeamStatsDF(homeDF)
                awayDF_filter = filterAwayTeamStatsDF(awayDF)
                
                homeTeamPts_mu = getHomeTeamMeanPts(homeDF_filter)
                homeTeamPts_std = getHomeTeamStdDevPts(homeDF_filter)
                homeTeamOpp_mu = getHomeTeamOppMeanPts(homeDF_filter)
                homeTeamOpp_std = getHomeTeamOppStdDevPts(homeDF_filter)
                
                awayTeamPts_mu = getAwayTeamMeanPts(awayDF_filter)
                awayTeamPts_std = getAwayTeamStdDevPts(awayDF_filter)
                awayTeamOpp_mu = getAwayTeamOppMeanPts(awayDF_filter)
                awayTeamOpp_std = getAwayTeamOppStdDevPts(awayDF_filter)
                                
                homeSimProb, awaySimProb = gamesSimulator(10000, homeTeamPts_mu, homeTeamPts_std, homeTeamOpp_mu, homeTeamOpp_std, awayTeamPts_mu, awayTeamPts_std, awayTeamOpp_mu, awayTeamOpp_std)
                
                displaySimulationProbs(homeTeam, awayTeam, homeSimProb, awaySimProb)
                
                homeOneKelly, homeHalfKelly, homeFourthKelly, awayOneKelly, awayHalfKelly, awayFourthKelly = calcKellyCriterion(homeDecOdd, awayDecOdd, homeSimProb, awaySimProb)
                
                outputKellyCriterion(homeTeam, awayTeam, homeOneKelly, homeHalfKelly, homeFourthKelly, awayOneKelly, awayHalfKelly, awayFourthKelly)

                # Ask User if they would like to adjust the probability?
                # Use Bayesian Module
                # Output Adjusted Probability
                # Output Adjusted Kelly Criterion
                

                go_to_main = input("Press enter to continue to next matchup..." + "\n")


        else:
            print("------------EXIT--------------")
            break
         
        # Go back to main function after viewing section by pressing enter
        go_to_main = input("Press enter to continue to return to MAIN MENU... ")
        
        if go_to_main == " ":
            main()   
            
def calcKellyCriterion(homeDecOdd, awayDecOdd, homeSimProb, awaySimProb):

    homeOneKelly = oneKelly(homeSimProb, homeDecOdd)
    homeHalfKelly = halfKelly(homeSimProb, homeDecOdd)
    homeFourthKelly = fourthKelly(homeSimProb, homeDecOdd)
    
    awayOneKelly = oneKelly(awaySimProb, homeDecOdd)
    awayHalfKelly = halfKelly(awaySimProb, homeDecOdd)
    awayFourthKelly = fourthKelly(awaySimProb, homeDecOdd)
    
    return homeOneKelly, homeHalfKelly, homeFourthKelly, awayOneKelly, awayHalfKelly, awayFourthKelly
                    
def outputKellyCriterion(homeTeam, awayTeam, homeOneKelly, homeHalfKelly, homeFourthKelly, awayOneKelly, awayHalfKelly, awayFourthKelly):
    
    print(homeTeam + " One Kelly: " + str(round(homeOneKelly, 4)))
    print(homeTeam + " Half Kelly: " + str(round(homeHalfKelly, 4)))
    print(homeTeam + " Fourth Kelly: " + str(round(homeFourthKelly, 4)) + "\n")
    print(awayTeam + " One Kelly: " + str(round(awayOneKelly, 4)))
    print(awayTeam + " Half Kelly: " + str(round(awayHalfKelly, 4)))
    print(awayTeam + " Fourth Kelly: " + str(round(awayFourthKelly, 4)))
    
def displaySimulationProbs(homeTeam, awayTeam, homeSimProb, awaySimProb):
    
    print("The Simulation Probabilities are: " + "\n")
    
    homeSimProb = homeSimProb * 100
    awaySimProb = awaySimProb * 100
    
    print(homeTeam + " " + str(round(homeSimProb, 2)) + "%")
    print(awayTeam + " " + str(round(awaySimProb, 2)) + "%" + "\n")
            
def displayImpliedProbs(homeTeam, awayTeam, homeProb, awayProb):
    
    print("\n" + "The Moneyline Implied Probabilities are: " + "\n")
    
    homeProb = homeProb * 100
    awayProb = awayProb * 100
    
    print(homeTeam + " " + str(round(homeProb, 3)) + "%")
    print(awayTeam + " " + str(round(awayProb, 3)) + "%" + "\n")
            
def getMoneyLines(homeTeam, awayTeam):
    
    while True:
        
        try:
            homeML = int(input("Enter " + homeTeam + " Moneyline: "))
    
            if homeML < -1000000 or homeML > 1000000:
                homeML = int(input("Enter " + homeTeam + " Moneyline: "))
        except ValueError:
         
            homeML = int(input("Enter " + homeTeam + " Moneyline: "))
    
            if homeML < -1000000 or homeML > 1000000:
                homeML = int(input("Enter " + homeTeam + " Moneyline: "))
    
        try:
            awayML = int(input("Enter " + awayTeam + " Moneyline: "))
    
            if awayML < -1000000 or awayML > 1000000:
                homeML = int(input("Enter " + awayTeam + " Moneyline: "))
        except ValueError:
         
            awayML = int(input("Enter " + awayTeam + " Moneyline: "))
    
            if awayML < -1000000 or awayML > 1000000:
                awayML = int(input("Enter " + awayTeam + " Moneyline: "))
                
        print("\n" + "You Entered the Following Moneylines: " + "\n" + homeTeam + ": " + str(homeML) + "\n" + awayTeam + ": " + str(awayML))
        
        checkML = input("Are those the correct Moneylines? (Y/N): ")
        
        if checkML.upper() == "Y":
            break
        else:
            continue
        
    return homeML, awayML
            
def matchupAnalysisGraph(homeTeam, awayTeam):
    
    homeDF = getTeamStatsDataFrame(homeTeam)
    awayDF = getTeamStatsDataFrame(awayTeam)
                
    home_graph_tm_pts = getHomeGraphTmPts(homeDF)
    home_graph_opp_pts = getHomeGraphOppPts(homeDF)
    home_graph_game_num = getHomeGraphGmNum(homeDF)
    
    displayGraph(homeTeam, home_graph_game_num, home_graph_tm_pts, 
                 home_graph_opp_pts)                
                
    away_graph_tm_pts = getAwayGraphTmPts(awayDF)
    away_graph_opp_pts = getAwayGraphOppPts(awayDF)
    away_graph_game_num = getHomeGraphGmNum(awayDF)
    
    displayGraph(awayTeam, away_graph_game_num, away_graph_tm_pts, 
                 away_graph_opp_pts)   

def displayGraph(teamName, gameNum, teamPts, oppPts):
    
    plt.plot(gameNum, teamPts, color='black', label=teamName + ' Points')
    plt.plot(gameNum, oppPts, color='gray', label='Opponent Points')
    plt.xticks(range(0, (len(gameNum) + 2), 1))
    plt.yticks(range(80, 150, 5))
    plt.xlabel('Games 1 to ' + (str(len(gameNum))))
    plt.ylabel('Total Points Scored')
    plt.title(teamName + ' Previous ' + str(len(gameNum)) + ' Games')
    plt.legend()
    plt.show()

def getHomeGraphTmPts(homeDF):
    
    homeDF_1 = homeDF['Tm']
    
    homeGraphTmPtsDF = pd.to_numeric(homeDF_1, errors='coerce')
    
    homeGraphTmPtsDF = homeGraphTmPtsDF.dropna()

    return homeGraphTmPtsDF
    
def getHomeGraphOppPts(homeDF): 
    
    homeDF_1 = homeDF['Opp.1']
    
    homeGraphOppPtsDF = pd.to_numeric(homeDF_1, errors='coerce')
    
    homeGraphOppPtsDF = homeGraphOppPtsDF.dropna()
    
    return homeGraphOppPtsDF

def getHomeGraphGmNum(homeDF):
    
    homeDF_1 = homeDF['G']

    homeGraphGameNum = pd.to_numeric(homeDF_1, errors='coerce')
    
    homeGraphGameNum = homeGraphGameNum.dropna()
    
    return homeGraphGameNum

def getAwayGraphTmPts(awayDF):
    
    awayDF_1 = awayDF['Tm']
    
    awayGraphTmPtsDF = pd.to_numeric(awayDF_1, errors='coerce') 
    
    awayGraphTmPtsDF = awayGraphTmPtsDF.dropna()
    
    return awayGraphTmPtsDF

def getAwayGraphOppPts(awayDF):
    
    awayDF_1 = awayDF['Opp.1']
    
    awayGraphOppPtsDF = pd.to_numeric(awayDF_1, errors='coerce')
    
    awayGraphOppPtsDF = awayGraphOppPtsDF.dropna()
    
    return awayGraphOppPtsDF

def getAwayGraphGmNum(awayDF):
    
    awayDF_1 = awayDF['G']
    
    awayGraphGameNum = pd.to_numeric(awayDF_1, errors='coerce')
    
    awayGraphGameNum = awayGraphGameNum.dropna()
    
    return awayGraphGameNum

def getHomeTeamMeanPts(filteredHomeDF):
    
    filteredHomeDF_1 = filteredHomeDF['Tm']
    
    removeStringDF = pd.to_numeric(filteredHomeDF_1, errors='coerce')
    
    homeTeamPtsMu = removeStringDF.mean()
    
    return homeTeamPtsMu
    
def getHomeTeamStdDevPts(filteredHomeDF):
    
    filteredHomeDF_1 = filteredHomeDF['Tm']
    
    removeStringDF = pd.to_numeric(filteredHomeDF_1, errors='coerce')
    
    homeTeamStdDevPts = removeStringDF.std()

    return homeTeamStdDevPts
    
def getHomeTeamOppMeanPts(filteredHomeDF):
    
    filteredHomeDF_1 = filteredHomeDF['Opp.1']
    
    removeStringDF = pd.to_numeric(filteredHomeDF_1, errors='coerce')
    
    homeTeamOppMeanPts = removeStringDF.mean()
    
    return homeTeamOppMeanPts
    
def getHomeTeamOppStdDevPts(filteredHomeDF):
    
    filteredHomeDF_1 = filteredHomeDF['Opp.1']
    
    removeStringDF = pd.to_numeric(filteredHomeDF_1, errors='coerce')
    
    homeTeamOppStdDevPts = removeStringDF.std()
    
    return homeTeamOppStdDevPts
    
def getAwayTeamMeanPts(filteredAwayDF):
    
    filteredAwayDF_1 = filteredAwayDF['Tm']
    
    removeStringDF = pd.to_numeric(filteredAwayDF_1, errors='coerce')
    
    awayTeamPtsMu = removeStringDF.mean()
    
    return awayTeamPtsMu
    
def getAwayTeamStdDevPts(filteredAwayDF):
    
    filteredAwayDF_1 = filteredAwayDF['Tm']
    
    removeStringDF = pd.to_numeric(filteredAwayDF_1, errors='coerce')
    
    awayTeamPtsMu = removeStringDF.std()
    
    return awayTeamPtsMu
    
def getAwayTeamOppMeanPts(filteredAwayDF):
    
    filteredAwayDF_1 = filteredAwayDF['Opp.1']
    
    removeStringDF = pd.to_numeric(filteredAwayDF_1, errors='coerce')
    
    awayTeamPtsMu = removeStringDF.mean()
    
    return awayTeamPtsMu
    
def getAwayTeamOppStdDevPts(filteredAwayDF): 
    
    filteredAwayDF_1 = filteredAwayDF['Opp.1']
    
    removeStringDF = pd.to_numeric(filteredAwayDF_1, errors='coerce')
    
    awayTeamPtsMu = removeStringDF.std()
    
    return awayTeamPtsMu    

def filterHomeTeamStatsDF(homeDF):
    
    homeDF_filter = homeDF.loc[homeDF['Unnamed: 3'].isnull()]
    
    return homeDF_filter
    
def filterAwayTeamStatsDF(awayDF):
    
    awayDF_filter = awayDF.loc[awayDF['Unnamed: 3'].isin(['@'])]
    
    return awayDF_filter
    
def getTeamStatsDataFrame(team):
    
    teamSym = convertTeamNameToSym(team)
    
    teamURL = buildTeamStatsURL(teamSym)
    
    teamDF = buildTeamStatsDataFrame(teamURL)
    
    return teamDF
    
def getTodayMatchups():    
    
    urlMonth = getMonthURL()
    schedURL = buildScheduleURL(urlMonth)
    schedDF = buildSchedDataFrame(schedURL)
    todaySched = getTodaySchedSearch()
    homeTeams = getHomeTeams(todaySched, schedDF)
    awayTeams = getAwayTeams(todaySched, schedDF)
    matchups = getTodayMatchupDict(homeTeams, awayTeams)
    
    return matchups

def getMonthURL():
    
    # Source for datetime = https://docs.python.org/2/library/datetime.html
    # Function Purpose: Return Month for the Basketball Reference Schedule URL
    
    today = dt.date.today()
    urlMonth = today.strftime('%B')
    
    return urlMonth

def buildScheduleURL(urlMonth):
    
    # Function Purpose: Return URL for the Basketball Reference Schedule
    # Use month from getMonthURL
    
    lowerMonth = (str(urlMonth)).lower()
    
    schedURL = 'https://www.basketball-reference.com/leagues/NBA_2020_games-'+ str(lowerMonth) + '.html'
    
    return schedURL

def buildSchedDataFrame(url):
    
    # Function Purpose: Generic Function to Build a DataFrame when given a URL

    dfs = pd.read_html(url)
    df = pd.DataFrame(dfs[0])
    df.set_index('Date', inplace=True)
    
    return df

def getTodaySchedSearch():
    
    # Function Purpose: To Build String to Search Basketball Reference DataFrame
    # For Game's Being Played 'Today'
    
    today = dt.date.today()
    
    weekDay = today.strftime('%a')
    month = today.strftime('%b')
    day = today.strftime('%d')
    day = day.lstrip('0').replace('0', '')
    year = today.strftime('%Y')
    
    todaySearch = str(weekDay + ', ' + month + ' ' + day + ', ' + year)
    
    return todaySearch

def getHomeTeams(today, df):
    
    try:
    
        dfsearch = df.loc[[today], ['Home/Neutral']]
        
        homeTeams = []

        for home in dfsearch['Home/Neutral']:
            homeTeams.append(home)
            
        return homeTeams
            
    except KeyError:
    
        print('There are no games today: ' + today)  
    

def getAwayTeams(today, df):
    
    try:
    
        dfsearch = df.loc[[today], ['Visitor/Neutral']]
        
        awayTeams = []

        for away in dfsearch['Visitor/Neutral']:
            awayTeams.append(away)
            
        return awayTeams
            
    except KeyError:
    
        print('There are no games today: ' + today)  
        
def getTodayMatchupDict(homeTeams, awayTeams):
    
    matchups = {}
    
    for home in homeTeams:
        for away in awayTeams:
            matchups[home] = away
            awayTeams.remove(away)
            break
        
    return matchups

def printTodayMatchups(matchups):
    
    count = 1
    
    for home, away in matchups.items():
        print('GAME ', count)
        print('Home Team: ', home)
        print('Away Team: ', away, "\n")
        count += 1
        
def convertTeamNameToSym(teamName):
    
    teamSym = teamAbbrev[teamName]

    return teamSym

def buildTeamStatsURL(teamSym):
    
    url = 'https://www.basketball-reference.com/teams/' + str(teamSym) + '/2020/gamelog/'
    
    return url

def buildTeamStatsDataFrame(url):
    
    # Function Purpose: Generic Function to Build a DataFrame when given a URL
    dfs = pd.read_html(url, header = 1)
    df = pd.DataFrame(dfs[0])
    
    return df


if __name__=='__main__':
    main()