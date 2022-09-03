'''
Script:  WK-2 Starter Script
Author:  Your Name
Date:    Submission Date
Version: 
Purpose: Descibe your script
'''

''' IMPORT STANDARD LIBRARIES '''
import os  # File System Methods
import time  # Time Conversion Methods

''' IMPORT 3RD PARTY LIBRARIES '''
# NONE

''' DEFINE PSEUDO CONSTANTS '''

TARGET = "TESTFILE.JPG"  # Get the local name of this script

''' LOCAL FUNCTIONS '''


def GetFileMetaData(fileName):
    """
        obtain filesystem metadata
        from the specified file
        specifically, fileSize and MAC Times

        return True, None, fileSize and MacTimeList
    """
    try:

        metaData = os.stat(fileName)  # Use the stat method to obtain meta data
        fileSize = metaData.st_size  # Extract fileSize and MAC Times
        timeLastAccess = metaData.st_atime
        timeLastModified = metaData.st_mtime
        timeCreated = metaData.st_ctime

        macTimeList = [timeLastModified, timeLastAccess, timeCreated]
        modEpoch = macTimeList  # Take our modified time we already got, and convert it to utcTime
        utcTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(modEpoch))
        # Group the MAC Times in a List
        return True, None, fileSize, macTimeList

    except Exception as err:
        return False, str(err), None, None




''' LOCAL CLASSES '''
# NONE

''' MAIN ENTRY POINT '''

if __name__ == '__main__':

    print("First Script: Obtain File Meta Data\n")
    while True:
        targetFolder = input('\nPlease Enter Folder To Process: ')
        if not os.path.isdir(targetFolder):
            print('Invalid folder name\n')
            continue
        else:
            targetFolderList = os.listdir(targetFolder)  # returns names in the directory
            print("Accessing Metadata for : ", targetFolder)
            print('=' * 60)

            for eachEntry in targetFolderList:
                fullPath = os.path.join(targetFolder, eachEntry)
                success, errInfo, fileSize, macList = GetFileMetaData(fullPath)

                if success:
                    print("Success: ", fullPath)
                    print("File size: ", fileSize)
                    print("MAC Times: ", macList)
                    # print("MAC Times: ", macList)
                else:
                    print("Fail: ", fullPath, "Exception = ", errInfo)
    # print("Accessing Metadata for : ", TARGET)
    # fullPath = os.path.abspath(TARGET)
    # success, errInfo, fileSize, macList = GetFileMetaData(TARGET)
    # if success:
    #     print("Success:   ", TARGET)
    #     print("File Size: ", fileSize)
    #     print("MAC Times: ", macList)
    # else:
    #     print("Fail:    ", TARGET, "Exception =     ", errInfo)

print("\nScript End")
