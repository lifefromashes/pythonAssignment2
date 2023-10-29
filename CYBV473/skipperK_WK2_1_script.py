from __future__ import print_function

from prettytable import PrettyTable

'''
Week Two Assignment 1 - File Processing
Kristin Skipper
CYBV 473
August 30, 2023
'''

'''
Complete the script below to do the following:
1) Add your name, date, assignment number to the top of this script
2) Open the file redhat.txt 
   a) Iterate through each line of the file
   b) Split eachline into individual fields (hint str.split() method)
   c) Examine each field of the resulting field list
   d) If the word "worm" appears in the field then add the worm name to the set of worms
   e) Once you have processed all the lines in the file
      sort the set 
      iterate through the set of worm names
      print each unqiue worm name 
3) Submit
   NamingConvention: lastNameFirstInitial_Assignment_.ext
   for example:  hosmerC_WK2-1_script.py
                 hosmerC_WK2-2_screenshot.jpg
   A) Screenshot of the results in WingIDE
   B) Your Script
'''

import os

uniqueWorms = set()

# Opening the file that is saved in same place as the script
# also tested with opening it from other saved location
# with open("c:/redhat.txt", 'r') as logFile:
with open("redhat.txt", 'r') as logFile:
    for eachLine in logFile:
        eachLineList = eachLine.split()
        for eachItem in eachLineList:
            '''
             Use builtin contains method.....to see if a string contains the 
             value and would return true/false if does and then add that item to the set
            '''
            if eachItem.__contains__('Worm'):
                uniqueWorms.add(eachItem)
    print('UniqueWorms: ', uniqueWorms)

    # Sort the set using python builtin sorted method
    sortedSet = sorted(uniqueWorms)
    print('Sorted set: ', sortedSet)

    # iterate through the set of worm names & print each unique worm names in a pretty table
    tbl = PrettyTable(['Worm', 'Name Of Worm Found In File'])

    for eachWorm in sortedSet:
        # print('UNIQUE WORM NAME: ', eachWorm)
        # iterate through sorted set and add each worm to the pretty table
        tbl.add_row(['Worm Name', eachWorm])
    print(tbl)


