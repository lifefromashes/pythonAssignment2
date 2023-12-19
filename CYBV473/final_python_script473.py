'''
Final Scripting Assignment
Kristin Skipper
December 2023
'''

# Python Standard Libaries
import requests  # Python Standard Library for url requests
import os
import re

# Python 3rd Party Libraries
from bs4 import BeautifulSoup  # 3rd Party BeautifulSoup Library - pip install Beautifulsoup4

# Python 3rd Party Libraries
import nltk  # 3rd Party NLTK Library - pip install nltk

# Psuedo Constants
URL = 'https://casl.website/'  # Specify the URL

# Other pages below are what is found from the site


IMG_SAVE = "./IMAGES/"  # Directory to store images

if not os.path.isdir(IMG_SAVE):  # check if the path is existing directory
    os.mkdir(IMG_SAVE)  # creates directory if doesn't exist

print("Searching URL: ", URL, "Please Wait ...")

page = requests.get(URL)  # retrieve a page from website
soup = BeautifulSoup(page.text, 'html.parser')  # convert the page into soup

pageTitle = soup.title  # Get the Page Title  (Assignment Step One)
pageLinks = set()  # Create a set to hold the unique links
imgLinks = set()  # Create a set to hold the unique image links
phone_pattern = r'\(?\d{3}\)?-? *\d{3}-? *-?\d{4}'  # Use pattern regex to search for phone numbers
linkTags = soup.findAll('a')  # Find all the possible links
all_text_content = ''  # Initialize string variable for text storage

''' Process all the possible links on the page '''

if linkTags:
    for eachLink in linkTags:

        newLink = eachLink.get('href')  # retrieves the value of the 'href' attribute from an HTML anchor (<a>) element

        if not newLink:  # Check if newLink is empty
            continue

        if 'http' not in newLink:  # Add 'http' to newLink
            newLink = URL + newLink

        pageLinks.add(newLink)  # Add link to list

''' Process all the possible images on the page '''
imageTags = soup.findAll('img')  # Find all the possible links

if imageTags:
    for eachImage in imageTags:
        try:
            imgURL = eachImage['src']
            if imgURL[0:4] != 'http':  # If URL path is relative
                imgURL = URL + imgURL  # try prepending the base url
            imgLinks.add(imgURL)  # Add link to list
        except:
            continue

''' Process all the possible phone numbers on the page '''
# Use re module to search all occurences of phone numbers on the page
phone_numbers = re.findall(phone_pattern, page.text)

''' Process all the possible zip codes on the page '''
# User regext to find the zip codes in the page
zip_codes = re.findall(r'\b\d{5}(?:-\d{4})?\b', page.text)

''' Process all text on the pages '''
# Iterate through each page link
for eachLink in pageLinks:
    try:
        # Make a request to the page link
        page = requests.get(eachLink)
        soup = BeautifulSoup(page.text, 'html.parser')

        # Extract the text content of all paragraphs on the page
        page_text_content = ' '.join([p.get_text() for p in soup.find_all(
            'p')])  # is using a list comprehension to extract the text content of all paragraphs (<p>)

        # Append the text content to the overall string
        all_text_content += page_text_content + ' '
    except:
        continue

# A list of all unique vocabulary found on the website
tokens = nltk.word_tokenize(
    all_text_content)  # use the (NLTK) library to tokenize the text content stored in the variable all_text_content
unique_vocabulary = set(tokens)  # Add tokens to set

# A list of all possible verbs
pos_tags = nltk.pos_tag(
    tokens)  # using the Natural Language Toolkit (NLTK) library's pos_tag function to perform part-of-speech tagging on a list of tokens
verbs = [word for word, pos in pos_tags if pos.startswith('VB')]  # break down the text into a list of words or tokens

# A list of all possible nouns
nouns = [word for word, pos in pos_tags if pos.startswith('NN')]  # break down the text into a list of words or tokens

print("\nRESULTS\n")
print("Page Title: ", pageTitle)

print("\nPage Links:")
for eachLink in pageLinks:  # Iterate through list and print each item
    print(eachLink)  # Print each link

print("\nImage Links:")
# Get the image from the URL
for eachImgLink in imgLinks:
    print(eachImgLink)
    try:
        img = requests.get(eachImgLink)
        imageName = os.path.basename(eachImgLink)
        imagePath = os.path.join(IMG_SAVE, imageName)
        with open(imagePath, 'wb') as outFile:
            outFile.write(img.content)
    except:
        continue

print("\nPhone Numbers: ")  # Print phone numbers
print(phone_numbers)

print('\nZip Codes:')  # Print zip codes
print(zip_codes)

print('\nAll Text Content:')  # Print all the text from the pages
print(all_text_content)

# Additional Output for NLTK Processing Part
print('\nNLTK Processing:')
print('Unique Vocabulary:')
for word in unique_vocabulary:  # Iterate through list and print each item
    print(word)  # Print unique vocabulary

print('Possible Verbs:')  # Print possible verbs
for verb in verbs:  # Iterate through list and print each item
    print(verb)

print('Possible Nouns:')
for noun in nouns:  # Iterate through list and print each item
    print(noun)  # Print nouns

print('\n\nScript Complete')

