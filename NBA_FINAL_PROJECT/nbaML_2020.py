"""
Joe Holleran
Python 2 - Final Project (12/11/2019)
Web Scrap NBA Statistics to Evaluate ML Probabilities
"""
# Import modules
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from mltodec import convertmltodec as cmd
from kelly import oneKelly, halfKelly, fourthKelly
from mlToImpliedProbability import convertMLtoProb as cmprob
from monteCarlo import gamesSimulator 
import csv
##############################################################################

# Team Abbreviations for Display and URL's
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
    
    # Main Menu Loop
    
    while True:
        
        # User has Four Options within the program: View NBA matchups today,
        # Analyze all of the matchups to be played today, Analyze an individual
        # matchup or EXIT
        print("*********************** MAIN MENU ***********************" + "\n")
        print("1.) NBA Matchups Tonight: " + str(getTodaySchedSearch()))
        print("2.) Analysis: NBA Matchups Tonight: " + str(getTodaySchedSearch()))
        print("3.) Analysis: Enter Your Own NBA Matchup")
        print("4.) EXIT" + "\n")
        
        print("*********************************************************" + "\n")
        
        # Input Validation 
        try:
            user_select = int(input("Please choose one of the options above: "))
        except ValueError:
            user_select = int(input("Please choose one of the options above: "))
            
        # Call functions if user selects from menu; ask again if user selects
        if user_select < 1 or user_select > 4:
            user_select = int(input("Please choose one of the options above: "))
            if user_select == 3:
                print("------------EXIT--------------")
                break
        elif user_select == 1:
            # Prints out the NBA Matchups Today using the getTodayMatchups function
            today_matchups = getTodayMatchups()
            printTodayMatchups(today_matchups)
        elif user_select == 2:
            # Get today's matchups from getTodayMatchups function
            today_matchups = getTodayMatchups()
            
            # Iterate through the getTodayMatchups dictionary
            for home, away in today_matchups.items():
                
                # Display the individual matchup to be analyzed
                print(home, " vs. ", away)
                print("--------------------------------------------------" + "\n")
                
                # Run matchup analysis function - See Function Description Below
                runMatchupAnalysis(home, away)
                
                # Give User the Option to continue through analysis or Exit after each matchup
                continue_analysis = input("Press enter to continue to next matchup... (X to Exit)" + "\n")
                if continue_analysis == "x" or continue_analysis == "X":
                    break
                
        elif user_select == 3:
            
            # Ask user to input an individual matchup using the getIndividualMatchup function
            home, away = getIndividualMatchup()
            
            # Display the individual matchup
            print(home, " vs. ", away)
            print("--------------------------------------------------" + "\n")
            
            # Run matchup analysis using individual matchup
            runMatchupAnalysis(home, away)
            
        else:
            print("------------EXIT--------------")
            break

        # Go back to main function after viewing section by pressing enter
        go_to_main = input("Press enter to continue to MAIN MENU... " + "\n")
        
        if go_to_main == " ":
            main()   
            
def writeMatchupDataToExcel(home_team, away_team, homeML, awayML, homeSimProb, awaySimProb):
    
    # Function purpose: to write analysis data to excel
    
    # Create Date variable - gets today's date in basketball reference format
    date = getTodaySchedSearch()   
   
    # Use Pandas to read CSV file and create variables for values to check in CSV file before appending
    check_file = pd.read_csv('nbaML_2020_MASTER.csv', header=0)
    df = pd.DataFrame(check_file)
    date_col = df['date']
    home_col = df['home_team']
    away_col = df['away_team']
    
    while True:
        
        excel_choice = input("Do you want to output this matchup data to Excel? (Y/N): ")
        
        if excel_choice == "Y" or excel_choice == "y":
            # Initialize check count
            check_count = 0
            
            # Loop through the date, home team, and away team columns
            # If all three items are already found in the CSV file then do not write to file
            for date_check in date_col:
                if date_check == date:
                    check_count += 1
    
            for home_check in home_col:
                if home_check == home_team:
                    check_count += 1
            
            for away_check in away_col:
                if away_check == away_team:
                    check_count += 1
    
            if check_count == 3:
                print("The matchup was previously uploaded to Excel.")
                break
            else:
                
                try:
                    # Write to Excel file if the check count does not equal 3
                    with open('nbaML_2020_MASTER.csv', 'a', newline='') as writeFile:
                        writeMatchupData = csv.writer(writeFile)
                        writeMatchupData.writerow([date, home_team, away_team, homeML, awayML, homeSimProb, awaySimProb])
                        break
                except PermissionError:
                        print("The CSV file is 'Open'. Please 'Close' and Try Again.")
        else:
            break

def getIndividualMatchup():
    
    # Function Purpose: allow user to input individual matchup
    
    # Display for user all Team Names and Symbols    
    print("\n" + "Team Name" + "\t" + "Symbol")
    for key, value in teamAbbrev.items():
        print(key, ":", value)
    
    # Ask User to input either a team name or symbol
    # If the user inputs a symbol (length = 3) then pass to getTeamNameFromSym function
    while True:
        try:
            home = input("Enter Home Team Name or Symbol: ")
            
            if type(home) != str:
               home = input("Enter Home Team Name or Symbol: ")
               break
            elif len(home) == 3:
                home = getTeamNameFromSym(home)
                break
        except ValueError:
            print("Please enter a valid Team Name or Symbol.")
            
    while True:
        try:
            away = input("Enter Away Team Name or Symbol: ")
            
            if type(away) != str:
                away = input("Enter Away Team Name or Symbol: ")
                break
            elif len(away) == 3:
                away = getTeamNameFromSym(away)
                break
        except ValueError:
            print("Please enter a valid Team Name or Symbol.")
            
    # Return home and away team names for matchup analysis
    
    return home, away

def getTeamNameFromSym(symbol):
    
    # For individual matchup analysis
    # If user inputs a symbol then the key is returned from TeamAbbrev dictionary
    
    try:
        
        for key, value in teamAbbrev.items():
            if symbol == value:
                teamName = key

    except ValueError:
        print("Please enter a valid team symbol.")
        
    # Return team name for matchup analysis        
    return teamName

def runMatchupAnalysis(home, away):
    
    # Main Matchup Analysis Function
    
    # Assign team names to variables homeTeam and awayTeam    
    homeTeam = home
    awayTeam = away
    
    # Display Matchup Analysis Graph
    matchupAnalysisGraph(homeTeam, awayTeam)         
     
    # Get home team and away team moneylines, convert to decimal odds, and
    # display the implied probabilities of the moneylines
    homeML, awayML = getMoneyLines(homeTeam, awayTeam)
    homeDecOdd = cmd(homeML)
    awayDecOdd = cmd(awayML)
    homeImpliedProb = cmprob(homeML)
    awayImpliedProb = cmprob(awayML)                
    displayImpliedProbs(homeTeam, awayTeam, homeImpliedProb, awayImpliedProb)
    
    # Assign the home and away Team Stats DataFrames to variable                
    homeDF = getTeamStatsDataFrame(homeTeam)
    awayDF = getTeamStatsDataFrame(awayTeam)
    
    # Filter the home and away dataframes for home or away status                                
    homeDF_filter = filterHomeTeamStatsDF(homeDF)
    awayDF_filter = filterAwayTeamStatsDF(awayDF)
    
    # Assign the variables for home/away team pts/opp pts mean and standard deviation
    # for the monte carlo simulation
    homeTeamPts_mu = getHomeTeamMeanPts(homeDF_filter)
    homeTeamPts_std = getHomeTeamStdDevPts(homeDF_filter)
    homeTeamOpp_mu = getHomeTeamOppMeanPts(homeDF_filter)
    homeTeamOpp_std = getHomeTeamOppStdDevPts(homeDF_filter)
                
    awayTeamPts_mu = getAwayTeamMeanPts(awayDF_filter)
    awayTeamPts_std = getAwayTeamStdDevPts(awayDF_filter)
    awayTeamOpp_mu = getAwayTeamOppMeanPts(awayDF_filter)
    awayTeamOpp_std = getAwayTeamOppStdDevPts(awayDF_filter)
    
    # Assign the variables for the Monte Carlo simulation - using mean/standard deviation and number of simulations                           
    homeSimProb, awaySimProb = gamesSimulator(10000, homeTeamPts_mu, homeTeamPts_std, homeTeamOpp_mu, homeTeamOpp_std, awayTeamPts_mu, awayTeamPts_std, awayTeamOpp_mu, awayTeamOpp_std)
    
    # Display the results of the Monte Carlo simulation
    displaySimulationProbs(homeTeam, awayTeam, homeSimProb, awaySimProb)
    
    # Assign the variables for the Kelly Criterion calculations                
    homeOneKelly, homeHalfKelly, homeFourthKelly = calcKellyCriterion(homeTeam, homeDecOdd, homeSimProb)
    awayOneKelly, awayHalfKelly, awayFourthKelly = calcKellyCriterion(awayTeam, awayDecOdd, awaySimProb) 
    outputKellyCriterion(homeTeam, homeOneKelly, homeHalfKelly, homeFourthKelly)
    outputKellyCriterion(awayTeam, awayOneKelly, awayHalfKelly, awayFourthKelly)    
                
    # Ask user if they would like to Adjust the model probabilities
    adjModelProbability(homeTeam, homeSimProb, homeDecOdd)
    adjModelProbability(awayTeam, awaySimProb, awayDecOdd)
    
    # Write matchup data to CSV
    writeMatchupDataToExcel(homeTeam, awayTeam, homeML, awayML, homeSimProb, awaySimProb)
    
def adjModelProbability(team, prob, teamDecOdd):
    
    # Function purpose is to ask the user if they would like to adjust the Monte Carlo
    # Simulation probability based on data held in the CSV file
    
    while True:
        try:
            user_input = input("Would you like to adjust " + team + " probability of " + str(round((prob * 100), 3)) + "%? (Y/N): ")
            if user_input == "Y" or user_input == "y":
                print(team + " Model Probability is: " + str(round((prob * 100), 3)))
                newProb = getNewProb(team)
                newProb = newProb / 100
                print(team + " New Probability is: " + str(round((newProb * 100), 3)) + "%\n")
                print("Kelly Criterion for New Probability: " + "\n")
                teamOneKelly, teamHalfKelly, teamFourthKelly = calcKellyCriterion(team, teamDecOdd, newProb)
                outputKellyCriterion(team, teamOneKelly, teamHalfKelly, teamFourthKelly)
                break
            if user_input == "N" or user_input == "n":
                break
        except ValueError:
            print("Sorry, that is not a valid input.  Please select Y or N.")


def getNewProb(team):
    
   # Function purpose is to collect the new probability input by the user 
    
    while True:
        try:
            newProb = input("Enter the New Probability for " + team + "(0 to 100): ")
            newProb = float(newProb)
            if newProb < 0 or newProb > 100:
               newProb = input("Enter the New Probability for " + team + " (0 to 100): ")
               newProb = int(newProb)
        except ValueError:
            print("That is not a valid probability.  Please enter a value between 0 and 100.")
        else:
            break
        
    return newProb
            
def calcKellyCriterion(teamName, teamDecOdd, teamSimProb):
    
    # Function purpose is to take in the decimal odds and probability and 
    # output the Kelly Criterion and a fraction of the Kelly Criterion 

    teamOneKelly = oneKelly(teamSimProb, teamDecOdd)
    teamHalfKelly = halfKelly(teamSimProb, teamDecOdd)
    teamFourthKelly = fourthKelly(teamSimProb, teamDecOdd)
    
    return teamOneKelly, teamHalfKelly, teamFourthKelly
                    
def outputKellyCriterion(teamName, teamOneKelly, teamHalfKelly, teamFourthKelly):
    
    # Function puprose is to display the Kelly Criterions
    
    print(teamName + " One Kelly: " + str(round(teamOneKelly, 4)))
    print(teamName + " Half Kelly: " + str(round(teamHalfKelly, 4)))
    print(teamName + " Fourth Kelly: " + str(round(teamFourthKelly, 4)) + "\n")
    
def displaySimulationProbs(homeTeam, awayTeam, homeSimProb, awaySimProb):
    
    # Function purpose is to display the Monte Carlo Simulation results
    
    print("The Simulation Probabilities are: " + "\n")
    
    homeSimProb = homeSimProb * 100
    awaySimProb = awaySimProb * 100
    
    print(homeTeam + " " + str(round(homeSimProb, 2)) + "%")
    print(awayTeam + " " + str(round(awaySimProb, 2)) + "%" + "\n")
            
def displayImpliedProbs(homeTeam, awayTeam, homeProb, awayProb):
    
    # Function purpose is to display the Implied Probabilities
    
    print("\n" + "The Moneyline Implied Probabilities are: " + "\n")
    
    homeProb = homeProb * 100
    awayProb = awayProb * 100
    
    print(homeTeam + " " + str(round(homeProb, 3)) + "%")
    print(awayTeam + " " + str(round(awayProb, 3)) + "%" + "\n")
            
def getMoneyLines(homeTeam, awayTeam):
    
    # Function puprose is to collect the Moneylines for each team (home & away)
    # User is asked to enter the Moneyline and then is given option to review
    # and re-enter the Moneylines if needed
    
    while True:
    
        while True:
            try:
                homeML = int(input("Enter " + homeTeam + " Moneyline: "))
                if homeML < -1000000 or homeML > 1000000:
                    homeML = int(input("Enter " + homeTeam + " Moneyline: "))
            except ValueError:
                print("Sorry, that is not a Moneyline.")
            else:
                break
                
        while True:
            try:
                awayML = int(input("Enter " + awayTeam + " Moneyline: "))
                if awayML < -1000000 or awayML > 1000000:
                    awayML = int(input("Enter " + awayTeam + " Moneyline: "))
            except ValueError:
                print("Sorry, that is not a Moneyline.")
            else:
                break

        print("\n" + "You Entered the Following Moneylines: " + "\n" + homeTeam + ": " + str(homeML) + "\n" + awayTeam + ": " + str(awayML))
        
        checkML = input("Are those the correct Moneylines? (Y/N): ")
        if checkML.upper() == "Y":
            break
        else:
            continue
        
    return homeML, awayML
            
def matchupAnalysisGraph(homeTeam, awayTeam):
    
    # Function purpose is to run the matchup analysis graph 
    # The DataFrames are used to display all prior games played of the season so far
    
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
    
    # Function purpose is to display the matchup analysis graph
    
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
    
    # Function collects the Home Team Graph Team Points and removes any 
    # rows with NaN values
    
    homeDF_1 = homeDF['Tm']
    
    homeGraphTmPtsDF = pd.to_numeric(homeDF_1, errors='coerce')
    
    homeGraphTmPtsDF = homeGraphTmPtsDF.dropna()

    return homeGraphTmPtsDF
    
def getHomeGraphOppPts(homeDF): 
    
    # Function collects the Home Team Graph Opp Points and removes any
    # rows with NaN values
    
    homeDF_1 = homeDF['Opp.1']
    
    homeGraphOppPtsDF = pd.to_numeric(homeDF_1, errors='coerce')
    
    homeGraphOppPtsDF = homeGraphOppPtsDF.dropna()
    
    return homeGraphOppPtsDF

def getHomeGraphGmNum(homeDF):
    
    # Function collecs the Home Team number of games and removes any 
    # rows with NaN values
    
    homeDF_1 = homeDF['G']

    homeGraphGameNum = pd.to_numeric(homeDF_1, errors='coerce')
    
    homeGraphGameNum = homeGraphGameNum.dropna()
    
    return homeGraphGameNum

def getAwayGraphTmPts(awayDF):
    
    # Function collects the Away Team Graph Team Points and removes any 
    # rows with NaN values
    
    awayDF_1 = awayDF['Tm']
    
    awayGraphTmPtsDF = pd.to_numeric(awayDF_1, errors='coerce') 
    
    awayGraphTmPtsDF = awayGraphTmPtsDF.dropna()
    
    return awayGraphTmPtsDF

def getAwayGraphOppPts(awayDF):
    
    # Function collects the Away Team Graph Opp Points and removes any
    # rows with NaN values
    
    awayDF_1 = awayDF['Opp.1']
    
    awayGraphOppPtsDF = pd.to_numeric(awayDF_1, errors='coerce')
    
    awayGraphOppPtsDF = awayGraphOppPtsDF.dropna()
    
    return awayGraphOppPtsDF

def getAwayGraphGmNum(awayDF):
    
    # Function collects the Away Team Graph Team Points and removes any 
    # rows with NaN values
    
    awayDF_1 = awayDF['G']
    
    awayGraphGameNum = pd.to_numeric(awayDF_1, errors='coerce')
    
    awayGraphGameNum = awayGraphGameNum.dropna()
    
    return awayGraphGameNum

def getHomeTeamMeanPts(filteredHomeDF):
    
    # Function gets the mean value of the Home Team Pts column and removes any
    # strings from rows
    
    filteredHomeDF_1 = filteredHomeDF['Tm']
    
    removeStringDF = pd.to_numeric(filteredHomeDF_1, errors='coerce')
    
    homeTeamPtsMu = removeStringDF.mean()
    
    return homeTeamPtsMu
    
def getHomeTeamStdDevPts(filteredHomeDF):
    
    # Function gets the standard deviation value of the Home Team Pts column and 
    # removes any strings from rows    
    
    filteredHomeDF_1 = filteredHomeDF['Tm']
    
    removeStringDF = pd.to_numeric(filteredHomeDF_1, errors='coerce')
    
    homeTeamStdDevPts = removeStringDF.std()

    return homeTeamStdDevPts
    
def getHomeTeamOppMeanPts(filteredHomeDF):
    
    # Function gets the mean of the Home Team Opp Pts column and removes any strings from rows
    
    filteredHomeDF_1 = filteredHomeDF['Opp.1']
    
    removeStringDF = pd.to_numeric(filteredHomeDF_1, errors='coerce')
    
    homeTeamOppMeanPts = removeStringDF.mean()
    
    return homeTeamOppMeanPts
    
def getHomeTeamOppStdDevPts(filteredHomeDF):
    
    # Function gets the standard deviation of the Home Team Opp Pts column and 
    # removes any strings from rows
    
    filteredHomeDF_1 = filteredHomeDF['Opp.1']
    
    removeStringDF = pd.to_numeric(filteredHomeDF_1, errors='coerce')
    
    homeTeamOppStdDevPts = removeStringDF.std()
    
    return homeTeamOppStdDevPts
    
def getAwayTeamMeanPts(filteredAwayDF):
    
    # Function gets the mean value of the Away Team Points column and removes 
    # any strings from rows
    
    filteredAwayDF_1 = filteredAwayDF['Tm']
    
    removeStringDF = pd.to_numeric(filteredAwayDF_1, errors='coerce')
    
    awayTeamPtsMu = removeStringDF.mean()
    
    return awayTeamPtsMu
    
def getAwayTeamStdDevPts(filteredAwayDF):
    
    # Function gets the standard deviation value of the Away Team Points column and
    # removes any strings from rows
    
    filteredAwayDF_1 = filteredAwayDF['Tm']
    
    removeStringDF = pd.to_numeric(filteredAwayDF_1, errors='coerce')
    
    awayTeamPtsStdDev = removeStringDF.std()
    
    return awayTeamPtsStdDev
    
def getAwayTeamOppMeanPts(filteredAwayDF):
    
    # Function gets the mean value of the Away Team Opp points column and 
    # removes any strings from rows
    
    filteredAwayDF_1 = filteredAwayDF['Opp.1']
    
    removeStringDF = pd.to_numeric(filteredAwayDF_1, errors='coerce')
    
    awayTeamOppPtsMu = removeStringDF.mean()
    
    return awayTeamOppPtsMu
    
def getAwayTeamOppStdDevPts(filteredAwayDF): 
    
    # Function gets the standard deviation value of the Away Team Opp points column
    # and removes any strings from rows
    
    filteredAwayDF_1 = filteredAwayDF['Opp.1']
    
    removeStringDF = pd.to_numeric(filteredAwayDF_1, errors='coerce')
    
    awayTeamOppStdDevPts = removeStringDF.std()
    
    return awayTeamOppStdDevPts  

def filterHomeTeamStatsDF(homeDF):
    
    # Function filters the Home Team dataframe to include only rows of Home Games
    
    homeDF_filter = homeDF.loc[homeDF['Unnamed: 3'].isnull()]
    
    return homeDF_filter
    
def filterAwayTeamStatsDF(awayDF):
    
    # Function filters the Away Team dataframe to include only rows of Away Games
    
    awayDF_filter = awayDF.loc[awayDF['Unnamed: 3'].isin(['@'])]
    
    return awayDF_filter
    
def getTeamStatsDataFrame(team):
    
    # Function creates a DataFrame for Team Name
    
    # Convert Team Name to Symbol, build URL, and create DataFrame
    teamSym = convertTeamNameToSym(team)
    
    teamURL = buildTeamStatsURL(teamSym)
    
    teamDF = buildTeamStatsDataFrame(teamURL)
    
    return teamDF
    
def getTodayMatchups():    
    
    # Function to build today's matchups

    # Get the URL month, build the schedule URL, create schedule dataframe,
    # search the schedule DataFrame and create matchup dictionary     
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
    day = today.strftime('%#d')
    """
    day = day.lstrip('0').replace('0', '')
    """
    year = today.strftime('%Y')
    
    todaySearch = str(weekDay + ', ' + month + ' ' + day + ', ' + year)
    
    return todaySearch

def getHomeTeams(today, df):
    
    # Function purpose is to build a list of home teams from the schedule
    # DataFrame
    
    try:
    
        dfsearch = df.loc[[today], ['Home/Neutral']]
        
        homeTeams = []

        for home in dfsearch['Home/Neutral']:
            homeTeams.append(home)
            
        return homeTeams
            
    except KeyError:
    
        print('There are no games today: ' + today)  
    

def getAwayTeams(today, df):
    
    # Function purpose is to build a list of away teams from the schedule
    # DataFrame
    
    try:
    
        dfsearch = df.loc[[today], ['Visitor/Neutral']]
        
        awayTeams = []

        for away in dfsearch['Visitor/Neutral']:
            awayTeams.append(away)
            
        return awayTeams
            
    except KeyError:
    
        print('There are no games today: ' + today)  
        
def getTodayMatchupDict(homeTeams, awayTeams):
    
    # Function purpose is to build a dictionary of the home and away teams
    
    matchups = {}
    
    for home in homeTeams:
        for away in awayTeams:
            matchups[home] = away
            awayTeams.remove(away)
            break
        
    return matchups

def printTodayMatchups(matchups):
    
    # Function purpose is to display the matchups today in the matchups dictionary
    
    count = 1
    
    print("\n" + "NBA Games Tonight: " + str(getTodaySchedSearch()) + "\n")
    
    for home, away in matchups.items():
        print('GAME ', count)
        print('Home Team: ', home)
        print('Away Team: ', away, "\n")
        count += 1
        
    print("\n" + "There are " + str(count - 1) + " games tonight (" + str(getTodaySchedSearch()) + ").\n")
        
def convertTeamNameToSym(teamName):
    
    # Function will convert a team name to a team symbol using the TeamAbbrev dictionary
    
    teamSym = teamAbbrev[teamName]

    return teamSym

def buildTeamStatsURL(teamSym):
    
    # URL for the individual team Game Log - Team Symbol is needed to build URL
    
    url = 'https://www.basketball-reference.com/teams/' + str(teamSym) + '/2020/gamelog/'
    
    return url

def buildTeamStatsDataFrame(url):
    
    # Function Purpose: Generic Function to Build a DataFrame when given a URL
    
    dfs = pd.read_html(url, header = 1)
    df = pd.DataFrame(dfs[0])
    
    return df


if __name__=='__main__':
    main()