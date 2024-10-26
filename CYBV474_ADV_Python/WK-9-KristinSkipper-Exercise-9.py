'''
Script Purpose: Week 9 Exercise #9
Script Version: Fall 2024
Script Author:  Kristin Skipper
'''

print("\nGender Analysis of Tweets")
print("Loading ML Libraries ... please wait")

import re
import pandas as pd
from nltk import trigrams, NaiveBayesClassifier, classify
from sklearn.model_selection import train_test_split


def scrubTweet(twt):
    # Updated to allow mentions and hashtags as females often use a lot of hashtags
    twt = re.sub(r"[^a-zA-Z#@ ]", " ", twt.lower())
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

    features = {}
    features['charCount'] = len(twt)
    # Total number of words in the tweet
    features['tweetLength'] = len(twt.split())
    # Find the average word length in the tweet
    features['avgWordLength'] = sum(len(word) for word in twt.split()) / (features['tweetLength'] + 1)
    # Calculate the number of words in male tweets and female tweets
    features['maleWordCount'] = sum(1 for word in twt.split() if word in maleWords)
    features['femaleWordCount'] = sum(1 for word in twt.split() if word in femaleWords)
    # Count the number of exclamation and question marks
    features['exclamationCount'] = twt.count('!')
    features['questionMarkCount'] = twt.count('?')
    features['mentionCount'] = twt.count('@')
    features['hashtagCount'] = twt.count('#')
    print(f'Male words: {len(maleWords)}, Female words: {len(femaleWords)}')
    print('Sample Female Words:', list(femaleWords)[:10])

    return features


def main():
    df = pd.read_csv("tweetsClean_1.csv")
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





