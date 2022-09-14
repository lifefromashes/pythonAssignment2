''' 
Skipper, Kristin
Week 4 Scripting Assignment
Date:
'''
import os
import re
import sys

from prettytable import PrettyTable

urlDict = {}  # Create an empty dictionary
urlPattern = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w\.?=%&=\-@/$,]*')

# def urlMatchesInTextFile(file):
#     urlPattern = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w\.?=%&=\-@/$,]*')
#
#     try:
#         with open("test.bin", 'rb') as targetFile:
#             fileContents = targetFile.read()
#
#             urlMatches = urlPattern.findall(fileContents)
#             for eachURL in urlMatches:
#                 try:
#                     cnt = hits[eachURL]
#                     cnt += 1
#                     hits[eachURL] = cnt
#                 except:
#                     hits[eachURL] = 1
#
#
#             print("\nURLs")
#         for eachURL in urlMatches:
#             print(eachURL)
#     except Exception as error:
#         print(error)


print("\nSimple File Search v2\n")

try:
    # Prompt user for a file and Chunk Size
    largeFile = input("Enter the name of a large File: ")
    chunkSize = int(input("What size chunks?  "))

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
                    tbl = PrettyTable(["URLs", "Occurrences"])
                    for word, cnt in urlDict.items():
                        tbl.add_row([word, cnt])
                    tbl.align = 'l'
                    print(tbl.get_string(sortby="Occurrences", reversesort=True))
                    print(tbl.get_json_string())
                    break
    else:
        print(largeFile, "is not a valid file")
        sys.exit("Script Aborted")

except Exception as err:
    sys.exit("\nException: " + str(err) + "Script Aborted")

tbl = PrettyTable(["Occurs", "URL"])

tbl.align = 'l'
print(tbl.get_string(sortby="Occurs", reversesort=True))
print(tbl.get_json_string())
print("\nFile Processed ... Script End")