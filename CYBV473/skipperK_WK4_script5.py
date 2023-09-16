'''
Kristin Skipper
Week 4 Assignment 5
September 15, 2023

Develop a script that:

1) Prompts the user for a directory path to search

2) Verify that the path provided exists and is a directory

3) Iterate through each file in that directory and examine it using PIL.

4) Generate a prettytable report of your search results (sample shown here)
'''
import os

from PIL import Image
from prettytable import PrettyTable

while True:
    # Prompt user for directory to search
    imageFileDir = input('Directory to process: ')
    # Convert relative path to absolute path (used this to prevent auth errors when reading files on my local machine)
    imageFileDir = os.path.abspath(imageFileDir)
    # Verify path is directory
    if not os.path.isdir(imageFileDir):
        print("Invalid Directory - try again")
        continue
    else:
        break

# Create a PrettyTable for image information
tbl = PrettyTable(['Image?', 'File Path', 'File Size', 'Ext', 'Format', 'Width', 'Height', 'Type'])

# Use the os.walk method to walk the path from root to bottom
for root, dirs, files in os.walk(imageFileDir):
    # Iterate through each file in directory and examine using PIL
    for eachItem in files:
        try:
            # Get file path
            fileFullPath = os.path.join(root, eachItem)
            # Get file extension using split txt to split it by root and extension and returns tuple so can get 2nd item
            # index[1] from that which would be the file ext
            fileExt = os.path.splitext(eachItem)[1]
            with Image.open(os.path.join(root, eachItem)) as im:
                imStatus = 'YES'
                imFormat = im.format
                imType = im.mode
                imWidth = im.width
                imHeight = im.height
                fileSize = os.path.getsize(fileFullPath)  # Get file size in bytes

                # Add each to pretty table
                tbl.add_row([imStatus, fileFullPath, fileSize, fileExt, imFormat, imWidth, imHeight, imType])

        except Exception as err:
            print('Exception occurred: ', str(err))

# Print the PrettyTable after processing all images
print(tbl)

