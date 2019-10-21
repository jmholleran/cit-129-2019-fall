# -*- coding: utf-8 -*-
"""
Joe Holleran
Python 2
10/09/2019
In-Class Practice
"""
# HTML scraping demo with requests library and beautifulsoup for goodreads.com
# Attempt to scrap book authors, title, and average ratings

# read through BeautifulSoup & urllib documentation

import urllib.request
import bs4

def getSearchURL(term):
    
    url = 'https://www.goodreads.com/search?query=%s' % (str(term))
    return url

def getHTMLPageText(url):
    request = urllib.request.Request(url)
    # use the resource manager to request the page from the internet
    # and retrieve the HTML from that response for use as the return value
    with urllib.request.urlopen(request) as response:
        return response.read()
    
def main():
    
    pageText = getHTMLPageText(getSearchURL('Milo'))
    soup = bs4.BeautifulSoup(pageText, 'html.parser')
    eles = soup.find_all('a', 'bookTitle')
    for item in eles:
        tag = item.find('span').string
        print(tag)
        

    
if __name__=='__main__':
    main()
    

    