'''
Skipper, Kristin
Week 4 Scripting Assignment
Date:
'''

import sys
import os
import re  # Python regular expression Library

from prettytable import PrettyTable  # 3rd Party Table Library


urlPattern = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w\.?=%&=\-@/$,]*')

try:
    # Prompt user for a file and Chunk Size    
    largeFile = input("Enter the name of a large File: ")
    chunkSize = int(input("What size chunks?  "))

    urlDict = {}  # Create an empty dictionary

    if os.path.isfile(largeFile):  # Verify file is real
        with open(largeFile, 'rb') as targetFile:
            while True:
                fileChunk = targetFile.read(chunkSize)

                if fileChunk:  # if we still have data
                    for eachURL in urlPattern.findall(fileChunk):
                        try:
                            cnt = urlDict[eachURL]  # obtain the value if key exists
                            cnt += 1  # Increment the count
                            urlDict[eachURL] = cnt  # Update the dictionary entry
                        except:
                            urlDict[eachURL] = 1  # otherwise, key doesn't exist, create it
                else:
                    # File has been processed
                    tbl = PrettyTable(["Occurrences", "URLs"])
                    for word, cnt in urlDict.items():
                        tbl.add_row([cnt, word])
                    tbl.align = 'l'
                    print(tbl.get_string(sortby="Occurrences", reversesort=True))
                    # print(tbl.get_html_string())
                    break
    else:
        print(largeFile, "is not a valid file")
        sys.exit("Script Aborted")


except Exception as err:
    sys.exit("\nException: " + str(err) + "Script Aborted")

with open('htmlPrettyTable.html', 'w') as outFile:
    tbl.get_string(sortby='Occurrences', reversesort=True)
    print(tbl.get_html_string(), file=outFile)

print("\nFile Processed ... Script End")
