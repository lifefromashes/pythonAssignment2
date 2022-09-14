'''
Simple Search of a file
Professor Hosmer
August 2020
'''

import sys
import os

print("\nSimple File Search v2\n")

try:
    # Prompt user for a file and Chunk Size    
    largeFile = input("Enter the name of a large File: ")
    chunkSize = int(input("What size chunks?  "))
    
    keywordList = [b"casey", b"anthony", b"secret", b"jfif", b"jpeg",b"adobe",b"rgb",b"killer"] 
    
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
                        print(key,"\t", value)
                    break
    else:
        print(largeFile, "is not a valid file")
        sys.exit("Script Aborted")
                
except Exception as err:
    sys.exit("\nException: "+str(err)+ "Script Aborted")
            
print("\nFile Processed ... Script End")

