'''
PrettyTable Usage example
Professor Hosmer
September 2020
'''
from prettytable import PrettyTable
import os

# Create a tbl object that also defines the headings
tbl = PrettyTable(['FilePath','FileSize'])

DIR = 'c:/'
fileList = os.listdir(DIR)
for eachFile in fileList:
    filePath = os.path.join(DIR, eachFile)
    if os.path.isfile(filePath):
        fileSize = os.path.getsize(filePath)
        tbl.add_row( [ filePath, fileSize] )

tbl.align = "l"
resultString = tbl.get_string(sortby="FileSize", reversesort=True)
print(resultString)

