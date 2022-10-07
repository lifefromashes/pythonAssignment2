'''
Add your name here
Final Script
June 2021
'''
import os
import re
import sys

print("Final Script")
with open("mem.raw", 'rb') as target:  # assumes that mem.raw is in the same folder as script
    
    contents = target.read() # read the entire contents of the file
    
    txt = re.sub(b"[^A-Za-z']", b' ', contents)  # strip all non alpha characters
    txt = txt.lower()                            # convert all to lower case
    txt = txt.decode("utf-8")                    # convert to simple ASCII
    
    wordList = txt.split()  # Create a list of possible words
    print(len(wordList))
    
    '''
    you will add your code here, that determines the number of occurrences
    of the following possible words found in the wordList
    
    kernel   encrypt  fairwitness  
    
    Note: You are NOT allowed to modify any other lines in the script, except
          to add your name in the comment block at the top
    Note: Your code will create the variables:  kernelCount, encryptCount, and fairwitnessCount
          so the print statements below will print out the correct number of occurrences
    '''

    keywordList = [b"kernel", b"encrypt", b"fairwitness"]

    hits = {}  # Create a dictionary to keep track of the hits
    for eachKeyword in keywordList:
        hits[eachKeyword] = 0

    if os.path.isfile(contents):  # Verify file is real
        with open(contents, 'rb') as targetFile:
            while True:
                fileChunk = targetFile.read(65535)
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
            print(hits.items())
            items = hits.keys()
            print(items)
            values = hits.values()
            print(values)
            kernelCount = hits[b'kernel']
            encryptCount = hits[b'encrypt']
            fairwitnessCount = hits[b'fairwitness']
            print('Kernel Count is : ', kernelCount, file=outFile)
            print('Encrypt Count is : ', encryptCount, file=outFile)
            print('Fair Witness Count is : ', fairwitnessCount, file=outFile)

        print("kernelCount: ", kernelCount)
        print("encryptCount:", encryptCount)
        print("fairwitnessCount: ", fairwitnessCount)
    else:
        print(contents, "is not a valid file")
        sys.exit("Script Aborted")


print("\nFile Processed ... Script End")
    
