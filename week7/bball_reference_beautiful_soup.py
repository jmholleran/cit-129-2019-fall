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
        
    #Create pandas dataframe (Ch 07) using headers as row labels    
    tsdf = pd.DataFrame(leagueStats, index = headers)
    #Print dataframe (transposed) due to the dictionary setup
    print(tsdf.T)
    #Create excel file based on the data frame
    tsdf.T.to_excel('team_stats_dataframe.xlsx')

if __name__=='__main__':
    main()