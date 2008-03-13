"""
Just a few utilities that can be of more general use.
"""
__author__    = "$Author$"
___date__     = "$Date$"

import csv, urllib

# No changes below this line.
##########################################################################

def read_entries( url, contains_header, dictionary ):

    resource = urllib.urlopen(url)
    reader = csv.reader(resource)

    try:
        if contains_header:
            header_read = reader.next()
            print "DEBUG: read header: ", header_read
        for row in reader:
            pdb_code = row[0]
            dictionary[ pdb_code ]  = ''
    # Never know when the connection is finally empty.
    except IOError:
        pass
    
    print "DEBUG: Found number of entries: ", len(dictionary.keys())
