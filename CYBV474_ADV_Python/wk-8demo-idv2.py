'''
Simple Name Classifier
Using NaiveBayes
Professor Hosmer
February 2021
'''

from nltk.corpus import names
from nltk import NaiveBayesClassifier

print("Simple Gender Name Identifier using a NaiveBayesClassifier\n")


def genderFeatures(theName):
    ''' Extract the last  letters of each name'''
    return {'last_letter': theName[-1]}


# Collect the names label from the NTLK Corpus names
nameLabels = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in
                                                                      names.words('female.txt')])

# Create a Feature set using the last Letter of each name
featureSet = [(genderFeatures(n), gender) for (n, gender) in nameLabels]
# Create a training set and a test set from the features

# Create a NaiveBayes Gender Classifer from the Training Set
genderClassifer = NaiveBayesClassifier.train(featureSet)

while True:
    testName = input("\nEnter Name to Classify: ")
    if testName.lower() == 'q':
        break
    else:
        gender = genderClassifer.classify(genderFeatures(testName))
        print(testName, gender)

print("\nScript Terminated by user")

