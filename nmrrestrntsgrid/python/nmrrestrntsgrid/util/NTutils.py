from gzip import GzipFile
from nmrrestrntsgrid import NaNstring
from nmrrestrntsgrid import verbosityDebug
from nmrrestrntsgrid import verbosityDetail
from nmrrestrntsgrid import verbosityError
from nmrrestrntsgrid import verbosityNothing
from nmrrestrntsgrid import verbosityOutput
from nmrrestrntsgrid import verbosityWarning
from nmrrestrntsgrid.util.fpconst import isNaN
from string  import find
from traceback import format_exc
from xml.dom import minidom, Node
from xml.sax import saxutils
import array
import fnmatch
import inspect
import math
import nmrrestrntsgrid
import optparse
import os
import pydoc
import sys

CONSENSUS_STR = 'consensus'

class NTlist(list):
    """
    NTlist: list which is callable:
      __call__(index=-1) index<0: returns last item added or None for empty list
                         index>=0: returns item 'index'

    Methods:
      index( item ):    returns -1 when item is not present
      push( item ):     pushes item at position 0 (front) of list
      pop( index=0 ):   pops item at position index
      last():           returns last element of list or None on empty list
      replace(item, newItem ):
                        replaces item with newItem

    Methods for numeric lists (None elements ignored):
      average():        returns (av,sd,n) triple of a numeric list
                        stores av,sd,n as attributes of the list
      cAverage(min=0,max=360,radians=0):
                        returns (cav, cv, cn) triple of a numeric list
                        stores cav,cv,cn as attributes of the list
      min()             Returns minimum value or None on emptylist.
      max()             Returns maximum value or None on empty list.
      minItem()         Returns (index,minimumValue) tuple or (None,None) on emptylist.
      maxItem()         Returns (index,maximumValue) tuple or (None,None) on emptylist.
      sum( start=0 )    Return sum of list.
      sumsq( start=0 )  Return squared sum of list.
      limit( min, max): limit between min and max by adding/subtracting
                        (max-min)

    Other methods as in list

    """
    #--------------------------------------------------------------
    # Basic methods
    #--------------------------------------------------------------
    def __init__(self, *args):
        list.__init__(self)
        self.current = None
        for a in args:
            self.append(a)
        #end for
        self.av = None
        self.sd = None
        self.n = 0

    #end def

    def __call__(self, index=-1):
        if index < 0:
            return self.current
        else:
            return self[ index ]
        #end if
    #end def

    def __getslice__(self, i, j):
        """To implement slicing"""
        return NTlist(*list.__getslice__(self, i, j))
    #end def

    def __getitem__(self, item):
        """To implement extended slicing"""
        if type(item) == slice:
            return NTlist(*list.__getitem__(self, item))
        else:
            return list.__getitem__(self, item)
    #end def

    def __add__(self, other):
        return NTlist(*list.__add__(self, other))
    #end def

    def doc(self):
        """
        Generate pydoc output of self
        """
        pydoc.doc(self, title='%s')
    #end def

    def getConsensus(self, minFraction=1.):
        if not hasattr(self, CONSENSUS_STR):
            self.setConsensus(minFraction=minFraction)
        return getattr(self, CONSENSUS_STR)

    def setConsensus(self, minFraction=1.):
        """Where there are only the same values set the consensus to it
        otherwise set it to None.
        They don't all need to be the same, at least the given fraction
        should be the same. If the fraction is set to .5 or lower the result
        is undefined.

        Return consensus or False if set to None. Consensus can be None.
        """
        setattr(self, CONSENSUS_STR, None)
        count = {}
        n = len(self)
        for v in self:
            count.setdefault(v, 0)
            count[v] +=1
        for v in count:
            if count[v] >= minFraction*n:
                setattr(self, CONSENSUS_STR, v)
                return v
        return False
    #end def

    def append(self, *items):
        for item in items:
            list.append(self, item)
            self.current = item
        #end for
    #end def

    def add(self, *items):
        '''Add a new item to a list only if not there before, like 'add' method
           for set() - AWSS 24OCT07'''
        for item in items:
            if not self.count(item):
                list.append(self, item)
                self.current = item
            #end if
        #end for
    #end def

    def addList(self, list_new):
        for item in list_new:
            list.append(self, item)
            self.current = item
        #end for
    #end def

    def insert(self, i, item):
        list.insert(self, i, item)
        self.current = item
    #end def

    def remove(self, item):
        list.remove(self, item)
        if item == self.current:
            self.current = self.last()
        #end if
    #end def

    def removeIfPresent(self, item):
        if self.index(item)>=0:
            self.remove(item)
        #end if
    #end def

    def replaceIfPresent(self, item, itemNew):
        idx = self.index(item)
        if idx >= 0:
            self.remove(item)
            self.insert(idx,itemNew)
        #end if
    #end def

    def replace(self, item, newItem):
        index = self.index(item)
        if (index < 0):
            return
        self.remove(item)
        self.insert(index, newItem)
    #end def

    def index(self, item):
        # JFD notes that this method is now twice as fast.
        # This was a very rate limiting piece of code when a chain
        # had many residues (E.g. an X-ray structure with many waters).
        try:
            return list.index(self, item)
        except ValueError:
            pass
        return -1
#        if item in self:
#            return list.index( self, item )
#        return -1
    #end def

    def last(self):
        l = len(self)
        if (l == 0):
            return None
        #end if
        return self[l-1]  # equivalent to self[-1:][0] or simply self[-1]
    #end def

    def push(self, item):
        self.insert(0, item)
    #end def

    def pop(self, index=0):
        """Return index'ed item from list or None on empty list
        """
        if len(self) == 0:
            return None
        item = list.pop(self, index)
        if item == self.current:
            self.current = self.last()
        #end if
        return item
    #end def

    def zap(self, *byItems):
        """use NTzap to yield a new list from self, extracting byItem from each
           element of self.
        """
        return NTzap(self, *byItems)
    #end def

    def removeDuplicates(self):
        """Can be optimized when needed by doing a sorted lookup table"""
        if len(self) <= 1:
            return
        i = 1
        while i < len(self):
#            print '>i=',i,  'list=',self[0:i],  'item=',self[i], 'len=',len(self)
            if self[i] in self[0:i]:
                self.pop(i)
            else:
                i += 1
        #end while
    #end def

    def reorder(self, indices):
        """Return a new NTlist, ordered according to indices or None on error
        """
        if (len(indices) != len(self)): return None

        result = NTlist()
        for idx in indices:
            result.append(self[idx])
        #end for
        return result
    #end def

    def setCurrent(self, item):
        if item in self:
            self.current = item
        #end if
    #end def

    def getDeepByKeysOrDefault(self, default, *keyList):
        result = self.getDeepByKeys(*keyList)
        if result == None:
            return default
        return result

    def getDeepByKeys(self, *keyList):
        """Return arbitrary deep element or None if key is absent at some point.
        The essence here is silence."""
        lk = len(keyList)
#        NTdebug("Now in getDeepByKeys for keylist length: %d" % lk)
        if not lk:
            NTdebug("Asked for a get on a dictionary without a key")
            return None
        key = keyList[0]

        if not isinstance(key, int):
            NTdebug("no int key in NTlist.getDeepByKeys: " + `key`)
            return None

        if key >= len(self):
            NTdebug("int key in NTlist.getDeepByKeys too large for this NTlist: " + `key`)
            return None

        value = self[key]
        if lk == 1:
#            NTdebug("value : " + `value`)
            return value
        if hasattr(value, 'getDeepByKeys'):
#            NTdebug("Going one level deeper")
            reducedKeyList = keyList[1:]
            return value.getDeepByKeys(*reducedKeyList)
#            NTdebug("In NTdict.getDeepByKeys the value is not a NTdict or subclass instance but there still are keys to go for digging deeper")
#            NTdebug(" for value : [" + `value` +']')
#            NTdebug(" type value: [" + `type(value)` +']')
        return None

    #--------------------------------------------------------------
    # numeric lists, None elements ignored
    #--------------------------------------------------------------
    def average(self, byItem=None):
        """return (av,sd,n) tuple of self
           Store av,sd,n as attributes of self
           Assumes numeric list, None elements ignored
           See also NTaverage routine
        """
        self.av, self.sd, self.n = NTaverage(self, byItem)
        return (self.av, self.sd, self.n)
    #end def

    def cAverage(self, min=0.0, max=360.0, radians = 0, byItem=None):
        """ Circular average.
           return (cav,cv,cn) tuple of a list
           return cav on min-max interval (that has to be spaced
           360 or 2pi depending on radians )
           Store cav,cv,cn as attributes of self
           Assumes numeric list, None elements ignored.
           If only None elements are found the cav, cv, cn will be set tO:
               ( None, None, 0)
           See also NTcAverage routine
        """
        self.cav, self.cv, self.cn = NTcAverage(self, min, max, radians, byItem)
        return (self.cav, self.cv, self.cn)
    #end def

    def min(self):
        if len(self) == 0: return None
        else: return min(self)
    #end def

    def max(self):
        if len(self) == 0: return None
        else: return max(self)
    #end def

    def minItem(self):
        if len(self) == 0: return (None, None)
        c = zip(self, range(len(self)))
        c.sort()
        return (c[0][1], c[0][0])
    #end def

    def maxItem(self):
        if len(self) == 0: return (None, None)
        c = zip(self, range(len(self)))
        c.sort()
        return (c[-1][1], c[-1][0])
    #end def

    def sum(self, start=0):
        return sum(self, start)
    #end def

    def sumsq(self, start=0):
        return sum(map(NTsq, self), start)
    #end def

    def limit(self, min, max, byItem=None):
        """Use NTlimit on self, return self
        """
        NTlimit(self, min, max, byItem)
        return self
    #end def

    #--------------------------------------------------------------
    # Formatting, str, XML etc
    #--------------------------------------------------------------
    def __str__(self):
        if len(self) == 0:
            return '[]'
        #end if

        string = '['
        for item in self:
            string = string + str(item) +', '
        #end for
        string = string[:-2]+']'
        return string
    #end def

# gv 19 Jun 08: reintroduced functionality, but shorter
    def __repr__(self):
        string = list.__repr__(self)
        return 'NTlist(' + string[1:-1] + ')'

#        if len(self) == 0:
#            return 'NTlist()'
#        #end if
#        string = 'NTlist('
#        for item in self:
#            string = string + repr( item ) +', '
#        #end for
#        string = string[:-2]+')'
#        return string
    #end def

    def format(self, fmt = None):
        if len(self) == 0:
            return ''
        #end if

        if (fmt == None and hasattr(self, '__FORMAT__')):
            fmt = self.__FORMAT__
        #end if
        string = ''
        for item in self:
            if fmt:
                if isinstance(item, list):
                    for subitem in item:
                        string += fmt % subitem
                else:
                    string += fmt % item
            else:
                string += `item` +' '
            #end if
        #end for
        return string
    #end def

#    def formatHtml(self):
#        if not self.format():
#            return ''
#        #end if
#        htmlLine = ''
#        formatLine = self.format().split('\n')[:-1]
#        for item in formatLine:
#            htmlLine = htmlLine + '<a> %s</a><br/>' % item
#        #end for
#        return htmlLine
#    #end def

    def toXML(self, depth=0, stream=sys.stdout, indent='\t', lineEnd='\n'):
        """
        Write XML-representation of elements of self to stream
        """
        NTindent(depth, stream, indent)
        fprintf(stream, "<NTlist>")
        fprintf(stream, lineEnd)

        for a in self:
            NTtoXML(a, depth+1, stream, indent, lineEnd)
        #end for
        NTindent(depth, stream, indent)
        fprintf(stream, "</NTlist>")
        fprintf(stream, lineEnd)
    #end def

    def toSML(self, stream=sys.stdout):
        if hasattr(NTlist, 'SMLhandler'):
            NTlist.SMLhandler.toSML(self, stream)
        else:
            NTerror('NTlist.toSML: no SMLhandler defined')
        #end if
    #end def
#end class

def NTfill(value, n):
    """Return a NTlist instance with n elements of value

    """
    result = NTlist()
    i=0
    while i<n:
        result.append(value)
        i +=1
    #end while
    return result
#end def

def NThistogram(theList, low, high, bins):
    """Return a histogram of theList
    """
    if bins < 1:
        return None

    his = NTfill(0, bins) # Returns NTlist
    binSize = (high-low)/bins

    his.low = low
    his.high = high
    his.bins = bins
    his.binSize= binSize


    tmp = theList[:] # creates a copy.
    tmp.sort()

    # reworked logic a bit.
    bin = 0
    currentBinlow  = low+bin*binSize
    currentBinhigh = currentBinlow + binSize
    for item in tmp:
        if item < currentBinlow:
            continue
        if item >= currentBinlow and item < currentBinhigh:
            his[bin] += 1
            continue
        while bin < bins and item > currentBinhigh:
            bin += 1
            currentBinlow  = low+bin*binSize
            currentBinhigh = currentBinlow + binSize
        if bin < bins:
            his[bin] += 1
    return his
#end def


class NTvector(list):
    """Lightweight class to implement a few vector operations
       Numeric or Numpy has compiled code; this is a python
       only class based on list
       See also:
       http://www.python.org/doc/2.4/ref/numeric-types.html
    """

    def __init__(self, *values):
        list.__init__(self)
        for v in values:
            self.append(v)
        #end for
        self.fmt = '%.2f'
    #end def

    def length(self):
        result = 0
        for i in range(0, len(self)):
            result += self[i]*self[i]
        #end for
        return math.sqrt(result)
    #end def

    def norm(self):
        lgth = 1.0/self.length()
        result = NTvector()
        for i in range(0, len(self)):
            result.append(self[i]*lgth)
        #end for
        return result
    #end def

    def polar(self, radians = False):
        """
        return triple of polar coordinates (r,u,v)
        with:
          -pi<=u<=pi
          -pi/2<=v<=pi/2

          x = rcos(v)cos(u)
          y = rcos(v)sin(u)
          z = rsin(v)
        """
        if len(self) != 3: return None
        fac = 1.0
        if not radians: fac = 180.0/math.pi

        r = self.length()
        u = math.atan2(self[1], self[0])
#        if u<0: u+=math.pi*2.0
        v = math.asin(self[2]/r)
        return r, u*fac, v*fac
    #end def

    def setFromPolar(self, polarCoordinates, radians = False):
        """
        set vector using polarCoordinates (r,u,v)
        with:
          0<=u<=2pi
          -pi/2<=v<=pi/2

          x = rcos(v)cos(u)
          y = rcos(v)sin(u)
          z = rsin(v)
        """
        if len(self) != 3: return
        fac = 1.0
        if not radians: fac = math.pi/180.0

        r, u, v = polarCoordinates
        self[0] = r*math.cos(v*fac)*math.cos(u*fac)
        self[1] = r*math.cos(v*fac)*math.sin(u*fac)
        self[2] = r*math.sin(v*fac)
    #end def

    def rotX(self, angle, radians=False):
        if len(self) != 3: return None

        fac = 1.0
        if not radians: fac = math.pi/180.0
        result = NTvector()
        m = [ NTvector(1.0, 0.0, 0.0),
              NTvector(0.0, math.cos(angle*fac), -math.sin(angle*fac)),
              NTvector(0.0, math.sin(angle*fac), math.cos(angle*fac))
            ]
        for v in m:
            result.append(v.dot(self))
        #end for
        return result
    #end def

    def rotY(self, angle, radians=False):
        if len(self) != 3: return None

        fac = 1.0
        if not radians: fac = math.pi/180.0
        result = NTvector()
        m = [ NTvector(math.cos(angle*fac), 0.0, -math.sin(angle*fac)),
              NTvector(0.0, 1.0, 0.0),
              NTvector(math.sin(angle*fac), 0.0, math.cos(angle*fac))
            ]
        for v in m:
            result.append(v.dot(self))
        #end for
        return result
    #end def

    def rotZ(self, angle, radians=False):
        """rotate clockwise along z-axis
        """
        if len(self) != 3: return None

        fac = 1.0
        if not radians: fac = math.pi/180.0
        result = NTvector()
        m = [
              NTvector(math.cos(angle*fac), -math.sin(angle*fac), 0.0),
              NTvector(math.sin(angle*fac), math.cos(angle*fac), 0.0),
              NTvector(0.0, 0.0, 1.0),
            ]
        for v in m:
            result.append(v.dot(self))
        #end for
        return result
    #end def

    def dot(self, other):
        l = len(self)
        if l != len(other): return None
        result = 0
        for i in range(0, l):
            result += self[i]*other[i]
        #end for
        return result
    #end def

    def cross(self, other):
        """
        return cross vector spanned by self and other

          result = self x other

        or None on error

        Definitions from Kreyszig, Advanced Enginering Mathematics, 4th edition, Wiley and Sons, p273

        NB: Only 3D vectors
        """
        l = len(self)
        if l != 3:
            return None
        if l != len(other):
            return None

        result = NTvector()
        result.append(self[1]*other[2]-self[2]*other[1]) # x-coordinate
        result.append(self[2]*other[0]-self[0]*other[2]) # y-coordinate
        result.append(self[0]*other[1]-self[1]*other[0]) # z-coordinate
        return result
    #end def


#    def triple( self, b, c):
#        """
#        return triple product of self,b,c
#        or None on error
#        """
#        l = len(self)
#        if l != 3: return None
#        if l != len(b): return None
#        if l != len(c): return None
#        return    self[0] * (b[1]*c[2]-b[2]*c[1] )
#                - self[1] * (b[0]*c[2]-b[2]*c[0] )
#                + self[2] * (b[0]*c[1]-b[1]*c[0] )


    def angle(self, other, radians = False):
        """
        return angle spanned by self and other
        or None on error
        range = [0, pi]
        positive angle is counterclockwise (to be in-line with 'polar' methods
        and atan2 routines).
        """
        l = len(self)
        if l != len(other): return None

        fac = 1.0
        if not radians: fac = 180.0/math.pi


        c = self.dot(other) /(self.length()*other.length())
        c = min(c, 1.0)
        c = max(c, -1.0)
        angle = math.acos(c)
        return (angle * fac)
    #end def

    def distance(self, other):
        """
        return distance between self and other
        or None on error
        """
        l = len(self)
        if l != len(other): return None
        diff = self-other
        return diff.length()
    #end def

    def __add__(self, other):
        l = len(self)
        if l != len(other): return None
        result = NTvector()
        for i in range(0, l):
            result.append(self[i]+other[i])
        #end for
        return result
    #end def

    def __radd__(self, other):
        l = len(self)
        if l != len(other): return None
        result = NTvector()
        for i in range(0, l):
            result.append(self[i]+other[i])
        #end for
        return result
    #end def

    def __iadd__(self, other):
        l = len(self)
        if l != len(other): return None
        for i in range(0, l):
            self[i] += other[i]
        #end for
        return self
    #end def

    def __sub__(self, other):
        l = len(self)
        if l != len(other): return None
        result = NTvector()
        for i in range(0, l):
            result.append(self[i]-other[i])
        #end for
        return result
    #end def

    def __rsub__(self, other):
        l = len(self)
        if l != len(other): return None
        result = NTvector()
        for i in range(0, l):
            result.append(other[i]-self[i])
        #end for
        return result
    #end def

    def __isub__(self, other):
        l = len(self)
        if l != len(other): return None
        for i in range(0, l):
            self[i] -= other[i]
        #end for
        return self
    #end def

    def __neg__(self):
        l = len(self)
        result = NTvector()
        for i in range(0, l):
            result.append(-self[i])
        #end for
        return result
    #end def

    def __pos__(self):
        l = len(self)
        result = NTvector()
        for i in range(0, l):
            result.append(self[i])
        #end for
        return result
    #end def
    #--------------------------------------------------------------
    # Formatting, str, XML etc
    #--------------------------------------------------------------
    def __str__(self):
        if len(self) == 0:
            return '(V:)'
        #end if

        string = '(V: '
        for item in self:
            string = string + sprintf(self.fmt, item) +', '
        #end for
        string = string[:-2]+')'
        return string
    #end def
#end class


class NTset(NTlist):
    """
    Class to define sets; i.e. list of objects
    A set is equal to another set if they have at least one element in common
    """

    def __eq__(self, other):
        if other == None:
            return False
        else:
            for item in self:
                if item in other:     # maybe to be replaced by (faster?):  if other.has_key( item ):
                    return True
            #end for
            return False
        #end if
    #end def

    def __ne__(self, other):
        return not (self == other)
    #end def

    def __str__(self):

        if len(self) == 0:
            return '//'

        string = '/'
        for item in self:
            string = string + str(item) +', '
        string = string[:-2]+'/'
        return string
    #end def

    def toXML(self, depth=0, stream=sys.stdout, indent='\t', lineEnd='\n'):
        """
        Write XML-representation of elements of self to stream
        """
        NTindent(depth, stream, indent)
        fprintf(stream, "<NTset>")
        fprintf(stream, lineEnd)

        for a in self:
            NTtoXML(a, depth+1, stream, indent, lineEnd)
        #end for
        NTindent(depth, stream, indent)
        fprintf(stream, "</NTset>")
        fprintf(stream, lineEnd)
    #end def

#end class

#class odict(dict):
#    """ Ordered dictionary.
#        Adapted from http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/107747
#    """
#    def __init__(self, *args):
#        self._keys = []
#        dict.__init__(self)
#        self.append( *args )
#
#    def __delitem__(self, key):
#        dict.__delitem__(self, key)
#        self._keys.remove(key)
#
#    def __setitem__(self, key, item):
#        dict.__setitem__(self, key, item)
#        if key not in self._keys: self._keys.append(key)
#
#    def clear(self):
#        dict.clear(self)
#        self._keys = []
#
#    def copy(self):
#
#        newInstance = odict()
#        newInstance.update(self)
#        return newInstance
#
## methods iterkeys(), values(), itervalues(), items() and iteritems()
## now all decend from method keys().
#    def keys(self):
#        return self._keys
#
#    def iterkeys( self ):
#        for key in self.keys():
#            yield key
#
#    def values( self ):
#        return map( self.get, self.keys() )
#
#    def itervalues( self ):
#        for value in self.values():
#           yield value
#
#    def items( self ):
#        return zip( self.keys(), self.values() )
#
#    def iteritems( self ):
#        for item in self.items():
#            yield item
#
#    def popitem(self):
#        try:
#            key = self._keys[-1]
#        except IndexError:
#            raise KeyError('dictionary is empty')
#
#        val = self[key]
#        del self[key]
#
#        return (key, val)
#
#    def setdefault(self, key, failobj = None):
#        if key not in self._keys:
#            self._keys.append(key)
#        return dict.setdefault(self, key, failobj)
#
#    def update(self, dict):
#        dict.update(self, dict)
#        for key in dict.keys():
#            if key not in self._keys:
#                self._keys.append(key)
#
#    def append( self, *items):
#        for key, value in items:
#           self.__setitem__( key, value )


NTdictObjectId = 0
# Variables to limit recursion and prevent cycles in __repr__() call
NTdictDepth    = 0
NTdictMaxDepth = 1
NTdictCycles   = []

class NTdict(dict):
    """
        class NTdict: Base class for all mapping NT objects.

        Keys can be referenced as in dictionary methods, or as an attribute; e.g.

            aap = NTdict( noot=3, mies=4, kees='not awake' )
            print aap['noot']
            > 3
            print aap.noot
            > 3

        Hashing and compare implemented.

        Methods:
            __call__( **kwds )                            Calling will update kwds and return self.

            format( format=None )                         Format the object according to format or __FORMAT__ (when
                                                          format == None) attribute.
            keysformat()                                  Set __FORMAT__ to include all keys.
            printAttr( hidden=0 )                         Print all attributes to stream (mainly for debugging purposes).
                                                          Also print 'hidden' attributes when hidden!=0.

            getdefault( key, defaultKey )                 Return self[key] if key exists, self[defaultKey] otherwise.
            uniqueKey( key )                              Return an unique key derived from key.

            saveXML( *attrs ):                            Add attrs to the list to save in XML format.
            toXML( stream=sys.stdout )                    Write XML code of object to stream; recursively decend; i.e.
                                                          cycles will wreck this routine.

        Inherited methods:
            most methods defined as in dict()

            methods __iter__(),iterkeys(), values(), itervalues(), items() and iteritems()
            len(), popitem(), clear(), update() all decend from method keys().
            Hence when subclassing, overriding the keys() method effectively implements the other methods

            popitem() returns None upon empty dictionary

        Reserved attributes:
            attribute '__CLASS__'                         is reserved to store a class identifier; usefull for subtyping
            attribute '__OBJECTID__'                      is reserved to store an unique object id
            attribute '__FORMAT__'                        is reserved to store format for method format()
            attribute '__HIDDEN__'                        is reserved to store the hidden attributes
            attribute '__SAVEXML__'                       is reserved to store the name of attributes saved as XML
            attribute '__SAVEALLXML__'                    is reserved to indicate saving all attributes as XML

        GV 12 Sep 2007:
          removed implementation with global storage in NTstructObjects since it was never used and
          will result in objects persisting even if they could be deleted (i.e. a memory leak).

        GV 26 Nov 2008:
          Changed implementation compare: removed __cmp__ and implemented __lt__, __le__, __gt__, __ge__;
          adapted __eq__.
          Changed implementation in __hash__ due to recursion error.
    """
    def __init__(self, *args, **kwds):
        global NTdictObjectId

        #print '>>>', args, kwds
        dict.__init__(self, *args, **kwds)
        self.setdefault('__CLASS__', 'NTdict')
        self.setdefault('__FORMAT__', None)      # set to None, which means by default not shown in repr() and toXML() methods
        self.setdefault('__SAVEXML__', None)      # set to None, which means by default not shown in repr() and toXML() methods
        self.setdefault('__SAVEALLXML__', True)   # when True, save all attributes in toXML() methods
#        self.__getstate__ =  self  # Trick for fooling shelve.

        self['__OBJECTID__'] = NTdictObjectId
        NTdictObjectId      += 1
        self['__HIDDEN__']   = ['__HIDDEN__', '__OBJECTID__', '__CLASS__', '__FORMAT__', '__SAVEXML__', '__SAVEALLXML__']
    #end def

    #------------------------------------------------------------------
    # Basic functionality
    #------------------------------------------------------------------
    def __getattr__(self, attr):
        """Implement basic functionality:
           Keys can be referenced as in dictionary methods, or as an attribute.
        """
#        if attr == '__getstate__':
#        return
#        if hasattr(self, attr):
        if not self.has_key(attr):
            raise AttributeError
        return self[attr]
    #end def


    def __setattr__(self, attr, value):
        """Implement basic functionality:
           Keys can be referenced as in dictionary methods, or as an attribute.
        """
        self[attr] = value

    def __delattr__(self, attr):
        """Implement basic functionality:
           Keys can be referenced as in dictionary methods, or as an attribute.
        """
        del(self[attr])

    def __lt__(self, other):
        if other == None:
            return False
        if not isinstance(other, NTdict): # eg when comparing with tuple.
            return False
        return self['__OBJECTID__'] < other['__OBJECTID__']

    def __le__(self, other):
        if other == None:
            return False
        if not isinstance(other, NTdict): # eg when comparing with tuple.
            return False
        return self['__OBJECTID__'] <= other['__OBJECTID__']

    def __eq__(self, other):
        if other == None:
            return False
        if not isinstance(other, NTdict): # eg when comparing with tuple.
            return False
        return self['__OBJECTID__'] == other['__OBJECTID__']

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if other == None:
            return False
        if not isinstance(other, NTdict): # eg when comparing with tuple.
            return False
        return self['__OBJECTID__'] > other['__OBJECTID__']

    def __ge__(self, other):
        if other == None:
            return False
        if not isinstance(other, NTdict): # eg when comparing with tuple.
            return False
        return self['__OBJECTID__'] >= other['__OBJECTID__']

#
#    def __cmp__(self, other):
#        """Optimized for speed a bit"""
#        if not hasattr(other, '__OBJECTID__'): return -1
#        if self.__OBJECTID__ == other.__OBJECTID__:
#            return 0
#        if self.__OBJECTID__ < other.__OBJECTID__:
#            return -1
#        return 1

    def __hash__(self):
        #print 'hash>', self, self['__OBJECTID__']
        return int(self['__OBJECTID__'])
        #return hash(self['__OBJECTID__'])
    #end def

    def __str__(self):
#        return '<%s-object (%d)>' % (self.__CLASS__,self.__OBJECTID__ )
#        return self.format()
        return '<%s-object (%d)>' % (self._className(), self.__OBJECTID__)

    def _className(self):
        return str(self.__class__)[7:-2].split('.')[-1:][0]
    #end def

    def __repr__(self):
#        return dict.__repr__( self )
#        return '<%s-object (%d)>' % (self.__CLASS__,self.__OBJECTID__ )
        global NTdictDepth, NTdictMaxDepth, NTdictCycles

        #prevent cycles
        if (NTdictDepth == 0):
            NTdictCycles = []
        #end if

        if (self.__OBJECTID__ in NTdictCycles):
            return  '<%s-object (%d)>' % (self.__CLASS__, self.__OBJECTID__)
        #end if
        NTdictCycles.append(self.__OBJECTID__)

        NTdictDepth += 1
        if (NTdictDepth > NTdictMaxDepth):
            NTdictDepth -= 1
            return '<%s-object (%d)>' % (self.__CLASS__, self.__OBJECTID__)
        #end if

        string = self.__CLASS__ + '( '
        remove2chars = 0
        for k in self.keys():
            string = string + str(k) + ' = ' + repr(self[k]) + ', '
            remove2chars = 1
        #end for
        #check if we also need to store some internals
        for k in ['__FORMAT__', '__SAVEXML__']:
            if self[k] != None:
                string = string + k + ' = ' + repr(self[k]) + ', '
                remove2chars = 1
        #end for
        #check if we need to remove the final (not needed) 2 chars
        if remove2chars: string = string[0:len(string)-2]
        # append closing paren
        string = string + ' )'

        NTdictDepth -= 1
        return string
    #end def

    def format(self, format=None):
        """Return a formatted string of the items
           Uses format or stored attribute __FORMAT__ or default
        """
        if (format == None):
            # use the predefined format if no format given
            format = self.__FORMAT__

        if (format == None):
            # use the default format if None
            format ='<%(__CLASS__)s-object (%(__OBJECTID__)d)>'

        return format % self
    #end def

    def keysformat(self, dots='-'*20):
        """set __FORMAT__ to list all keys
        """
        fmt = self.header(dots) + '\n'
        for key in self.keys():
            s = '%-' + str(len(dots)) + 's '
            fmt = fmt +  s%(str(key)+':') + '%(' + str(key) + ')s\n'
        #end for
        fmt = fmt + self.footer(dots)
        self.__FORMAT__ = fmt
    #end def


    def printAttr(self, stream=sys.stdout, hidden=0):
        """print attributes of structure; mainly fo debugging.
        """
        msg = sprintf('=== <%s-object (%d)> ===\n', self.__CLASS__, self.__OBJECTID__)
        # append hidden keys if asked for
        keys = self.keys()
        if hidden:
            keys = keys + self.__HIDDEN__
#    print '>>',keys
        for key in keys:
            msg += sprintf('%-12s : %s\n', key, str(self[key]))
        return msg
    #end def

    def header(self, dots = '-'*20):
        """Generate a header using __CLASS__ and dots.
        """
        return sprintf('%s %s %s', dots, self.__CLASS__, dots)
    #end def

    def footer(self, dots = '-'*20):
        """Generate a footer using dots of the same length as header.
        """
        header = self.header(dots)
        lheader = len(header)
        s = dots
        while len(s) < lheader:
            s = s + dots
        #end while
        return s[0:lheader]
    #end def

    #------------------------------------------------------------------
    # Misc routines
    #------------------------------------------------------------------
    def doc(self):
        """
        Generate pydoc output of self
        """
        pydoc.doc(self, title='%s')
    #end def

    def copy(self):
        """Generate a copy with 'shallow' references"""
        newInstance = self.__class__(**dict(self.items()))
        for k in ['__SAVEXML__', '__FORMAT__']:
            newInstance[k] = self[k]
        #end for
        return newInstance

    def __call__(self, **kwds):
        self.update(kwds)
        return self
    #end def

    def setDeepByKeys(self, value, *keyList):
        """Set arbitrary deep element to value by keyList.
        The essence here is silence.
        keyList needs to have at least one key.
        Return None on success and True on error.
        """
        lk = len(keyList)
        if not lk:
            NTerror("Can't setDeepByKeys without any key")
            return True

        k = keyList[0]
        if lk == 1:
            self[k] = value
            return

        if self.has_key(k):
            deeper = self[k]
        else:
            deeper = NTdict()
            self[k] = deeper

        reducedKeyList = keyList[1:]
        return deeper.setDeepByKeys(value, *reducedKeyList)

    def appendDeepByKeys(self, value, *keyList):
        """Append value to arbitrary deep list.
        The essence here is silence.
        keyList needs to have at least one key.
        Return None on success and True on error.
        """
        lk = len(keyList)
        NTdebug("Now in appendDeepByKeys with keyList: %s", `keyList`)
        if not lk:
            NTerror("Can't appendDeepByKeys without any key")
            return True

        k = keyList[0]
        if lk == 1:
            if not self.has_key(k):
                self[k] = []
            self[k].append(value) # No extra checks done here for speed purposes.
            return

        if self.has_key(k):
            deeper = self[k]
        else:
            deeper = NTdict()
            self[k] = deeper

        reducedKeyList = keyList[1:]
        return deeper.appendDeepByKeys(value, *reducedKeyList)


    def getDeepByKeysOrDefault(self, default, *keyList):
        result = self.getDeepByKeys(*keyList)
        if result == None:
            return default
        return result

    def getDeepByKeys(self, *keyList):
        """Return arbitrary deep element or default=None if key is absent at some point.
        The essence here is silence."""
        lk = len(keyList)
#      NTdebug("Now in getDeepByKeys for keylist length: %d" % lk)
        if not lk:
            NTdebug("Asked for a get on a dictionary without a key")
            return None
        key = keyList[0]

        if not self.has_key(key):
#          NTdebug("no key: " + `key`)
            return None
        value = self[key]
        if lk == 1:
#          NTdebug("value : " + `value`)
            return value
        if hasattr(value, 'getDeepByKeys'):
#          NTdebug("Going one level deeper")
            reducedKeyList = keyList[1:]
            return value.getDeepByKeys(*reducedKeyList)
#      NTdebug("In NTdict.getDeepByKeys the value is not a NTdict or subclass instance but there still are keys to go for digging deeper")
#      NTdebug(" for value : [" + `value` +']')
#      NTdebug(" type value: [" + `type(value)` +']')
        return None





    def getdefault(self, key, defaultKey):
        'Return self[key] if key exists, self[defaultKey] otherwise'
        if self.has_key(key):
            return self[key]
        else:
            return self[defaultKey]
    #end def

    def uniqueKey(self, key):
        """return a unique key derived from key"""
        i = 1
        newkey = key
        while (newkey in self):
            newkey = sprintf('%s_%d', key, i)
            i += 1
        #end while
        return newkey
    #end def

    #------------------------------------------------------------------
    # methods __iter__(), iterkeys(),
    #         values(),   itervalues(),
    #         items(),    iteritems()
    #         len(),      popitem(),     clear(),   update()
    # now all decend from method keys().
    #------------------------------------------------------------------
    def keys(self):
        keys = dict.keys(self)
        # i.e. we only need to remove the 'local' stuff here
        # remove keys that should be hidden
        for key in self.__HIDDEN__:
            keys.remove(key)
        # sort keys as well
        keys.sort()
        return keys

    def __iter__(self):
        """__iter__ returns keys
        """
        for key in self.keys():
            yield key
    #end def

    def iterkeys(self):
        for key in self.keys():
            yield key

    def values(self):
        return map(self.get, self.keys())

    def itervalues(self):
        for value in self.values():
            yield value

    def items(self):
        return zip(self.keys(), self.values())

    def iteritems(self):
        for item in self.items():
            yield item

    def __len__(self):
        return len(self.keys())

    def popitem(self):
        keys = self.keys()
        try:
            key = keys[0]
        except IndexError:
            return None

        val = self[key]
        del self[key]
        return (key, val)

    def clear(self):
        p = self.popitem()
        while p:
            p = self.popitem()

    def update(self, fromDict):
        for key, value in fromDict.iteritems():
            self[key] = value

    #------------------------------------------------------------------
    # XML routines
    #------------------------------------------------------------------
    def toXML(self, depth=0, stream=sys.stdout, indent='  ', lineEnd='\n'):
        """
        Write XML-representation of keys/attributes of self (defined by the
        saveXML or saveAllXML methods) to stream
        """
        NTindent(depth, stream, indent)
        fprintf(stream, "<%s>", self.__CLASS__)
        fprintf(stream, lineEnd)
#       print node

        # check for what we need to write out
        if (self.__SAVEALLXML__):
            keys = self.keys()
        elif (self.__SAVEXML__ != None):
            keys = self.__SAVEXML__
        else:
            keys = []
        #end if

        for a in keys:
            NTindent(depth+1, stream, indent)
            fprintf(stream, "<Attr name=%s>", quote(a))
            fprintf(stream, lineEnd)

            NTtoXML(self[a], depth+2, stream, indent, lineEnd)

            NTindent(depth+1, stream, indent)
            fprintf(stream, "</Attr>")
            fprintf(stream, lineEnd)
        #end for
        NTindent(depth, stream, indent)
        fprintf(stream, "</%s>", self.__CLASS__)
        fprintf(stream, lineEnd)
    #end def

    def saveXML(self, *attrs):
        """add attrributes to save list
        """
        if (self.__SAVEXML__ == None):
            self.__SAVEXML__ =  []
        self.__SAVEALLXML__ = False

        for a in attrs:
            if a not in self.__SAVEXML__:
                self.__SAVEXML__.append(a)
        #end for
    #end def

    def removeXML(self, *attrs):
        """remove attrributes from __SAVEXML__ list
        """
        if self.__SAVEXML__:
            for a in attrs:
                if a in self.__SAVEXML__:
                    self.__SAVEXML__.remove(a)
                #end if
            #end for
        #end if
    #end def

    def saveAllXML(self):
        """Define __SAVEALLXML__
        """
        self.__SAVEALLXML__ = True
    #end def

    def toSML(self, stream=sys.stdout):
        if hasattr(NTdict, 'SMLhandler'):
            NTdict.SMLhandler.toSML(self, stream)
        else:
            NTerror('NTdict.toSML: no SMLhandler defined')
        #end if
    #end def

#end class

# Discouraged name for NTdict; please replace in your scripts asap.
NTstruct = NTdict

class NoneObjectClass(NTdict):
    """
    Class representing None; based on NTdict

    Allows attribute assignment, extraction, deletion
    Allows iteration
    Allows calling

    Returns self where ever appropriate

    NB: Only one instance should be used:

        from NTutils import NoneObject

    Experimental
    """
    def __init__(self):
        NTdict.__init__(self, __CLASS__ = 'NoneObjectClass')
    #end def
    def __getattr__(self, attr):
        return dict.__getattr__( self, attr )
    #end def

    def __setattr__(self, attr, value):
        pass

    def __delattr__(self, attr):
        pass
    #end def

    def __nonzero__(self):
        return False

    # To allow iteration
    def keys(self):
        return []
    #end def

    def __call__(self, *args, **kwds):
        return self
    #end def

    def __str__(self):
        return 'NoneObject'

    def __repr__(self):
        return 'NoneObject'

    def format(self, *args, **kwds):
        return '<NoneObject>'
#end def
NoneObject = NoneObjectClass()
#NoneObject = None
noneobject = NoneObject


class NTtree(NTdict):
    """NTTree class
       Linked tree-like structure class
    """

    def __init__(self, name, **kwds):
        kwds.setdefault('__CLASS__', 'NTtree')
        NTdict.__init__(self, **kwds)
        self._parent   = None
        self._children = NTlist()

        # set names
        self.name = name        # keeping name is essential for later referencing

        # saving name and children will allow to save the tree as XML and reconstruct
        self.saveXML('name', '_children')
    #end def

    def _Cname(self, depth=0):
        """Return name constructor with 'depth' levels"""
        result = self.name
        parent = self._parent
        while depth != 0 and parent != None:
            result = parent.name + '.' + result
            depth -= 1
            parent = parent._parent
        return result

    def _Cname2(self, depth=0):
        """Return name constructor using ['name']
           with 'depth' levels
        """
        result = sprintf('[%s]', quote(self.name))
        parent = self._parent
        while (depth != 0 and parent != None):
            result = sprintf('[%s]', quote(parent.name)) + result
            depth -= 1
            parent = parent._parent
        return result

    def __str__(self):
        return '<%s %s>' % (self._className(), self.name)

    def __repr__( self ):
        return '<%s-Object (%d): %s>' % (self.__CLASS__, self.__OBJECTID__, self._Cname( -1 ))
    #end def

    def addChild(self, name, **kwds):
        child = NTtree(name=name, **kwds)
        self._addChild(child)
        return child
    #end def

    def _addChild(self, child):
        """Internal routine, set references
        """
        self._children.append(child)
        self[child.name] = child
        self[child]      = child
        child._parent    = self
        return child
    #end def

    def removeChild(self, child):
        if not child in self._children:
            return None
        if child.name in self:
            del(self[ child.name ])
        self._children.remove(child)
        child._parent = None
        return child

    def renameChild(self, child, newName):
        if not child in self._children:
            return None
        if child.name in self:
            del(self[ child.name ])
        child.name = newName
        self[child.name] = child
        return child

    def replaceChild(self, child, newChild):
        if (not child in self._children): return None
        if child.name in self: del(self[ child.name ])
        child._parent = None
        self._children.replace(child, newChild)
        self[newChild.name] = newChild
        newChild._parent = self
        return newChild
    #end def

    def _sibling(self, relativeIndex):
        """Internal routine: Return index relative to self
           or -1 if it does not exist.
           This routine is the slowest part in a typical read of a molecule
           at the point of trying to match atom specifications in a dihedral
           which can span the residue.
        """
        if not self._parent:
            return -1

        selfIndex = self._parent._children.index(self)
        if selfIndex < 0:
            NTerror('NTtree.sibling: child "%s" not in parent "%s". This should never happen!!\n',
                    str(self), str(self._parent)
                   )
            return -1

        targetIndex = selfIndex + relativeIndex
        if targetIndex < 0:
            return -1
        if targetIndex >= len(self._parent._children):
            return -1

        return targetIndex

    def sibling(self, relativeIndex):
        """Return NTtree instance (relative to self)
           or None if it does not exist
        """
        # Next check greatly speeds up trivial lookups.
        if relativeIndex == 0:
            return self

        targetIndex = self._sibling(relativeIndex)
        if targetIndex < 0:
            return None
        else:
            return self._parent._children[targetIndex]

    def youngerSiblings(self):
        """return NTlist of elements following self
           or None in case of error
        """
        if self._parent == None:
            return None
        sibling = self._sibling(1)
        if sibling < 0:
            return []
        return self._parent._children[sibling:]

    def olderSiblings(self):
        """return NTlist of elements preceding self
           or None if it does not exist
        """
        if self._parent == None:
            return None
        sibling = self.sibling(-1)
        if sibling == None:
            return []
        return self._parent._children[0:sibling+1]

    def __iter__(self):
        """iteration routine: loop of children"""
        self._iter = 0
        return self

    def next(self):
        if self._iter >= len(self._children):
            raise StopIteration
            return None
        s = self._children[self._iter]
        self._iter += 1
        return s

    def traverse(self, depthFirst=1, result = None, depth = -1):
        """Traverse the tree,
           infinite depth recursion for depth < 0
           finite depth recursion for depth > 0
        """
#        print '>>', self, depth
        if result == None:
            result = NTlist()

        result.append(self)
        for child in self._children:
            if depth != 0:
                child.traverse(depthFirst=depthFirst, result = result, depth = depth-1)
        return result

    def subNodes(self, result = None, depth = -1):
        """Traverse the tree, returning all subnodes at depth
        """
#        print '>>', self, depth

        if result == None:
            result = NTlist()
        #end if
        if depth == 0:
            result.append(self)
        elif depth > 0:
            for child in self._children:
                child.subNodes(result = result, depth = depth-1)
        return result

    def header(self, dots = '---------'):
        """Subclass header to generate using __CLASS__, name and dots.
        """
        return sprintf('%s %s: %s %s', dots, self.__CLASS__, self.name, dots)

#end class


class NTparameter(NTtree):
    """
    Class to generate a parameter tree

    Methods:

        set( value )                    Set value of parameter
        __call__()                      Calling returns value of parameter

        setDefault( recursion = True )  Set parameters to default value

        allLeaves()                     Return all leaves of parameter tree, i.e.
                                        the 'active' parameters
        allBranches()                   Return all the branches of parameter tree

    Methods inherited form NTtree and NTdict

    """

    def __init__(self, name, **kwds):
        NTtree.__init__(self,
                           __CLASS__ = 'NTparameter',
                           branch    =  False, # branch=True indicate a node
                                                   # without a value
                                                   # Leaves carry a value
                           mutable   =  True,
                           parType   = 'generic', # 'generic', 'string', 'integer'
                                                   # 'float', 'enumerate','boolean'
                           name      =  name,
                           value     =  None,
                           default   =  None,
                           options   =  None,
                           minValue  =  None,
                           maxValue  =  None,
                           prettyS   =  None,
                           help      =  None,
                         )
        self.update(kwds)
        self.value = self.default

    def update(self, fromDict):
        """Update preserves/establises the linked structure
        """
        for key, value in fromDict.iteritems():
#            print '>>', repr(self), type(self), repr(value), type(value)
            if (type(self) == type(value) and not self.has_key(key)):
                self._addChild(value)
            else:
                self[key] = value
            #end if
        #end for
    #end def

    def set(self, value):
        if (self.mutable):
            self.value = value
        #end if
    #end def

    def __call__(self):
        return self.value
    #end def

    def setDefault(self, recursion = True):
        if (recursion):
            for p in self.allLeaves():
                p.set(p.default)
            #end for
        else:
            self.set(self.default)
        #end if
    #end def

    def allLeaves(self):
        leaves = NTlist()
        for p in self.traverse():
            if not p.branch:
                leaves.append(p)
            #end if
        #end for
        return leaves
    #end def

    def allBranches(self):
        branches = NTlist()
        for p in self.traverse():
            if p.branch:
                branches.append(p)
            #end if
        #end for
        return branches
    #end def

    def writeFile(self, fileName)   :
        fp = open(fileName, 'w')
        for p in self.allLeaves():
            fprintf(fp, '%-40s = %s\n', p._Cname(-1) + '.value', repr(p))
        #end for
        fp.close()
    #end def

    def __str__(self):
        return self._Cname(-1)
    #end def

    def __repr__(self):
        return repr(self.value)
    #end def

    def format(self):
        if self.branch:
            return str(self)
        else:
            return sprintf('%s: %s', str(self), str(self.value))
    #end def
#end class


class NTvalue(NTdict):
    """
    Class to store a value and its error
    Callable: returns value
    Simple arithmic: +, -, *, /, ==, !=, >, >=, <, <=,
    fmt2 will be used when value exists but error does not.
    """
    def __init__(self, value, error=0.0, fmt='%s (+- %s)', fmt2='%s', **kwds):
        kwds.setdefault('__CLASS__', 'NTvalue')
        NTdict.__init__(self, value=value, error=error, fmt=fmt, fmt2=fmt2, **kwds)
        self.saveXML('value', 'error', 'fmt', 'fmt2')
    #end def

    def __call__(self):
        return self.value
    #end def

    def __str__(self):
        # Note that the below cases for None value/error loose fixed width formatting.
        if self.value == None or isNaN(self.value):
            return '%s (+- %s)' % (NaNstring, NaNstring)
        if self.error == None or isNaN(self.error):
#            return `self.value`+' (+- %s)' % (NaNstring)
            # The problem here is of course that the whole fmt is lost if only the error is unknonw.
            # Added new parameter to init of this class to cover it.
            r = self.fmt2 % self.value
            return r + ' (+- %s)' % (NaNstring)
        return  self.fmt % (self.value, self.error)
    #end def

    def __repr__(self):
        return sprintf('NTvalue( value = %s, error = %s, fmt = %s, fmt2 = %s )',
                       repr(self.value), repr(self.error), self.fmt, self.fmt2)
    #end def

    def __add__(self, other):
        if hasattr(other, 'value'):
            v = self.value+other.value
            e = math.sqrt(self.error**2+other.error**2)
        else:
            v = self.value+other
            e = self.error
        return NTvalue(v, e, self.fmt, self.fmt2)
    #end def

    def __radd__(self, other):
        v = other + self.value
        return NTvalue(v, self.error, self.fmt, self.fmt2)
    #end def

    def __iadd__(self, other):
        if hasattr(other, 'value'):
            self.value += other.value
            self.error = math.sqrt(self.error**2+other.error**2)
        else:
            self.value += other
        return self
    #end def

    def __sub__(self, other):
        if hasattr(other, 'value'):
            v = self.value-other.value
            e = math.sqrt(self.error**2+other.error**2)
        else:
            v = self.value-other
            e = self.error
        return NTvalue(v, e, self.fmt, self.fmt2)
    #end def

    def __rsub__(self, other):
        v = other - self.value
        return NTvalue(v, self.error, self.fmt, self.fmt2)
    #end def

    def __isub__(self, other):
        if hasattr(other, 'value'):
            self.value -= other.value
            self.error = math.sqrt(self.error**2+other.error**2)
        else:
            self.value -= other
        return self
    #end def

    def __mul__(self, other):
        if hasattr(other, 'value'):
            v = self.value*other.value
            e = v*math.sqrt((self.error/self.value)**2+(other.error/other.value)**2)
        else:
            v = self.value*other
            e = self.error*other
        return NTvalue(v, e, self.fmt, self.fmt2)
    #end def

    def __rmul__(self, other):
        v = other * self.value
        e = v*self.error/self.value
        return NTvalue(v, e, self.fmt, self.fmt2)
    #end def

    def __imul__(self, other):
        if hasattr(other, 'value'):
            v = self.value
            self.value *= other.value
            self.error = v*math.sqrt((self.error/self.value)**2+(other.error/other.value)**2)
        else:
            self.value *= other
            self.error *= other
        return self
    #end def

    def __div__(self, other):
        if hasattr(other, 'value'):
            v = self.value/other.value
            e = v*math.sqrt((self.error/self.value)**2+(other.error/other.value)**2)
        else:
            v = self.value/other
            e = self.error/other
        return NTvalue(v, e, self.fmt, self.fmt2)
    #end def

    def __rdiv__(self, other):
        v = other / self.value
        e = v*self.error/self.value
        return NTvalue(v, e, self.fmt, self.fmt2)
    #end def

    def __idiv__(self, other):
        if hasattr(other, 'value'):
            self.value /= other.value
            # JFD: Next line should be checked
            self.error = self.value*math.sqrt((self.error/self.value)**2+(other.error/other.value)**2)
        else:
            self.value /= other
            self.error /= other
        return self
    #end def

    def __neg__(self):
        v = -self.value
        e = self.error
        return NTvalue(v, e, self.fmt, self.fmt2)
    #end def

    def __pos__(self):
        v = self.value
        e = self.error
        return NTvalue(v, e, self.fmt, self.fmt2)
    #end def

    def __abs__(self):
        v = abs(self.value)
        e = self.error
        return NTvalue(v, e, self.fmt, self.fmt2)
    #end def

    def __cmp__(self, other):
        if isinstance(other, NTvalue):
            value = other.value
        else:
            value = other
        #endif
        if (self.value < value):
            return -1
        elif (self.value > value):
            return 1
        else:
            return 0
        #end if
    #end def

    def __eq__(self, other):
        if other == None:
            return False
        elif isinstance(other, NTvalue):
            return self.value == other.value
        else:
            return self.value == other
        #end if
    #end def

    def __ne__(self, other):
        if other == None:
            return True
        elif isinstance(other, NTvalue):
            return self.value != other.value
        else:
            return self.value != other
        #end if
    #end def

    def toTuple(self):
        """
        Return a (value,error) tuple
        """
        return (self.value, self.error)
    #end def

    def fromTuple(theTuple):
        """
        Static method to generate a NTvalue instance from two-element
        (value,error) tuple
        or None on error
        """
        if len(theTuple)!=2:
            return None
        return NTvalue(value=theTuple[0], error=theTuple[1])
    #end def
    fromTuple = staticmethod(fromTuple)
#end class


class NTplist(NTdict):
    """
    Class to parse plist files
    """
    def __init__(self):
        NTdict.__init__(self, __CLASS__ = 'plist')
    #end def
#end class


def NTlimit(theList, min, max, byItem=None):
    """
    Limit the the values of theList between min and max, assuming periodicity
    i.e, like for angles.
    Assumes numeric list, None elements are ignored
    Elements are modified in-place
    byItem allows for list of lists
    """
    l = len(theList)
    listRange = max-min
    for i in range(0, l):
        if (theList[i] != None):
            if byItem == None:
                while theList[i] < min:
                    theList[i] += listRange
                while theList[i] > max:
                    theList[i] -= listRange
            else:
                while theList[i][byItem] < min:
                    theList[i][byItem] += listRange
                while theList[i][byItem] > max:
                    theList[i][byItem] -= listRange
        #end if
    #end for
#end def

def NTlimitSingleValue(value, min, max):
    """
    Limit the the values of theList between min and max, assuming periodicity
    i.e, like for angles.
    Assumes numeric value, None element is ignored.

    Could easily be optimized. If the value is far away from the allowed range
    then round off errors also become important with this algorithm.
    """
    listRange = max-min
    if value == None:
        return value

    while value < min:
        value += listRange
    while value > max:
        value -= listRange
    return value


def NTaverage(theList, byIndex=None):
    """returns (av, sd, n) tuple of theList or
       (None, None, 0) in case of zero elements in theList
       Assumes numeric list, None elements are ignored
       byIndex allows for list of tuples r other elements
    """
    sum = 0.0
    sumsqd = 0.0
    n = 0.0
    for item in theList:
        if item != None:
            if byIndex == None:
                val = item
            else:
                val = item[byIndex]
            if not isNaN(val):
                sum   += val
                n += 1
            #end if
    #end fpr

    if n == 0:
        return (NaN, NaN, 0)
    if n == 1:
        return (sum, NaN, 1) # sd not defined for serie of length one.
#    fn = float(n)
#    print '>>', n, sum, sumsq, sumsq/(fn-1.0), (sum*sum)/(fn*(fn-1.0))
    av = sum/n
    # routine below makes it much slower but easier to read than one pass.
    for item in theList:
        if item != None:
            if byIndex == None:
                val = item
            else:
                val = item[byIndex]
            if not isNaN(val):
                sumsqd += (val-av)*(val-av) # sum of squared deviations.

    # some python implementations (Linux) crash in case of all same numbers,
    # => zero sd, but roundoffs likely generate a very small negative number
    # here
    sd = sumsqd/(n-1)
    if sd <= 0.0:
        sd = 0.0
    sd = math.sqrt(sd)
    return (av, sd, int(round(n)))
#end def

def NTcAverage(theList, min=0.0, max=360.0, radians = 0, byIndex=None):
    """return (circularAverage,circularVariance,n) tuple of thelist or
       (None, None, 0) in case of zero elements in theList
       return circularMean on min-max interval (that has to be spaced
       360 or 2pi depending on radians )
       Assumes numeric list, None elements ignored
       byIndex allows for list of tuples
    """
    n    = 0
    csum = 0.0
    ssum = 0.0
    if radians:
        fac = 1.0
        fac2 = math.pi
    else:
        fac = math.pi/180.0
        fac2 = 360.0
    #end if
    for item in theList:
        if item != None:
            if byIndex == None:
                v = item
            else:
                v = item[byIndex]
            #end if
            if (v != None):
                csum += math.cos(v*fac)
                ssum += math.sin(v*fac)
                n += 1
            #end if
        #end if
    #end for

    if not n:
        return(None, None, 0)
    #end if

    #calculate cmean, avoid zero divisions
    if (math.fabs(csum) < 1e-10):
        csum = 1e-10
    #end if
    cav = math.atan(ssum/csum)
    if (csum < 0):
        cav += math.pi
    #end if
    cav /= fac

    #now scale on min-max interval
    while (cav < min):
        cav += fac2
    #end while
    while (cav > max):
        cav -= fac2
    #end while

    #calculate cv
    cv = 1.0 - math.sqrt(csum*csum + ssum*ssum) / n

    return (cav, cv, n)
#end def

def NTzap(theList, *byItems):
    """yield a new list from theList, extracting byItems from each
       element of theList or None if not present
    """
    result = NTlist()
    for v in theList:
        if v:
            result.append(getDeepByKeysOrAttributes(v, *byItems))
        else:
            result.append(None)
        #end if
    #end for
    return result
#end def


#def NTzap( theList, byItem ):
#    """yield a new list from theList, extracting byItem from each
#       element of theList or None if not present
#    """
#    result = NTlist()
#    for v in theList:
#        if v:
#            try:
#                result.append(v[byItem])
#            except KeyError, AttributeError:
#                result.append( None )
#        else:
#            result.append( None )
#        #end if
#    #end for
#    return result
##end def

def NTsq(value):
    return value*value # fastest
    # only problem might be the returned type which is not garanteed
    # to be a double like below.
#    return math.pow(value, 2)
#end def
# -----------------------------------------------------------------------------
# XML code
# -----------------------------------------------------------------------------

def NTindent(depth, stream, indent):
    """Indent strem to depth; to prettty format XML
    """
    for dummy in range(depth):
        fprintf(stream, indent)
    #end for
#end def

XMLhandlers             = {}

class XMLhandler:
    """Generic handler class

       methods:
       __init__                 : will register the handler in XMLhandlers
       handle                   : to be implemented in specific handler
       handleSingleElement      : for float,int,string etc)
       handleMultipleElements   : for list, tuple
       handleDictElements       : for dict, NTdict and the like

    """
    def __init__(self, name):
        global XMLhandlers
        self.name = name
        XMLhandlers[name] = self

    def handle(self, node):
        pass
    #end def

    def handleSingleElement(self, node):
        """Returns single element below node from DOM tree"""
        self.printDebugNode(node)
        if node.nodeName != self.name:
            NTerror('XML%sHandler: invalid XML handler for node <%s>', self.name, node.nodeName)
            return None
        #end if
        if len(node.childNodes) != 1:
            NTerror("XML%sHandler: malformed DOM tree", self.name)
            return None
        #end if
        if node.childNodes[0].nodeType != Node.TEXT_NODE:
            NTerror("XML%sHandler: malformed DOM tree, expected TEXT_NODE containing value", self.name)
            return None
        #end if
        result = node.childNodes[0].nodeValue
#        NTdebug("==>%s %s",repr(node), result)
        return result
    #end def

    def handleMultipleElements(self, node):
        self.printDebugNode(node)
        if node.nodeName != self.name:
            NTerror('XML%Handler: invalid XML handler for node <%s>\n', self.name, node.nodeName)
            return None
        #end if
        result = []
        for subNode in node.childNodes:
            if subNode.nodeType == Node.ELEMENT_NODE:
                result.append(NThandle(subNode))
            #end if
        #end for
#        NTdebug("==>%s %s",repr(node), result)
        return  result
    #end def

    def handleDictElements(self, node):
        self.printDebugNode(node)
        if node.nodeName != self.name:
            NTerror('XML%sHandler: invalid XML handler for node <%s>\n', self.name, node.nodeName)
            return None
        #end if

        result = {}

# We have two dict formats
# original 'NT' format:
##
##<dict>
##    <key name="noot">
##        <int>2</int>
##    </key>
##    <key name="mies">
##        <int>3</int>
##    </key>
##    <key name="aap">
##        <int>1</int>
##    </key>
##</dict>
##
# Or Apple plist dict's
##<dict>
##      <key>Key</key>
##      <string>3F344E56-C8C2-4A1C-B6C7-CD84EAA1E70A</string>
##      <key>Title</key>
##      <string>New on palm</string>
##      <key>Type</key>
##      <string>com.apple.ical.sources.naivereadwrite</string>
##</dict>

        # first collect all element nodes, skipping the 'empty' text nodes
        subNodes = []
        for n in node.childNodes:
#            print '>>',n
            if n.nodeType == Node.ELEMENT_NODE: subNodes.append(n)
        #end for
        if len(subNodes) == 0: return result

        #append all keys, checking for 'format' as outlined above
        i = 0
        while (i < len(subNodes)):
            self.printDebugNode(subNodes[i])

            try:
                keyName = subNodes[i].attributes.get('name').nodeValue
                value = NThandle(subNodes[i].childNodes[1])
                i += 1
            except AttributeError:
                keyName = subNodes[i].childNodes[0].nodeValue
                value = NThandle(subNodes[i+1])
                i += 2

#            print ">>", keyName, value
            result[keyName] = value
        #end while
#        NTdebug("==>%s %s",repr(node), result)
        return result
    #end def

    def printDebugNode(self, node):
        pass
#        NTdebug("   %s, type %s, subnodes %d", str(node), node.nodeType, len(node.childNodes) )
    #end def
#end class

class XMLNoneHandler(XMLhandler):
    """None handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='None')
    #end def

    def handle(self, node):
        return None
    #end def
#end class

class XMLintHandler(XMLhandler):
    """int handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='int')
    #end def

    def handle(self, node):
        result = self.handleSingleElement(node)
        if result == None:  return None
        return int(result)
    #end def
#end class

class XMLboolHandler(XMLhandler):
    """bool handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='bool')
    #end def

    def handle(self, node):
        result = self.handleSingleElement(node)
        if result == None:  return None
        # NB: bool('False') returns True!
        return bool(result=='True')
    #end def
#end class

class XMLfloatHandler(XMLhandler):
    """float handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='float')
    #end def

    def handle(self, node):
        result = self.handleSingleElement(node)
        if result == None:  return None
        return float(result)
    #end def
#end class

class XMLstringHandler(XMLhandler):
    """string handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='string')
    #end def

    def handle(self, node):
        # strings can be empty
        if len(node.childNodes) == 0: return ''

        result = self.handleSingleElement(node)
        if result == None:  return None
        return str(saxutils.unescape(result))
    #end def
#end class

class XMLunicodeHandler(XMLhandler):
    """unicode handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='unicode')
    #end def

    def handle(self, node):
        # strings can be empty
        if len(node.childNodes) == 0: return unicode('')

        result = self.handleSingleElement(node)
        if result == None:  return None
        return unicode(saxutils.unescape(result))
    #end def
#end class

class XMLlistHandler(XMLhandler):
    """list handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='list')
    #end def

    def handle(self, node):
        result = self.handleMultipleElements(node)
        if result == None: return None
        return result
    #end def
#end class

class XMLNTlistHandler(XMLhandler):
    """NTlist handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='NTlist')
    #end def

    def handle(self, node):
        items = self.handleMultipleElements(node)
        if items == None: return None
        result = NTlist()
        for item in items:
            result.append(item)
        return result
    #end def
#end class

class XMLtupleHandler(XMLhandler):
    """tuple handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='tuple')
    #end def

    def handle(self, node):
        result = self.handleMultipleElements(node)
        if result == None: return None
        return tuple(result)
    #end def
#end class


class XMLdictHandler(XMLhandler):
    """dict handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='dict')
    #end def

    def handle(self, node):
        result = self.handleDictElements(node)
        if result == None: return None
        return result
    #end def
#end class

class XMLNTdictHandler(XMLhandler):
    """NTdict handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='NTdict')
    #end def

    def handle(self, node):
        attrs = self.handleDictElements(node)
        if attrs == None: return None
        result = NTdict()
        result.update(attrs)
        return result
    #end def
#end class

# dummy: leave for compatibility
class XMLNTstructHandler(XMLhandler):
    """NTstruct handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='NTstruct')
    #end def

    def handle(self, node):
        attrs = self.handleDictElements(node)
        if attrs == None: return None
        result = NTdict()
        result.update(attrs)
        return result
    #end def
#end class

class XMLNTtreeHandler(XMLhandler):
    """NTtree handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='NTtree')
    #end def

    def handle(self, node):
        attrs = self.handleDictElements(node)
        if attrs == None: return None
#       print ">>attrs", attrs
        result = NTtree(name = attrs['name'])

        # update the attrs values
        result.update(attrs)

        # restore the tree structure
        for child in result._children:
#           print '>child>', repr(child)
            result[child.name] = child
            child._parent = result
        return result
    #end def
#end class


class XMLNTvalueHandler(XMLhandler):
    """NTvalue handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='NTvalue')
    #end def

    def handle(self, node):
        attrs = self.handleDictElements(node)
        if attrs == None: return None
        result = NTvalue(value = attrs['value'], error = attrs['error'], fmt = attrs['fmt'], fmt2 = attrs['fmt2'])
        result.update(attrs)
        return result
    #end def
#end class

class XMLNTplistHandler(XMLhandler):
    """NTplist handler class"""
    def __init__(self):
        XMLhandler.__init__(self, name='plist')
    #end def

    def handle(self, node):
        result = NTplist()
        for subNode in node.childNodes:
            if (subNode.nodeType == Node.ELEMENT_NODE):
                attrs = NThandle(subNode)
                if attrs == None: return None
                result.update(attrs)
            #end if
        #end for
        return result
    #end def
#end class

#define one instance of the handlers
nonehandler     = XMLNoneHandler()
inthandler      = XMLintHandler()
boolhandler     = XMLboolHandler()
floathandler    = XMLfloatHandler()
stringhandler   = XMLstringHandler()
unicodehandler  = XMLunicodeHandler()
listhandler     = XMLlistHandler()
tuplehandler    = XMLtupleHandler()
dicthandler     = XMLdictHandler()
# link handler of own classes to class def
NTlist.XMLhandler  = XMLNTlistHandler()
NTdict.XMLhandler  = XMLNTdictHandler()
NTstructhandler    = XMLNTstructHandler() # Handler cannot be linked to NTstruct/NTdict!!
NTtree.XMLhandler  = XMLNTtreeHandler()
NTvalue.XMLhandler = XMLNTvalueHandler()
NTplist.XMLhandler = XMLNTplistHandler()


def NThandle(node):
    """Handle a given node, return object of None in case of Error
    """
    if node == None:
        NTerror("NThandle: None node")
        return None
    #end if
    if node.nodeName not in XMLhandlers:
        NTerror('NThandle: no handler for XML <%s>', node.nodeName)
        return None
    #end if
    return XMLhandlers[node.nodeName].handle(node)
#end def

def NTtoXML(obj, depth=0, stream=sys.stdout, indent='\t', lineEnd='\n'):
    """Generate XML:
       check for method toXML
       or
       standard types int, float, tuple, list, dict
    """
    if (obj == None):
        NTindent(depth, stream, indent)
        fprintf(stream, "<None/>")
        fprintf(stream, lineEnd)
    elif hasattr(obj, 'toXML'):
        obj.toXML(depth, stream, indent, lineEnd)
    elif (type(obj) == int):
        NTindent(depth, stream, indent)
        fprintf(stream, "<int>%s</int>", repr(obj))
        fprintf(stream, lineEnd)
    elif (type(obj) == bool):
        NTindent(depth, stream, indent)
        fprintf(stream, "<bool>%s</bool>", repr(obj))
        fprintf(stream, lineEnd)
    elif (type(obj) == float):
        NTindent(depth, stream, indent)
        fprintf(stream, "<float>%s</float>", repr(obj))
        fprintf(stream, lineEnd)
    elif (type(obj) == str):
        NTindent(depth, stream, indent)
#        fprintf( stream, "<string>%s</string>",  saxutils.escape( obj )  )
        fprintf(stream, "<string>%s</string>", unicode(saxutils.escape(obj)))
        fprintf(stream, lineEnd)
    elif (type(obj) == unicode):
        NTindent(depth, stream, indent)
        fprintf(stream, "<unicode>%s</unicode>", unicode(saxutils.escape(obj)))
        fprintf(stream, lineEnd)
    elif (type(obj) == list):
        NTindent(depth, stream, indent)
        fprintf(stream, "<list>")
        fprintf(stream, lineEnd)
        for a in obj:
            NTtoXML(a, depth+1, stream, indent, lineEnd)
        #end for
        NTindent(depth, stream, indent)
        fprintf(stream, "</list>")
        fprintf(stream, lineEnd)
    elif (type(obj) == tuple):
        NTindent(depth, stream, indent)
        fprintf(stream, "<tuple>")
        fprintf(stream, lineEnd)
        for a in list(obj):
            NTtoXML(a, depth+1, stream, indent, lineEnd)
        #end for
        NTindent(depth, stream, indent)
        fprintf(stream, "</tuple>")
        fprintf(stream, lineEnd)
    elif (type(obj) == dict):
        NTindent(depth, stream, indent)
        fprintf(stream, "<dict>")
        fprintf(stream, lineEnd)
        for key, value in obj.iteritems():
            NTindent(depth+1, stream, indent)
            fprintf(stream, "<key name=%s>", quote(key))
            fprintf(stream, lineEnd)
            NTtoXML(value, depth+2, stream, indent, lineEnd)
            NTindent(depth+1, stream, indent)
            fprintf(stream, "</key>")
            fprintf(stream, lineEnd)
        #end for
        NTindent(depth, stream, indent)
        fprintf(stream, "</dict>")
        fprintf(stream, lineEnd)
    else:
        NTerror('NTtoXML: undefined object "%s": cannot generate XML\n', obj)
    #end if
#end def

def obj2XML(obj, stream=None, path=None):
    """Convert an object to XML
       output to stream or path
       gwv 13 Jun08: return object or None on error
    """
    if obj == None:
        NTerror("obj2XML: no object")
        return None
    if stream == None and path == None:
        NTerror("obj2XML: no output defined")
        return None

    closeFile = 0
    if not stream:
        stream = open(path, 'w')
        closeFile = 1

    fprintf(stream, '<?xml version="1.0" encoding="ISO-8859-1"?>\n')
    NTtoXML(obj, depth=0, stream=stream, indent='    ')

    if closeFile:
        stream.close()

    return obj
#end def

def XML2obj(path=None, string=None):
    """Convert XML file to object
       returns object or None on error
    """
    if path == None and string==None:
        NTerror("XML2obj: no input defined")
        return None

    NTdebug("Starting to read XML from path: " + `path`+ " or string: " + `string`)
    if path:
        doc = minidom.parse(path)
    else:
        doc = minidom.parseString(string)
    NTdebug("Done reading XML")
    root = doc.documentElement

    result = NThandle(root)
    doc.unlink()
    return result

#end def

class Sorter:
    def _helper (self, data, aux, inplace):
#        print 'data', data
#        print 'aux>', aux
        aux.sort()

        result = [data[i] for dummy, i in aux]
        if inplace: data[:] = result
        return result
    #end def

    def byItem(self, data, itemindex=None, inplace=False):
        if itemindex is None:
            if inplace:
                data.sort()
                result = data
            else:
                result = data[:]
                result.sort()
            #end if
            return result
        else:
            aux = []
            for i in range(len(data)):
                try:
                    aux.append((data[i][itemindex], i))
                except KeyError:
                    aux.append((None, i))
                except IndexError:
                    aux.append((None, i))
#           aux = [(data[i][itemindex], i) for i in range(len(data))]
            return self._helper(data, aux, inplace)
        #end if

    # a couple of handy synonyms
    sort = byItem
    __call__ = byItem

    def byAttribute(self, data, attributename, inplace=False):
        aux = [(getattr(data[i], attributename), i) for i in range(len(data))]
        return self._helper(data, aux, inplace)
    #end def
#end class
NTsort = Sorter()


def quote(inputString):
    "return a single or double quoted string"
    single = (find(inputString, "'") >= 0)
    double = (find(inputString, '"') >= 0)
    if single and double:
        NTerror("in quote: both single and double quotes in [%s]" % inputString)
        return None
    if double:
        return "'" + inputString + "'"
    return '"' + inputString + '"'
#end def


def asci2list(string):
    """ Convert a string with "," and "-" to a list of integers
    eg. 1,2,5-8,11,20-40
    returns empty list on empty string
    """
    result = NTlist()
    if string == None:
        return result
    elif len(string) == 0:
        return result

    for elm in string.split(','):
        tmp = elm.split('-')
        if len(tmp) == 1:
            result.append(int(tmp[0]))
        elif len(tmp) == 2:
            for i in range(int(tmp[0]), int(tmp[1])+1):
                result.append(i)
        else:
            NTerror('asci2list: invalid construct "%s"\n', string)
        #end if
    #end for

    return result
#end def

def list2asci(theList):
    """ Converts the numeric integer list theList to a string with "," and "-"
    eg. 1,3,5-8,11,20-40
    nb. inverse of asci2list
    returns '' for empty list
    """
    if len(theList) == 0: return ''

    l = theList[:]
    l.sort()

    # reduce this sorted list l to pairs start, stop
    ls = l[0:1]
    #print '>>',ls
    for i in range(0, len(l)-1):
        if l[i] < l[i+1]-1:
            ls.append(l[i])
            ls.append(l[i+1])
        #end if
    #end for
    ls.append(l[-1])

    #print '>>',ls

    # generate the string from ls
    result = ''
    for i in range(0, len(ls), 2):
        #print '>', i, result
        if ls[i] == ls[i+1]:
            result = sprintf('%s%s,', result, str(ls[i]))
        else:
            result = sprintf('%s%s-%s,', result, str(ls[i]), str(ls[i+1]))
        #end if
    #end for
    return result[0:-1]
#end def

def list2string(mylist):
    "Return a string representation of mylist"
    if len(mylist) == 0: return ''
    result = ''
    for e in mylist:
        result = result + str(e) + ' '
    #end for
    return result[0:-1]
#end def


def NTsign(value):
    """return sign of value:
    """
    if (value < 0.0):
        return -1.0
    else:
        return 1.0
    #end if
#end def


def length(object):
    """return length object
    """
    try:
        l = len(object)
        return l
    except TypeError:
        return 1

def object2list(object):
    """return object as list
    """
    if object==None:
        return []
    if isinstance(object, list):
        return object
    else:
        return [object]

#def NTsetNone( var ):
#  """Set var to None
#  """
#  var = None

class CommandWrap:
    """Wrapper for command callbacks
       From Python Cookbook, section 9.1 (p. 302)
    """

    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        return self.callback(*self.args, **self.kwargs)


class EventWrap:
    """Wrapper for event callbacks
         Adapted from Python Cookbook, section 9.1 (p. 302)
    """

    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def __call__(self, event):
        return self.callback(event, *self.args, **self.kwargs)


class EventSkip:
    """Wrapper for callbacks, skipping the event argument
         Adapted from Python Cookbook, section 9.1 (p. 302)
    """

    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def __call__(self, event):
        return self.callback(*self.args, **self.kwargs)

def NTinspect(something):
    m = inspect.getmembers(something)
    for item in m:
        print str(item)

class NTprogressIndicator:
    """
    Iterator class to loop over myList and print dots
    """
    def __init__(self, theList, charactersPerLine = 80):
        self._iter = -1
        self._len   = len(theList)
        self._list  = theList
        self._charactersPerLine = charactersPerLine
    #end def

    def __iter__(self):
        """iteration routine: loop of children"""
        self._iter = 0
        self._printedDots = 0
        return self
    #end def

    def next(self):
        if self._iter >= self._len:
            NTmessage("")
            raise StopIteration
            return None

        if not self._printedDots % 10:
            digit = self._printedDots / 10
            NTmessageNoEOL(`digit`)
        else:
            NTmessageNoEOL('.')
        #end if
        self._printedDots += 1
        if not self._printedDots % self._charactersPerLine:
            NTmessage("")
            self._printedDots = 0

        s = self._list[self._iter]
        self._iter += 1
        return s
#end class

def fprintf(stream, format, *args):
    """C's fprintf routine"""
    if args:
        stream.write((format) % (args))
    else:
        stream.write(format)

def mprintf(fps, fmt, *args):
    """
    Print to list of filepointers (fps) using format and args.
    Use fp only if it evaluates to True.
    """
    for fp in fps:
        if fp:
            fprintf(fp, fmt, *args)

def sprintf(format, *args):
    """return a string according to C's sprintf routine"""
    return ((format) % (args))

def printf(format, *args):
    """print string according to C's printf routine"""
    fprintf(sys.stdout, format, *args)

class PrintWrap:
    def __init__(self, stream = None,
                       autoFlush = True,
                       verbose=verbosityOutput,
                       noEOL=False,
                       prefix = ''
                ):
        self.autoFlush = autoFlush
        self.verbose   = verbose
        self.noEOL     = noEOL
        if self.verbose > verbosityError:
            self.stream = sys.stdout
        else:
            self.stream = sys.stderr
        if stream: # Allow override.
            self.stream = stream
        self.prefix = prefix
#        if self.verbose == verbosityError:
#            self.prefix = prefixError
#        elif self.verbose == verbosityWarning:
#            self.prefix = prefixWarning
#        elif self.verbose == verbosityDetail:
#            self.prefix = prefixDetail
#        elif self.verbose == verbosityDebug:
#            self.prefix = prefixDebug

    def __call__(self, format, *args):
        if self.verbose > nmrrestrntsgrid.verbosity: # keep my mouth shut per request.
            return
        if self.prefix:
            format = self.prefix + format
        if not self.noEOL:
            format += '\n'
        fprintf(self.stream, format, *args)
        if self.prefix.find('EXCEPTION')>=0:
            pass
#            fprintf( self.stream, "Exception below:\n" )
#            traceback.print_exc() # Just prints None on my Mac. Strange.
        if self.autoFlush:
            self.stream.flush()
            self.flush()
    def flush(self):
        self.stream.flush()
    def setVerbosity(self, verbose):
        self.verbose=verbose

ERROR_ID = "ERROR"
WARNING_ID = "WARNING"
MESSAGE_ID = "MESSAGE"
DEBUG_ID = "DEBUG"

NTnothing = PrintWrap(verbose=verbosityNothing) # JFD added but totally silly
NTerror   = PrintWrap(verbose=verbosityError, prefix = 'ERROR: ')
NTcodeerror=PrintWrap(verbose=verbosityError, prefix = 'ERROR IN CODE: ')
NTexception=PrintWrap(verbose=verbosityError, prefix = 'EXCEPTION CAUGHT: ')
NTwarning = PrintWrap(verbose=verbosityWarning, prefix = 'WARNING: ')
NTmessage = PrintWrap(verbose=verbosityOutput)
NTdetail  = PrintWrap(verbose=verbosityDetail)
NTdebug   = PrintWrap(verbose=verbosityDebug, prefix = 'DEBUG: ')

NTmessageNoEOL = PrintWrap(verbose=verbosityOutput, noEOL=True)
#NTcodeerror.prefix += " IN CODE"
#NTcodeerror.prefix += " EXCEPTION CAUGHT"

def NTexit(msg, exitCode=1):
    NTerror(msg)
    sys.exit(exitCode)

#def setVerbosity(verbosity):
#    cing.verbosity = verbosity
#    # Notify instances.
#    NTnothing.setVerbosity(verbosity):
#    NTerror.setVerbosity(verbosity):
#    NTwarning.setVerbosity(verbosity):
#    NTmessage.setVerbosity(verbosity):
#    NTdetail.setVerbosity(verbosity):
#    NTdebug.setVerbosity(verbosity):

class SetupError(Exception):
    "Setup check error"

class CodeError(Exception):
    "Program code error"


class NTfile(file):
    """File class with a binary read/write
           typecode as defined for array module:

This module defines an object type which can efficiently represent an array of basic values: characters, integers,
floating point numbers. Arrays are sequence types and behave very much like lists, except that the type of objects
stored in them is constrained. The type is specified at object creation time by using a type code, which is a single
character. The following type codes are defined:

 Type code  C-Type          Python-Type         Minimum size in bytes
'c'         char            character           1
'b'         signed char     int                 1
'B'         unsigned char   int                 1
'u'         Py UNICODE      Unicode character   2
'h'         signed short    int                 2
'H'         unsigned short  int                 2
'i'         signed int      int                 2
'I'         unsigned int    long                2
'l'         signed long     int                 4
'L'         unsigned long   long                4
'f'         float           float               4
'd'         double          float               8

The actual representation of values is determined by the machine architecture (strictly speaking, by the C imple-
mentation). The actual size can be accessed through the itemsize attribute. The values stored for 'L' and
'I' items will be represented as Python long integers when retrieved, because Python's plain integer type cannot
represent the full range of C's unsigned (long) integers.
    """
    def __init__(self, *args, **kwds):
        file.__init__(self, *args, **kwds)
    #end def

    def binaryWrite(self, typecode, *numbers):
        """Binary write of numbers
           typecode as defined for array module
        """
        n = array.array(typecode, numbers)
        self.write(n.tostring())
    #end def

    def binaryRead(self, typecode, size):
        """Return a list of numbers
        """
        n = array.array(typecode)
        n.fromfile(self, size)
        return n.tolist()
    #end def

    def rewind(self):
        """rewind the file"""
        self.seek(0)
    #end def
#end class
NTopen = NTfile


def removedir(path):
    """Recursive remove"""
    while (1):
        try:
            filelist=os.listdir(path)
        except:
            NTerror("ERROR: Subdirectory %s could not be entered", path)
        # DELETE ALL THE FILES
        for file in filelist:
            file=os.path.join(path, file)
            try:
                os.remove(file)
            except:
                if os.path.isdir(file):
                    removedir(file)
        try:
            os.rmdir(path)
        except:
            NTerror("ERROR: Directory could not be removed, most likely an NFS problem. Try again later.")
#            continue # disabled because was leading to a infinite loop
        break
    #end while
#end def


def NTpath(path):

    """Return a triple (directory, basename, extension) from path"
    """
    d = os.path.split(path)
    dirname = d[0]
    if len(dirname) == 0:
        dirname = '.'
    f = os.path.splitext(d[1])
    return dirname, f[0], f[1]
#end def

def NTmkdir(path):

    """ creates missing directories for the given path and
        returns a normalized absolute version of the path.

    - if the given path already exists in the filesystem
      the filesystem is not modified.

    - otherwise makepath creates directories along the given path
      using the dirname() of the path. You may append
      a '/' to the path if you want it to be a directory path.

    from holger@trillke.net 2002/03/18
    Adusted gv with expanduser

    """

    from os import makedirs
    from os.path import normpath, dirname, exists, expanduser

    path=expanduser(path)
    dpath = normpath(dirname(path))
    if not exists(dpath): makedirs(dpath)
    return normpath(path)
#end def

def show(NTobject=None):
    if NTobject != None and hasattr(NTobject, 'format'):
        NTmessage("%s", NTobject.format())
    else:
        NTmessage("%s %s", type(NTobject), str(NTobject))
    #end if
#End def


def formatList(theList, fmt = '%s\n'):
    """
    Apply the format method to every element of theList,
    and return their joined strings.
    """
    result = []
    for element in theList:
#        NTdebug("Doing element: " +`element`)
        result.append(fmt%element.format())
    return ''.join(result)
#end def

######################################################################################################
# This code is repeated in cing/setup.py and cing/Libs/NTutils.py please keep it sync-ed
######################################################################################################
def NTgetoutput(cmd):
    """Return output from command as (stdout,sterr) tuple"""
    inp, out, err = os.popen3(cmd)
    output = ''
    for line in out.readlines(): output += line
    errors = ''
    for line in err.readlines(): errors += line
    inp.close()
    out.close()
    err.close()
    return (output, errors)
#end def


class ExecuteProgram(NTdict):
    """
    Base Class for executing external programs on Unix like systems.
    """
    def __init__(self, pathToProgram,
                 rootPath = None,
                 redirectOutput= True,
                 redirectOutputToFile = False,
                 redirectInputFromDummy = False,
                 redirectInputFromFile = False,
                 *args, **kwds):
        NTdict.__init__(self, pathToProgram  = pathToProgram,
                               rootPath       = rootPath,
                               redirectOutput = redirectOutput,
                               redirectOutputToFile   = redirectOutputToFile,
                               redirectInputFromDummy = redirectInputFromDummy,
                               redirectInputFromFile  = redirectInputFromFile,
                               *args, **kwds
                       )
        self.jobcount = 0
    #end def

    def __call__(self, *args):
        """
        Execute the program.
        Return exit code
        """
        if not self.pathToProgram:
            raise SetupError("No program given for arguments: "+`args`)

        if self.rootPath:
            cmd = sprintf('cd %s; %s %s', self.rootPath, self.pathToProgram, " ".join(args))
        else:
            cmd = sprintf('%s %s', self.pathToProgram, " ".join(args))
        #end if

        if self.redirectInputFromDummy and self.redirectInputFromFile:
            NTerror("Can't redirect from dummy and from a file at the same time")
            return 1

        if self.redirectOutputToFile and self.redirectOutput:
#            NTdebug("Can't redirect output to standard filename and given file name at the same time; will use specific filename")
            self.redirectOutput = False


        if self.redirectInputFromDummy:
            cmd = sprintf('%s < /dev/null', cmd)
        elif self.redirectInputFromFile:
            cmd = '%s < %s' % (cmd, self.redirectInputFromFile)


        if self.redirectOutput:
            dir, name, _ext = NTpath(self.pathToProgram)
            # python call shell sh and in some os (e.g. linux) >& may not work
            # see http://diveintomark.org/archives/2006/09/19/bad-fd-number
            cmd = sprintf('%s > %s.out%d 2>&1', cmd, name, self.jobcount)
            self.jobcount += 1
        elif self.redirectOutputToFile:
            cmd = sprintf('%s > %s 2>&1', cmd, self.redirectOutputToFile)
            self.jobcount += 1
#        NTdebug('==> Executing ('+cmd+') ... ')
        code = os.system(cmd)
#        NTdebug( "Got back from system the exit code: " + `code` )
        return code
#end class

def getOsResult( cmd ):
    """
    Returns tuple (status, msg)
    status 0 for success. > 0 for failure.
    """
#    NTdebug( "Doing command: %s" % cmd )

    ##  Try command and check for non-zero exit status
    pipe = os.popen( cmd )
    output = pipe.read()

    ##  The program exit status is available by the following construct
    ##  The status will be the exit number unless the program executed
    ##  successfully in which case it will be None.
    status = pipe.close()

#    if output:
#        NTdebug( "Found os msg: %s" % output )

#    if status:
#        NTdebug("Failed shell command:")
#        NTdebug( cmd )
#        NTdebug("Output: %s" % output)
#        NTdebug("Status: %s" % status)

    return ( status, output )


class OptionParser (optparse.OptionParser):
    """
    OptionParser.py: implement required options
    from: http://docs.python.org/lib/optparse-extending-examples.html

    """
    def check_required (self, opt):
        option = self.get_option(opt)

        # Assumes the option's 'default' is set to None!
        if getattr(self.values, option.dest) is None:
            self.error("%s option not supplied" % option)
    #end def
#end class


def findFiles_old(pattern, startdir=os.curdir):
    matches = []
    os.path.walk(startdir, findvisitor, (matches, pattern))
    matches.sort()
    return matches

def findvisitor((matches, pattern), thisdir, nameshere):
    for name in nameshere:
        if fnmatch(name, pattern):
            fullpath = os.path.join(thisdir, name)
            matches.append(fullpath)

def findFiles(pattern, startdir, exclude=[]):
    """
    Find files matching pattern, based upon os.walk
    """
    result = []
    #print exclude
    for dirpath, _dirs, files in os.walk(startdir):

        excludePath = False
        for e in exclude:
            #print '>>',dirpath,e
            if fnmatch(str(dirpath), e):
                excludePath = True
                break
            #end if
        #end for
        #print '>>',dirpath, excludePath

        if not excludePath:
            for file in files:
                if fnmatch(file, pattern):
                    result.append(os.path.join(dirpath, file))
                #end if
            #end for
        #end if
    #end for
    result.sort()
    #print '>>',result
    return result
#end def

def matchString( source, target ):
    """
    Poor mans approach to match a target with wildcards (*) to source.
    Does not properly match XZS* yet because aaXZSxx wil also yield True
    Returns True upon match or False otherwise
    """
    parts = target.split('*')
    for p in parts:
        if source.find(p) < 0:
            return False
    #end for
    return True
#end def

def val2Str(value, fmt, count=None):
    """Utility for translating numeric values to strings allowing the value
    to be a None and returning the NaNstring in such case. When the value is
    None the count determines how long the return string will be.
    Regular formatting is used otherwise."""
    if value==None or isNaN(value):
        value = None
    if value == None:
        if not count:
            return NaNstring
        return ("%"+`count`+"s") % NaNstring
    return fmt % value

def limitToRange(v, low, hi):
    """Return a value in range [low,hi}
    truncating the value to given bounds
    E.g. a value of 5 with bounds [0,1] will
    return 1.
    """
    # use equal signs for speed.
    if v >= hi:
        return hi
    if v <= low:
        return low
    return v

def NTmax(*args):
    """Usefull as matplotlib overrides buildin"""
    result = args[0]
    for a in args:
        if a > result:
            result = a
    return result

#
def NTmin(*args):
    """Usefull as matplotlib overrides buildin"""
    result = args[0]
    for a in args:
        if a < result:
            result = a
    return result



#
#def splitpdb( fileName = None, modelNum = None ):
#    """
#    Author: Ton Rullmann
#    Adapted by JFD
#    # jfd@Fri Jan 14 14:43:02 CST 2000
#    # Moved the file name generation outside the BEGIN statement
#    # maybe we have an awk version not supporting it.
#    Moved to Python on 19 nov 2007.
#    """
#    usage = """usage: splitpdb [modelnum=?] file
#
#Split a multi-model PDB file into separate PDB files, named xxx_001.yyy etc.
#where xxx is the name of the input file (minus directory path)
#and yyy its extension (if present).
#
#Returns None on error and 1 for success.
#
#If modelnum is given, only the model with the corresponding model number
#is extracted.
#
#Everything before the first MODEL (except JRNL and REMARK records)
#is removed and does not occur in any output file.
#Everything between MODEL and ENDMDL is copied.
#The MODEL records are replaced by a REMARK.
#The ENDMDL records are replaced by END.
#Everything after the last ENDMDL (including CONECT's) is discarded.
#A MASTER record is not added.
#
#If no MODEL records are present no new PDB files are produced
#and the script exits with status 1
#A MODEL 0 record (as in entry 1CRQ) is ignored by the script.
#"""
#    NTerror("Don't use this code until completed")
#    return None
#    if not fileName:
#        NTwarning(usage)
#        return None
#
#    if not os.path.exists( fileName ):
#        NTerror("Input file : "+fileName+" doesn't exist")
#        return None
#
#    modelId = 1
#    fileNameModel = _fileNameModel( fileName, modelId )
#    file = open( fileNameModel, 'w')
#    for line in AwkLike(fileName):
##         if line.NF > 1:
##             print line.dollar[0], line.dollar[1]
#        if line.dollar[0].startsWith("JRNL"):
#            continue
#        if line.dollar[0].startsWith("REMARK"):
#            continue
#        if line.dollar[0].startsWith("MODEL"):
#            ## JFD to add perhaps: Special case for entry 1crq with MODEL 0 record
#            ## and       Special case for entry 1crr with MODEL 21 record
#            ## Skip the whole model, treat it as if it is not an ensemble.
#            ## if the first model listed is not number 1
#            if line.NF < 2:
#                NTerror("Add special case for when model record doesn't contain model number")
#                return None
#
#            modelStr = line.dollar[2]
#            modelId = `modelStr`
##            modelFileNamePart = sprintf( "%03i", modelId )
#            fileNameModel = _fileNameModel( fileName=fileName, modelId=modelId )
#            NTmessage( "copying model" + modelId +  "to" + fileNameModel )
#            if modelId > 1:
#                file.write( "END")
#            # Normally the first file will be closed and reopened here for multimodel files.
#            # In some cases the first model is not numbered 1!
#            file.close()
#            file = open( fileNameModel, 'w')
#            file.write ("REMARK model" + modelId )
#            continue
#        if line.dollar[0].startsWith("CONECT"):
#            continue
#        if line.dollar[0].startsWith("MASTER"):
#            continue
#
#        file.write (line.dollar[0] )
#
#""" Returns new file name for a given model number
#or None for Error.
#"""
#def _fileNameModel( fileName=None, modelId=None ):
#    if modelId is None:
#        return None
#    if not os.path.exists(fileName):
#        return None
##    modelFileNamePart = ""
##    ext = os.path.getExtension(fileName)
##    base = os.path.getBase(fileName)
##    return base + "_" + sprintf( "%03i", modelId ) + ext

def cross3Dopt(a, b):
    return [
    a[1]*b[2]-a[2]*b[1], # x-coordinate
    a[2]*b[0]-a[0]*b[2], # y-coordinate
    a[0]*b[1]-a[1]*b[0]  # z-coordinate
    ]

def dot3Dopt(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def length3Dopt(a):
    return math.sqrt(a[0]*a[0]+a[1]*a[1]+a[2]*a[2])

FAC = 180.0/math.pi


def angle3Dopt(a, b):
    """
    return angle spanned by a and b
    or None on error
    range = [0, pi]
    positive angle is counterclockwise (to be in-line with 'polar' methods
    and atan2 routines).
    """
    # optimized out.
#        c = self.dot(other) /(self.length()*other.length())
    c = dot3Dopt(a, b)
    c /= length3Dopt(a)
    c /= length3Dopt(b)

    # Are the below needed for rounding effects?
    c = min(c, 1.0)
    c = max(c, -1.0)
#        if radians:
#            return math.acos( c )
    return math.acos(c) * FAC


def appendDeepByKeys(c, value, *keyList):
    """
    Append value to arbitrary deep list.
    If value is a (subclass of) list then append individual values from the list
    to the c (complex object) which needs to be a (subclass of) list itself.
    The essence here is silence.

    NB:
    - keyList needs to have at least one key.

    - All but the last level of the complex object should be (subclasses of)
    dictionaries. The last level must be a (subclasses of) list. If the
    itermediate objects (dictionaries and list) do not exist, they will be
    silently created.

    - The last key is not the id to the list to append to.

    - The complex argument needs to exist.

    Return None on success and True on error.
    """

    if c == None:
        NTerror("Can't appendDeepByKeys without complex object on input.")
        return True

    lk = len(keyList)
#  NTdebug("Now in appendDeepByKeys with keyList: %s", `keyList`)
    if not lk:
        NTerror("Can't appendDeepByKeys without any key")
        return True

    key = keyList[0]

    # At the level where only one key exists; do the actual append to the list.
    if lk == 1:
        # First make sure the list to append to exists.
        if isinstance(c, list):
            # Make sure the list already has an element with the key as index.
            if key >= len(c):
                NTdebug("Impossible situation: trying to go into a list at an index that isn't present.")
                NTdebug("key: %d and list length: %d" % (key, len(c)))
                return True
        elif isinstance(c, dict):
            if not c.has_key(key):
                c[key] = [] # For last level a new -list- is made when absent.
        else:
            NTdebug("The input complex object needs to be a (subclass of) dict or list")
            return True

        l = c[key]
        if not isinstance(l, list):
            NTdebug("At the bottom level the input complex object needs to be a (subclass of) list")
            return True
        if isinstance(value, list):
            for v in value:
                l.append(v)
            return
        l.append(value) # No extra checks done here for speed purposes.
        return
    # endif on lk==1, above section was misalligned before.

    if c.has_key(key):
        deeper = c[key]
    else:
        deeper = {}
        c[key] = deeper

    reducedKeyList = keyList[1:]
    return appendDeepByKeys(deeper, value, *reducedKeyList)


def setDeepByKeys(d, value, *keyList):
    """Set arbitrary deep element to value by keyList.
    The essence here is silence.
    keyList needs to have at least one key.
    Return None on success and True on error.
    """
    lk = len(keyList)
    if not lk:
        NTerror("Can't setDeepByKeys without any key")
        return True

    k = keyList[0]
    if lk == 1:
        d[k] = value
        return

    if d.has_key(k):
        deeper = d[k]
    else:
        deeper = {}
        d[k] = deeper

    reducedKeyList = keyList[1:]
    return setDeepByKeys(deeper, value, *reducedKeyList)

def addDeepByKeys(d, value, *keyList):
    """Increase found value (or zero in case absent) by given value.
    Return None on success and True on error.
    """
    v = d.getDeepByKeys(*keyList)
    if not v:
        v = 0
    v += value
    return d.setDeepByKeys(v, *keyList)

def getDeepByKeysOrDefault(c, default, *keyList):
    result = getDeepByKeys(c, *keyList)
    if result == None:
        return default
    return result

def getDeepByKeys(c, *keyList):
    """Return arbitrary deep element or None if key is absent at some point.
    The essence here is silence.
    If the key is an integer and the dict is not a dict but a list of sorts
    then the nice thing is that the element can be returned too!

    c for complex object.
    """
    lk = len(keyList)
#      NTdebug("Now in getDeepByKeys for keylist length: %d" % lk)
    if not lk:
        NTdebug("Asked for a get on a dictionary without a key")
        return None
    key = keyList[0]

    if isinstance(c, dict):
        if not c.has_key(key):
#          NTdebug("no key: " + `key`)
            return None
        value = c[key]
        if lk == 1:
#          NTdebug("value : " + `value`)
            return value
#      NTdebug("Going one level deeper")
        reducedKeyList = keyList[1:]
        return getDeepByKeys(value, *reducedKeyList)

    if not isinstance(c, list):
#      NTdebug("complex object not an instance of list")
        return None

    if not isinstance(key, int):
#      NTdebug("no int key in getDeepByKeys: " + `key`)
        return None

    if key >= len(c):
#      NTdebug("int key in getDeepByKeys to large for this NTlist: " + `key`)
        return None

    value = c[key]
    if lk == 1:
#      NTdebug("value : " + `value`)
        return value

#  NTdebug("Going one level deeper")
    reducedKeyList = keyList[1:]
    return getDeepByKeys(value, *reducedKeyList)
#end def


def getDeepByKeysOrAttributes(c, *keyList):
    """Return arbitrary deep element or None if key is absent at some point.
    The essence here is silence.

    If the key is an integer and the dict is not a dict but a list of sorts
    then the nice thing is that the element can be returned too!

    c for complex objects.
    Hacked for attributes too, in case key does not exist

    """
    lk  = len(keyList)
    key = keyList[0]

    #NTdebug("getDeepByKeysOrAtributes: c:%s  keylist:%s  lk:%d  key: %s", c, keyList, lk, key)

    if not lk:
        return None

    value = None
    if isinstance(c, dict):
        if c.has_key(key):
            value = c[key]
        elif hasattr(c, key):
            value = getattr(c, key)
        else:
            return None
        #endif

        if lk == 1:
            return value

    elif isinstance(c, list):
        if isinstance(key, int):
            if key < len(c):
                value = c[key]
            else:
                return None
            #endif
        elif hasattr(c, key):
            value = getattr(c, key)
        else:
            return None
        #endif

    elif isinstance(c, tuple):
        if isinstance(key, int) and key < len(c):
            value = c[key]
        else:
            return None

    else:
        if hasattr(c, key):
            value = getattr(c, key)
        else:
            return None
        #endif
    #end if

    #NTdebug("getDeepByKeysOrAtributes: value: %s", value)

    if lk-1 == 0 or value==None:
        return value

    # still have keys left; use recursion for next element
    reducedKeyList = keyList[1:]
    return getDeepByKeysOrAttributes(value, *reducedKeyList)
#end def



def gunzip(fileNameZipped, outputFileName=None):
    """Returns true on error. Uses python api instead of OS defaults"""
    if not fileNameZipped.endswith('.gz'):
        NTerror("Expected zipped file to have .gz extension; giving up.")
        return True

    inF = GzipFile(fileNameZipped, 'rb');
    s=inF.read()
    inF.close()
    fileName = fileNameZipped[:-3]
    if outputFileName:
        fileName = outputFileName
    outF = file(fileName, 'wb');
    outF.write(s)
    outF.close()


def getEnsembleAverageAndSigmaFromHistogram(his):
    """According to Rob's paper. Note that weird cases exist which to me
    are counter intuitive
[[ 0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.]]
Gives an c_av of 1. And the c_sd can't be calculated.
Rob might have caught this by requiring c_av be at least 2.0.

        # Calculate the count database average for this histogram and
        # the sigma (s.d.) of it. this is done as defined by equations
        # in: Hooft et al. Objectively judging the quality of a protein
        # structure from a Ramachandran plot. Comput.Appl.Biosci. (1997)
        # vol. 13 (4) pp. 425-430

    """
#    NTdebug("getEnsembleAverageAndSigmaFromHistogram on his:\n%s" % his)
    (nr, nc) = his.shape
    sum = 0.
    sumsq = 0.
    for r in range(nr):
        for c in range(nc):
            v = his[r, c] # convenience variable
            sum += v
            sumsq += v*v
    c_av = sumsq / sum # this is not a regular average as far as I can tell.
    if sum <= 1.: # possible for small sets.
        return (c_av, None)
    sumsdsq = 0.
    for r in range(nr):
        for c in range(nc):
            v = his[r, c] # convenience variable
            v2 = v - c_av # convenience variable
            sumsdsq += v * v2*v2
#    NTdebug("sumsdsq: %8.3f" % sumsdsq)
    c_sd = sumsdsq / (sum-1)
    c_sd = math.sqrt(c_sd)
    return (c_av, c_sd)

def floatFormat(v, format):
    ''' Just check for nans.'''
    if isNaN(v):
        return NaNstring
    return format % v

def floatParse(v_str):
    '''Just check for nans.'''
#    NTdebug('''NaNstring [%s]''' % NaNstring)
#    NTdebug('''v_str [%s]''' % v_str)
    if v_str == NaNstring:
        return NaN
    return float(v_str)

def getTextBetween(s, startString, endString, startIncl=True, endIncl=True):
    """Slice the text to include only that inbetween. Input strings maybe None"""
    if startString:
        startIdx = s.find(startString)
    else:
        startIdx = 0
    if startIdx < 0:
        NTwarning('Failed to find starting string in given string')
        return
    if endString:
        endIdx = s.find(endString, startIdx)
    else:
        endIdx = len(s)

    if endIdx < 0:
        NTwarning('Failed to find ending string in given string')
        return
    if not startIncl:
        startIdx += len(startString)
    if endIncl:
        if endString:
            endIdx += len(endString)
        else:
            endIdx = len(s)

    return s[startIdx:endIdx]




def stripExtension(path):
    directory, basename, _extension = NTpath(path)
    return os.path.join(directory, basename)

def stripExtensions(pathList):
    result = []
    for path in pathList:
        result.append(stripExtension(path))
    return result

_visitedHashes = {}
def removeRecursivelyAttribute(x, attributeToRemove):
    _visitedHashes.clear()
    _removeRecursivelyAttribute(x, attributeToRemove)
    _visitedHashes.clear()


def _removeRecursivelyAttribute(x, attributeToRemove):
    """Watch out because this can remove any attribute; be carefull what argument you give.
    """
    #    Needed for cyclic graphed objects such as project...
    # TODO: make it work more than once...
    if isinstance(x, int) or isinstance(x, float) or x == None:
        return

    h = id(x)
    if not h:
        return
    if _visitedHashes.has_key(h):
        return
    _visitedHashes[h] = None

    if isinstance(x, list) or isinstance(x, tuple):
        for e in x:
            if e == attributeToRemove:
                del x[e]
            _removeRecursivelyAttribute(e, attributeToRemove)
    if isinstance(x, dict):
        for k in x.keys():
            if k == attributeToRemove:
                del x[k]
            else:
                _removeRecursivelyAttribute(x[k], attributeToRemove)


def bytesToFormattedString(size):
    """1600 bytes will be rounded to 2K"""
    k = 1024
    M = k*k
    G = k*M
    T = M*M
    ck = 'K'
    cM = 'M'
    cG = 'G'
    cT = 'T'
    postFix = ck

    divider = k
    if  size < M:
        divider = k
        postFix = ck
    elif size < G:
        divider = M
        postFix = cM
    elif size < T:
        divider = G
        postFix = cG
    else:
        divider = T
        postFix = cT

    r = size/float(divider)
    result = ("%.0f" % r) + postFix
    return result


def getCallerName():
    return inspect.stack()[1][3]
# end def

def NTtracebackWarning():
    traceBackString = format_exc()
#    print 'DEBUG: NTtracebackError: [%s]' % traceBackString
    if traceBackString == None:
        traceBackString = 'No traceback error string available.'
    NTwarning(traceBackString)

def NTtracebackError():
    traceBackString = format_exc()
#    print 'DEBUG: NTtracebackError: [%s]' % traceBackString
    if traceBackString == None:
        traceBackString = 'No traceback error string available.'
    NTerror(traceBackString)

if __name__ == '__main__':
    nmrrestrntsgrid.verbosity = nmrrestrntsgrid.verbosityDebug
    input = ['1brv', '9pcy' ]
