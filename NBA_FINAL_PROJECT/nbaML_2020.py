"""
Joe Holleran
11/28/2019
Python 2 - Final Project
Web Scrap NBA Stats to Evaluate ML Probabilities
"""
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib as plt
from mltodec import convertmltodec as cmd
from kelly import oneKelly, halfKelly, fourthKelly

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
        print("3.) EXIT" + "\n")
    
        user_select = int(input("Please choose one of the options above: "))
        print()
        
        # Call functions if user selects from menu; ask again if user selects
        # option outside 1-7
        if user_select < 1 or user_select > 3:
            user_select = int(input("Please choose one of the options above: "))
        elif user_select == 1:
            today_matchups = getTodayMatchups()
            printTodayMatchups(today_matchups)
        elif user_select == 2:
            today_matchups = getTodayMatchups()
            
            for home, away in today_matchups.items():
                homeTeam = home
                awayTeam = away
                
                homeSym = convertTeamNameToSym(homeTeam)
                awaySym = convertTeamNameToSym(awayTeam)
                
                homeURL = buildTeamStatsURL(homeSym)
                awayURL = buildTeamStatsURL(awaySym)
                
                homeDF = buildTeamStatsDataFrame(homeURL)
                awayDF = buildTeamStatsDataFrame(awayURL)
                
                homeDF_1 = homeDF.loc[homeDF['Unnamed: 3'].isnull()]
                awayDF_1 = awayDF.loc[awayDF['Unnamed: 3'].isin(['@'])]
                
                print(home, homeDF_1['Tm'])
                print(away, awayDF_1['Tm'])
                
                
                

        else:
            print("Thanks and have a nice day!")   
            print("------------EXIT--------------")
            break
         
        # Go back to main function after viewing section by pressing enter
        go_to_main = input("Press enter to continue... ")
        
        if go_to_main == " ":
            main()   

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