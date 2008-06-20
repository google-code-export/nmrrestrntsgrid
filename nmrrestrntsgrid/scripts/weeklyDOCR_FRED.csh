#!/bin/csh -f
# Author: Jurgen F. Doreleijers 
# Thu Jun 1 13:51:19 CDT 2006
echo "Last update: Fri Jun 20 13:54:53 CEST 2008"
echo $scripts_dir
# $scripts_dir/weeklyDOCR_FRED.csh

# If no subl variable defined here, the last weekly batch will be retrieved.
#set subl = ( 1a4d 1a24 1afp 1ai0 1brv 1bus 1cjg 1hue 1ieh 1iv6 1kr8 2hgh   )
set subl = (  1a24 1afp 1ai0 1bus 1cjg 1hue 1ieh 1iv6 1kr8 2hgh )
#set subl = ( `cat $list_dir/setDocrFredBaddies786.csv` )

# Overwrites the below 3 settings. Checks will always be done.
set doChecksOnly = 0

set doGet        = 1
set doProcessing = 1
set doLogShow    = 1
set doChecks     = 1

set max_cpu      = 2
set max_entries  = 5000    
set this_prog    = $scripts_dir/weeklyDOCR_FRED.csh
set list_file    = $list_dir/list_tmp.csv # note that this is a temporary file not the input.

# Maxium distance violation for reporting.
set distanceCutOffMaxViol = 1.8
set countCutOffPercentage = 99

# No changes below this line. 
#######################################################################################

if ( $doChecksOnly ) then
    set doGet        = 0
    set doProcessing = 0
    set doLogShow    = 0
    set doChecks     = 1
endif 

if ( $?subl ) then 
    echo "Using specified subset; not the weekly batch"
else    
    echo "Will be looking for added or modified entries in the last week's pdb status files."
    cd $dir_pdb_status
    set last_dir = (`find . -maxdepth 1 -type d | cut -c3- | sort -r | head -1`)
    # In case the weekly should be older: 
    #set last_dir = (`find . -maxdepth 1 -type d | cut -c3- | sort -r | head -2 | tail -1`)
    cd $last_dir
    set subl = ( `gawk '{print substr($(NF),1,4)}' added.nmr modified.nmr |sort -u` )    
    set sublm = ( `gawk '{print substr($(NF),1,4)}' modified.nmr |sort -u` )
    if ( $#sublm ) then
        echo "Found modified entries: " $sublm
    endif
endif    

echo "Doing batch of $#subl entries: $subl"

if ( $doGet ) then
    echo "Getting files from grid for processing"
    set sublcsv = ( `echo $subl | gawk '{i=1;while (i<=NF) {printf "%s",$(i);if(i!=NF)printf ",";i++}}'` )
    if ( $#sublcsv < 1 ) then
        echo "ERROR: No entries in todo list this week"
        exit 1
    endif
    echo "1"
    $scripts_dir/getFilesFromGrid.csh $sublcsv 
    if ( $status ) then
        echo "ERROR $x found in getFilesFromGrid.csh"
        exit 1
    endif
    echo "2"
    $scripts_dir/getMmCif.csh $subl
    if ( $status ) then
        echo "ERROR $x found in getMmCif.csh"
        exit 1
    endif
else
	echo "Skipping doGet"
endif

echo "Creating list file for python script to fork through"
\rm -f $list_file >& /dev/null
foreach x ( $subl ) 
    echo $x >> $list_file
end    
endif

if ( $doProcessing ) then        
    echo "Processing"
    set date_string = (`date | sed -e 's/ /_/g'`)
    set prog_string = $this_prog:t
    set log_file    = $tmp_dir/$prog_string"_$date_string".log
    
    python -u $dir_nrg_python/nmrrestrntsgrid/core/CloneWars.py $list_file $max_cpu $max_entries |& tee $log_file 
    egrep --quiet "^ERROR" $log_file
    if ( ! $status ) then
        echo "ERROR $x found in processDOCR_FRED.csh log file"
    endif
else
	echo "Skipping doProcessing"
endif

if ( $doLogShow ) then
    echo "Individual Log files" 
    foreach x ( $subl )
        echo
        echo
        echo
        echo "Log file of entry $x"
        cat $perEntry_dir/$x.log
    end    
else
	echo "Skipping doLogShow"
endif

if ( $doChecks ) then        
    echo "Checking max violations etc."
    cd $tmp_dir
    foreach x ( $subl )
        echo
        echo $x
            
        if ( -e $dir_viol/$x/$x"_viol".str ) then
            set violations = (`grep "_Distance_constraint_stats_list.Viol_max" $dir_viol/$x/$x"_viol".str |\
                gawk -v c=$distanceCutOffMaxViol '{if ($2 >c) print $2}'`)
            if ( "$violations" != "" ) then
                echo $x Violations $violations
            endif
        else 
            echo "$x no violation report"
            continue
        endif

        set url = '&format=n%2Fa&pdb_id='$x'&request_type=block_set&subtype=full&type=entry'
        lynx -dump -width=999 $servletUrl'?'$url | egrep 'STAR *entry *full' |\
            gawk -f $scripts_dir/getGridCounts.gawk -v x=$x -v cutoff=$countCutOffPercentage 

        if ( ! -e $dir_compl/$x/$x"_compl".str ) then
            echo "$x no completeness report"
            continue
        endif

    end    
endif


echo "Finished processing weekly for DOCR/FRED batch."
