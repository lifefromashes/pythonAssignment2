'''
Hash File Class/Object and usage example
'''
from __future__ import print_function

import hashlib
import os
import sys
import time

''' Determine which version of Python '''
if sys.version_info[0] < 3:
    PYTHON_2 = True
else:
    PYTHON_2 = False


class FileHasher:

    def __init__(self):
        ''' Create object variables and Constants '''
        self.filePath = ''
        self.fileSize = ''
        self.modifiedTime = ''
        self.createTime = ''
        self.fileHash = ''
        self.hashType = ''
        self.VALID_HASH_TYPES = ['MD5', 'SHA1', 'SHA256', 'SHA512']
        self.lastErr = ''

    def SetFilePath(self, filePath):
        ''' Set the file path if valid
            Obtain file size and timestamps
            return True if valid and set the self.filePath object variable
        '''
        if os.path.isfile(filePath):
            if os.access(filePath, os.R_OK):
                self.filePath = filePath
                stats = os.stat(self.filePath)
                self.fileSize = stats.st_size
                self.modifiedTime = time.ctime(stats.st_mtime)
                self.createTime = time.ctime(stats.st_atime)
                self.lastErr = ''
                return True
            else:
                self.filePath = ''
                self.lastErr = 'Invalid File Path'
                return False

    def SetHashType(self, hashType):
        ''' Set the Hash Type verify it is supported '''
        if hashType in self.VALID_HASH_TYPES:
            self.hashType = hashType
            self.lastErr = ''
            return True
        else:
            self.hashType = ''
            self.lastErr = 'Invalid Hash Type'
            return False

    def __InitializeHashObject(self):

        if self.hashType == 'MD5':
            self.hashObj = hashlib.md5()
        elif self.hashType == 'SHA1':
            self.hashObj = hashlib.sha1()
        elif self.hashType == 'SHA256':
            self.hashObj = hashlib.sha256()
        elif self.hashType == 'SHA512':
            self.hashObj = hashlib.sha512()
        else:
            self.hashObj = hashlib.md5()

    def HashFile(self):
        ''' Using the object variables hash the file '''
        try:
            if self.hashType:
                self.__InitializeHashObject()
            else:
                self.lastErr = 'Hash Type not Set'
                return False
            with open(self.filePath, 'rb') as fileToHash:
                fileContents = fileToHash.read()
                self.hashObj.update(fileContents)
                self.fileHash = self.hashObj.hexdigest()
                self.lastErr = ''
                return True
        except Exception as err:
            self.lastErr = str(err)
            return False


print("Hash File Class Demonstration\n")

if PYTHON_2:
    fileName = raw_input("Enter file to hash: ")
else:
    fileName = input("Enter file to hash: ")

obj = FileHasher()

print("\nProcessing File ...\n")

if obj.SetFilePath(fileName):
    if obj.SetHashType('SHA256'):
        if obj.HashFile():
            print("Path:               ", obj.filePath)
            print("File Size:          ", '{:,}'.format(obj.fileSize), "Bytes")
            print("File Created Time:  ", obj.createTime)
            print("File Modified Time: ", obj.modifiedTime)
            print("Hash Type:          ", obj.hashType)
            print("Hash Value:         ", obj.fileHash)
        else:
            print("Hashing Failed: ", obj.lastErr)
    else:
        print("Failed to Set HashType: ", obj.lastErr)
else:
    print("File Name Err: ", obj.lastErr)

print("\nScript End")
