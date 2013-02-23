#! /usr/env/python

# This script counts lines, sentences, and words of a text file. 
# In order for the output to make sense, it requires each paragraph to be
# one line with no blank lines between paragraphs.

# First, just to be sure, we set all the counters to zero:
lines, blanklines, sentences, words = 0, 0, 0, 0

# Now we need to get a file to work with:
textfile = open('mdg.txt', 'r')

# And now we are going to read one line at a time:
for line in textfile:
    lines += 1
    # Check for blank lines
    if line.startswith('\n'):
        blanklines += 1
    else:
        # assume that each sentence ends with . or ! or ?
        # so simply count these characters
        sentences += line.count('.') + line.count('!') + line.count('?')
        # create a list of words
        # use None to split at any whitespace regardless of length
        # so for instance double space counts as one space
        tempwords = line.split(None)
        #print tempwords  # test
        # word total count
        words += len(tempwords)

# We'll be tidy and close the file:
textfile.close()

sentavg = sentences / lines
wordavg = words / lines

# And now print the results:
print '-' * 50
print "COUNTS "
print "Paragraphs      : " + str(lines)
print "Section Breaks: " + str(blanklines)
print "Sentences  : " + str(sentences)
print "Words      : " + str(words)
print "\n"
print "AVERAGES"
print "Sentences per paragraph: " + str(sentavg)
print "Words per paragraph: " + str(wordavg)
# print same for section