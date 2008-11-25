#!/bin/csh
# Author: Jurgen F. Doreleijers @ Thu Apr 21 16:02:31 CDT 2005
# Will also set subl variable list.
source $SJ/BMRB/Matches_BMRB_PDB/scripts/settings.csh

# The programs run very fast except the ones listed at the end of this file.
# Total run time is still below 20 minutes. Make sure getPdbnmrMrAndBmrbEntries.csh
# is the first to run.

# default is all 1
set doPrep      = 1
set doScore     = 1
set doPost      = 1
set doPublish   = 1

# Set the output level of the Wattos code.
set verbosity = 9
## No changes below this line
##############################################################################

set script_list = ( \
    getPdbnmrMrAndBmrbEntries.csh \
    getAuthorsBmrb.csh \
    getSequenceBmrb.csh \
    getBlast.csh \
    getEtsData.csh \
    getLigandsBmrb.csh \
    getLigandsPdb.csh \
    getModelsPdb.csh \
    getAuthorsPdb.csh \
)

set script_post_list = ( \
    doInternal_method_linking.csh \
)

echo "Starting top level script to score BMRB/PDB matches."

if ( ! -e $tmp_dir ) then
    mkdir -p $tmp_dir
endif

cd $list_dir
echo "Before executing this script we have:"
echo "PDB NMR entries: $#pdb_nmr_list"
echo "PDB MR entries : $#pdb_mr_list"
echo "BMRB entries   : $#bmrb_main_list"

echo "Initializing Wattos"
wsetup

if ( $doPrep ) then 
    foreach phase ( $script_list )
        ##echo "doing $phase"
        set base = $phase:r
        set cmd = $phase
        set log = $base.log
        echo "Logging to file: $tmp_dir/$log"
        $scripts_dir/$cmd >& $tmp_dir/$log
        if ( $status ) then
            echo "ERROR: failed phase: $phase"
            tail $tmp_dir/$log
            exit 1
        endif
        grep ERROR $tmp_dir/$log 
        if ( ! $status ) then
            echo "ERROR: failed phase: $phase"
            echo "ERROR: found an error in the log file; whose tail is:"
            tail $tmp_dir/$log
            exit 1
        endif
    end
endif

if ( $doScore ) then 
    #echo "Copying manual override list from $overrideFile"
    #cp -f $overrideFile $list_dir/override.csv
    set verbosity = 3
    set log = BMRBMatchWithPDBUpdate.log
    echo "Logging to file: $tmp_dir/$log"
    java -Xmx256m Wattos.Gobbler.Converters.BMRBMatchWithPDBUpdate \
        $verbosity >& $tmp_dir/$log
    if ( $status ) then 
        echo "ERROR: in Wattos.Gobbler.Converters.BMRBMatchWithPDBUpdate"
        exit 1
    endif
    grep ERROR $tmp_dir/$log
    if ( ! $status ) then
        echo "ERROR: failed BMRBMatchWithPDBUpdate"
        echo "ERROR: found an error in the log file; whose tail is:"
        tail $tmp_dir/$log
        exit 1
    endif
endif


if ( $doPost ) then 
    echo "Postprocessing results"
    foreach phase ( $script_post_list )
        ##echo "doing $phase"
        set base = $phase:r
        set cmd = $phase
        set log = $base.log
        echo "Logging to file: $tmp_dir/$log"
        $scripts_dir/$cmd >& $tmp_dir/$log
        if ( $status ) then
            echo "ERROR: failed phase: $phase"
            tail $tmp_dir/$log
            exit 1
        endif
        grep ERROR $tmp_dir/$log 
        if ( ! $status ) then
            echo "ERROR: failed phase: $phase"
            echo "ERROR: found an error in the log file; whose tail is:"
            tail $tmp_dir/$log
            exit 1
        endif
    end
endif

if ( $doPublish ) then 
    echo "Publish the resources on the web site off of the servlet data"
    \rm -rf $match_dir >& /dev/null
    mkdir -p $match_dir
    cp -rf $results_dir/*   $match_dir
    cp -rf $list_dir        $match_dir
    cp -rf $scripts_dir     $match_dir
    cp -rf $doc_dir         $match_dir
    
    set log = MRUpdateLinksBMRB.log
    echo "Logging to file: $tmp_dir/$log"
    java -Xmx128m Wattos.Episode_II.MRUpdateLinksToExternalDBs $results_dir >& $tmp_dir/$log
    if ( $status ) then 
        echo "ERROR: in Wattos.Episode_II.MRUpdateLinksToExternalDBs for result dir: $results_dir" 
        exit 1
    endif
    grep ERROR $tmp_dir/$log
    if ( ! $status ) then
        echo "ERROR: failed MRUpdateLinksToExternalDBs"
        echo "ERROR: found an error in the log file; whose tail is:"
        tail $tmp_dir/$log
        exit 1
    endif
    
endif
    
echo "Done with top level script."   

exit 0

##
#Timings
    getAuthorsPdb.csh \                 # 2:21.69
    getBlast.csh \                      # ?
    getLigandsPdb.csh \                 # 2:58.96
    getModelsPdb.csh \                  # 4:25.94
    getPdbnmrMrAndBmrbEntries.csh \     # 0:16.80
    doInternal_method_linking.csh.      # 0.00.60
    
    
    
