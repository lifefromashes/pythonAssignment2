'''
Simple Search of a file
Professor Hosmer
August 2020
'''

import sys
import os

print("\nSimple File Search\n")

try:
    # Prompt user for a file and Chunk Size    
    largeFile = input("Enter the name of a large File: ")
    chunkSize = int(input("What size chunks?  "))
    keyword   = input("Keyword to Search: ") 
    
    keyword = bytes(keyword, 'ascii')   # convert the string to bytes
    keyword = keyword.lower()           # broaden the search 

    if os.path.isfile(largeFile):  # Verify file is real
        with open(largeFile, 'rb') as targetFile:
            while True:          
                fileChunk = targetFile.read(chunkSize)
                fileChunk = fileChunk.lower()  # broaden search
    
                if fileChunk:  # if we still have data
                    # Search this chunk for our keyword
                    if keyword in fileChunk:
                        print("Found Keyword: ", keyword)
                        break
                else:
                    # File has been processed
                    print("\nFile Processed:", keyword, "Not Found")
                    break
    else:
        print(largeFile, "is not a valid file")
        sys.exit("Script Aborted")
                
except Exception as err:
    sys.exit("\nException: "+str(err)+ "Script Aborted")
            
print("\nFile Processed ... Script End")

