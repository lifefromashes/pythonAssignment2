'''
Dictionary Example
Leveraging the Dictionary Data Type
'''
import re  #Python Regular Expression Library

wordDictionary = {}

with open("test.txt", 'rb') as srcFile:
    content = srcFile.read()

filterContent = re.sub(b"[^A-Za-z\-']", b' ', content)
wordList = filterContent.split()
for eachWord in wordList:
    try:
        cnt = wordDictionary[eachWord] 
        cnt += 1
        wordDictionary[eachWord] = cnt
    except:
        wordDictionary[eachWord] = 1
    
for key, value in wordDictionary.items():
    key = str(key)
    print('{:15s}'.format(key), value)
    
    
