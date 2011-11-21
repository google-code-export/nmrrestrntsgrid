#!/bin/tcsh
# $nrg_dir/scripts/rsyncPDB.csh
#
echo "DEBUG in rsyncPDB.csh"

source $0:h/settings.csh

set LOGFILE=/tmp/rsyncPDB.log
set RSYNC=/usr/bin/rsync
# If using a double -v flag there will be an extra line per file.
set specificFlagsForThisJob = "rlptz --delete --max-delete=40"

echo "Using following settings:"
echo "PDB rsync site:           $PDB_RSYNC_SITE"
echo "PDB base dir:             $pdbbase_dir"
echo "LOGFILE:                  $LOGFILE"
echo "specificFlagsForThisJob:  $specificFlagsForThisJob"

# status on the final grep will be zero when it did grep something.
ps -ww | grep "$0" | grep -v grep | grep -v $$
if ( ! $status ) then
    echo "Stopping this job for another hasn't finished; see above list"
    exit 0
endif

if ( -f $LOGFILE ) then
    \rm -f $LOGFILE
endif

## Use the following to GRAB a specific sub directory if necessary
## (dont forget to *exclude* the trailing slash!)...
# split up because PDB is timing out on any one operation.
# Doing progressively more as to see when the failure occurs.
# The all directory only contains sym links without actual data.
set GRAB_LIST = (\
"data/status"\
"data/structures/divided/mmCIF/br"\
"data/structures/divided/mmCIF"\
"data/structures/divided/nmr_chemical_shifts"\
"data/structures/divided/nmr_restraints"\
"data/structures/divided/nmr_restraints_v2"\
"data/structures/divided/pdb"\
)


echo "Syncing PDB archive"
#echo "DEBUUG: stopping for now"
#exit 1
foreach GRAB ( $GRAB_LIST )
    echo "GRAB: $GRAB"                                                                          |& tee $LOGFILE
    $RSYNC -$specificFlagsForThisJob $PDB_RSYNC_SITE/$GRAB/ $pdbbase_dir/$GRAB                  |& tee $LOGFILE
#    echo; echo
end
echo "Done with syncing PDB archive"
