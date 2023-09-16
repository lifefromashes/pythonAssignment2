import os

from PIL import Image
from prettytable import PrettyTable

while True:
    imageFileDir = input('Directory to process: ')
    # Convert relative path to absolute path (used this to prevent auth errors when reading files on my local machine)
    imageFileDir = os.path.abspath(imageFileDir)
    if not os.path.isdir(imageFileDir):
        print("Invalid Directory - try again")
        continue
    else:
        break

# Create a PrettyTable for image information
tbl = PrettyTable(['Image?', 'Format', 'Type', 'Width', 'Height'])


# Use os.listdir to extract filenames from the directory path above
# imageFiles = os.listdir(imageFileDir)

# Use the os.walk method to walk the path from root to bottom
for root, dirs, files in os.walk(imageFileDir):
    # Iterate through each file it finds in the directory
    for eachItem in files:
        try:
            with Image.open(os.path.join(root, eachItem)) as im:
                imStatus = 'YES'
                imFormat = im.format
                imType = im.mode
                imWidth = im.width
                imHeight = im.height

                # print('Status: ', imStatus)
                # print('Format: ', imFormat)
                # print('Type: ', imType)
                # print('Width: ', imWidth)
                # print('Height: ', imHeight)

                tbl.add_row([imStatus, imFormat, imType, imWidth, imHeight])

        except Exception as err:
            print('Exception occurred: ', str(err))

# Print the PrettyTable after processing all images
print(tbl)

