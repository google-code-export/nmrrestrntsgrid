#!/bin/tcsh -f

############################################################################
#
# Script for mirroring a certain mmCIF file from the PDB FTP archive using rsync
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
#set SERVER=rsync.wwpdb.org::ftp/                                # remote server name
set SERVER=rcsb-rsync-4.rutgers.edu::ftp-v3.2/pdb/

#set PORT=33444                                                  # port remote server is using
set PORT=8730
set USER_ID=wwpdb
set PASSWORD_FILE=$nrg_dir/passwordFilePdb.txt


#set subl = (`cat $list_dir/NMR_Restraints_Grid_entries_2008_02-14.txt`)
set subl = ( 1a4d 1a24 1afp 1ai0 1brv 1bus 1cjg 1hue 1ieh 1iv6 1kr8 2hgh 2k0e )

# Get argument pdb code if it exists.
if ( $1 != "" ) then
#    set subl = (  $1  )
    set subl = (  `echo $1 | sed 's/,/ /'g`  )
endif


echo "Doing" $#subl "pdb entries"
foreach x ( $subl )
   echo "Doing $x"
   set ch23 = ( `echo $x | cut -c2-3` )
   set subdirLoc = $MIRRORDIR/data/structures/divided/pdb/$ch23
   if ( ! -e $subdirLoc ) then
        echo "Creating dir: " $subdirLoc
        mkdir -p $subdirLoc
   endif
   
   $RSYNC -rlpt -z --delete --port=$PORT \
    --password-file=$PASSWORD_FILE \
    $USER_ID@$SERVER/data/structures/divided/pdb/$ch23/pdb$x.ent.gz \
    $subdirLoc/pdb$x.ent.gz \
    |& tee $LOGFILE 
end

echo "Done with syncing PDB files for number of entries: $#subl"

