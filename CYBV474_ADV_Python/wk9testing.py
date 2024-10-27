'''
Script Purpose: Practical Exercise #9 Starter Script
Script Version: Fall 2023
Script Author:  Professor Hand
'''

print("\nGender Analysis of Tweets")
print("Loading ML Libraries ... please wait")

import re
import pandas as pd
from nltk import trigrams, NaiveBayesClassifier, classify
from sklearn.model_selection import train_test_split


def scrubTweet(twt):
    twt = re.sub("[^a-zA-Z]", ' ', twt.lower())
    return twt


def GenerateWordUsage(df):
    maleWords = set()
    femaleWords = set()

    for row in df.itertuples():

        gender = row.gender

        twt = scrubTweet(row.tweet)

        wordList = twt.split()
        for eachWord in wordList:
            if len(eachWord) >= 3 and len(eachWord) <= 12:
                if 'female' in gender:
                    femaleWords.add(eachWord)
                elif 'male' in gender:
                    maleWords.add(eachWord)

    maleWords, femaleWords = maleWords - femaleWords, femaleWords - maleWords

    return maleWords, femaleWords


def getFeatures(gender, twt, maleWords, femaleWords):
    ''' Model for feature extraction
        This is just and example not the real features
        that will be included.
    '''

    twtLength = len(twt)

    features = {}
    features['tweetLength'] = twtLength

    '''
    Your Code Goes Here add more features
    '''

    return features


def main():
    df = pd.read_csv("tweetsClean.csv")
    dfTrain, dfTest = train_test_split(df, test_size=0.1, random_state=11)
    maleWords, femaleWords = GenerateWordUsage(dfTrain)

    trainingFeatureSet = []
    testingFeatureSet = []

    for row in dfTrain.itertuples():
        gender = row.gender
        tweet = scrubTweet(row.tweet)
        rowFeatures = getFeatures(gender, tweet, maleWords, femaleWords)
        trainingFeatureSet.append((rowFeatures, gender))

    for row in dfTest.itertuples():
        gender = row.gender
        tweet = scrubTweet(row.tweet)
        rowFeatures = getFeatures(gender, tweet, maleWords, femaleWords)
        testingFeatureSet.append((rowFeatures, gender))

        # Create a NaiveBayes Gender Classifer from the Training Set
    genderClassifer = NaiveBayesClassifier.train(trainingFeatureSet)

    print('TrainSet Accuracy: ', classify.accuracy(genderClassifer, trainingFeatureSet))
    print('TestSet  Accuracy: ', classify.accuracy(genderClassifer, testingFeatureSet))

    genderClassifer.show_most_informative_features(20)


if __name__ == '__main__':
    main()




