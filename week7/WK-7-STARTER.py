'''
Searching for Images with PIL
Professor Hosmer

February 2022
'''

import sys
import os
from PIL import Image

print("\nWeek 7 Starter Script\n")
while True:
    path = input("\nFileName to Examine Q to Quit: ")
    if path.lower() == 'q':
        break
    if os.path.isfile(path):
        ext = os.path.splitext(path)[1]
        try:
            with Image.open(path) as im:
                print("File Details")
                print("Extension:    ", ext)
                print("Image Format: ", im.format)
                print("Image Width:  ", im.width,  "Pixels")
                print("Image.Height: ", im.height, "Pixels")
                print("Image.Mode:   ", im.mode) 
        except Exception as err:
            print("File is not a known Image Type: ", path)
    else:
        print("Path Provide is Not a File")
    
print("Script Done")
        