'''
Week 8 Exercise
Kristin Skipper
October 2024
'''

from nltk.corpus import names
from nltk import NaiveBayesClassifier,classify, accuracy
import random

print("Gender Name Identifier using a NaiveBayesClassifier\n")


def genderFeatures(theName):
    theName = theName.lower()
    theNameLen = len(theName)
    VOWELS = 'aeiouy'
    vowelCnt = 0

    # Count the number of vowels and consonants
    for eachLetter in theName:
        if eachLetter in VOWELS:
            vowelCnt += 1
    consonantCount = theNameLen - vowelCnt

    # Define common female suffixes to check
    # Added since it was classifying my name as male
    common_female_suffixes = ('a', 'ine', 'ina', 'ette', 'elle', 'n')

    features = {}
    features['first_letter'] = theName[0]
    features['last_letter'] = theName[-1]
    features['second_last_letter'] = theName[-2]
    features['consonant_count'] = consonantCount
    features['vowel_count'] = vowelCnt
    features['nameLen'] = theNameLen
    features['is_female_suffix'] = True if any(theName.endswith(suffix) for suffix in common_female_suffixes) else False
    features['prefix_kris'] = theName.startswith('kris')
    features['vowelPercent'] = round(vowelCnt / theNameLen, 2)

    return features

def evaluate_test_names_set(test_set):
    correct = 0
    for (name, gender) in test_set:
        guess = genderClassifer.classify(genderFeatures(name)) # Use genderFeatures to classify the name
        print(f'{name} is classified as {guess} (Actual: {gender})')
        if guess == gender:
            correct += 1
    accuracy = correct / len(test_set)
    print(f'Test Set Accuracy: {accuracy}')
    return correct


# Collect the names label from the NTLK Corpus names
nameLabels = ([(name, 'male') for name in names.words('male.txt')] +
              [(name, 'female') for name in names.words('female.txt')])
random.shuffle(nameLabels)

sampleSize = len(nameLabels)
trainingSize = int(sampleSize * 0.70)
testSize = sampleSize - trainingSize

# Create a Feature set using the last Letter of each name
trainingFeatureSet = [(genderFeatures(n), gender) for (n, gender) in nameLabels[0:trainingSize]]
testingFeatureSet = [(genderFeatures(n), gender) for (n, gender) in nameLabels[trainingSize:]]

# Create a NaiveBayes Gender Classifer from the Training Set
genderClassifer = NaiveBayesClassifier.train(trainingFeatureSet)

print('TrainSet Accuracy: ', classify.accuracy(genderClassifer, trainingFeatureSet))
print('TestSet  Accuracy: ', classify.accuracy(genderClassifer, testingFeatureSet), "\n")
# Show the most informative features
genderClassifer.show_most_informative_features(20)

# Comment / Uncomment if wanting to use interactively
while True:
    testName = input("\nEnter Name to Classify (or 'q' to quit): ")
    if testName.lower() == 'q':
        break
    else:
        gender = genderClassifer.classify(genderFeatures(testName))
        print(f'{testName} is classified as {gender}')
        print(testName, gender)

test_names = [
    ("Kristin", "female"),
    ("Kristine", "female"),
    ("Collin", "male"),
    ("Colton", "male"),
    ("Kassidy", "female"),
    ("Tomyla", "female"),
    ("Sarah", "female"),
    ("Kaden", "male"),
    ("Rioyce", "male"),
    ("Trish", "female"),
]
print("\nClassifying Test Set: ")
evaluate_test_names_set(test_names)

print("\nScript Terminated by user")
