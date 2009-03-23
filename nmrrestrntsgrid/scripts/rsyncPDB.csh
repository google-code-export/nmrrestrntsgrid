#!/bin/csh

# Updated by Jurgen Doreleijers Thu Mar  5 10:30:45 CET 2009
source $0:h/settings.csh

# Set to 0 for using normal archive.
set useRemediated=1

#set MIRRORDIR=/dumpzone/pdb/pdbRem                          # your top level rsync directory
set MIRRORDIR=$pdbbase_dir                          # your top level rsync directory
set LOGFILE=/tmp/rsyncPDB.log                           # file for storing logs
set RSYNC=/usr/bin/rsync                                 # location of local rsync
set specificFlagsForThisJob = rlptv
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

# status on the final grep will be zero when it did grep something.
#ps -elf | grep $specificFlagsForThisJob | grep rsync | grep -v grep
ps -ww | grep "$0" | grep -v grep | grep -v $$
if ( ! $status ) then
    echo "Stopping this cron job for another hasn't finished; see above list"
    exit 0
endif



if ( -f $LOGFILE ) then
    \rm -f $LOGFILE
endif

echo "Syncing PDB archive with useRemediated set to: $useRemediated"

$RSYNC -$specificFlagsForThisJob -z --delete --port=$PORT \
    --progress \
    --bwlimit=80 \
    --password-file=$PASSWORD_FILE \
    $USER_ID@$SERVER $MIRRORDIR |& tee $LOGFILE
echo "Done with syncing PDB archive"
