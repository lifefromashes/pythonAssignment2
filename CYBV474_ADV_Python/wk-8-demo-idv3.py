'''
Simple Name Classifier
Using NaiveBayes
Professor Hosmer
February 2021
'''

from nltk.corpus import names
from nltk import NaiveBayesClassifier,classify, accuracy
import random

print("Simple Gender Name Identifier using a NaiveBayesClassifier\n")

def genderFeatures(theName):

    theName = theName.lower()
    theNameLen = len(theName)
    VOWELS = 'aeiouy'
    vowelCnt = 0
    for eachLetter in theName:
        if eachLetter in VOWELS:
            vowelCnt += 1

    features = {}
    features['nameLen']      = theNameLen
    features['vowelPercent'] = round(vowelCnt/theNameLen, 2)
    features['lastLetter']     = theName[-1]

    return features

# Collect the names label from the NTLK Corpus names
nameLabels = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(nameLabels)

sampleSize = len(nameLabels)
trainingSize = int(sampleSize * .70)
testSize = sampleSize - trainingSize

# Create a Feature set using the last Letter of each name
trainingFeatureSet = [(genderFeatures(n), gender) for (n, gender) in nameLabels[0:trainingSize]]
testingFeatureSet  = [(genderFeatures(n), gender) for (n, gender) in nameLabels[trainingSize:]]

# Create a NaiveBayes Gender Classifer from the Training Set
genderClassifer = NaiveBayesClassifier.train(trainingFeatureSet)

print('TrainSet Accuracy: ',classify.accuracy(genderClassifer, trainingFeatureSet))
print('TestSet  Accuracy: ',classify.accuracy(genderClassifer, testingFeatureSet),"\n")
genderClassifer.show_most_informative_features(20)

print("\nScript End")
