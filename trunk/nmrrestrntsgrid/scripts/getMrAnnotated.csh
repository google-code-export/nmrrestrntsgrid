#!/bin/tcsh -f

############################################################################
#
# Script for mirroring all MR files from the PDB FTP archive using rsync
#
############################################################################
source $0:h/settings.csh


#set subl = ( 2k5b )
#set subl = ( 1brv 2jnd 2jqs 2ofc 2pmc )
set subl = ( 1go0 1ccf 1e0n 1ftt 1pjd )

# Get argument pdb code if it exists.
if ( $1 != "" ) then
    set subl = (  `echo $1 | sed 's/,/ /'`  )
endif

echo "Doing" $#subl "pdb entries"
foreach x ( $subl )
   echo "Doing $x"
   if ( ! -e $mr_anno_progress_dir/$x.mr ) then
       scp jurgen@tang.bmrb.wisc.edu:/share/wattos/mr_anno_backup/$x.mr \
       $mr_anno_progress_dir
   endif
end

echo "Done with retrieving the annotated MR file from BMRB"

