'''
WK-5 Text Processing Exercise
Kristin Skipper
September 28, 2024
1. For each speech you will first normalize the text,
2. then remove all StopWords,
3.  and then extract the remaining words used in the speech.
4 You will place the words, the number of occurrences of each word along with the frequency of each word in a DataFrame
(one DataFrame per speech).
5. Your DataFrame will contain only the highest occurring 25 words ordered highest first.
'''
import re

import pandas as pd
from pandas import DataFrame

# Read in the Content of a file
def open_files(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as speech:
        file_contents =speech.read()
    return file_contents

# Normalize text to make it lower and remove special characters and return a list
def normalize_text(file_contents: str) -> list:
    # Convert to Lowercase
    content = file_contents.lower()
    # remove all extraneous content
    content = re.sub("[^a-z]", ' ', content)
    # Get the list of words
    wordList = content.split()
    return wordList

# Method for getting a list of STOP_WORDS
def get_list_of_stop_words() -> list:
    # Prepare a STOP_WORD List
    with open("STOP_WORDS.txt", 'r') as stops:
        stopWords = stops.read()
    STOP_WORDS = stopWords.split()
    return STOP_WORDS

# Create a dictionary of words along with the number of times they occur and return top 25
def get_word_info_and_top_25_words(file_contents: str) -> dict:
    STOP_WORDS = get_list_of_stop_words()
    word_dict = {}
    word_list = normalize_text(file_contents)

    for word in word_list:
        # ignore articles and STOP_WORDS
        if word in STOP_WORDS or len(word) <= 3:
            continue
        try:
            word_dict[word] += 1
        except:
            word_dict[word] = 1

    top_25_words = dict(sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[:25])

    return top_25_words


# Method to create a DF from the speech with the word, count & frequency and return it
def speech_to_df(filename: str) -> DataFrame:
    speech = open_files(filename)
    word_freq_dict = get_word_info_and_top_25_words(speech)
    total_words = sum(word_freq_dict.values())
    df = pd.DataFrame(list(word_freq_dict.items()), columns=['Word', 'Count'])
    df['Frequency'] = df['Count'] / total_words
    print(df)
    return df


# Main Script Starts Here
if __name__ == '__main__':
    #Print each DF to console
    print(f"\nSpeech 1 DataFrame\n")
    df1 = speech_to_df('SPEECH1.txt')
    print(f"\nSpeech 2 DataFrame\n")
    df2 = speech_to_df('SPEECH2.txt')
    print(f"\nSpeech 3 DataFrame\n")
    df3 = speech_to_df('SPEECH3.txt')
    print(f"\nSpeech 4 DataFrame\n")
    df4 = speech_to_df('SPEECH4.txt')
    print(f"\nSpeech 5 DataFrame\n")
    df5 = speech_to_df('SPEECH5.txt')

    # Write each speech DF to a csv file
    with open('C:\CYBV474_Adv_Python\Week5\speech_data_1.csv', 'w') as f:
        f.write("Speech 1 DataFrame\n")
        df1.to_csv(f, index=False)
    with open('C:\CYBV474_Adv_Python\Week5\speech_data_2.csv', 'w') as f:
        f.write("\nSpeech 2 DataFrame\n")
        df2.to_csv(f, index=False)
    with open('C:\CYBV474_Adv_Python\Week5\speech_data_3.csv', 'w') as f:
        f.write("\nSpeech 3 DataFrame\n")
        df3.to_csv(f, index=False)
    with open('C:\CYBV474_Adv_Python\Week5\speech_data_4.csv', 'w') as f:
        f.write("\nSpeech 4 DataFrame\n")
        df4.to_csv(f, index=False)
    with open('C:\CYBV474_Adv_Python\Week5\speech_data_5.csv', 'w') as f:
        f.write("\nSpeech 5 DataFrame\n")
        df5.to_csv(f, index=False)

