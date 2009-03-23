#!/bin/tcsh -f
# Author: Thomas Solomon
# Date:   November 1, 2002
# Updated by Kenneth J. Addess Jan 29,2004
# Updated by Chen, L. Nov 10, 2006
# Updated by Jurgen Doreleijers Thu Mar  5 10:30:45 CET 2009

source $0:h/settings.csh

set subl = (`cat $list_dir/entry_list_nrg_2009-03-12.txt`)
#set subl = ( 1a1p 1a93 1abz 1ad7 1aft 1as5 1awy 1bde 1bfw 1bh1 )

# Get argument pdb code if it exists.
if ( $1 != "" ) then
    set subl = (  `echo $1 | sed 's/,/ /g'`  )
endif

echo "Doing" $#subl "pdb entries"
foreach x ( $subl )
   echo "Doing $x"
   set ch23 = ( `echo $x | cut -c2-3` )
   set subdirLoc = $pdbbase_dir/data/structures/divided/nmr_restraints/$ch23
   set inputFile = $subdirLoc/$x.mr.gz
   if ( ! -e $inputFile ) then
    	echo "ERROR: no $inputFile"
        continue
   endif
   set patchFile = $UJ/wattosTestingPlatform/Wattos/mr_diff/$x.dif
   set outputFile = $mr_anno_progress_dir/$x.mr
   set tmpFile = /tmp/useDiffs_$$.tmp
   
   gunzip -c $inputFile > $tmpFile 
   patch --quiet $tmpFile $patchFile --output=$outputFile
   \rm -f $tmpFile 
end

echo "Done"

