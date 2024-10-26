'''
The Python Natural Language Toolkit
Quick Introduction
Word Tagging
'''
from nltk import word_tokenize, pos_tag, trigrams
from collections import Counter
from prettytable import PrettyTable
import nltk

tagMeaning = {
    'CC':  'conjunction, coordinating',
    'CD':  'numeral, cardinal',
    'DT':  'determiner',
    'EX':  'existential there',
    'IN':  'preposition or conjunction, subordinating',
    'JJ':  'adjective or numeral, ordinal',
    'JJR': 'adjective, comparative',
    'JJS': 'adjective, superlative',
    'LS':  'list item marker',
    'MD':  'modal auxiliary',
    'NN':  'noun, common, singular or mass',
    'NNP': 'noun, proper, singular',
    'NNS': 'noun, common, plural',
    'PDT': 'pre-determiner',
    'POS': 'genitive marker',
    'PRP': 'pronoun, personal',
    'PRP$': 'pronoun, possessive',
    'RB':  'adverb',
    'RBR': 'adverb, comparative',
    'RBS': 'adverb, superlative',
    'RP':  'particle',
    'UH':  'interjection',
    'VB':  'verb, base form',
    'VBD': 'verb, past tense',
    'VBG': 'verb, present participle, or gerund',
    'VBN': 'verb, past participle',
    'VBP': 'verb, present tense, not 3rd person singular',
    'VBZ': 'verb, present tense, 3rd person singular',
    'WDT': 'WH-determiner',
    'WP':  'WH-pronoun',
    'WRB': 'WH-adverb'

}
sampleText = 'That is one small step for a man one giant leap for mankind Neil Armstrong'

words = word_tokenize(sampleText) # Tokenize text
tags = pos_tag(words) # Part of Speech Tagging
trigramList = list(trigrams(words))

tbl = PrettyTable(['Word', 'Part-of-Speech', 'Meaning'])
tbl.title = "Part of Speech Mapping"
for eachTag in tags:
    tbl.add_row([eachTag[0], eachTag[1], tagMeaning[eachTag[1]] ])

tbl.align='l'
print("\n")
print(tbl.get_string())

counts = Counter( tag for word,  tag in tags)

''' tally each category'''
tblFreq = PrettyTable(['Part-of-Speech', 'Counts'])
tblFreq.title="Part of Speech Counts"
for pos, cnt in counts.items():
    tblFreq.add_row([pos, cnt])

tblFreq.align='l'
print("\n")
print(tblFreq.get_string(sortby='Counts', reversesort=True))

tbl = PrettyTable(['W1','W2', 'W3'])
tbl.title="Trigrams"
for eachTrigram in trigramList:
    tbl.add_row([eachTrigram[0], eachTrigram[1], eachTrigram[2]])

tbl.align = 'l'
print(tbl.get_string())