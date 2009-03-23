#!/bin/tcsh -f

############################################################################
#
# Script for mirroring all MR files from the PDB FTP archive using rsync
#
############################################################################

# This script is being provided to PDB users as a template for using rsync 
# to mirror the FTP archive from an anonymous rsync server. You may want 
# to review rsync documentation for options that better suit your needs.
#
# Author: Thomas Solomon
# Date:   November 1, 2002
# Updated by Kenneth J. Addess Jan 29,2004
# Updated by Chen, L. Nov 10, 2006
# Updated by Jurgen Doreleijers 2007


source $0:h/settings.csh

set MIRRORDIR=$pdbbase_dir                         # your top level rsync directory
set LOGFILE=$MIRRORDIR/logs                        # file for storing logs
set RSYNC=rsync                            # location of local rsync

set SERVER=rcsb-rsync-4.rutgers.edu::ftp-v3.2/pdb/
set PORT=8730
set USER_ID=wwpdb
set PASSWORD_FILE=$nrg_dir/passwordFilePdb.txt

set subl = ( 1a1p 1a93 1abz 1ad7 1aft 1as5 1awy 1bde 1bfw 1bh1 )

#set subl = ( 1cjg 1hue 1ieh 1iv6 1kr8 2hgh 2juy 2jvf 2k0e 2k17 2o7w )
# Get argument pdb code if it exists.
if ( $1 != "" ) then    
    set subl = (  `echo $1 | sed 's/,/ /g'`  )
endif

echo "Doing" $#subl "pdb entries"
foreach x ( $subl )
   echo "Doing $x"
   set ch23 = ( `echo $x | cut -c2-3` )
   set subdirLoc = $MIRRORDIR/data/structures/divided/nmr_restraints/$ch23


#	set subdirLoc = $MIRRORDIR/data/structures/divided
	if ( ! -e $subdirLoc ) then
	    echo "Creating dir: " $subdirLoc
	    mkdir -p $subdirLoc
	endif
    if ( -e $subdirLoc/$x.mr.gz ) then
    	continue
    endif
   $RSYNC -rlpt -z --delete --port=$PORT \
    --password-file=$PASSWORD_FILE \
    $USER_ID@$SERVER/data/structures/divided/nmr_restraints/$ch23/$x.mr.gz \
    $subdirLoc/$x.mr.gz
end
echo "Done with syncing PDB MR files"

