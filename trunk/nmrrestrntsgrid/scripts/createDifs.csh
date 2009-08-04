#!/bin/tcsh -f
# Author: Thomas Solomon
# Date:   November 1, 2002
# Updated by Kenneth J. Addess Jan 29,2004
# Updated by Chen, L. Nov 10, 2006
# Updated by Jurgen Doreleijers Thu Mar  5 10:30:45 CET 2009

source $0:h/settings.csh

set subl = (`cat $list_dir/entry_list_nrg_2009-03-12.txt `)
set subl = ( 1brv )

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
   gunzip -c $inputFile | diff - ../mr_anno_backup/$x.mr > $x.dif
end

echo "Done"

