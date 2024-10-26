'''
WK-5 Text Processing Demo 1
'''
import re

from prettytable import PrettyTable

with open("dialog.txt", 'r') as book:
    text = book.read()

text = text.lower()
content = re.sub("[^a-z]", ' ', text)

wordList = content.split()

wordDict = {}

for eachWord in wordList:
    try:
        cnt = wordDict[eachWord]
        cnt += 1
        wordDict[eachWord] = cnt
    except:
        wordDict[eachWord] = 1

tbl = PrettyTable(["cnt", "word"])

for word, cnt in wordDict.items():
    tbl.add_row([cnt, word])

tbl.align = 'l'
print(tbl.get_string(sortby="cnt", reversesort=True))
