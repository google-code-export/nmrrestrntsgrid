#!/bin/csh -f
# Author: Jurgen F. Doreleijers 

set subl = ( 1a4d 1cw5 1brv )
#set subl = ( `cat  $list_dir/NMR_Restraints_Grid_entries_2008_11-21.txt`)
#set subl = ( 1a4d 1a24 1afp 1ai0 1brv 1bus 1cjg 1hue 1ieh 1iv6 1kr8 2hgh 2k0e )

echo "Doing" $#subl "pdb entries"
foreach x ( $subl )
   echo "Doing $x"
   if ( ! -e $ccpn_tmp_dir/data/recoord/$x ) then
        echo "WARNING: $x no ccpn folder"
        continue
   endif
   cd $ccpn_tmp_dir/data/recoord/$x
   if ( ! -e linkNmrStarData ) then
        echo "WARNING: $x no ccpn subfolder"
        continue
   endif
   tar -cf - linkNmrStarData | gzip --fast > $x.tgz
end

echo "Finished"
