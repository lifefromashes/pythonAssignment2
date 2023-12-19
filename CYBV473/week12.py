#
# NLTK QUERY Example
# Professor Hosmer
# August 2020
#

import os  # Standard Library OS functions
import sys
import logging  # Standard Library Logging functions
import nltk  # Import the Natural Language Toolkit
from nltk.corpus import PlaintextCorpusReader  # Import the PlainTextCorpusReader Module
from nltk.corpus import stopwords
from time import sleep
from prettytable import PrettyTable

stopSet = set(stopwords.words('english'))


class classNLTKQuery:
    ''' NLTK Query Class '''

    def textCorpusInit(self, thePath):

        # Validate the path is a directory
        if not os.path.isdir(thePath):
            return "Path is not a Directory"

        # Validate the path is readable
        if not os.access(thePath, os.R_OK):
            return "Directory is not Readable"

        # Attempt to Create a corpus with all .txt files found in the directory
        try:

            self.Corpus = PlaintextCorpusReader(thePath, '.*')
            print("Processing Files : ")
            print(self.Corpus.fileids())
            print("Please wait ...")
            self.rawText = self.Corpus.raw()
            self.tokens = nltk.word_tokenize(self.rawText)
            self.TextCorpus = nltk.Text(self.tokens)
        except:
            return "Corpus Creation Failed"

        self.ActiveTextCorpus = True

        return "Success"

    def printCorpusLength(self):
        print("\n\nCorpus Text Length: ", '{:,}'.format(len(self.rawText)))

    def printTokensFound(self):
        print("\n\nTokens Found: ", '{:,}'.format(len(self.tokens)))

    def printVocabSize(self):
        print("\n\nCalculating Vocabulary Size...")
        ''' YOUR CODE GOES HERE '''

    def printCollocation(self):
        print("\n\nCompiling Top 100 Collocations ...")
        ''' YOUR CODE GOES HERE '''

    def searchWordOccurrence(self):
        myWord = input("\n\nEnter Search Word : ")
        if myWord:
            print("Searching for: ", myWord)
            ''' YOUR CODE GOES HERE '''

    def generateConcordance(self):
        myWord = input("\n\nEnter word to Concord : ")
        if myWord:
            print("Compiling First 100 Concordance Entries ...")
            ''' YOUR CODE GOES HERE '''

    def generateSimiliarities(self):

        myWord = input("\n\nEnter seed word : ")
        if myWord:
            print("Compiling First 200 Similiarity Entries ...")
            ''' YOUR CODE GOES HERE '''

    def printVocabulary(self):
        print("\n\nCompiling Vocabulary Frequencies")

        tbl = PrettyTable(["Vocabulary", "Occurs"])
        ''' YOUR CODE GOES HERE '''


def printMenu():
    # Function to print the NLTK Query Option Menu

    print("==========NLTK Query Options =========")
    print("[1]    Print Length of Corpus")
    print("[2]    Print Number of Token Found")
    print("[3]    Print Vocabulary Size")
    print("[4]    Search for Word Occurrence")
    print("[5]    Generate Concordance")
    print("[6]    Generate Similarities")
    print("[7]    Print Vocabulary")
    print()
    print("[0]    Exit NLTK Experimentation")

    print()


# Function to obtain user input

def getUserSelection():
    printMenu()

    while True:
        try:
            sel = input('Enter Selection (0-8) >> ')
            menuSelection = int(sel)
        except ValueError:
            print('Invalid input. Enter a value between 0-7.')
            continue

        if not menuSelection in range(0, 8):
            print('Invalid input. Enter a value between 0 - 8')
            continue

        return menuSelection


if __name__ == '__main__':

    print("Welcome to the NLTK Query Experimentation")
    print("Please wait loading NLTK ... \n")

    print("Input full path name where intended corpus file or files are stored")
    print("Format for Windows e.g. ./CORPUS \n")

    userSpecifiedPath = input("Path: ")

    # Attempt to create a text Corpus
    oNLTK = classNLTKQuery()
    result = oNLTK.textCorpusInit(userSpecifiedPath)

    if result == "Success":

        menuSelection = -1

        while menuSelection != 0:

            if menuSelection != -1:
                print()
                s = input('Press Enter to continue...')
                printMenu()

            menuSelection = getUserSelection()

            if menuSelection == 1:
                oNLTK.printCorpusLength()

            elif menuSelection == 2:
                oNLTK.printTokensFound()

            elif menuSelection == 3:
                oNLTK.printVocabSize()

            elif menuSelection == 4:
                oNLTK.searchWordOccurrence()

            elif menuSelection == 5:
                oNLTK.generateConcordance()

            elif menuSelection == 6:
                oNLTK.generateSimiliarities()

            elif menuSelection == 7:
                oNLTK.printVocabulary()

            elif menuSelection == 0:
                print("Goodbye")
                print()

            elif menuSelection == -1:
                continue

            else:
                print("unexpected error condition")
                menuSelection = 0

            sleep(3)

    else:
        print("Closing NLTK Query Experimentation")


