"""
Just utilities to determine if a file contains any binary data within the overall text.

Execute like:
python -u $dir_nrg_python/nmrrestrntsgrid/util/binaryDataInText.py inputFile
"""
import sys
__author__    = "jurgenfd"
___date__     = "Tue Mar 24 09:40:26 CET 2009"


def containsSomeBinaryDataInText( text ):
    for i, c in enumerate(text[0:2000]):
        o = ord(c)
#        print "data at [%3d] [%s] id [%d]" % ( i, c, o) 
        if o > 127 or o == 0:
            m = max(0, i-40)
            lengthPostString = i - m
            print "Bin data at %d preceded by [%s] length [%d]" % ( i, text[m:i], lengthPostString) 
            return True

if __name__ == '__main__':
#    inputFile = sys.stdin
    inputFile = sys.argv[1]
#    fullText = inputFile.read()
    fullText = open(inputFile, 'r').read()
    if not fullText:
        print "ERROR: containsSomeBinaryDataInText: Failed to parse file %s" % inputFile
        sys.exit(1)
    if containsSomeBinaryDataInText( fullText ):
        print "Bin data in %s" % inputFile
        
    
