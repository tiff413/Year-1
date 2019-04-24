# ANALYSE SPEECH FROM TRANSCRIPTS
# This algorithm reads the speech text collected from the webscraping
# algorithms and uses NLTK functions to analyse the most frequent words used.

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import csv

# Read in the speech data
with open("speechData.txt", "r") as words:
    text = words.read()
    text = str(text).replace("][",", ")

# Retokenise words and create frequency distribution
words = word_tokenize(str(text))
fdist = FreqDist(words)

# Write the results into a csv file
with open("frequency.csv", "w") as fp:
    writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
    writer.writerows(fdist.items())
