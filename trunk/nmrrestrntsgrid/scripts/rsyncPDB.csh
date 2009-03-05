#!/bin/tcsh -f

# Updated by Jurgen Doreleijers Thu Mar  5 10:30:45 CET 2009

# Set to 0 for using normal archive.
set useRemediated=1

#set MIRRORDIR=/dumpzone/pdb/pdbRem                          # your top level rsync directory
set MIRRORDIR=$pdbbase_dir                          # your top level rsync directory
set LOGFILE=/tmp/rsyncPDB.log                           # file for storing logs
set RSYNC=/usr/bin/rsync                                 # location of local rsync

#set SERVER=rsync.rcsb.org::ftp/                                # remote server name OLD
set SERVER=rsync.wwpdb.org::ftp/                                # remote server name
set PORT=33444                                                  # port remote server is using
set USER_ID=anonymous
set PASSWORD_FILE=$scripts_dir/passwordFileAnonymous.txt

if ( $useRemediated) then
    set SERVER=rcsb-rsync-4.rutgers.edu::ftp-v3.2/pdb/
    set PORT=8730
    set USER_ID=wwpdb
    set PASSWORD_FILE=$nrg_dir/passwordFilePdb.txt
endif

if ( -f $LOGFILE ) then
	rm $LOGFILE
endif

echo "Syncing PDB archive with useRemediated set to: $useRemediated"

$RSYNC -rlpt -v -z --delete --port=$PORT \
    --password-file=$PASSWORD_FILE \
    $USER_ID@$SERVER $MIRRORDIR |& tee $LOGFILE
echo "Done with syncing PDB archive"
