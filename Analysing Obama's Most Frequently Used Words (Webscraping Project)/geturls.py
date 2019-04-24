# WEBSCRAPER TO COLLECT DESIRED URLS FROM ARCHIVE
# This webscraper collects urls to transcripts of Obama's speeches from the
# White House archive website. It iterates over 472 pages of transcripts to
# pull out the desired urls.

from bs4 import BeautifulSoup
import requests
import re
#------------------------------------------------------------

# Function to iterate over the pages
def getURLs(url):
    for i in range(472):
        newURL = url + str(i)
        getURLsPerPage(newURL)

# Function to get urls from a page
def getURLsPerPage(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,features="lxml")

    tags = soup.find_all('a')

    for tag in soup.find_all('a', href=re.compile('/the-press-office/')):
        listOfUrls = tag.get('href')

        with open("urls.txt", "a") as output:
            output.write(listOfUrls)
            output.write("\n")


# Execute the algorithm
a = "https://obamawhitehouse.archives.gov/briefing-room/speeches-and-remarks?term_node_tid_depth=31&page="
getURLs(a)
