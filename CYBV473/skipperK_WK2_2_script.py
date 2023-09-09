from __future__ import print_function

from prettytable import PrettyTable

'''
Week Two Assignment 2 - File Hashing
Kristin Skipper
September 4, 2023
'''

'''
Complete the script below to do the following:
1) Add your name, date, assignment number to the top of this script
2) Using the os library and the os.walk() method 
   a) Create a list of all files
   b) Create an empty dictionary named fileHashes 
   c) Iterate through the list of files and
      - calculate the md5 hash of each file
      - create a dictionary entry where:
        key   = md5 hash
        value = filepath
    d) Iterate through the dictionary
       - print out each key, value pair

3) Submit
   NamingConvention: lastNameFirstInitial_Assignment_.ext
   for example:  hosmerC_WK1_script.py
                 hosmerC_WK1_screenshot.jpg
   A) Screenshot of the results in WingIDE
   B) Your Script
'''

import os
import hashlib

directory = "."

fileList = []  # 2a) create list
fileHashes = {}  # 2b) create dictionary

if __name__ == '__main__':

    for root, dirs, files in os.walk(directory):

        # Walk the path from top to bottom.
        # For each file obtain the filename
        for fileName in files:
            path = os.path.join(root, fileName)
            fullPath = os.path.abspath(path)
            # Create a list of allfiles
            fileList = fullPath
            # Using print statement to test
            # print('File List: ', fileList)

            # Open files in the file list in binary read mode, with statement makes sure the file closes after executing
            with open(fileList, 'rb') as fileToHash:
                fileContents = fileToHash.read()
                # Use md5 hash from hash library
                hashObj = hashlib.md5()
                # Updates the obj and hashes the files contents
                hashObj.update(fileContents)
                # Calculates the hexadecimal digest ad stores in filehash variable
                fileHash = hashObj.hexdigest()
                # Using print statement to test
                # print('File Hash: ', fileHash)

            # Create dictionary with filehash as key and full path as value
            fileHashes[fileHash] = fullPath
            # Using print statement to test
            # print('Dict: ', fileHashes)
        # Create pretty table headers
        tbl = PrettyTable(['FileHash', 'FilePath'])
        # Iterate through dictionary and print the key and value and then add the key and value to the pretty table
        # with the.add_row function
        for key, value in fileHashes.items():
            # Using print statement to test
            # print('Dictionary key: ', key, '   ', 'Dictionary Value: ', value)
            tbl.add_row([key, value])
        print('******************************************************************************************************')
        print('Key & Value in Pretty Table')
        print(tbl)
