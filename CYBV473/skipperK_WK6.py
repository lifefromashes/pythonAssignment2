'''
Kristin Skipper
Week 6
September 30, 2023
'''
#For the web-page, you will extract the following information

#page-title
#Return to page title to the screen
#page-links URLs
#Return any URLs to the screen
#images found on the page
#Download to your system any images from the web-page

# Python Standard Libaries
import requests                         # Python Standard Library for url requests
import os
from bs4 import BeautifulSoup           # 3rd Party BeautifulSoup Library - pip install Beautifulsoup4

url = 'https://casl.website/login'
base = 'https://casl.website'
#IMG_SAVE = "./IMAGES/"
IMG_SAVE = 'C:/Users/Administrator/Desktop/week6/'  # Directory where I want to store images

# Create the directory if necessary
if not os.path.exists(IMG_SAVE):
    os.makedirs(IMG_SAVE)

page = requests.get(url)       # retrieve a page from your favorite website
soup = BeautifulSoup(page.text, 'html.parser')  # convert the page into soup

title_tag = soup.find('title') # Find title from title html attribute of the page
page_title = title_tag.string if title_tag else 'Title not found.' # Title to string or if not found then return not found
print('Page Title: ', page_title)

links = soup.find_all('a') #  Find all the anchor elements <a> in the HTML within the page and extract urls from href html attribute
for link in links:
    href = link.get('href')
    if href:
        print('Link: ', href)


print("Extracting Images from: ", url)
print("Please Wait")

images = soup.findAll('img')  # Find the image tags
for eachImage in images:      # Process and display each image
    try:
        imgURL = eachImage['src']
        print("Processing Image:", imgURL, end="")
        if imgURL[0:4] != 'http':       # If URL path is relative
            imgURL = base+imgURL         # try prepending the base url

        response = requests.get(imgURL)                 # Get the image from the URL
        imageName = os.path.basename(imgURL)

        imgOutputPath = IMG_SAVE+imageName

        with open(imgOutputPath, 'wb') as outFile:
            outFile.write(response.content)

        # Save the image
        print("  >> Saved Image:", imgOutputPath)
    except Exception as err:
        print(imgURL, err)
        continue



print('\n\nScript Complete')

