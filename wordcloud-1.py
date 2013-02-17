#! /usr/bin/env python


# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).
 
def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

# Given a list of words, return a dictionary of
# word-frequency pairs.
 
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))
    
# Sort a dictionary of word-frequency pairs in
# order of descending frequency.
 
def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

# Use stop words
# stopwords = read a file, make a list

# Given a list of stop words, remove any that are in that list:
 
def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

# Given a URL, return string of lowercase text from page.
 
def webPageToText(url):
    import urllib2
    response = urllib2.urlopen(url)
    html = response.read()
    text = stripTags(html).replace('&nbsp;', ' ')
    return text.lower()
    
# Given name of calling program, a url and a string to wrap,
# output string in HTML body with basic metadata
# and open in Firefox tab.
 
def wrapStringInHTML(program, url, body):
    import datetime
    from webbrowser import open_new_tab
    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
    filename = program + '.html'
    f = open(filename,'w')
    wrapper = """<html>
        <head>
        <title>%s output - %s</title>
        </head>
        <body><p>URL: <a href=\"%s\">%s</a></p><p>%s</p></body>
        </html>"""
    whole = wrapper % (program, now, url, url, body)
    f.write(whole)
    f.close()   
    open_new_tab(filename)

# Given a list of keywords and a link name, return an
# HTML link to a Google search for those terms.
 
def keywordListToGoogleSearchLink(keywords, linkname):
    gsearch = '<a style=\"text-decoration:none\" '
    gsearch += 'href=\"http://www.google.com/search?q='
    gsearch += '+'.join(keywords)
    gsearch += '\">'
    gsearch += linkname
    gsearch += '</a>'
    return gsearch

#   
#   KEYWORDS IN CONTEXT-----------------------------
#   ------------------------------------------------
#   

# Given a list of words and a number n, return a list
# of n-grams.
 
def getNGrams(wordlist, n):
    return [wordlist[i:i+n] for i in range(len(wordlist)-(n-1))]

# Given a list of n-grams, return a dictionary of KWICs,
# indexed by keyword.
 
def nGramsToKWICDict(ngrams):
    kwicdict = {}
    keyindex = len(ngrams[0]) // 2
    for k in ngrams:
      if k[keyindex] not in kwicdict:
        kwicdict[k[keyindex]] = [k]
      else:
        kwicdict[k[keyindex]].append(k)
    return kwicdict

# Given a KWIC, return a string that is formatted for
# pretty printing.
 
def prettyPrintKWIC(kwic):
    n = len(kwic)
    keyindex = n // 2
    width = 10
    outstring = ' '.join(kwic[:keyindex]).rjust(width*keyindex)
    outstring += str(kwic[keyindex]).center(len(kwic[keyindex])+6)
    outstring += ' '.join(kwic[(keyindex+1):])
    return outstring

# Given a list of keywords and a link name, return an
# HTML link to a Google search for those terms.
 
def keywordListToGoogleSearchLink(keywords, linkname):
    url = 'http://www.google.com/search?q='
    url += '+'.join(keywords)
    gsearch = undecoratedHyperlink(url, linkname)
    return gsearch

#
#   TAG CLOUD ---------------------------------------
#   -------------------------------------------------
#

# Given a url and link name, return a string containing
# HTML and inline CSS for an undecorated hyperlink.
 
def undecoratedHyperlink(url, linkname):
    astr = """<a
    style=\"text-decoration:none\" href=\"%s\">%s</a>
    """
    return astr % (url, linkname)

# Given the body of a div and an optional string of
# property-value pairs, return string containing HTML
# and inline CSS for default div.
 
def defaultCSSDiv(divbody, opt=''):
    divstr = """<div style=\"
    width: 560px;
    background-color: rgb(250,250,250);
    border: 1px grey solid;
    text-align: center;
    %s\">%s</div>
    """
    return divstr % (opt, divbody)
    
# Given the body of a span and a scaling factor, return
# string containing HTML span with scaled font size.
 
def scaledFontSizeSpan(body, scalingfactor):
    import math
    minfont = 24
    maxfont = 54
    fontrange = maxfont - minfont
    fontsize = int(minfont + math.floor(fontrange * scalingfactor))
    spanstr = '<span style=\"font-size:%spx;\">%s</span>'
    return spanstr % (str(fontsize), body)
    
# Given the body of a span and a scaling factor, return
# string containing HTML span with scaled font size and
# darkness of greyscale adjusted.
 
def scaledFontShadeSpan(body, scalingfactor):
    import math
    minfont = 24
    maxfont = 54
    fontrange = maxfont - minfont
    fontsize = int(minfont + math.floor(fontrange * scalingfactor))
    fontcolor = int(200 - math.ceil(200 * scalingfactor))
    spanstr = """<span style=\"font-size:%spx;
    color: rgb(%d,%d,%d);
    \">%s</span>
    """
    return spanstr % (str(fontsize), fontcolor, fontcolor, fontcolor, body)

# Given the body of a span and a scaling factor, return
# string containing HTML span with scaled font size and
# shading from cool blue to hot red.
 
def scaledFontHeatmapSpan(body, scalingfactor):
    import math
    minfont = 24
    maxfont = 54
    fontrange = maxfont - minfont
    fontsize = int(minfont + math.floor(fontrange * scalingfactor))
    fontcolor = int(250 - math.ceil(250 * scalingfactor))
    spanstr = """<span style=\"font-size:%spx;
    color: rgb(%d,0,%d);
    \">%s</span>
    """
    return spanstr % (str(fontsize), 250-fontcolor, fontcolor, body)

# Given a dictionary of frequency-word pairs sorted
# in order of descending frequency, re-sort so it is
# in alphabetical order by word.
 
def reSortFreqDictAlpha(sorteddict):
    import operator
    aux = [pair for pair in sorteddict]
    aux.sort(key=operator.itemgetter(1))
    return aux