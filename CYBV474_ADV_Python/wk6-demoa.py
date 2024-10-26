'''
WK-6 Sample
Professor Hand
Spring 2023
'''
# import python standard libraries
from collections import Counter
import re
import nltk
from nltk import pos_tag
import pandas as pd

# import python 3rd party libs
from nltk import word_tokenize, pos_tag, FreqDist


def main():
    sampleText = 'thank you. We have to take a quick break. When we come back, the Democratic Presidential Debate continues right after this. Only on CBS'
    sampleText = sampleText.lower()
    sampleText = re.sub("[^a-zA-Z ]", ' ', sampleText)

    ''' Part of Speech Tagging '''
    words = word_tokenize(sampleText)
    tags = pos_tag(words)
    for eachWord in tags:
        print(eachWord)

    ''' Tally each category '''
    counts = Counter(tag for word, tag in tags)
    print(counts)

    ''' Calculate the Distribution '''
    fd = FreqDist(counts)

    ''' Plot the results '''
    fd.plot(title="Part of Speech Tagging Example")


# Main Program Starts Here
# ===================================

if __name__ == '__main__':
    main()