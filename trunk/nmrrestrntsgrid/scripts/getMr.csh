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

set SERVER=rsync.wwpdb.org::ftp/
set PORT=33444
set USER_ID=anonymous
#set PASSWORD_FILE=$nrg_dir/passwordFilePdb.txt

set subl = ( 1a1p 1a93 1abz 1ad7 1aft 1as5 1awy 1bde 1bfw 1bh1 )
#set subl = ( `cat $list_dir/entry_list_nrg_2009-03-12.txt`)

# Get argument pdb code if it exists.
if ( $1 != "" ) then
    set subl = (  `echo $1 | sed 's/,/ /g'`  )
endif

echo "Doing" $#subl "pdb entries"
foreach x ( $subl )
    echo "Doing $x"
    set ch23 = ( `echo $x | cut -c2-3` )
    set subdirLoc = $MIRRORDIR/data/structures/divided/nmr_restraints/$ch23

    if ( ! -e $subdirLoc ) then
        echo "Creating dir: " $subdirLoc
        mkdir -p $subdirLoc
    endif

    set localFile = $subdirLoc/$x.mr.gz
    if ( -e $localFile ) then
        rm $localFile
    endif
    # Added quiet because the data doesn't exist for all entries.
    $RSYNC -rlpt -z --delete --port=$PORT --quiet \
        $USER_ID@$SERVER/data/structures/divided/nmr_restraints/$ch23/$x.mr.gz \
        $subdirLoc/$x.mr.gz >& /dev/null
    if ( ! -e $localFile ) then
        echo "WARNING: not retrieved $localFile"
    endif
end
echo "Done with syncing PDB MR files"