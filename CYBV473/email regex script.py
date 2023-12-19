'''
Using Regular Expressions to Find e-mails
Professor Hosmer
August 2020
'''

import sys
import re
from binascii import hexlify

# File Chunk Size
CHUNK_SIZE = 1024

# regular expressions

ePatt = re.compile(b'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')

# Create empty lists
emailList = []

# Read in the binary file test.bin
with open('test.bin', 'rb') as binaryFile:
    while True:
        chunk = binaryFile.read(CHUNK_SIZE)
        if chunk:
            emails = ePatt.findall(chunk)

            for eachEmail in emails:
                emailList.append(eachEmail)
        else:
            break

print("\nPossible e-mails\n")
for eachPossibleEmail in emailList:
    print(eachPossibleEmail)


