'''
WK 6
Kristin Skipper
Fall 2024
 Step One: Pre-process the text file to create a CSV file that contains two columns.
 Candidate, Candidate Response (Note, only the candidate responses will be included, you will eliminate the moderator lines)
'''
import csv
import re
from collections import Counter

import nltk
from nltk import pos_tag, word_tokenize, FreqDist
import pandas as pd
'''
Assumes that the debateRaw.txt file is in the 
same folder as the script
'''


def extract_candidate_responses(input_file, output_file, candidate_names):
    """
    Extract candidate responses from a text file and write to a CSV file.
    """
    # Define a regular expression pattern to match candidate names
    candidate_pattern = re.compile(r'(%s),' % '|'.join(candidate_names))

    # Initialize an empty list to store the candidate responses
    responses = []

    # Open the input file and read it line by line
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Check if the line matches the candidate pattern
            match = candidate_pattern.match(line)
            if match:
                # Extract the candidate name and response
                candidate = match.group(1)
                response = line[len(candidate) + 1:].strip()
                # Add the candidate and response to the list
                responses.append((candidate, response))

    # Open the output file and write the CSV data
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Candidate', 'Candidate Response'])  # header row
        writer.writerows(responses)



if __name__ == '__main__':
    DEBATE_FILE = "debateRaw.txt"
    output_file = 'C:/CYBV474_Adv_Python/Week6/candidate_responses.csv'
    candidate_names = ['Joe Biden', 'Bernie Sanders', 'Pete Buttigieg', 'Elizabeth Warren', 'Michael Bloomberg', 'Amy Klobuchar', 'Steve Bullock', 'Tom Steyer']

    print("Processing Debate File : ")

    try:
        extract_candidate_responses(DEBATE_FILE, output_file, candidate_names)
    except Exception as e:
        print(f"Error: {e}")


    # Read the .csv file
    df = pd.read_csv(output_file)

    # Dictionary to store POS tag counts for each candidate
    pos_counts_per_candidate = {}

    # Process each candidate's text
    for index, row in df.iterrows():
        candidate = row['Candidate']
        text = row['Candidate Response']

        # Convert to lowercase and remove non-alphabetic characters
        text = text.lower()
        text = re.sub("[^a-zA-Z ]", ' ', text)

        # Tokenize and POS tagging
        words = word_tokenize(text)
        tags = pos_tag(words)

        # Count POS tags
        counts = Counter(tag for word, tag in tags)

        # Store the counts in the dictionary with the candidate as the key
        pos_counts_per_candidate[candidate] = counts

    # Convert the dictionary into a DataFrame
    df_pos = pd.DataFrame(pos_counts_per_candidate).T.fillna(0).astype(int)

    # Reset index to add the 'Candidate' column
    df_pos.reset_index(inplace=True)
    df_pos.rename(columns={'index': 'Candidate'}, inplace=True)

    # Display the DataFrame
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    print(df_pos)






