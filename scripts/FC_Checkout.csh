#!/bin/csh 
# Author: Jurgen F. Doreleijers 
# Thu Aug 23 11:47:22 CDT 2007
# Script for updating the ccpn and recoord code base.
# Do by 'hand' because the cvs access from Wim's account on tang to
# jurgenfd's account to cvs hasn't been automated.

# THIS CODE WAS NEVER RUN AUTOMATICALLY YET.



echo "Working from CCPNMR_TOP_DIR: $CCPNMR_TOP_DIR"

# Update CCPN
cd $CCPNMR_TOP_DIR/../ccpn
cvs -z3 -d jurgenfd@ccpn.cvs.sourceforge.net:/cvsroot/ccpn update -r branch2 

# Update RECOORD
# set myFilesA = (CloneWars.py forkoff.py guessOffset.py PDBEntryLists.py presetDict.py )
# set myFiles = ( $myFilesA localConstants.py )
# cp $myFiles  ../../../recoord/python/recoord/
# 
# cd $CCPNMR_TOP_DIR/../recoord/python/recoord
# 
# cvs -d :pserver:jurgen_bmrb.wisc.edu@cvsebi.ebi.ac.uk:/ebi/cvs/recoord commit -m "JFD mods" $myFilesA
# cvs -d :pserver:jurgen_bmrb.wisc.edu@cvsebi.ebi.ac.uk:/ebi/cvs/recoord update

# Create links between recoord/ccpn and all.
python $CCPNMR_TOP_DIR/../recoord/python/recoord/copyFromRep.py copy

# Create python api
python $CCPNMR_TOP_DIR/python/memops/scripts_v2/makePython.py



