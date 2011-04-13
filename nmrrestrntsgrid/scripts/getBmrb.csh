#!/bin/csh

# To be executed from cron on at least a weekly basis.

source $0:h/settings.csh


set base_url    = 'rsync://www.bmrb.wisc.edu/bmrb_entries'
set target_dir  = $bmrb_dir/rsync
set wgetLogFile = "getBmrb_rsync".log

echo "Syncing ALL BMRB entries"
cd $target_dir
rsync -az --include='bmr*/' --include='**_21.str'\
    --exclude='**' --delete --max-delete=1000\
    $base_url . |& tee $wgetLogFile
echo "Done syncing BMRB"
