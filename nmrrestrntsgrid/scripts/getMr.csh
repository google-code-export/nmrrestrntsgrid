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



# You should CHANGE THE NEXT THREE LINES to suit your local setup
#/Users/jd/wattosTestingPlatform/pdb/data/structures/divided/nmr_restraints
set MIRRORDIR=$pdbbase_dir                         # your top level rsync directory
set LOGFILE=$MIRRORDIR/logs                        # file for storing logs
set RSYNC=rsync                            # location of local rsync

# You should NOT CHANGE THE NEXT TWO LINES

#set SERVER=rsync.rcsb.org::ftp/                                # remote server name OLD
set SERVER=rsync.wwpdb.org::ftp/                                # remote server name
set PORT=33444                                           # port remote server is using


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
    $SERVER/data/structures/divided/nmr_restraints/$ch23/$x.mr.gz \
    $subdirLoc/$x.mr.gz
end
echo "Done with syncing PDB MR files"

