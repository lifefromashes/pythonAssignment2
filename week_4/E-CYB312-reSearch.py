''' 
Regular Expression Search
Professor Hosmer
August 2020
'''

import re

print("\nRegular Expession Example")
emailPattern    = re.compile(b'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')  
urlPattern      = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w\.?=%&=\-@/$,]*')

try:
    with open("test.bin", 'rb') as targetFile:
        fileContents = targetFile.read()

        emailMatches = emailPattern.findall(fileContents)
        urlMatches   = urlPattern.findall(fileContents)

        print("\nE-MAIL")
        
        for eachEmail in emailMatches:
            print(eachEmail)
            
        print("\nURLs")
        for eachURL in urlMatches:
            print(eachURL)    
            
except Exception as err:
    print(err)
    
        
        