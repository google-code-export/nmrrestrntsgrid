#!/bin/tcsh -f

############################################################################
#
# Script for getting:
#   - pdb file
#   - mmCIF
#   - mr file
#   - mr annotated file
############################################################################

# Updated by Jurgen Doreleijers 2009

source $0:h/settings.csh

set MIRRORDIR=$pdbbase_dir                         # your top level rsync directory

set subl = ( 1j6t 1jtw 1dx1 1f8h 1vrc 2con 2exg )
#set subl = (`cat $list_dir/NMR_Restraints_Grid_entries_2009-08-03.txt`)
#set subl = ( 1a4d 1a24 1afp 1ai0 1brv 1bus 1cjg 1hue 1ieh 1iv6 1kr8 2hgh 2k0e )

# Get argument pdb code if it exists.
if ( $1 != "" ) then
#    set subl = (  $1  )
    set subl = (  `echo $1 | sed 's/,/ /'g`  )
endif


echo "==>     DOING" $#subl "pdb entries"
foreach x ( $subl )
    echo "==>      DOING $x"
    set ch23 = ( `echo $x | cut -c2-3` )


    set subdirLoc = $MIRRORDIR/data/structures/divided/pdb/$ch23
    \rm -f $subdirLoc/pdb$x.ent.gz
    $scripts_dir/getPdb.csh $x
    if ( $status ) then
        echo "ERROR: failed getPdb"
        continue
    endif

    set subdirLoc = $MIRRORDIR/data/structures/divided/mmCIF/$ch23
    \rm -f $subdirLoc/$x.cif.gz
    $scripts_dir/getMmCif.csh $x
    if ( $status ) then
        echo "ERROR: failed getMmCif"
        continue
    endif

    set subdirLoc = $MIRRORDIR/data/structures/divided/nmr_restraints/$ch23
    \rm -f $subdirLoc/$x.mr.gz
    $scripts_dir/getMr.csh $x
    if ( $status ) then
        echo "ERROR: failed getMr"
        continue
    endif

    \rm -f $mr_anno_progress_dir/$x.mr
    $scripts_dir/getMrAnnotated.csh $x
    if ( $status ) then
        echo "ERROR: failed getMrAnnotated"
        continue
    endif
end

echo "==> DONE with syncing PDB files for number of entries: $#subl"

