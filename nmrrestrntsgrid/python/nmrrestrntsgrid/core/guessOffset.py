import sys,string
# Guess offset between restraints and seqreimport os,sys,string

verbosity = 2

def getSeqRes(fileName):
  result = []
#SEQRES   1 A  113  HIS HIS HIS HIS HIS HIS GLU SER ASP ASP ASP ASP LYS  6I1B 137        
#SEQRES   2 A  113  LEU ALA PHE GLY ALA ILE GLN LEU ASP GLY ASP GLY ASN          
  r = open(fileName, 'r')
  data = r.read()
  r.close()
  dataLines = data.split("\n")
  resNumb = 1
  chainId = " "
  for dataLine in dataLines:
    if dataLine:
        chainIdNew = dataLine[11]
##        print "Found chainIdNew: [%s]" % (chainIdNew,)
        if chainId != chainIdNew:
          resNumb = 1
        chainId = chainIdNew
        infoLine=dataLine[19:71]
        resListLine = infoLine.split()
        for resName in resListLine:
          residueTuple = (chainId, resNumb, resName )          
          result.append( residueTuple )
          resNumb += 1
  return result

def getAtomRes(fileName):
  result = []
#"            29   GLY HA2   
#"            31     . HG12  
#"            31     . HG12  
#AN1         133     . HN   
#AN1         134     . HA   
  r = open(fileName, 'r')
  data = r.read()
  r.close()
  dataLines = data.split("\n")   
  for dataLine in dataLines:
    if dataLine:
        resListLine = dataLine.split()
        chainId = resListLine[-4] # Might contain extra column(s) at beginning.
        resNumb = resListLine[-3]
        resName = string.upper(resListLine[-2])
        atoName = string.upper(resListLine[-1])
        try:
          resNumb = string.atoi(resNumb)
        except: # Skip unparsable residue numbers.
          continue
##        print "Found chainId:", chainId
##        print "Found resName:", resName
##        print "Found resNumb:", resNumb
##        print "Found atoName:", atoName
        # Truncate residue names for like: CYSS, GLU-, LYS+
        if len(resName) > 3:
          resName = resName[0:3]
        ## Try to get res name.
## From Wim's FormatConverter code:          
##(resId,offset,score) = matchResidues(('GLY',),residues,           ('HA1','HA2','HA3','HA*','HA#','HA+','HA%'),resResidues,resResidueDict[resChainCode],test=test)
##(resId,offset,score) = matchResidues(('VAL','ILE','THR'),residues,('HG2*','HG2#','HG2+','HG2%','CG2'),resResidues,resResidueDict[resChainCode],matchScore = 5,test=test)
##(resId,offset,score) = matchResidues(('GLN',),residues,           ('HE21','HE22'),resResidues,resResidueDict[resChainCode],matchScore = 20,test=test)
##(resId,offset,score) = matchResidues(('LEU','ILE'),residues,      ('HD1*','HD1#','HD1+','HD1%'),resResidues,resResidueDict[resChainCode],matchScore = 5,test=test)
##(resId,offset,score) = matchResidues(('LEU','ASN'),residues,      ('HD2*','HD2#','HD2+','HD2%'),resResidues,resResidueDict[resChainCode],matchScore = 7,test=test)
##(resId,offset,score) = matchResidues(('T',),residues,             ('1H5M','2H5M','3H5M','H51','H52','H53','H71','H72','H73'),resResidues,resResidueDict[resChainCode],matchScore = 5,test=test)
##(resId,offset,score) = matchResidues(('C',),residues,             ('1H4','2H4','H41','H42'),resResidues,resResidueDict[resChainCode],matchScore = 8,test=test)
##(resId,offset,score) = matchResidues(('A',),residues,             ('1H6','2H6','H61','H62','H2'),resResidues,resResidueDict[resChainCode],matchScore = 6,test=test)
##(resId,offset,score) = matchResidues(('G',),residues,             ('1H2','2H2','H21','H22','H1'),resResidues,resResidueDict[resChainCode],matchScore = 6,test=test)          
        if resName == ".":
          if atoName == "HA2":  resName="GLY"
#          if atoName == "HG12": resName="ILE"
          if atoName == "HD21": resName="ASN"
          #if atoName == "HD2#": resName="LEU"
          if atoName == "HE21": resName="GLN"
#          if atoName == "HE2#": resName="GLN"
          if atoName == "HH1#": resName="ARG"            
          if atoName == "H61":  resName="A"
          if atoName == "H41":  resName="C"
          if atoName == "H21":  resName="G"
          if atoName == "O6":  resName="G"
          if atoName == "N4":  resName="C"
        result.append( (chainId, resNumb, resName, atoName ) )
  result.sort(sortRes)
#  print "RESULT:",result
  return result

def printRange(startAtom,endAtom,range):  
  if (not startAtom) or (not endAtom):
    print "DEBUG: skipping range printing unexisting atom"
    return
  diff = endAtom[1]-startAtom[1]
  print "Rst: %4s %3s %3s %4s - %3s %3s %4s diff %3d ch.range %3d" % (
    startAtom[0],startAtom[1],startAtom[2],startAtom[3],
                   endAtom[1],endAtom[2],endAtom[3], diff, (range+diff+1))

def isSameChain(r1,r2):
  if r1[0] == r2[0]:
    return 1
  else:
    return 0
  
def isSameRes(r1,r2):
##  print "DEBUG: Comparing (0) chains r1[0],r2[0]", r1[0],r2[0]
  if r1[0] != r2[0]:
    return 0
##  print "DEBUG: Comparing (0) residu r1[1],r2[1]", r1[1],r2[1]
  if r1[1] == r2[1]:
    return 1
  return 0

"""Returns true if r1 is right after r2"""  
def isNextRes(r1,r2):
##  print "DEBUG: Comparing (1) chains r1[0],r2[0]", r1[0],r2[0]
  if r1[0] != r2[0]:
    return 0
##  print "DEBUG: Comparing (1) residu r1[1],r2[1]", r1[1],r2[1]
  if r1[1] == (r2[1]+1):
    return 1
  return 0
  
  
def printRstRanges(list):
  print "Restraint ranges"
  startAtom = None
  prevAtom  = None
  range = 0
  for atom in list:
##    print "DEBUG: Looking at:",atom
    if not startAtom:
      startAtom = atom
      prevAtom = atom
      continue
##    print "DEBUG: Got a startAtom:",startAtom
    if isSameRes(atom,prevAtom):
##      print "DEBUG: isSameRes(atom,prevAtom):",atom,prevAtom
      continue
    if isNextRes(atom,prevAtom):
##      print "DEBUG: isNextRes(atom,prevAtom):",atom,prevAtom
      prevAtom = atom
      continue
    printRange(startAtom,prevAtom,range)
    range += prevAtom[1]-startAtom[1]+1
    if not isSameChain(atom,prevAtom):
      range=0
      print
    startAtom = atom
    prevAtom = atom
  if prevAtom:
    printRange(startAtom,prevAtom,range)
          
def sortRes(r1,r2):
##  print "DEBUG: Comparing r1[0],r2[0]", r1[0],r2[0]
  c = cmp(r1[0],r2[0])
  if c:
    return c
##  print "DEBUG: Comparing r1[1],r2[1]", r1[1],r2[1]
  c = cmp(r1[1],r2[1])
  if c:
    return c
##  print "DEBUG: Comparing r1[3],r2[3]", r1[3],r2[3]
  c = cmp(r1[1],r2[1])
  return c


"""
Return the index in res_list for a match
Algorithm:
Loop over all in seqres
  match 1 or next
  match 2 or next
  match 3 or next
If match residue 2 or 3 aren't in same chain then next.
"""
def findMatch(i,res_list_rst, res_list):

  # Need at least two residues following.
  idx2 = i+1
  idx3 = i+2  
  if len(res_list_rst) <= idx3:
    return None
  
  res1=res_list_rst[i]
  res1Chai=res1[0]
  res1Numb=res1[1]
  res1Name=res1[2]
  if verbosity > 2:
    print "DEBUG: Looking at 1st res: ", res1

  for matchRes1 in res_list:
    ## check 1
    matchRes1Chai = matchRes1[0]
    matchRes1Numb = matchRes1[1]
    matchRes1Name = matchRes1[2]
    if res1Name != matchRes1Name:
##      if verbosity > 2:
##        print "DEBUG: res1Name != matchRes1Name:", res1Name, matchRes1Name    
      continue
    offset1 = matchRes1Numb-res1Numb
    
    ## check 2
    res2=res_list_rst[idx2]
    res2Chai=res2[0]
    res2Numb=res2[1]
    res2Name=res2[2]    
    if verbosity > 2:
      print "DEBUG: Looking at 2nd res: ", res2
    if res2Chai != res1Chai:
      if verbosity > 2:
        print "DEBUG: res2Chai != res1Chai:", res2Chai, res1Chai   
      continue
    candidateMatchRes2Numb = res2Numb + offset1
    candidateMatchRes2 = ( matchRes1Chai, candidateMatchRes2Numb, res2Name)
    if not candidateMatchRes2 in res_list:
      if verbosity > 2:
        print "DEBUG: candidateMatchRes2 not in list: ", candidateMatchRes2      
      continue

    ## check 3
    res3=res_list_rst[idx3]
    res3Chai=res3[0]
    res3Numb=res3[1]
    res3Name=res3[2]    
    if verbosity > 2:
      print "DEBUG: Looking at 3rd res: ", res3
    if res3Chai != res1Chai:
      if verbosity > 2:
        print "DEBUG: res3Chai != res1Chai:", res3Chai, res1Chai   
      continue
    candidateMatchRes3Numb = res3Numb + offset1
    candidateMatchRes3 = ( matchRes1Chai, candidateMatchRes3Numb, res3Name)
    if not candidateMatchRes3 in res_list:
      if verbosity > 2:
        print "DEBUG: candidateMatchRes3 not in list: ", candidateMatchRes3      
      continue
    return matchRes1     
  return None

def trimUnknownResidues(res_list_rst):
  result = []
  for atom in res_list_rst:
    (chainId, resNumb, resName, _atoName ) = atom
    atom = (chainId, resNumb, resName, None )
    # don't append unknown residue types.
    if atom[2] == ".":
      continue
    # don't append same residue twice
    if (len(result) > 0) and (atom == result[-1]):
      continue
    # for debugging.
##    if len(result) > 10:
##      continue;
    result.append(atom)
  return result

def printSeqres(res_list):
  if not res_list: # Skip emty lists.
    return
  print "SEQRES derived records"
  chainId = (res_list[0])[0]
  started = None
  for res in res_list:
    chainIdNew = res[0]
    if chainIdNew != chainId:
      print 
      chainId = chainIdNew
    if ((res[1]-1) % 10 ):
      print      " %3d %4s" % (         res[1], res[2]),
    else:
      if started:
        print "\n",
      print "%1s %3d %4s" % ( res[0], res[1], res[2]),
    started = 1
  print

"""
Let's try to find an offset that matches for at least 3 res.
"""
def printTripletMatches(res_list_rst):
  print "Triplet matches"
  i=0
  res_list_rst_known_res = trimUnknownResidues( res_list_rst )  
  print "Restraint    SEQRS Offset"
  for res in res_list_rst_known_res:
##        print "DEBUG: looking at res: ", res, " with id: ", startResList
      resChai = res[0]
      resNumb = res[1]
      resName = res[2]
      matchRes = findMatch(i,res_list_rst_known_res,res_list)
      if matchRes:
        matchChai= matchRes[0]
        matchNumb= matchRes[1]
        offset = resNumb-matchNumb
        print "%4s %3d %3s %1s %3s %3s" % ( resChai, resNumb, resName, matchChai, matchNumb, offset )
      else:
        print "%4s %3d %3s .   .   ."    % ( resChai, resNumb, resName )
      i+=1  
###############################################################################

## Always nice to have a main:

if __name__ == '__main__':    
    if len(sys.argv) < 2:
        print "ERROR: need to specify the list filename of entries todo"
        sys.exit(1)

##    print "DEBUG"        
    seqResFileName  = sys.argv[1]
    atomResFileName = sys.argv[2]
    res_list      =  getSeqRes(seqResFileName)
    res_list_rst  =  getAtomRes(atomResFileName)

    printSeqres(res_list)
    print
    printRstRanges(res_list_rst)
    print      
    printTripletMatches(res_list_rst)
