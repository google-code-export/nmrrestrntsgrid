#!/bin/csh

# Updated by Jurgen Doreleijers Thu Mar  5 10:30:45 CET 2009
source $0:h/settings.csh

set MIRRORDIR=$pdbbase_dir                          # your top level rsync directory
set LOGFILE=/tmp/rsyncPDB.log                           # file for storing logs
set RSYNC=/usr/bin/rsync                                 # location of local rsync
set specificFlagsForThisJob = rlptv
set SERVER=rsync.wwpdb.org::ftp/                                # remote server name
set PORT=33444                                                  # port remote server is using
set USER_ID=anonymous

# status on the final grep will be zero when it did grep something.
ps -ww | grep "$0" | grep -v grep | grep -v $$
if ( ! $status ) then
    echo "Stopping this job for another hasn't finished; see above list"
    exit 0
endif

if ( -f $LOGFILE ) then
    \rm -f $LOGFILE
endif

echo "Syncing PDB archive"

$RSYNC -$specificFlagsForThisJob -z --delete --port=$PORT \
    --progress \
    --bwlimit=80 \
    $USER_ID@$SERVER $MIRRORDIR |& tee $LOGFILE

echo "Done with syncing PDB archive"
