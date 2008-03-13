#!/bin/csh 
# Author: Jurgen F. Doreleijers @ Tue May 24 10:19:48 CDT 2005
#
# TASK: Use WHAT IF PDB files to rename FormatConverter STAR files to 
#           update atom nomenclature.
# USE:  Wattos_rename.csh 


# Overwrite the subl list for testing purposes
#set subl = ( 1brv )
set subl            = (`cat $list_step_2_file`)

# No need to change things below this line
###############################################################################
wsetup
cd $tmp_dir_big_all

echo "Doing" $#subl "pdb entries"
foreach x ( $subl )
    if ( -e $x"_extra".str ) then
        #echo "DEBUG: already done entry: $x"
        continue
    endif
    if ( ! -e $dir_wi_all/$x"_wi".pdb ) then
        echo "ERROR: no WI PDB file for entry: $x"
        continue
    endif
    #set script_file     = $scripts_dir/addCoordinates.wcf
    set script_file     = $scripts_dir/readPDBCoordinates.wcf

    if ( ! -e $dir_star_begin/$x/$x.str ) then
        echo "ERROR: no FormatConverter STAR file for entry: $x"
        continue
    endif
    
    echo "Doing entry: $x"
    set script_file_new = $x"_extra".wcf  
    set log_file        = $x"_extra".log
    gawk                                                \
        -v x=$x                                         \
        -v DIR_STAR_BEGIN=$dir_star_begin             \
        -v DIR_WI_ALL=$dir_wi_all                       \
        -v TMP_DIR_BIG_ALL=$tmp_dir_big_all             \
        '{                                              \
        gsub(/ENTRY_ID/,        x);                     \
        gsub(/DIR_STAR_BEGIN/,  DIR_STAR_BEGIN);       \
        gsub(/DIR_WI_ALL/,      DIR_WI_ALL);            \
        gsub(/TMP_DIR_BIG_ALL/, TMP_DIR_BIG_ALL);       \
        print}' \
        $script_file > $script_file_new            
           
    wattos < $script_file_new >& $log_file
    if ( $status ) then
        echo "ERROR in Wattos rename script for entry $x"
        continue
    endif
    grep ERROR $log_file
    if ( ! $status ) then
        echo "ERROR found in log file for entry $x"
        continue
    endif
    if ( ! -e $x"_extra".str ) then
        echo "ERROR found no star file for entry $x"
        continue
    endif
    \rm $script_file_new
end

echo "Finished Wattos_rename.csh"

