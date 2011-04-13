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

source $0:h/settings.csh


# You should CHANGE THE NEXT THREE LINES to suit your local setup
set MIRRORDIR=$pdbbase_dir                         # your top level rsync directory
set LOGFILE=$MIRRORDIR/logs                        # file for storing logs
set RSYNC=rsync                            # location of local rsync

set SERVER=rsync.wwpdb.org::ftp/
set PORT=33444
set USER_ID=anonymous
#set PASSWORD_FILE=$nrg_dir/passwordFilePdb.txt

#set subl = ( 1a1p 1a93 1abz 1ad7 1aft 1as5 1awy 1bde 1bfw 1bh1 )
#set subl = (`cat /Users/jd/entry_list_97.csv`)
set subl = (`cat $list_dir/bmrbPdbEntryList.csv`)

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
#        echo "Creating dir: " $subdirLoc
        mkdir -p $subdirLoc
   endif

    # skip entries already present
   if ( -e $subdirLoc/pdb$x.ent.gz && -e $MIRRORDIR/data/structures/all/pdb/pdb$x.ent.gz ) then
        continue
   endif

   $RSYNC -rlpt -z --delete --port=$PORT \
#    --password-file=$PASSWORD_FILE \
    $USER_ID@$SERVER/data/structures/divided/pdb/$ch23/pdb$x.ent.gz \
    $subdirLoc/pdb$x.ent.gz \
    |& tee $LOGFILE

   if ( -e $subdirLoc/pdb$x.ent.gz ) then
#           echo "linking to all dir"
#   		cd $MIRRORDIR/data/structures/all/pdb
           ln -s ../../divided/pdb/$ch23/pdb$x.ent.gz $MIRRORDIR/data/structures/all/pdb/pdb$x.ent.gz
   endif
end

echo "Done with syncing PDB files for number of entries: $#subl"

