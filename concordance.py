#! /usr/bin/env python

import nltk
import sys

# First, let's get the word from the user:

print "Enter the word you would like to see in context:",
word = raw_input()

# Then we need to transform the base text using a series of steps.
# Please note this could be one line:

thefile = open('mdg.txt')
rawtext = thefile.read()
tokens = nltk.word_tokenize(rawtext)
text = nltk.Text(tokens)

# Now we can actually look at a word:

concordword = text.concordance(word)

print(concordword)