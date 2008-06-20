#!/bin/csh -f 
# Author: Jurgen F. Doreleijers 
# Thu May 17 08:53:47 CDT 2007
  


set run_id          = weekly20061016
set urlBase         = http://www.bmrb.wisc.edu/servlet_data/viavia/mr_mysql_backup
set fileNameList    = ( mrfile.txt mrblock.txt )
set wgetLogFile     = $run_id"_wget".log

if ( ! -e $results_dir/$run_id ) then
    mkdir $results_dir/$run_id
endif
cd $results_dir/$run_id

foreach x ( $fileNameList )
    echo "-1- Getting file from NMR Restraint Grid"
    # Write all output to 1 zip file as it should be.
    wget -v -o $wgetLogFile $urlBase/$x
    if ( $status ) then
        echo "ERROR: failed to wget from url: $urlBase/$x"
        exit 1
    endif
    
    echo "-2- Patching eol"
    sed -e 's/\t\n\t/\t/g' $x > $x.csv
    \mv -f $x.csv $x
end




