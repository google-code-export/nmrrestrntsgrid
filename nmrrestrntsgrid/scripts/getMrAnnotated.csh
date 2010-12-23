#!/bin/tcsh -f

############################################################################
#
# Script for mirroring all MR files from the PDB FTP archive using rsync
#
############################################################################
source $0:h/settings.csh


#set subl = ( 2k5b )
#set subl = ( 1brv 2jnd 2jqs 2ofc 2pmc )
set subl = ( 1brv )

# Get argument pdb code if it exists.
if ( $1 != "" ) then
    set subl = (  `echo $1 | sed 's/,/ /'`  )
endif

echo "Doing" $#subl "pdb entries"
foreach x ( $subl )
   echo "Doing $x"
   set ch23 = ( `echo $x | cut -c2-3` )
   if ( ! -e $mr_anno_progress_dir/$x.mr ) then
            #scp -P 39677 jurgen@localhost-grunt:/raid/backup/mr_anno_backup/$x.mr $mr_anno_progress_dir
            scp -P 39676 jurgen@localhost-nmr:/Users/jd/wattosTestingPlatform/Wattos/mr_anno_backup/$x.mr $mr_anno_progress_dir
            #scp nmr:$mr_anno_progress_dir/../mr_anno_backup/$x.mr $mr_anno_progress_dir
            if ( ! -e $mr_anno_progress_dir/$x.mr ) then
                echo "ERROR: failed to copy from nmr: $mr_anno_progress_dir/$x.mr"
            endif
   endif
end

echo "Done with retrieving the annotated MR file from BMRB via NMR"

