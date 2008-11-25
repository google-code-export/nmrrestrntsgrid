#!/bin/tcsh -f

# Load common settings
source $SJ/BMRB/Matches_BMRB_PDB/scripts/settings.csh

set ETS_file_loc = /bmrb/admin/ETS_text_exports/ETS-Entry_log.txt
# Takes 45 wall clock seconds on halbeak (Pentium(R) 4 2.66GHz)
# for 4486 entries but that's when the disk access has been cached
# a couple of times.
######### NO CHANGES BELOW THIS LINE #############

echo "Scanning ETS entry log file"

echo "bmrb_id,pdb_id" > $ets_pdbFile
cat $ETS_file_loc    | \
    gawk '{if((NR>6)&&($3=="rel")) print}' | \
    sed -e 's/,/;/g'            | \
    sed -e 's/\t/,/g'           | \
    gawk -F',' 'BEGIN{getline}{printf "%s,%s\n", $2, tolower($16)}' | \
    gawk -F',' '/^[0-9]+,\.,\./{next}{print}' | \
    gawk -F',' '{if ($2==".") {next}}{print}' | \
    sed -e 's/rcsb//g'          | \
    sed -e 's/\&//g'            | \
    sed -e 's/\.//g'            | \
    gawk -F',' -v col=2 -f $scripts_dir/loopField >> \
    $ets_pdbFile  
    # The above does respectively in words:
    # Skip 6 header lines and select only released entries
    # Replace , by ;
    # Replace tabs by ,
    # Skip first line, print 3 selected columns
    # Skip lines without info (contain .,.)
    # Skip lines without pdb code at all
    # Excise rcsb prefix
    # Excise possible & 
    # Excise excessive whitespace (tabs and twice for regular spaces.)
    # Excise possible .        


echo "bmrb_id,rcsb_id" > $ets_rcsbFile
cat $ETS_file_loc    | \
    gawk '{if((NR>6)&&($3=="rel")) print}' | \
    sed -e 's/,/;/g'            | \
    sed -e 's/\t/,/g'           | \
    gawk -F',' 'BEGIN{getline}{printf "%s,%s\n", $2, $17}' | \
    gawk -F',' '/^[0-9]+,\.,\./{next}{print}' | \
    gawk -F',' '{if ($2==".") {next}}{print}' | \
    gawk -F',' '{if ($2 ~ "-") {next}}{print}' | \
    sed -e 's/rcsb//g'          | \
    sed -e 's/\&//g'            | \
    sed -e 's/\.//g'            | \
    gawk -F',' -v col=2 -f $scripts_dir/loopField >> \
    $ets_rcsbFile
    # Same as above except additionally it:
    # Excise possible value with a dash. 

