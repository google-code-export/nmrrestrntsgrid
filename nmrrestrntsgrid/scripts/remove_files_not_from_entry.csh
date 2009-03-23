#!/bin/csh -f
# Author: Jurgen F. Doreleijers @ Fri Jun 24 15:25:15 CDT 2005

source $0:h/settings.csh

set src_dir = $dir_wi_all

# The good entries:
set subl = (`cat $list_step_1_file`)
# No changes below this line.
##########################################################################
cd $src_dir

echo "Using list of good entries: " $#subl
foreach f ( `ls -1|sort -r` )
    set entryPartF = `echo $f| cut -c1-4`
    set isGood = 0
    foreach y ( $subl )
        if ( $entryPartF == $y ) then
            set isGood = 1
        endif
    end
    if ( ! $isGood ) then
        echo "Removing $f"
        \rm $f
    endif
end

