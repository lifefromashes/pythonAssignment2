'''
WK 7
Kristin Skipper
Fall 2024
'''
import pandas as pd
from nltk.corpus import stopwords

# List of candidates to track
CANDIDATES = ['joe biden', 'bernie sanders', 'pete buttigieg', 'elizabeth warren',
              'michael bloomberg', 'amy klobuchar', 'steve bullock', 'tom steyer']

stops = set(stopwords.words('english'))

DEBATE_FILE = "speechByCandidate.csv"

topWords = {}
candidateWordCounts = {}


# take second element for sorting
def CountElement(elem):
    return elem[1]


with open(DEBATE_FILE) as debate:
    for eachLine in debate:
        eachLine = eachLine.lower()
        lineList = eachLine.split(',')

        candidate = lineList[0].strip()  # Assuming the first column is the candidate's name

        # Only process if the candidate is in the list of tracked candidates
        if candidate in CANDIDATES:
            wordList = lineList[1].split()

            for eachWord in wordList:
                if eachWord not in stops and len(eachWord) >= 5:
                    # Track global count of each word
                    topWords[eachWord] = topWords.get(eachWord, 0) + 1

                    # Track word count for each candidate
                    if candidate not in candidateWordCounts:
                        candidateWordCounts[candidate] = {}

                    candidateWordCounts[candidate][eachWord] = candidateWordCounts[candidate].get(eachWord, 0) + 1

# Sort the top words by their count
topWordList = list(topWords.items())
topWordList.sort(key=CountElement, reverse=True)

# Get the top 50 words
top50Words = [word for word, _ in topWordList[:50]]

# Create an empty DataFrame with candidates as rows and top 50 words as columns
df = pd.DataFrame(columns=top50Words)

# Populate the DataFrame with counts
rows_list = []
for candidate, wordCounts in candidateWordCounts.items():
    row = {word: wordCounts.get(word, 0) for word in top50Words}
    row['candidate'] = candidate  # Add candidate name as a column
    rows_list.append(row)

# Create the DataFrame from the list of rows
df = pd.concat([pd.DataFrame(rows_list)], ignore_index=True)

# Set 'candidate' as the index
df.set_index('candidate', inplace=True)

# Display the DataFrame
print(df)

# Write the DataFrame to a CSV file
df.to_csv('candidate_word_counts.csv', index=True)
