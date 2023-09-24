'''
Week 4 Assignment 6
Kristin Skipper
September 17, 2023
'''
import csv

'''
Using this script provide as a baseline.
Expand the script as follows:

1) Allow the user to enter a path to a directory containing jpeg files.
2) Using that path, process all the .jpg files contained in that folder  (use the testimages.zip set of images)
3) Extract the GPS Coordinates for each jpg (if they exist) and then map the coordinates

NOTE: There are several ways to do this, however, the easiest method would be to use the MapMaker App, at https://mapmakerapp.com/
      you can either manually enter the lat/lon values your script generates or you can place your results in a CSV file and upload
      the data to the map.

'''
# Usage Example:
# python Assignment 6
#
# Requirement: Python 3.x
#
# Requirement: 3rd Party Library that is utilized is: PILLOW
#                   pip install PILLOW  from the command line
#                   this is already installed in the Virtual Desktop


''' LIBRARY IMPORT SECTION '''

import os  # Python Standard Library : Operating System Methods
import sys  # Python Standard Library : System Methods
from datetime import datetime  # Python Standard Libary datetime method from Standard Library

# import the Python Image Library
# along with TAGS and GPS related TAGS
# Note you must install the PILLOW Module
# pip install PILLOW

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# import the prettytable library
from prettytable import PrettyTable


def ExtractGPSDictionary(fileName):
    ''' Function to Extract GPS Dictionary '''
    try:
        pilImage = Image.open(fileName)
        exifData = pilImage._getexif()

    except Exception:
        # If exception occurs from PIL processing
        # Report the
        return None, None

    # Interate through the exifData
    # Searching for GPS Tags

    imageTimeStamp = "NA"
    cameraModel = "NA"
    cameraMake = "NA"
    gpsData = False

    gpsDictionary = {}

    if exifData:

        for tag, theValue in exifData.items():

            # obtain the tag
            tagValue = TAGS.get(tag, tag)
            print('Tag Value: ', tagValue)
            # Collect basic image data if available

            if tagValue == 'DateTimeOriginal':
                imageTimeStamp = exifData.get(tag).strip()

            if tagValue == "Make":
                cameraMake = exifData.get(tag).strip()

            if tagValue == 'Model':
                cameraModel = exifData.get(tag).strip()

            # check the tag for GPS
            if tagValue == "GPSInfo":

                gpsData = True;

                # Found it !
                # Now create a Dictionary to hold the GPS Data

                # Loop through the GPS Information
                for curTag in theValue:
                    gpsTag = GPSTAGS.get(curTag, curTag)
                    gpsDictionary[gpsTag] = theValue[curTag]

        basicExifData = [imageTimeStamp, cameraMake, cameraModel]

        return gpsDictionary, basicExifData

    else:
        return None, None


# End ExtractGPSDictionary ============================


def ExtractLatLon(gps):
    ''' Function to Extract Lattitude and Longitude Values '''

    # to perform the calcuation we need at least
    # lat, lon, latRef and lonRef

    try:
        latitude = gps["GPSLatitude"]
        latitudeRef = gps["GPSLatitudeRef"]
        longitude = gps["GPSLongitude"]
        longitudeRef = gps["GPSLongitudeRef"]

        lat, lon = ConvertToDegreesV1(latitude, latitudeRef, longitude, longitudeRef)

        gpsCoor = {"Lat": lat, "LatRef": latitudeRef, "Lon": lon, "LonRef": longitudeRef}

        return gpsCoor

    except Exception as err:
        return None


# End Extract Lat Lon ==============================================


def ConvertToDegreesV1(lat, latRef, lon, lonRef):
    degrees = lat[0]
    minutes = lat[1]
    seconds = lat[2]
    try:
        seconds = float(seconds)
    except:
        seconds = 0.0

    latDecimal = float((degrees + (minutes / 60) + (seconds) / (60 * 60)))

    if latRef == 'S':
        latDecimal = latDecimal * -1.0

    degrees = lon[0]
    minutes = lon[1]
    seconds = lon[2]
    try:
        seconds = float(seconds)
    except:
        seconds = 0.0

    lonDecimal = float((degrees + (minutes / 60) + (seconds) / (60 * 60)))

    if lonRef == 'W':
        lonDecimal = lonDecimal * -1.0

    return (latDecimal, lonDecimal)


def ProcessDirectory(directory_path, csv_filename):
    # Function to process all .jpg files in a directory
    # Basically took what was in the main start and made it able to process mult files
    latLonList = []

    # Make sure directory exists
    if not os.path.isdir(directory_path):
        print("Error: The specified directory does not exist.")
        return
    # Loop through files in directory
    for filename in os.listdir(directory_path):
        # Change to lower and check if file is a .jpg
        if filename.lower().endswith(".jpg"):
            filepath = os.path.join(directory_path, filename)
            # Call method to extract the gps dictionary using file path provided
            gpsDictionary, exifList = ExtractGPSDictionary(filepath)

            if exifList:
                TS = exifList[0]
                MAKE = exifList[1]
                MODEL = exifList[2]
            else:
                TS = 'NA'
                MAKE = 'NA'
                MODEL = 'NA'

            # If gps dictionary exists then call extrac lat and lon method
            if gpsDictionary:
                dCoor = ExtractLatLon(gpsDictionary)

                if dCoor:
                    lat = dCoor.get("Lat")
                    latRef = dCoor.get("LatRef")
                    lon = dCoor.get("Lon")
                    lonRef = dCoor.get("LonRef")

                    # If contains all these then append those to latLonList
                    if lat and lon and latRef and lonRef:
                        # also use formatting to put lon and lat to within 4 decimals as well as add TS, MAKE, MODEL
                        latLonList.append((filename, '{:4.4f}'.format(lat), '{:4.4f}'.format(lon), TS, MAKE, MODEL))

    # Write the gps data to a CSV file
    # This is writing to the same folder as my script is in at this point
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['File-Name', 'Lat', 'Lon', 'TimeStamp', 'Make', 'Model'])  # Write header row
        csv_writer.writerows(latLonList)  # Write data rows

    return latLonList

    # return latLonList


''' MAIN PROGRAM ENTRY SECTION '''

if __name__ == "__main__":
    '''
    pyExif Main Entry Point
    '''
    print("\nExtract EXIF Data from JPEG Files")

    print("Script Started", str(datetime.now()))
    print()

    ''' PROCESS EACH JPEG FILE SECTION '''
   # TODO: NOTE: commented out since processing multiple files instead of just the barn.jpg, but did run that first to test
    # latLonList = []
    # targetFile = "barn.jpg"  # file must be located in the same folder
    #
    # if os.path.isfile(targetFile):
    #     gpsDictionary, exifList = ExtractGPSDictionary(targetFile)
    #
    #     if exifList:
    #         TS = exifList[0]
    #         MAKE = exifList[1]
    #         MODEL = exifList[2]
    #     else:
    #         TS = 'NA'
    #         MAKE = 'NA'
    #         MODEL = 'NA'
    #
    #     print("Photo Details")
    #     print("-------------")
    #     print("TimeStamp:    ", TS)
    #     print("Camera Make:  ", MAKE)
    #     print("Camera Model: ", MODEL)
    #
    #     if (gpsDictionary != None):
    #
    #         # Obtain the Lat Lon values from the gpsDictionary
    #         # Converted to degrees
    #         # The return value is a dictionary key value pairs
    #
    #         dCoor = ExtractLatLon(gpsDictionary)
    #
    #         print("\nGeo-Location Data")
    #         print("-----------------")
    #
    #         if dCoor:
    #             lat = dCoor.get("Lat")
    #             latRef = dCoor.get("LatRef")
    #             lon = dCoor.get("Lon")
    #             lonRef = dCoor.get("LonRef")
    #
    #             if (lat and lon and latRef and lonRef):
    #                 print("Lattitude: ", '{:4.4f}'.format(lat))
    #                 print("Longitude: ", '{:4.4f}'.format(lon))
    #             else:
    #                 print("WARNING No GPS EXIF Data")
    #         else:
    #             print("WARNING No GPS EXIF Data")
    #     else:
    #         print("WARNING", " not a valid file", targetFile)

    # Create Result Table Display using PrettyTable
    ''' GENERATE RESULTS TABLE SECTION'''

    ''' Result Table Heading'''
    resultTable = PrettyTable(['File-Name', 'Lat', 'Lon', 'TimeStamp', 'Make', 'Model'])

    ''' Your work starts here '''
    # Require user input for jpeg directory
    directory_path = input("Enter the path to the directory containing JPEG files: ")
    csv_filename = input("Enter the name of the CSV file to save the data (e.g., output.csv): ")

    # Store input as variable and process the input using method to take multiple files
    result = ProcessDirectory(directory_path, csv_filename)
    # Check if result contains jpg files with GPS data in directory
    if not result:
        print("No JPEG files with GPS data found in the specified directory.")
    else:
        # Create Result Table Display using PrettyTable
        # resultTable = PrettyTable(['File-Name', 'Lat', 'Lon', 'TimeStamp', 'Make', 'Model'])
        for row in result:
            resultTable.add_row(row)

        print(resultTable)

    # print()
