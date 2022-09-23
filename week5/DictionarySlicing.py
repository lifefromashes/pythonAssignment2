'''
Slicing a Dictionary
Professor Hosmer
June 2021 
Demonstration
'''
import os

DIR = "c:/"     # Target Directory

d={}            # create an empty dictionary

dirList = os.listdir(DIR)  # Get list of entries in the directory

for eachEntry in dirList:                   # interate through each entry
    path = os.path.join(DIR, eachEntry)     # get the full path 
    d[path] = os.path.getsize(path)    # Add entry to dictionary key = path, value = size

entryList = list(d.items())   # Next convert the dictionary to a list
# Now slice the list

print("First-Five:",entryList[:5])
print("Last-Five: ",entryList[-5:])

print("\nEnd Sample script")

