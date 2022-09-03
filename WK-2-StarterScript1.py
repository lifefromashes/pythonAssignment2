'''
Script:  WK-2 Starter Script
Author:  Kristin Skipper
Date:    Submission Date
Version: 
Purpose: Search a file directory and iterate through to see each files path, size and Mac Times
'''
from prettytable import PrettyTable

''' IMPORT STANDARD LIBRARIES '''
import os  # File System Methods
import time  # Time Conversion Methods

''' IMPORT 3RD PARTY LIBRARIES '''
# NONE

''' DEFINE PSEUDO CONSTANTS '''

''' LOCAL FUNCTIONS '''


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
                            readableTimeCreated]  # Group the human-readable MAC Times in a List
        return True, None, fileSize, readableTimeList

    except Exception as err:
        return False, str(err), None, None


def makeTimeReadable(timeTOChange):
    timeToModify = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeTOChange))
    return timeToModify


''' MAIN ENTRY POINT '''

if __name__ == '__main__':

    print("First Script: Obtain File Meta Data\n")
    # targetFile = input("Enter File Path to Process: ")
    while True:
        targetDirectory = input("\nPlease Enter a Directory: ")
        if os.path.isdir(targetDirectory):

            print("\nProcessing: ", targetDirectory)

            dirEntries = os.listdir(targetDirectory)
            for eachEntry in dirEntries:
                fullPath = os.path.join(targetDirectory, eachEntry)
                success, errInfo, fileSize, timeList = GetFileMetaData(fullPath)
                print("=" * 100)

                if success:
                    print("Success:   ", fullPath)
                    print("File Size: ", fileSize)
                    print("UTC_LastAccessed: ", timeList[0])
                    print("UTC_LastModified: ", timeList[1])
                    print("UTC_Created: ", timeList[2])
                else:
                    print("Fail:    ", fullPath, "Exception =     ", errInfo)
                print(eachEntry)
        else:
            print("\nInvalid Directory ... Please Try Again\n")
    # DIR = input("Enter Directory Path: ")
    #
    # tbl = PrettyTable(['FilePath', 'FileType', 'FileSize', 'UTC_Modified', 'UTC_Accessed', 'UTC_Created'])
    #
    # fileList = os.listdir(DIR)
    # for eachFile in fileList:
    #     filePath = os.path.join(DIR, eachFile)
    #     absPath = os.path.abspath(filePath)
    #     if os.path.isfile(absPath):
    #         fileSize = os.path.getsize(absPath)
    #         tbl.add_row([absPath, fileSize])
    #         utcModified = os.path.getmtime(absPath)
    #         tbl.add_row([absPath, utcModified])
    #         utcAccessed = os.path.getatime(absPath)
    #         tbl.add_row([absPath, utcAccessed])
    #         utcCreated = os.path.getctime(absPath)
    #         tbl.add_row([absPath, utcCreated])

    # print("Accessing Metadata for : ", targetFile)
    #     fullPath = os.path.abspath(targetFile)
    #     success, errInfo, fileSize, macList = GetFileMetaData(fileList)

    # if success:
    #     print("Success:   ", fileList)
    #     print("File Size: ", fileSize)
    #     print("MAC Times: ", macList)
    # else:
    #     print("Fail:    ", fileList, "Exception =     ", errInfo)

    tbl.align = "l"
    resultString = tbl.get_string(sortby="FileSize", reversesort=True)
    print(resultString)

print("\nScript End")
