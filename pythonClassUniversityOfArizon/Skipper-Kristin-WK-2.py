'''
Script:  WK-2 Starter Script
Author:  Kristin Skipper
Date:    09/03/2022
Version: 
Purpose: Search a file directory and iterate through to see each files path, size and Mac Times
'''
from prettytable import PrettyTable

''' IMPORT STANDARD LIBRARIES '''
import os  # File System Methods
import time  # Time Conversion Methods

''' IMPORT 3RD PARTY LIBRARIES '''
# NONE


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
        readableTimeList = [readableTimeLastAccess, readableTimeLastModified, # Group the human-readable MAC Times in a List
                            readableTimeCreated]
        return True, None, fileSize, readableTimeList

    except Exception as err:
        return False, str(err), None, None


def makeTimeReadable(timeTOChange):  #function to make time human readable
    timeToModify = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeTOChange))
    return timeToModify


''' MAIN ENTRY POINT '''

if __name__ == '__main__':

    print("Skipper-Kristin-WK-2-Scripting-Assignment\n")
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

print("\nScript End")
