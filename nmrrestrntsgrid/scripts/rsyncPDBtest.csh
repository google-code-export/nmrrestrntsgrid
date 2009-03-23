#!/bin/csh

# Updated by Jurgen Doreleijers Thu Mar  5 10:30:45 CET 2009

echo "DEBUG: dollar zero  : [$0]"
echo "DEBUG: dollar dollar: [$$]"

source $0:h/settings.csh

# status on the final grep will be zero when it did grep something.
#ps -elf | grep $specificFlagsForThisJob | grep rsync | grep -v grep
ps -ww | grep "$0" | grep -v grep | grep -v $$
if ( ! $status ) then
    echo "Stopping this cron job for another hasn't finished; see above list"
    exit 0
endif

set sleepTime = 100
echo "DEBUG: sleeping $sleepTime"
sleep $sleepTime
