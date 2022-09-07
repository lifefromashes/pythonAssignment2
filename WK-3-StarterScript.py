'''
WK-3 STARTER SCRIPT
PROFESSOR HOSMER
MAY 22
'''

# Python Standard Libaries 
import os
import hashlib

# Python 3rd Party Libraries
from prettytable import PrettyTable     # pip install prettytable

# Psuedo Constants

targetFolder = input("Enter Target Folder: ")
# Start of the Script
print("Walking: ", targetFolder, "\n")

tbl = PrettyTable(['FilePath','FileSize'])  

for currentRoot, dirList, fileList in os.walk(targetFolder):

    for nextFile in fileList:
        
        fullPath = os.path.join(currentRoot, nextFile)
        absPath  = os.path.abspath(fullPath)
        fileSize = os.path.getsize(absPath)
        
        tbl.add_row( [ absPath, fileSize] ) 

tbl.align = "l" # align the columns left justified
# display the table
print (tbl.get_string(sortby="FileSize", reversesort=True))


print("\nScript-End\n")