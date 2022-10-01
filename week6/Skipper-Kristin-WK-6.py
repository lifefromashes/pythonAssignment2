'''
WK-6 Scripting Assignment
CYBV 312
Kristin Skipper
Date:
'''

# Python Standard Libaries 
import os
import re
import logging
import platform
import socket
import sys
import time
import uuid
import hashlib  # Python standard library hashlib

import psutil  # pip install psutil


def getSystemInfo():
    try:

        info = {}
        info['platform'] = platform.system()
        info['platform-release'] = platform.release()
        info['platform-version'] = platform.version()
        info['architecture'] = platform.machine()
        info['hostname'] = socket.gethostname()
        info['ip-address'] = socket.gethostbyname(socket.gethostname())
        info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor'] = platform.processor()
        info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
        return info
    except Exception as e:
        logging.exception(e)
        return False


def main():
    # Remove any old logging script
    if os.path.isfile('Kristin Skipper-ScriptLog.txt'):  # REPLACE YOURNAME with Your Name
        os.remove("Kristin Skipper-ScriptLog.txt")

    # configure the python logger, Replace YOURNAME
    logging.basicConfig(filename='Kristin Skipper-ScriptLog.txt', level=logging.DEBUG,
                        format='%(process)d-%(levelname)s-%(asctime)s %(message)s')
    logging.info("Script Start\n")

    investigator = input("Investigator Name:  ")  # Enter Your Name at this prompt
    organization = input("Class Code  :       ")  # Enter the Class at this prompt i.e. CYBV-312 YOUR SECTION

    sysInfo = getSystemInfo()

    def hashFileContents(contents):
        sha512Obj = hashlib.sha512()
        sha512Obj.update(contents)
        hexDigest = sha512Obj.hexdigest()
        return hexDigest

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

    if sysInfo:
        ''' YOUR CODE GOES HERE 
            Write all collected information to the log file
        '''
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

                    fileInfoDictionary = {}
                    fileInfoDictionary['Path'] = absPath
                    fileInfoDictionary['FileSize'] = fileSize

                    for key, value in fileInfoDictionary.items():
                        logging.info(key, '\t', value)

                    with open(fullPath, 'rb') as target:
                        fileContents = target.read()
                        sha256Hash = hashFileContents(fileContents)

                    # tbl.add_row([absPath, fileType, fileSize, lastAccessed, lastModified, createdTime, sha256Hash])


        startTime = time.time()

        systemInfoDictionary = getSystemInfo()
        logging.info(startTime)
        for key, value in systemInfoDictionary.items():
            logging.info(key + "\t" + value)

        endTime = time.time()
        elapsedTime = endTime - startTime

        logging.info(elapsedTime)


if __name__ == '__main__':
    print("\n\nWeek-6 Logging Starter Script - Kristin Skipper \n")
    print()
    main()
    print("\nScript End")
