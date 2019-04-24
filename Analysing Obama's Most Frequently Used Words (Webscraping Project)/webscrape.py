# WEBSCRAPER TO COLLECT AND PROCESS TRANSCRIPT TEXT
# This algorithm was created to scrape the links to speeches in the White House
# archive website that was used under Obama's presidency. The program reads a
# txt file with all the urls to Obama's speeches collected by the previous
# algorithm. It then iterates over all the urls to find and process the
# transcipt text, and finally appends it to a txt file to prepare for analysis
# by separate algorithm.

from bs4 import BeautifulSoup
import requests
import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
#------------------------------------------------------------------------------

def getText(url):
    url = ("https://obamawhitehouse.archives.gov" + url).rstrip()
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html,features="lxml")
    # print(soup.prettify())

    # Find transcript from website
    for paragraph in soup.find_all('p'):
        speech = paragraph.get_text()

    # Remove questions and time stamp from transcript
    for line in speech.splitlines():
        if "	Q   " in line:
            speech = speech.replace(line,"")
        if "EST" in line:
            speech = speech.replace(line,"")

    # Remove headers
    speech = speech.replace("	THE PRESIDENT:  ","")

    # Tokenize text and remove punctuation
    speech = word_tokenize(speech)
    speech = [word.lower() for word in speech if word.isalpha()]

    # Remove stopwords
    stopWordsSet=set(stopwords.words("english"))
    filteredSpeech = []
    for w in speech:
        if w not in stopWordsSet:
            filteredSpeech.append(w)

    # Stem text
    ps = PorterStemmer()
    stemmedSpeech=[]
    for w in filteredSpeech:
        stemmedSpeech.append(ps.stem(w))

    # stemmedSpeech = str(stemmedSpeech).replace("]",",")
    # stemmedSpeech = str(stemmedSpeech).replace("["," ")

    # Append final text into a txt file
    with open("speechData.txt", "a") as output:
        output.write(str(stemmedSpeech))
#------------------------------------------------------------------------------
# Read in the urls and execute the function:

# Read the txt file with the URLs
with open("urls.txt", "r") as output:
    listOfURLs = output.readlines()

# getText out of these URLs one by one
for i in range(len(listOfURLs)):
    getText(listOfURLs[i])
