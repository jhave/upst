#! /usr/bin/env python

import re

# We start by telling the script what file to use:
textfile = open('mdg.txt', 'r')

# Create list of lower case words, \s+ --> match any whitespace(s)
word_list = re.split('\s+', textfile.read().lower())
print 'Words in text:', len(word_list)

# Create dictionary of word:frequency pairs
freq_dic = {}

# Remove punctuation marks:
punctuation = re.compile(r'[.?!,":;]') 

# Build the dictionary:
for word in word_list:
    # remove punctuation marks
    word = punctuation.sub("", word)
    # form dictionary
    try: 
        freq_dic[word] += 1
    except: 
        freq_dic[word] = 1
    
print 'Unique words:', len(freq_dic)
    
print '-'*30
print "Sorted by highest frequency first:"
# create list of (val, key) tuple pairs
freq_list2 = [(val, key) for key, val in freq_dic.items()]
# sort by value or frequency
freq_list2.sort(reverse=True)
# display result
for freq, word in freq_list2:
    print word + "," + str(freq)
    

# If you want to sort words by alphabetical order, use this:
# freq_list = freq_dic.items()
# freq_list.sort()
# for word, freq in freq_list:
#    print word, freq