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

set subl = ( 134d 135d 136d 177d 1crq 1crr 1ezc 1ezd 1gnc 1kld 1l0r 1lcc 1lcd 1msh 1qch 1r4e 1sah 1saj 1vve 2axx 2ezq 2ezr 2ezs 2i7z 2ku2 2neo 2ofg )
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

