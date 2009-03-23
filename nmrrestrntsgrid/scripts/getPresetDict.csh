#!/bin/tcsh -f

############################################################################
#
# 
#
############################################################################

source $0:h/settings.csh


echo "Script for mirroring python presetDict.py file from BMRB to local setup."
# P is defined in settings.csh.
scp jurgen@tang.bmrb.wisc.edu:/big/docr/workspace/recoord/python/recoord2/presetDict.py $P

echo "Done"

