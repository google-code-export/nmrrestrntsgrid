#!/bin/csh -f 
# Author: Jurgen F. Doreleijers 
# Fri Jun  2 14:37:52 CDT 2006
# Use: set x=2ain; $scripts_dir/getAuthorEmail.csh $x

# Only works at BMRB because data is sensitive.
set dir_annotated = /dumpzone/rcsb_unpacked/annotated
###################################################################
## No changes below


# Get argument pdb code if it exists.
if ( $1 != "" ) then
    set x = (  $1  )
else 
    echo "ERROR: need to give entry code"    
endif

# To find author names and email addresses:
#set x = 2grg
set y = (`grep -i $x $dir_annotated/info_file`)
if ( $#y == 0 ) then
    echo "WARNING: entry $x not found in $dir_annotated/info_file"
    exit 0
endif
set y = $y[1]
set cifFile = $dir_annotated/rcsb$y/rcsb$y.cif
echo "From cif file: $cifFile"
egrep --before-context=1 \@ $cifFile

