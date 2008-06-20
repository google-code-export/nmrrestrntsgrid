"""
Just a few utilities that can be of more general use.
"""
__author__    = "$Author$"
___date__     = "$Date$"

import csv, urllib

# No changes below this line.
##########################################################################

class Lister:
    """Example from 'Learning Python from O'Reilly publisher'"""
    def __repr__(self):
        return ("<Instance of %s, address %s:\n%s>" %
           (self.__class__.__name__, id(self), self.attrnames()))

    def attrnames(self):
        result=''
        keys = self.__dict__.keys()
        keys.sort()
        for attr in keys:
            if attr[:2] == "__":
                result = result + "\tname %s=<built-in>\n" % attr
            else:
                result = result + "\tname %s=%s\n" % (attr, self.__dict__[attr])
        return result

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
