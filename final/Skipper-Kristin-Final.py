'''
Skipper, Kristin
Final Scripting Assignment
October 7, 2022
'''

import sys
import os
import re

print("\nSimple File Search v2\n")
print("Final Script")
with open("mem.raw", 'rb') as target:  # assumes that mem.raw is in the same folder as script

    contents = target.read()  # read the entire contents of the file

    txt = re.sub(b"[^A-Za-z']", b' ', contents)  # strip all non alpha characters
    txt = txt.lower()  # convert all to lower case
    txt = txt.decode("utf-8")  # convert to simple ASCII

    wordList = txt.split()  # Create a list of possible words
    print(len(wordList))
try:
    # Prompt user for a file and Chunk Size
    largeFile = input("Enter the name of a large File: ")
    chunkSize = 65535

    keywordList = [ b"kernel", b"encrypt", b"fairwitness"]

    hits = {}  # Create a dictionary to keep track of the hits
    for eachKeyword in keywordList:
        hits[eachKeyword] = 0

    if os.path.isfile(largeFile):  # Verify file is real
        with open(largeFile, 'rb') as targetFile:
            while True:
                fileChunk = targetFile.read(chunkSize)
                fileChunk = fileChunk.lower()  # broaden search

                if fileChunk:  # if we still have data
                    # Search this chunk for our keyword
                    for eachKeyword in keywordList:

                        if eachKeyword in fileChunk:
                            cnt = hits[eachKeyword]
                            hits[eachKeyword] = cnt + 1

                else:
                    # File has been processed
                    print("\nkeyword \tHits")
                    for key, value in hits.items():
                        print(key, "\t", value)
                    break

        with open('out.txt', 'w') as outFile:
            for key, value in hits.items():
                print(key, "\t", value, file=outFile)
            # print(hits.items())
            # items = hits.keys()
            # print(items)
            # values = hits.values()
            # print(values)
            kernelCount = hits[b'kernel']
            encryptCount = hits[b'encrypt']
            fairwitnessCount = hits[b'fairwitness']
            print('Kernel Count is : ', kernelCount , file=outFile)
            print('Encrypt Count is : ', encryptCount, file=outFile)
            print('Fair Witness Count is : ', fairwitnessCount, file=outFile)

        print("kernelCount: ", kernelCount)
        print("encryptCount:", encryptCount)
        print("fairwitnessCount: ", fairwitnessCount)
    else:
        print(largeFile, "is not a valid file")
        sys.exit("Script Aborted")

except Exception as err:
    sys.exit("\nException: " + str(err) + "Script Aborted")


print("\nFile Processed ... Script End")
