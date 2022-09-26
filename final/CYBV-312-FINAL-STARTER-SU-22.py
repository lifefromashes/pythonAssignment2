'''
Add your name here
Final Script
June 2021
'''
import re

print("Final Script")
with open("mem.raw", 'rb') as target:  # assumes that mem.raw is in the same folder as script

    contents = target.read()  # read the entire contents of the file

    txt = re.sub(b"[^A-Za-z']", b' ', contents)  # strip all non alpha characters
    txt = txt.lower()  # convert all to lower case
    txt = txt.decode("utf-8")  # convert to simple ASCII

    wordList = txt.split()  # Create a list of possible words
    print(len(wordList))

    '''
    you will add your code here, that determines the number of occurrences
    of the following possible words found in the wordList
    
    kernel   encrypt  fairwitness  
    
    
    Note: You are NOT allowed to modify any other lines in the script, except
          to add your name in the comment block at the top
    Note: Your code will create the variables:  kernelCount, encryptCount, and fairwitnessCount
          so the print statements below will print out the correct number of occurrences
    '''
    kernelCount = 0
    encryptCount = 0
    fairwitnessCount = 0

    for eachWord in wordList:
        if eachWord == 'kernel':
            kernelCount += 1
        elif eachWord == 'encrypt':
            encryptCount += 1
        elif eachWord == 'fairwitness':
            fairwitnessCount += 1

    print("kernelCount: ", kernelCount)
    print("encryptCount:", encryptCount)
    print("fairwitnessCount: ", fairwitnessCount)

    with open('out.txt', 'w') as outFile:
        print('Kernel Count is : ', kernelCount, file=outFile)
        print('Encrypt Count is : ', encryptCount, file=outFile)
        print('Fair Witness Count is : ', fairwitnessCount, file=outFile)
