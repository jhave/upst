#!/usr/bin/env python

import nltk
import sys

# First, some advanced scripting straight from the NLTK book:

class IndexedText(object):
	def __init__(self, stemmer, text):
		self._text = text
		self._stemmer = stemmer
		self._index = nltk.Index((self._stem(word), i) 
								for (i, word) in enumerate(text))
	def concordance(self, word, width=40):
		key = self.stem(word)
		wc = width/4			# words of context
		for i in self._index[key]:
			lcontext = ' '.join(self._text[i-wc:i])
			rcontext = ' '.join(self,_text[i:i+wc])
			ldisplay = '%*s' % (width, lcontext[-width:])
			rdisplay = '%*s' % (width, rcontext[:width])
			print ldisplay, rdisplay
	def _stem(self, word):
		return self._stemmer.stem(word).lower()

# Now back to the part where we do things

#  So we get the word from the user:

print "Enter the word you would like to see in context:",
word = raw_input()

# We also need to choose our stemmer:

porter = nltk.PorterStemmer()

# Then we need to transform the base text using a series of steps.
# Please note this could be one line:

thefile = open('mdg.txt')
rawtext = thefile.read()
# tokens = nltk.word_tokenize(rawtext)
processedtext = nltk.corpus.
text = IndexedText(porter,tokens)

# Now we can actually look at a word:

concordstem = text.concordance(word)

print(concordstem)

