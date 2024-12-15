'''
Kristin Skipper
Week 15 Assignment
CYBV474
12/14/2024
'''

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.metrics import classification_report, accuracy_score
from textblob import TextBlob  # For sentiment analysis
from scipy.sparse import hstack


# Load the dataset
file_path = 'CombinedNews.csv'
data = pd.read_csv(file_path, encoding='utf-8', on_bad_lines='skip', header=None)

# Print the shape of the dataset to understand the number of columns
print(f"Dataset shape: {data.shape}")
data = data[[0, 1]]
# Assign column names
data.columns = ['label', 'text']

# Remove rows with missing values
data = data.dropna()

# Ensure labels contain only "REAL" or "FAKE"
data = data[data['label'].isin(['REAL', 'FAKE'])]

# Remove rows with empty or whitespace-only text
data['text'] = data['text'].str.strip()  # Remove leading/trailing whitespace
data = data[data['text'] != ""]  # Drop empty rows

# Debug: Check dataset stats
print(f"Dataset after cleaning: {data.shape[0]} rows, {data.shape[1]} columns")
print(data['label'].value_counts())
print(data.head())

# Save cleaned dataset to a new file (if needed)
cleaned_file_path = 'CleanedCombinedNews.csv'
data.to_csv(cleaned_file_path, index=False)


# Load the dataset & suppress mixed types warning
file_path = 'CombinedNews.csv'
data = pd.read_csv(file_path, encoding='utf-8', on_bad_lines='skip', header=None, low_memory=False)

# Inspect dataset structure
print(f"Dataset shape: {data.shape}")
print(data.head())

# Keep only the first two columns
data = data[[0, 1]]  # first column is 'label' and the second column is 'text'

# Assign the column names
data.columns = ['label', 'text']

# Remove rows with missing values
data = data.dropna()

# Ensure labels contain only "REAL" or "FAKE"
data = data[data['label'].isin(['REAL', 'FAKE'])]

# Remove rows with empty or whitespace-only text
data['text'] = data['text'].str.strip()
data = data[data['text'] != ""]  # Drop empty rows

# For Debugging: Checking the dataset stats
print(f"Dataset after cleaning: {data.shape[0]} rows, {data.shape[1]} columns")
print(data['label'].value_counts())
print(data.head())

# Save cleaned dataset to a new file
cleaned_file_path = 'CleanedCombinedNews.csv'
data.to_csv(cleaned_file_path, index=False)

# 1. Load the Cleaned Data
file_path = 'CleanedCombinedNews.csv'
data = pd.read_csv(file_path)

# 2. Feature Extraction
# Add word count
data['word_count'] = data['text'].apply(lambda x: len(str(x).split()))

# Add sentence count
data['sentence_count'] = data['text'].apply(lambda x: len(str(x).split('.')))

# Add average word length
data['avg_word_length'] = data['text'].apply(lambda x: np.mean([len(word) for word in str(x).split()]))

# Add sentiment polarity which TextBlob returns a value between -1 (negative) and 1 (positive)
data['sentiment'] = data['text'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Detect clickbait phrases
clickbait_phrases = ["you won't believe", "shocking", "unbelievable", "amazing", "what happened next"]
data['has_clickbait'] = data['text'].apply(lambda x: int(any(phrase in x.lower() for phrase in clickbait_phrases)))


data['has_author'] = 0  # Assume no author info is available

# Combine numerical features
numerical_features = ['word_count', 'sentence_count', 'avg_word_length', 'sentiment', 'has_clickbait', 'has_author']
X_numerical = data[numerical_features]

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_tfidf = tfidf_vectorizer.fit_transform(data['text']).toarray()  # Convert sparse matrix to dense array for GaussianNB

# Combine TF-IDF and numerical features
X_combined = np.hstack([X_tfidf, X_numerical])

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_combined, data['label'].map({'REAL': 1, 'FAKE': 0}),
                                                    test_size=0.3, random_state=42) # Use 0.3 fr 30% test data

# 4. Model Training
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

# 5. Make Predictions
y_pred = nb_classifier.predict(X_test)

# 6. Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Check if accuracy is >= 75%
if accuracy >= 0.75:
    print("The model accuracy is greater than or equal to 75%")
else:
    print("The model accuracy is less than 75% and may not be reliable")

print("Classification Report:\n", classification_report(y_test, y_pred))

# Calculate and report the results
correctly_identified = (y_pred == y_test).sum()  # Count correct predictions
test_set_size = len(y_test)  # Total number of samples in the test set

print(f"Correctly Identified: {correctly_identified} / Testing Set Size: {test_set_size}")

# Combine the training and testing sets with labels
train_set = pd.DataFrame(X_train)
train_set['label'] = y_train.values

test_set = pd.DataFrame(X_test)
test_set['label'] = y_test.values

# Save to CSV files uncomment if want to use
# train_set.to_csv('training_set.csv', index=False)
# test_set.to_csv('testing_set.csv', index=False)
#
# print("Training and testing sets saved successfully!")



