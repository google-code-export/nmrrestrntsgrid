#!/bin/tcsh
# $nrg_dir/scripts/rsyncPDB.csh
source $0:h/settings.csh

#set MIRRORDIR=$pdbbase_dir                           # your top level rsync directory
set MIRRORDIR=/Users/jd/wattosTestingPlatform/pdb/   # your top level rsync directory

set LOGFILE=/tmp/rsyncPDB.log                           # file for storing logs
set RSYNC=/usr/bin/rsync                                 # location of local rsync
set specificFlagsForThisJob = "rlptv --max-delete=40"

echo "Using PDB rsync site: $PDB_RSYNC_SITE as set in settings.csh and perhaps overwritten in localSettings.csh"

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

$RSYNC -$specificFlagsForThisJob -z --delete --progress -v $PDB_RSYNC_SITE $MIRRORDIR |& tee $LOGFILE

echo "Done with syncing PDB archive"
