'''
Reading Files in Chunks
Professor Hosmer
August 2020
'''

import sys
import os
from binascii import hexlify

print("\nProcessing File Chunks\n")

try:
    # Prompt user for a large file and Chunk Size    
    largeFile = input("Enter the name of a large File: ")
    chunkSize = int(input("What size chunks?  "))

    if os.path.isfile(largeFile):  # Verify file is real
        fileSize = os.path.getsize(largeFile)
        # Display details of file 
        print("\nProcessing file: ", largeFile)
        print("Total FileSize:    ", "{:,}".format(fileSize))
        print("in chunks of:      ", "{:,}".format(chunkSize), "Bytes\n")
    
        bytesProcessed = 0
        # Open and Loop through the file by chunk
        chunkCnt = 0
        print('{:<6s}'.format('CHUNK'), 'HEX')
        with open(largeFile, 'rb') as targetFile:
            while True:
                fileChunk = targetFile.read(chunkSize)
                bytesProcessed += len(fileChunk)
                if fileChunk:  # if we still have data
                    # Dump the first few bytes of the chunk
                    hexDump = hexlify(fileChunk[0:32])
                    print('{: <6d}'.format(chunkCnt), hexDump)
                    chunkCnt += 1
                else:
                    # File has been processed
                    print("\nProcessed:", "{:,}".format(bytesProcessed))
                    break
    else:
        print(largeFile, "is not a valid file")
        sys.exit("Script Aborted")
        
except Exception as err:
    sys.exit("\nException: "+str(err)+ "Script Aborted")
    
print("\nFile Processed ... Script End")
        
            