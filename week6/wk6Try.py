'''
Python Logging Example
Professor Hosmer
August 2020
'''
import hashlib
import logging  # Python Standard Logging Library

# Turn on Logging
import os
import sys
import time

from prettytable import PrettyTable

print("\nSample Python Logging\n")
# logging.basicConfig(filename='ScriptLog.txt', level=logging.DEBUG,
#                     format='%(process)d-%(levelname)s-%(asctime)s %(message)s')

tbl = PrettyTable(['AbsPath', 'FileType', 'FileSize', 'LastModified', 'LastAccess', 'CreatedTime', 'SHA-256 HASH'])


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

        # Group the human-readable MAC Times in a List
        readableTimeList = [readableTimeLastAccess, readableTimeLastModified,
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


while True:
    targetFolder = input("Enter Target Folder: ")
    if os.path.isdir(targetFolder):
        print('Path is folder: ', targetFolder)
        break
    else:
        print('Invalid folder choice please try again')
        continue

print("Walking: ", targetFolder, "\n")

for currentRoot, dirList, fileList in os.walk(targetFolder):
    try:
        for nextFile in fileList:
            fullPath = os.path.join(currentRoot, nextFile)
            absPath = os.path.abspath(fullPath)

            success, errInfo, fileSize, timeList = GetFileMetaData(absPath)

            if success:
                if os.path.isfile(fullPath):
                    fileType = 'File'
                elif os.path.isdir(fullPath):
                    fileType = 'Directory'
                elif os.path.islink(fullPath):
                    fileType = 'Link'

            lastAccessed = timeList[0]
            lastModified = timeList[1]
            createdTime = timeList[2]

            with open(fullPath, 'rb') as target:
                fileContents = target.read()
                sha256Hash = hashFileContents(fileContents)

            tbl.add_row([absPath, fileType, fileSize, lastAccessed, lastModified, createdTime, sha256Hash])
    except Exception as err:
        sys.exit("\nException: " + str(err))

def getFileInfo():
    try:
        fileInformationDict = {}
        fileInformationDict['Path'] = absPath
        return fileInformationDict
    except Exception as error:
        logging.exception(error)
        return False

def main():
    # Remove any old logging script
    if os.path.isfile('Kristin-Skipper-Wk-6-ScriptLog.txt'):  # REPLACE YOURNAME with Your Name
        os.remove("Kristin-Skipper-Wk-6-ScriptLog.txt")

    # configure the python logger, Replace YOURNAME
    logging.basicConfig(filename='YOURNAME-ScriptLog.txt', level=logging.DEBUG,
                        format='%(process)d-%(levelname)s-%(asctime)s %(message)s')
    logging.info("Script Start\n")

    investigator = input("Investigator Name:  ")  # Enter Your Name at this prompt
    organization = input("Class Code  :       ")

    fileInfo = getFileInfo()

    for key, value in fileInfo.items():
        logging.info(key, value)


# logging.info('Script Started')
# logging.warning('Sample Warning Message  ')
# logging.error('Sample Error Message    ')
# logging.critical('Sample Critical Message ')
#
# print("\nScript Complete")
if __name__ == '__main__':
    print("\n\nWeek-6 Logging Starter Script - YOUR NAME \n")
    main()
    print("\nScript End")
