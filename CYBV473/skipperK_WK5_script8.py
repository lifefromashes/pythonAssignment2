"""
Kristin Skipper
September 22, 2023
Assignment 8
An excerpt of a memory dump extracted by Access Data's FTK Imager mem.raw has been provided.

1) Copy the memory dump to the virtual desktop environment persistent storage area.

2) Develop a Python script to process the memory dump and identify unique strings of 5-15 characters along
 with the number of occurrences of each unique string.
 Then display the resulting list of strings and occurrences in a prettytable sorted by the highest number of occurrences.

REGULAR EXPRESSION HELP

word regx (more specifically continuous alpha string pattern)

wPatt = re.compile(b'[a-zA-Z]{5,15}')
"""

import os
import re
from prettytable import PrettyTable

# File Chunk Size
CHUNK_SIZE = 4096
# Regex pattern to find unique strings between 5 and 15 chars
wPatt = re.compile(b'[a-zA-Z]{5,15}')
stringDictionary = {}
sorted_strings = []
# Create pretty table
resultTable = PrettyTable(['String', 'Number of Occurrences'])
# Open binary file
with open('mem.raw', 'rb') as binaryFile:
    while True:
        fileContents = binaryFile.read(CHUNK_SIZE)
        if not fileContents:
            break  # This will exit the loop when reaching end of file
        # Find all strings matching the pattern
        matches = wPatt.findall(fileContents)
        for match in matches:
            # Make matches human-readable with decode
            match_string = match.decode('utf-8').lower()
            if match_string in stringDictionary:
                # Add each value found to the dictionary with count as key and match string as value
                value = stringDictionary[match_string]
                value += 1
                stringDictionary[match_string] = value
            else:
                # Add to dictionary if not found
                stringDictionary[match_string] = 1
# Using lambda with the key as the item on which it is sorted and list in reverse order so highest values are printed first
sorted_strings = sorted(stringDictionary.items(), key=lambda item: item[1], reverse=True)
# Limit rows to 50 printed out since large file
row_limit = 50
# Iterate through dict and add each row to the pretty table with the row limit
for string, occurrences in sorted_strings[:row_limit]:
    resultTable.add_row([string, occurrences])

print(resultTable)
