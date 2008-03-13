#!/bin/csh -f
# Author: Jurgen F. Doreleijers 
# $scripts_dir/testNewPDB.csh

cd /Users/jd/pdb-v3


#set list = ( `find . -name "*.gz" ` )
set list = (1a1t 1a4t 1aud 1biv 1d6k 1dz5 1ekz 1etf 1etg 1exy 1f6u 1fje 1fnx 1g70 1hji 1i9f 1k1g 1l1c 1mnb 1nyb 1oln 1qfq 1rgo 1rkj 1t2r 1t4l 1u6p 1ull 1wwd 1wwe 1wwf 1wwg 1zbn 2a9x 2ad9 2adb 2adc 2b6g 2c06 2cjk 2err 2ese 2hgh 484d)
echo "Looking for entries: $#list"
foreach x ( $list )
    set subdir = ( `echo $x | gawk '{print substr($0,2,2)}'` )
    set file = $subdir/$x/$x.pdb.gz
    if ( ! -e $file ) then
        continue
    endif
    echo $x
    gunzip -c $file | grep "EXPDTA    NMR"
end


# Junk follows
#        echo "DEBUG: skipping $x.gz"

