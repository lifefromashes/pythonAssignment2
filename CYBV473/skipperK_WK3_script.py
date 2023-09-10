'''
Week Three Assignment 4 - File Processing Object
Kristin Skipper
September 9, 2023


Complete the script below to do the following:
1) Add your name, date, assignment number to the top of this script
2) Create a class named FileProcessor
   a) The Init method shall:
      i) verify the file exists
      ii) Extract key file system metadata from the file (size, creation timestamp, modified timestamp, access timestamp, and owner (UID))
          and store them as instance attribute
   b) Create a GetFileHeader Method which will
      i) Extract the first 20 bytes of the header
         and store them in an instance attribute
   c) Create a PrintFileDetails Method which will
      i) Print the metadata
      ii) Print the hex representation of the header

3) Demonstrate the use of the new class
   a) prompt the user for a directory path
   b) using the os.listdir() method extract the filenames from the directory path
   c) Loop through each filename and instantiate and object using the FileProcessor Class
   d) Using the object
      i) invoke the GetFileHeader Method
      ii) invoke the PrintFileDetails Method

4) Submit
   NamingConvention: lastNameFirstInitial_Assignment_.ext
   for example:  hosmerC_WK3_script.py
                 hosmerC_WK3_screenshot.jpg
   A) Screenshot of the results in WingIDE
   B) Your Script
'''

''' Import Python Standard Libraries '''

import os  # File system library
import time  # Time Conversion Library
from binascii import hexlify  # hexlify module


class FileProcessor:
    ''' FileProcessor Class Defintion '''

    def __init__(self, filePath):
        ''' Class Constructor '''
        # Storing instance attributes
        self.filePath = filePath
        self.size = os.path.getsize(filePath)
        self.creationTimestamp = os.path.getctime(filePath)
        self.creationTimestamp = os.path.getctime(filePath)
        self.modifiedTimestamp = os.path.getmtime(filePath)
        self.accessTimestamp = os.path.getatime(filePath)
        self.owner = os.stat(filePath).st_uid

    def GetFileHeader(self):
        ''' Extract the first 20 bytes of the file header '''

        # attempt to process the file
        try:
            # attempt open
            with open(fullPath, 'rb') as file:
                # attempt to read the contents
                fileContents = file.read(20)
                return fileContents
        except Exception as err:
            print("Exception Occurred: ", err)

    def PrintFileDetails(self):
        ''' Print the metadata and print the hex representation of the header'''
        print('Owner: ', self.owner)
        print('Size: ', self.size)
        # Use ctime to make timestamp human readable
        accessFormattedTime = time.ctime(self.accessTimestamp)
        print('Access Timestamp: ', accessFormattedTime)
        creationFormattedTime = time.ctime(self.creationTimestamp)
        print('Created Timestamp: ', creationFormattedTime)
        modifiedFormattedTime = time.ctime(self.modifiedTimestamp)
        print('Modified Timestamp: ', modifiedFormattedTime)
        try:
            with open(fullPath, 'rb') as hexFileRep:
                fileContents = hexFileRep.read(20)
                # use for loop to iterate over each byte in fileContents
                # Use a string format that converts the bytes into two char hex representation
                # Use .join to join the bytes with a space in between
                hexRepresentation = ' '.join(f'{byte:02x}' for byte in fileContents)
        except Exception as err:
            print("Exception Occurred: ", err)
        print(f"Hexadecimal representation of the header: {hexRepresentation}")


while True:
    # prompt user for directory path
    dirPath = input("Enter a Directory to Scan or Q to Quit: ")
    # verify valid directory input
    if not os.path.isdir(dirPath):
        print("Invalid Directory - try again")
        continue
    else:
        break

# Use os.listdir to extract filenames from the directory path above
files = os.listdir(dirPath)
# print('Files in directory: ', files)
# Use the os.walk method to walk the path from
# root to bottom
for root, dirs, files in os.walk(dirPath):
    # Iterate through each file it finds in the directory
    for file in files:
        # Get the file path
        path = os.path.join(root, file)
        fullPath = os.path.abspath(path)
        print('File full path: ', fullPath)
        # Instantiate class
        file = FileProcessor(fullPath)
        # Invoke file header class method
        file.GetFileHeader()
        # Invoke print file details class method
        file.PrintFileDetails()
