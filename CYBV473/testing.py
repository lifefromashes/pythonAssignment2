import os
import re
from prettytable import PrettyTable

# File Chunk Size
CHUNK_SIZE = 4096
wPatt = re.compile(b'[a-zA-Z]{5,15}')
stringDictionary = {}
sorted_strings = []
resultTable = PrettyTable(['String', 'Number of Occurrences'])

with open('mem.raw', 'rb') as binaryFile:
    while True:
        fileContents = binaryFile.read(CHUNK_SIZE)
        if not fileContents:
            break  # Exit the loop when reaching the end of the file

        # Find all strings matching the pattern
        matches = wPatt.findall(fileContents)

        for match in matches:
            match_string = match.decode('utf-8')

            # Update the occurrences in the dictionary
            if match_string in stringDictionary:
                stringDictionary[match_string] += 1
            else:
                stringDictionary[match_string] = 1

# Sort the dictionary by occurrences and populate the sorted_strings list
sorted_strings = sorted(stringDictionary.items(), key=lambda item: item[1], reverse=True)

row_limit = 20

# Add rows to the PrettyTable, respecting the row limit
for string, occurrences in sorted_strings[:row_limit]:
    resultTable.add_row([string, occurrences])

# Print the PrettyTable
print(resultTable)
