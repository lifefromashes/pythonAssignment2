'''
Week 5 Working with Dataframes
Professor Hand
Fall 2023
'''

import pandas as pd
import numpy as np

# Set Panda Display Options
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 2000)

print("\nPanda Intro")
'''
Creating a simple Dataframe
'''
print("\nSample-Data - Hard-Wired\n")
df = pd.DataFrame([["Ford", 88.75, 32.0], ["GM", 86.75, 30.0], ["Tesla", 98.75, 50.1]],
                  columns=["Make", "Ranking", "MPG"])
print(df.head())

print("\nSample-Data - random numpy data\n")
df = pd.DataFrame(np.random.randint(0, 100, size=(10, 4)), columns=["AA", "BB", "CC", "DD"])
print(df.head(10))

wordDict = {}

print("\nSample-Dataframe creation from a Dictionary\n")
s = "the quick brown fox jumps over the lazy dog"
sLen = len(s)
wordList = s.split()

for eachWord in wordList:
    wordLen = len(eachWord)
    wordDict[eachWord] = [wordLen, round(((wordLen / sLen) * 100.0), 2)]

df = pd.DataFrame(wordDict)
df = df.transpose()
df.columns = ["Length", "Length/StrLen"]
print(df)

print("\nSample Data - From CSV Dataset\n")
df = pd.read_csv("CENTRAL-PARK-WEATHER.CSV")
print(df.head(20))

