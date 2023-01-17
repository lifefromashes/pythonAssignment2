'''
Searching for Images with PIL
Skipper, Kristin
Week 7 Scripting Assignment
October 5, 2022
'''

import os
from PIL import Image
from prettytable import PrettyTable

table = PrettyTable(['File', 'Ext', 'Format', 'Width', 'Height', 'Mode'])

DIR = input("Enter Directory Path: ")
fileList = os.listdir(DIR)
for file in fileList:
    path = os.path.join(DIR, file)
    if os.path.isfile(path):
        ext = os.path.splitext(path)[1]
        try:
            with Image.open(path) as image:
                table.add_row([path, ext, image.format, image.size[0], image.size[1], image.mode])
        except Exception as error:
            table.add_row([path, ext, '[NA]', '[NA]', '[NA]', '[NA]'])
            pass
    else:
        continue

table.align = 'l'
print(table.get_string(sortby='Format'))
