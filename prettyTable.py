''' 
PrettyTable Usage example
Professor Hosmer
September 2020
'''
from prettytable import PrettyTable
import os

# Create a tbl object that also defines the headings
tbl = PrettyTable(['FilePath','FileSize'])

DIR = input("Enter Directory Path: ")
fileList = os.listdir(DIR)
for eachFile in fileList:
    filePath = os.path.join(DIR, eachFile)
    absPath  = os.path.abspath(filePath)
    if os.path.isfile(absPath):
        fileSize = os.path.getsize(absPath)
        tbl.add_row( [ absPath, fileSize] )                    

tbl.align = "l" 
resultString = tbl.get_string(sortby="FileSize", reversesort=True)
print(resultString)

