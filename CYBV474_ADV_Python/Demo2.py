'''
WK-5 Text Processing Demo 2
'''
import re
from prettytable import PrettyTable

# Preapre a STOP_WORD List
with open("STOP_WORDS.txt", 'r') as stops:
    stopWords = stops.read()

STOP_WORDS = stopWords.split()

# Read in the Content of a Book
with open("dialog.txt", 'r') as book:
    text = book.read()

# Convert to Lowercase
text = text.lower()

# remove all extraneous content
content = re.sub("[^a-z]", ' ', text)

# Get the list of words
wordList = content.split()

wordCnt = 0

# Create a dictionary of words along with the number of times they occur

wordDict = {}
for eachWord in wordList:
    # ignore articles and STOP_WORDS
    if eachWord in STOP_WORDS or len(eachWord) <= 3:
        continue
    try:
        wordCnt += 1
        cnt = wordDict[eachWord]
        cnt += 1
        wordDict[eachWord] = cnt
    except:
        wordDict[eachWord] = 1

tbl = PrettyTable(["Word", "Occurrence", "Frequency %"])

for word, occurrence, in wordDict.items():
    freq = round(((occurrence / wordCnt) * 100.0), 2)
    tbl.add_row([word, occurrence, freq])

tbl.align = 'l'
print(tbl.get_string(sortby="Occurrence", reversesort=True))
