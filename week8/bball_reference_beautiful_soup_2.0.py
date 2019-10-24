"""
Joe Holleran
Beautiful Soup - Basketball Reference - Team Stats
10/22/2019
Python 2
"""
# Pandas DataFrame: Text Book Chapter 07 & https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
# Pandas To_Excel: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html

import urllib.request
import bs4
import pandas as pd

def getSearchURL(term):
    
    url = 'https://www.basketball-reference.com/leagues/NBA_' + (str(term)) + '_ratings.html'
    return url

def getHTMLPageText(url):
    request = urllib.request.Request(url)
    # use the resource manager to request the page from the internet
    # and retrieve the HTML from that response for use as the return value
    with urllib.request.urlopen(request) as response:
        return response.read()
    
def main():
       
    pageText = getHTMLPageText(getSearchURL('2019'))
    soup = bs4.BeautifulSoup(pageText, 'html.parser')
    
    # Scrap the column headers into a list
    for hRow in soup.find_all('thead'):
        teamStatHeaders = []
        for ths in soup.find_all('th'):
            teamStatHeaders += [ths.text]
    
    # Slice column headers     
    headers = teamStatHeaders[5:18]
        
    # Create dictionary to hold teams (keys) and stats (values)
    leagueStats = {}
    
    # Scrap the rows of team stats into a dictionary    
    for row in soup.find_all('tr'):
        teamStatData = []
        if row.find('td') == None:
            continue        
        for td in row.find_all('td'):
            teamStatData += [td.text]
        leagueStats[teamStatData[0]] = teamStatData[1:]
        
    print("***** NBA Team Stats Table *****")
    #Create pandas dataframe (Ch 07) using headers as column labels    
    tsdf = pd.DataFrame(leagueStats, index = headers)
    #Print dataframe (transposed) due to the dictionary setup
    print(tsdf.T)
    #Create excel file based on the data frame
    tsdf.T.to_excel('team_stats_dataframe.xlsx')
    
    home_team = input("Input Home Team Name (Full Team Name including City): ")
    away_team = input("Input Away Team Name (Full Team Name including City): ")
    
    hto = leagueStats[home_team][6]
    htd = leagueStats[home_team][7]
    htn = leagueStats[home_team][8]
    hwp = float(leagueStats[home_team][4])
    ato = leagueStats[away_team][6]
    atd = leagueStats[away_team][7]
    atn = leagueStats[away_team][8]
    awp = float(leagueStats[away_team][4])
    
    # Projected Win%=[(Points Differential)*2.7)+41]/82
    
    hewp = (((float(htn)*2.7)+41)/82)
    aewp = (((float(atn)*2.7)+41)/82)
    
    print("*****", home_team, "Team Ratings *****", "\n")
    print(" Offensive Rating: ", hto, "\n", "Defensive Rating: ", htd, "\n", "Net Rating: ", htn, "\n")
    print(home_team, "Projected Winning Percentage: ", '{:.2%}'.format(hewp))
    print(home_team, "Actual Winning Percentage: ", '{:.2%}'.format(hwp), "\n")
    print("*****", away_team, "Team Ratings *****", "\n")
    print(" Offensive Rating: ", ato, "\n", "Defensive Rating: ", atd, "\n", "Net Rating: ", atn, "\n")
    print(away_team, "Projected Winning Percentage: ", '{:.2%}'.format(aewp))
    print(away_team, "Actual Winning Percentage: ", '{:.2%}'.format(awp))
    
if __name__=='__main__':
    main()