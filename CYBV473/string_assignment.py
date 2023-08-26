'''
Week One Assignment - Simple String Searching
Kristin Skipper
August 26, 2023
'''
'''
Given excerpt from the hacker manifesto 
Complete the script below to do the following:
1) Add your name, date, assignment number to the top of this script
2) Convert the string to all lower case
3) Count the number characters in the string
4) Count the number of words in the string
5) Sort the words in alphabetical order
6) Search the excerpt variable given below
   For the following and report how many occurances of each are found
   scandal
   arrested
   er
   good
   tomorrow
7) Submit
   NamingConvention: lastNameFirstInitial_Assignment_.ext
   for example:  hosmerC_WK1_script.py
                 hosmerC_WK1_screenshot.jpg
   A) Screenshot of the results in WingIDE
   B) Your Script
'''

excerpt = " Another one got caught today, it's all over the papers. Teenager\
            Arrested in Computer Crime Scandal, Hacker Arrested after Bank Tampering\
            Damn kids.  They're all alike"

# Main Script Starts Here

if __name__ == '__main__':
    # 1 Convert String to all lower case
    # Use built in python lower method to transform string to lower case
    lowerCaseString = excerpt.lower()
    print('LowerCase String: ', lowerCaseString)

    # 2 count chars in string
    # Use python len method to count the chars in the string.
    stringCount = len(excerpt)
    print('Length of string: ', stringCount)

    # 3 Num of words in string
    # Transform string into a list and then use len method to get the length of the list
    wordList = excerpt.split()
    wordCount = len(wordList)
    print('Number of words in string: ', wordCount)

    # 4 Words in alphabetical order
    # Use python sort method to put words in abc order
    lowerString = excerpt.lower()
    stringList = lowerString.split()
    stringList.sort()
    print('Sorted word list: ', stringList)

    # 5  Search the excerpt variable given below
    searchWords = ['scandal', 'arrested', 'er', 'good', 'tomorrow']
    ''' create a dictionary with key value pairs to count and make words lower case to match case of list
      use .count(word) method count how many times the current word (from searchWords) appears in the lowercased excerpt '''
    wordCounts = {word: excerpt.lower().count(word) for word in searchWords}
    ''' Use for loop to iterate through items in word count dict and format prints out each word and its count from
     wordCounts into a print msg'''
    for word, count in wordCounts.items():
        print(f'{word} appears {count} times in the excerpt.')