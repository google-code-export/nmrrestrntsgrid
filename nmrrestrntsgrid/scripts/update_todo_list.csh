#!/bin/csh -f
# Author: Jurgen F. Doreleijers @ Fri Apr  1 15:01:48 CST 2005

source $0:h/settings.csh


# REQUIRED: - Wattos is installed.

## Files with lists of entries to do
# list_step_1_file For converting PDB file to STAR (FormatConverter)
# list_step_2_file For correcting atom nomenclature and synchronize models (WHAT IF)
# list_step_3_file For syncing coordinates (Wattos)
# list_step_4_file For linking with restraints (FormatConverter)
# list_step_5_file For DOCR 
# list_step_6_file For FRED
# list_step_7_file For analyzing results


# Note that for the final run the first selection should be made with the SQL
# commands in: getViableEntries.sql

set date_last_update_listing    = "2005-03-29"
# File generated by this program that contains all the entries to exclude.
set minus_listing_file          = list_minusOverall.txt
# File with entries that could be converted from PDB to STAR by
#   the FormatConverter.
set good_star_file              = list_good_star_file.txt
# File with entries that could be processed with WHATIF from PDB to PDB
# Excludes 276 any error producing log file entries
set bad_whatif_log_file         = list_bad_whatif_log_file.txt
# Including 2049 resulting (excluding 133 PDB files below 9 kb.)
    set good_whatif_size_file        = list_good_whatif_size_file.txt
set good_whatif_file            = list_good_whatif_file.txt
# File with good entries after Wattos sync and atom corrections on STAR files.
set good_star2_file             = list_good_star2_file.txt

# Entries that became obsolete after initial selection
set obsolete_file               = list_minus_obsolete.txt
# Entries that have another reason documented in the file. First word is entry code.
set minus_other_file            = list_minus_other.txt
## No changes below this line
##############################################################################

set tmp_file = list_tmp.txt

wsetup
if ( $status ) then
    echo "ERROR: Install Wattos first"
    exit 1
endif    

cd $list_dir
set last_listing_file = list_all_$date_last_update_listing.txt
set last_list = ( `cat $last_listing_file `)
echo "Found number of lines in last listing file: $#last_list"

gawk '{print $1}' $minus_other_file > $tmp_dir/minus_other_file.txt 
cat $obsolete_file \
    $tmp_dir/minus_other_file.txt \
    | sort -u > $minus_listing_file
\rm -f $tmp_dir/minus_other_file.txt  
set minus_list = ( `cat $minus_listing_file `)
echo "Found number of lines in minus listing files together: $#minus_list"
 

relate $last_listing_file difference $minus_listing_file $list_step_1_file
set list_step_1 = ( `cat $list_step_1_file `)
echo "Found number of entries todo list_step_1_file: $#list_step_1"

relate $list_step_1_file intersection $good_star_file $list_step_2_file
set list_step_2 = ( `cat $list_step_2_file `)
echo "Found number of entries todo list_step_2_file: $#list_step_2"

# None in bad whatif log actually are in good whatif size... so next line is
# redundant.
#relate $good_whatif_size_file difference $bad_whatif_log_file $list_step_3_file
cp $good_whatif_size_file $list_step_3_file
set list_step_3 = ( `cat $list_step_3_file `)
echo "Found number of entries todo list_step_3_file: $#list_step_3"

cp $good_star2_file $list_step_4_file

#relate $list_step_3_file intersection $good_star2_file $list_step_4_file
#set list_step_4 = ( `cat $list_step_3_file `)
#echo "Found number of entries todo list_step_4_file: $#list_step_3"

#set list_step_4 = ( `cat $list_step_4_file `)
#echo "Found number of entries todo list_step_4_file: $#list_step_4"
#set list_step_5 = ( `cat $list_step_5_file `)
#echo "Found number of entries todo list_step_5_file: $#list_step_5"
#set list_step_6 = ( `cat $list_step_6_file `)
#echo "Found number of entries todo list_step_6_file: $#list_step_6"


\rm -f $tmp_file

