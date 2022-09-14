'''
Create a Possible Word List
Professor Hosmer
August 2020
'''

import sys
import os
import re       # Python regular expression Library

from prettytable import PrettyTable   # 3rd Party Table Library
                                      # pip install prettytable
print("\nPossible Word List\n")

try:
    # Prompt user for a file and Chunk Size    
    largeFile = input("Enter the name of a large File: ")
    chunkSize = int(input("What size chunks?  "))
    
    wordDict = {}  # Create an empty dictionary
    
    if os.path.isfile(largeFile):  # Verify file is real
        with open(largeFile, 'rb') as targetFile:
            while True:          
                fileChunk = targetFile.read(chunkSize)
    
                if fileChunk:  # if we still have data
                    txt = re.sub(b"[^A-Za-z\-']", b' ', fileChunk)
                    txt = txt.lower()  # broaden search                    
                    wordList = txt.split()
                    for eachWord in wordList:
                        if len(eachWord) >=4 and len(eachWord) < 15:
                            try:
                                cnt = wordDict[eachWord]  # obtain the value if key exists
                                cnt += 1                  # Increment the count
                                wordDict[eachWord] = cnt  # Update the dictionary entry
                            except:
                                wordDict[eachWord] = 1    # otherwise, key doesn't exist, create it
                else:
                    # File has been processed
                    tbl = PrettyTable(["Words", "Occurrences"])
                    for word, cnt in wordDict.items():
                        tbl.add_row([word, cnt])
                    tbl.align = 'l'
                    print(tbl.get_string(sortby="Occurrences", reversesort=True))
                    print(tbl.get_json_string())
                    break
    else:
        print(largeFile, "is not a valid file")
        sys.exit("Script Aborted")
                
except Exception as err:
    sys.exit("\nException: "+str(err)+ "Script Aborted")
            
print("\nFile Processed ... Script End")

