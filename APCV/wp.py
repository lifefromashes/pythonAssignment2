def text_to_words(the_text):
    """ return a list of words with all punctuation and numbers removed,
      and all in lowercase based on the given text string.
  """
    my_substitutions = str.maketrans(
        # If you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        # Replace them by these
        "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


def load_string_from_file(filename):
    """ Read words from filename, return a string composed of the file content. """
    file = open(filename, "r")
    lines = file.read()
    return lines


def getWordcount(filetext):
    """ Return the number of words extracted from the filetext.
         Note that the duplicate words are also counted
    """
    words = text_to_words(filetext)
    return len(words)


def getDict(filetext):
    """ Return the dictionary extracted from the filetext.
        Note that each dictionary entry has
        a word as its key and the word's frequency number as its value
    """
    words = text_to_words(filetext)
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


def getVocabulary(filetext):
    """ Return the vocabulary list extracted from the filetext.
        Note that there is no duplicate word contained in the vocabulary
    """
    words = text_to_words(filetext)
    word_set = set(words)

    return word_set


file_content = load_string_from_file("brooks.txt")
print('File Contents:\n', file_content)

print('\n')

file_word_count = getWordcount(file_content)
print('Word Count: ', file_word_count)
print('\n')

print('Dictionary Values: ')
for key, value in getDict(file_content).items():
    print(key, value)
print('\n')

print('Vocab: \n', getVocabulary(file_content))
