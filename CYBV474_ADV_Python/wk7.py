'''
WK 7
Kristin Skipper
Fall 2024
'''
import re

from nltk import word_tokenize

# PSUEDO CONTANTS
'''
Assumes that the debateRaw.txt file is in the 
same folder as the script
'''
from nltk.corpus import stopwords
stops = set(stopwords.words('english'))

DEBATE_FILE = "speechByCandidate.csv"

topWords = {}

# take second element for sort
def CountElement(elem):
    return elem[1]

with open(DEBATE_FILE) as debate:
    for eachLine in debate:

        eachLine = eachLine.lower()
        lineList = eachLine.split(',')
        wordList = lineList[1].split()

        for eachWord in wordList:

            if eachWord not in stops and len(eachWord) >= 5:
                try:
                    cnt = topWords[eachWord]
                    cnt += 1
                    topWords[eachWord] = cnt
                except:
                    topWords[eachWord] = 1

    topWordList = list(topWords.items())
    topWordList.sort(key=CountElement, reverse=True)

    print('Top 50 Words Used Across All Candidates')
    print(topWordList[0:50])
    # Create a dictionary to store the word counts for each candidate
    candidate_word_counts = {}

    # Iterate over the top 50 words
    for word, _ in topWordList[0:50]:
        # Initialize a dictionary to store the word count for each candidate
        candidate_word_counts[word] = {}

        # Iterate over the debate file again
        with open(DEBATE_FILE) as debate:
            for eachLine in debate:
                eachLine = eachLine.lower()
                lineList = eachLine.split(',')
                speaker = lineList[0]  # assuming the speaker is the first element
                wordList = lineList[1].split()

                # Check if the speaker is already in the dictionary
                if speaker not in candidate_word_counts[word]:
                    candidate_word_counts[word][speaker] = 0

                # Count the occurrences of the word for the current speaker
                candidate_word_counts[word][speaker] += wordList.count(word)

    # Print the results
    for word, candidate_counts in candidate_word_counts.items():
        print(f"Word: {word}")
        for candidate, count in candidate_counts.items():
            print(f"  {candidate}: {count}")
        print()



