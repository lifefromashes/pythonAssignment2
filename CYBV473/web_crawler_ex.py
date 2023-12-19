'''
Example
Recursive URL Scan
Staying within the target domain
Professor Hosmer
Feb 22
Note the script only obtains the unique URLs
not the additional information required
'''

# Python Standard Libaries
import requests  # Python Standard Library for url requests
import re  # Python regular expression library

# Python 3rd Party Libraries
from bs4 import BeautifulSoup  # 3rd Party BeautifulSoup Library - pip install Beautifulsoup4

pageLinks = set()


def RecurseURL(newURL, base, local):
    try:
        page = requests.get(newURL)  # retrieve a page from your favorite website
        soup = BeautifulSoup(page.text, 'html.parser')  # convert the page into soup

        links = soup.findAll('a')  # Find all the possible links
        if links:
            for eachLink in links:

                newLink = eachLink.get('href')

                if not newLink:
                    continue

                if 'http' not in newLink:
                    newLink = base + newLink

                if not local in newLink:
                    continue

                if newLink not in pageLinks:
                    # verify this is a true new link
                    pageLinks.add(newLink)  # add the link to our set of unique links
                    RecurseURL(newLink, base, local)  # Process this link
                else:
                    continue

    except Exception as err:
        # display any errors that we encounter
        print(err)


if __name__ == '__main__':

    ''' Main Program Entry Point '''

    baseURL = 'https://casl.website/'
    baseDomain = 'https://casl.website/'
    mustInclude = 'casl'

    pageLinks.add(baseURL)

    print("\nScanning: ", baseURL, '\n')
    RecurseURL(baseURL, baseDomain, mustInclude)

    print("\nScanning Complete\n")
    print("Unique URLs Discovered\n")

    for eachEntry in pageLinks:
        print(eachEntry)

print('\n\nScript Complete')

