"""
Joe Holleran
Beautiful Soup - Basketball Reference - Team Stats
10/16/2019
Python 2
"""
import urllib.request
import bs4

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
    
    team_stats = ""
    
    for i in soup.findAll('tr'):
        stats = ""
        for j in i.findAll('td'):
            stats = stats+","+j.text
        team_stats = team_stats + "\n" + stats[1:]
    
    header = "Team, Conf, Div, W, L, W/L%, MOV, ORtg, DRtg, NRtg, MOV/A, ORtg/A, DRtg/A, NRtg/A"      
    file = open("team_stats.csv", "w")
    file.write(header)
    file.write(team_stats)
    file.close()
    
if __name__=='__main__':
    main()