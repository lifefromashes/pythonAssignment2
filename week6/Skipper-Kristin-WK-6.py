'''
Skipper, Kristin
Week 6 Assignment
October 1st, 2022
'''

# Python Standard Libraries
import hashlib
import os
import re
import logging
import platform
import socket
import sys
import uuid
import psutil  # pip install psutil
import time

from prettytable import PrettyTable


def hashFileContents(contents):
    sha512Obj = hashlib.sha512()
    sha512Obj.update(contents)
    hexDigest = sha512Obj.hexdigest()
    return hexDigest


def makeTimeReadable(timeTOChange):  # function to make time human-readable
    timeToModify = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeTOChange))
    return timeToModify


def GetFileMetaData(fileName):
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


def getFileInfo():
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

                fileDict = {}
                fileDict['FilePath'] = absPath
                fileDict['File Type'] = fileType
                fileDict['File Size'] = str(fileSize)
                fileDict['Last Modified'] = lastModified
                fileDict['Last Access'] = lastAccessed
                fileDict['Created Time'] = createdTime
                fileDict['sha256Hash'] = sha256Hash
                return fileDict

        except Exception as err:
            sys.exit("\nException: " + str(err))


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
    if os.path.isfile('KristinSkipper-ScriptLog.txt'):  # REPLACE YOURNAME with Your Name
        os.remove("KristinSkipper-ScriptLog.txt")

    # configure the python logger, Replace YOURNAME
    logging.basicConfig(filename='KristinSkipper-ScriptLog.txt', level=logging.DEBUG,
                        format='%(process)d-%(levelname)s-%(asctime)s %(message)s')
    logging.info("Script Start\n")

    investigator = input("Investigator Name:  ")  # Enter Your Name at this prompt
    organization = input("Class Code  :       ")  # Enter the Class at this prompt i.e. CYBV-312 YOUR SECTION

    sysInfo = getSystemInfo()

    if sysInfo:
        ''' YOUR CODE GOES HERE 
            Write all collected information to the log file
        '''
        startTime = time.time()

        systemInfoDictionary = getSystemInfo()
        logging.info(startTime)
        for key, value in systemInfoDictionary.items():
            logging.info(key + "\t" + value)

        endTime = time.time()
        elapsedTime = endTime - startTime

        logging.info(elapsedTime)
        logging.info('=' * 80)

        fileInfoDict = getFileInfo()
        for key, value in fileInfoDict.items():
            logging.info(key + '\t' + value)
        logging.info('=' * 80)



if __name__ == '__main__':
    print("\n\nWeek-6 Logging Starter Script - YOUR NAME \n")
    main()
    print("\nScript End")
