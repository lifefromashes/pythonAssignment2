import os


DIR = input("Enter Directory Path: ")
fileList = os.listdir(DIR)
for eachFile in fileList:
    filePath = os.path.join(DIR, eachFile)
    absPath  = os.path.abspath(filePath)
    if os.path.isfile(absPath):
        fileSize = os.path.getsize(absPath)


print(resultString)
