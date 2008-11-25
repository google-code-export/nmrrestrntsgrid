#!/bin/tcsh -f

# Load common settings
source $SJ/BMRB/Matches_BMRB_PDB/scripts/settings.csh

# Set to 1 for testing or to zero for not.
set testing = 0

######### NO CHANGES BELOW THIS LINE #############
#Linking from BMRB entries to PDB entries for the BMRB summary pages. 

#For getting from BMRB entries to the PDB entries that are also in: 
#"NMR Restraints Grid"
################################################################################

echo "Creating links from BMRB entries to PDB entries for the BMRB summary pages."

\rm $results_dir/summary_pages_bmrb/*.csv >& /dev/null
#mkdir -p $results_dir/summary_pages
cd $results_dir/summary_pages_bmrb


#- Read the PDB entries in the Grid and the links.
wget -q $mysql_url/entry.txt
#wget -q $bmrb_pdb_url/score_many2many.csv
#wget -q $bmrb_pdb_url/score_one2many.csv

gawk '{print $3}' entry.txt | sort > entry_mod.txt
gawk -F',' '{printf "%s %s %s\n", $2,$1,$3}' ../score_many2many.csv | \
    sort > score_many2many_mod.txt
# Note that the files should be sorted on the join field before the join.        
# Get only those scores for which the pdb id is also in the Grid
#   this is done by joining on pdb code and 
# Sort numerically by BMRB id and overall score. 
# Get the lowest scoring target for each BMRB id.
# Convert to csv formatting.
join -o "2.2,2.1,2.3" entry_mod.txt score_many2many_mod.txt | \
    sort -n -k 1 -k 3 | \
    gawk '{if ($1!=prev) { print;prev=$1 }}' | \
    sed 's/  */,/g' > \
    bmrb_2_nmr_restraints_grid_link.csv

#For getting from BMRB entries to a NMR PDB entry.
################################################################################
#- If the BMRB entry has a link from the above to the Grid, use that PDB entry.
#- Else if present use the link from score_one2many.csv

# Get BMRB entries with scores for those without a related entry in the Grid.
#   Do this by sorting on BMRB id and then printing the scores for those
#   that don't match in the join (by using the -a option). 

# Skipping the header row.
sed 's/,/ /g' ../score_one2many.csv | \
    sort -n | gawk '{if(NR!=1)print}' > score_one2many_mod.txt
sed 's/,/ /g' bmrb_2_nmr_restraints_grid_link.csv | \
    sort -n > bmrb_2_nmr_restraints_grid_link_mod.txt

join -v 1 score_one2many_mod.txt bmrb_2_nmr_restraints_grid_link_mod.txt > \
    bmrb_2_pdb_for_pdb_image_only.txt

# Generate the file used for the BMRB entry summary pages
sed 's/  */,/g' bmrb_2_pdb_for_pdb_image_only.txt > \
    bmrb_2_pdb_for_pdb_image_only.csv
    
cat bmrb_2_nmr_restraints_grid_link_mod.txt bmrb_2_pdb_for_pdb_image_only.txt | \
    sort -n | \
    sed 's/  */,/g' > \
    bmrb_2_pdb_for_pdb_image_all.csv

if ( ! $testing ) then     
    \rm bmrb_2_pdb_for_pdb_image_only.txt
    \rm *_mod.*
    \rm entry.txt
endif

echo "Done."

