#!/bin/csh
# Author: Jurgen F. Doreleijers @ Fri Apr  1 15:01:48 CST 2005



set listing_file = $list_dir/list_minusOverall.txt
## No changes below this line
##############################################################################


set list = ( `cat $listing_file `)
echo "Found number of entries in minus listing files together: $#list"

foreach x ( $list ) 
    echo "Doing $x"
    ls $big_dir/wi/Proton_Check/all/$x*    
end




