import time

'''
Script:  First Script
Author:  Chet Hosmer
Date:    July 2020
Version: .50
Purpose: script Description
'''

''' IMPORT STANDARD LIBRARIES '''
import os       # File System Methods
import time     # Time Conversion Methods
import sys      # System Methods

''' IMPORT 3RD PARTY LIBRARIES '''
# NONE

''' DEFINE PSEUDO CONSTANTS '''


''' LOCAL FUNCTIONS '''
# NONE

''' LOCAL CLASSES '''
# NONE

''' MAIN ENTRY POINT '''

if __name__ == '__main__':
    
    print("First Script: Obtain File Meta Data\n")

    targetFile = input("Enter File Path to Process: ")
    
    if not os.path.isfile(targetFile):
        sys.exit("Invalid File: " + targetFile)
    
    print("Accessing Metadata for : ", targetFile)    
    
    try:
        
        metaData         = os.stat(targetFile)       # Use the stat method to obtain meta data
        fileSize         = metaData.st_size          # Extract fileSize and MAC Times
        timeLastAccess   = metaData.st_atime
        timeLastModified = metaData.st_mtime
        timeCreated      = metaData.st_ctime
        
        print("MetaData:           ", metaData)
        print("File Size:          ", fileSize)
        print("Last Access Time:   ", timeLastAccess)
        print("Last Modified Time: ", timeLastModified)
        print("Creation Time:      ", timeCreated)
        
        # We have the times, but the system's representation of the time isn't human-readable
        # We need to convert the epoch times
        modEpoch = timeLastModified # Take our modified time we already got, and convert it to utcTime
        utcTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(modEpoch))
        
        print("\nEpoch time converted to human-readable form:")
        print("UTC time: " , utcTime)
    
    except Exception as err:
        print("Fail:    ", targetFile, "Exception = ", str(err))

print("\nScript End")
