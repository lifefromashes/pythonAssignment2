'''
Skipper, Kristin
Week 3 Assignment
Date:
'''

import csv
import os
import hashlib
import sys
from prettytable import PrettyTable  # pip install prettytable
import time  # Time Conversion Methods



# Start of the Script


while True:
    targetFolder = input("Enter Target Folder: ")
    if os.path.isdir(targetFolder):
        print('Path is folder: ', targetFolder)
        break
    else:
        print('Invalid folder choice please try again')
        continue

print("Walking: ", targetFolder, "\n")

tbl = PrettyTable(['AbsPath', 'FileSize', 'LastModified', 'LastAccess', 'CreatedTime', 'SHA-256 HASH'])


def GetFileMetaData(fileName):
    '''
        obtain filesystem metadata
        from the specified file
        specifically, fileSize and MAC Times

        return True, None, fileSize and MacTimeList
    '''
    try:

        metaData = os.stat(fileName)  # Use the stat method to obtain meta data
        fileSize = metaData.st_size  # Extract fileSize and MAC Times
        timeLastAccess = metaData.st_atime
        timeLastModified = metaData.st_mtime
        timeCreated = metaData.st_ctime

        readableTimeLastAccess = makeTimeReadable(timeLastAccess)
        readableTimeLastModified = makeTimeReadable(timeLastModified)
        readableTimeCreated = makeTimeReadable(timeCreated)
        readableTimeList = [readableTimeLastAccess, readableTimeLastModified,
                            # Group the human-readable MAC Times in a List
                            readableTimeCreated]
        return True, None, fileSize, readableTimeList

    except Exception as err:
        return False, str(err), None, None


def makeTimeReadable(timeTOChange):  # function to make time human-readable
    timeToModify = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeTOChange))
    return timeToModify


def hashFileContents(contents):
    sha512Obj = hashlib.sha512()
    sha512Obj.update(contents)
    hexDigest = sha512Obj.hexdigest()
    return hexDigest


for currentRoot, dirList, fileList in os.walk(targetFolder):
    try:
        for nextFile in fileList:
            fullPath = os.path.join(currentRoot, nextFile)
            absPath = os.path.abspath(fullPath)

            success, errInfo, fileSize, timeList = GetFileMetaData(absPath)

            lastAccessed = timeList[0]
            lastModified = timeList[1]
            createdTime = timeList[2]

            with open(fullPath, 'rb') as target:
                fileContents = target.read()
                sha256Hash = hashFileContents(fileContents)

            tbl.add_row([absPath, fileSize, lastAccessed, lastModified, createdTime, sha256Hash])
    except Exception as err:
        sys.exit("\nException: " + str(err))

tbl.align = "l"  # align the columns left justified
# display the table
print(tbl.get_string(sortby="FileSize", reversesort=True))

# display as csv string
csvString = tbl.get_csv_string()
# print(csvString)

#  Save to csv file:
with open('out.csv', 'w') as outFile:
    print(csvString, file=outFile)
# print(os.getcwd())  # My current dir = C:\Users\Owner\PycharmProjects\UniversityOfArizonaPractice\week3

print("\nScript-End\n")
