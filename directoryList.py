'''
C. Hosmer
Obtain a list of entries found in a directory
July 2022
'''
import os   # Python Standard operating system library

while True:
    targetDirectory = input("\nPlease Enter a Directory: ")
    if os.path.isdir(targetDirectory):
        print("\nProcessing: ", targetDirectory)
        dirEntries = os.listdir(targetDirectory)
        for eachEntry in dirEntries:
            print(eachEntry)
    else:
        print("\nInvalid Directory ... Please Try Again\n")

    