'''
WK-12 Sentiment Analysis
11/2024
Kristin Skipper
'''
import re
import seaborn as sns
import matplotlib.pyplot as plt
print("Demonstration Sentiment Processing Model ... Kristin Skipper 2024")
print("Loading ML Libraries ..... Please Wait ...")
import pandas as pd

# Setup Prettytable for results
from prettytable import PrettyTable

tbl = PrettyTable(["Sentiment", "Tweet"])

# Machine Learning Imports
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

le = preprocessing.LabelEncoder()

# Psuedo Constants
DEBUG = True  # set DEBUG = True, for debug messages

# Psuedo Lookup for positive and negative sentiments
SENTIMENT = {1: "POSITIVE", 0: "NEGATIVE"}

# Set Panda Options
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 2000)

# Create simplified dataframe for globalWarming.csv
# Just two columns, existence, tweet
print("\nCreating dataframe from globalWarming.csv ...")
df = pd.read_csv('globalWarming.csv', encoding='ISO-8859-1')

df = df.rename(columns={'existence': 'Sentiment', 'tweet': 'Tweet'})
df = df[['Sentiment', 'Tweet']]
print(df.head())

# Psuedo Lookup for positive and negative sentiments
SENTIMENT = {1: "Yes", 0: "No"}


def getFeatures(twt):
    ''' Model for feature extraction
        This is just and example not the real features
        that will be included.
    '''
    twtLen = len(twt)
    wordList = twt.split()
    wordLen = len(wordList)
    return [twtLen, wordLen]


def main():
    featureList = []  # List of features for each sample
    sentimentList = []  # Corresponding sentiment

    # Select a simple training and testing set
    # as an example

    dfTrain = df[0:40]
    dfTest = df[40:80]

    if DEBUG:
        print("\nCheck the trianing and testing dataframes")
        print("Train:", dfTrain)
        print("Test: ", dfTest)

    '''
    Process each row in the training dataframe
    '''
    print("Processing Training Dataframe ...")
    for row in dfTrain.itertuples():
        # only process rows that are either Yes or No Sentiment Values
        if row.Sentiment != 'Yes' and row.Sentiment != 'No':
            continue
        sentimentList.append(row.Sentiment)  # update the sentiment list

        curTweet = row.Tweet

        # tLen, tWords = getFeatures(curTweet)
        # featureList.append([tLen, tWords])  # Updat the corresponding feature list

        features = getFeatures(curTweet)
        featureList.append(features)  # Update the corresponding feature list

    # encode the Sentiment either 0 = No or 1 = Yes
    encodedSentiment = le.fit_transform(sentimentList)

    # print the resulting feature and sentiment list as a check
    if DEBUG:
        print()
        print("Features:  ", featureList)
        print("Sentiments:", encodedSentiment)

    # Create a K Nearest Neighbor Classifier
    print("Creating Nearest Neighbor Classifer Model ...")
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(featureList, encodedSentiment)

    # Now test the modeul using the dfTest dataframe
    print("Applying the Model to the testing data ...")
    for row in dfTest.itertuples():
        # get the tweet and get the features
        tstTweet = row.Tweet
        features = getFeatures(tstTweet)

        # use the features to predict the result
        prediction = model.predict([features])
        result = SENTIMENT[prediction[0]]
        tbl.add_row([result, tstTweet])

    print()
    tbl.align = 'l'
    print(tbl.get_string())


if __name__ == '__main__':
    main()
    print("\nScript End")

# Importing necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
import pandas as pd

dataset = pd.read_csv('globalWarming.csv', encoding='ISO-8859-1')

# Feature extraction using TF-IDF (Transforming 'tweet' column)
vectorizer = TfidfVectorizer(max_features=500)
X = vectorizer.fit_transform(dataset['tweet']).toarray()
y = dataset['existence'].apply(lambda x: 1 if x == 'Yes' else 0)  # Encoding labels

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the K-Nearest Neighbors model
knn = KNeighborsClassifier(n_neighbors=3)  # Using 3 as the number of neighbors
knn.fit(X_train, y_train)

# Evaluating the model's performance
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Printing the evaluation results
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:\n", report)


# Plotting the evaluation results
plt.figure(figsize=(8, 6))
sns.countplot(x=dataset['existence'], palette='viridis')
plt.title('Class Distribution in Dataset')
plt.xlabel('Global Warming Existence (Yes/No)')
plt.ylabel('Count')
plt.show()
