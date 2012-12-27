#! /usr/env/python

# This script counts lines, sentences, and words of a text file.

# First, just to be sure, we set all the counters to zero:
lines, blanklines, sentences, words = 0, 0, 0, 0

# Now we need to get a file to work with:
textfile = open('/Users/john/Desktop/mm.txt', 'r')

# And now we are going to read one line at a time:
for line in textfile:
    #print line,   # test
    lines += 1
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

# And now print the results:
print '-' * 50
print "Lines      : ", lines
print "Blank lines: ", blanklines
print "Sentences  : ", sentences
print "Words      : ", words