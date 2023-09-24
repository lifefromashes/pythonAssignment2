"""
Week 5 Assignment 7
Kristin Skipper
September 23, 2023

Instructions
An excerpt of a memory dump extracted by Access Data's FTK Imager mem.raw has been provided.

1) Copy the memory dump to the virtual desktop environment persistent storage area.

2) Develop a python script and regular expressions to extract and report ALL the e-mail and urls found in the memory dump.

REGULAR EXPRESSIONS HELP

e-mail and url patterns

ePatt = re.compile(b'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')
uPatt = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w.\.?=%&=\-@$,]*')

Submit:

1) Your Python script

2) Screenshot of your results.
"""
# File Chunk Size
import os
import re

from prettytable import PrettyTable
# Chunk size to read
CHUNK_SIZE = 4096
# Regex patterns
ePatt = re.compile(b'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')
uPatt = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w.\.?=%&=\-@$,]*')
# Create empty dict
emailDict = {}
urlDict = {}
# Open binary file
with open('mem.raw', 'rb') as binaryFile:
    while True:
        # Read in by chunk size
        chunk = binaryFile.read(CHUNK_SIZE)
        if chunk:
            # Use find all method to find regex patterns in the file for email and urls
            emails = ePatt.findall(chunk)
            urls = uPatt.findall(chunk)

            # Iterate through each email found and turn to lower case
            for eachEmail in emails:
                eachEmail = eachEmail.lower()
                try:
                    # Add each value found to the dictionary with count as key and email as value
                    value = emailDict[eachEmail]
                    # Increment by 1 if found again
                    value += 1
                    emailDict[eachEmail] = value
                except:
                    # Add to dictionary if not found
                    emailDict[eachEmail] = 1
            # Iterate through each url and turn to lower case
            for eachUrl in urls:
                eachUrl = eachUrl.lower()
                try:
                    # Add each value found to the dictionary with count as key and url as value
                    urlVal = urlDict[eachUrl]
                    # Increment by 1 if found again
                    urlVal += 1
                    urlDict[eachUrl] = urlVal
                except:
                    # Add to dictionary if not found
                    urlDict[eachUrl] = 1
        else:
            break

# Create pretty tables for emails and urls
resultTable = PrettyTable(['Count', 'Email Address'])
urlResultTable = PrettyTable(['UrlCount', 'URL'])

print("\nPossible e-mails\n")
# Iterate through dictionary and add rows to the table and decode using ascii to make human-readable
for key, value in emailDict.items():
    resultTable.add_row([value, key.decode('ascii', 'ignore')])
# Sort table by Count and put the most count at the top and print
print(resultTable.get_string(sortby='Count', reversesort=True))

print("\nPossible urls\n")
# Iterate through dictionary and add rows to the table and decode using ascii to make human-readable
for key, value in urlDict.items():
    urlResultTable.add_row([value, key.decode('ascii', 'ignore')])
    # Sort table by Count and put the most count at the top and print
print(urlResultTable.get_string(sortby='UrlCount', reversesort=True))
