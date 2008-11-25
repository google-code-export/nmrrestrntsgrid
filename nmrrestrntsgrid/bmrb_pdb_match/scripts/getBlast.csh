#!/bin/tcsh -f

# Load common settings
source $SJ/BMRB/Matches_BMRB_PDB/scripts/settings.csh

#set blast_bin_dir = /mnt/big/condor/blastio/processed/weekly_bak_tmp_2005-04-28
set blast_bin_dir = /mnt/big/condor/blastio/processed/weekly

######### NO CHANGES BELOW THIS LINE #############

echo "Finding blast bmrb versus pdb csv files."
set list = (`find $blast_bin_dir/pdb -name "bmrb*.csv"`)
echo "Found $#list files"

if ( $#list == 0 ) then
    echo "ERROR: expected at least 1 bmrb file in $blast_bin_dir/pdb"
    exit 1
endif

#s := start of matching region
#n := end of query sequence; length of sequence
#q := number of residues in the gaps combined
#t := end of matching region ( s + m - q - 1 ) 
#r := number of X residues in matching region combined
#m := size of matching region including gaps
#i := number of identical residues in matching region
#The minimal necessary set of elements to scoring are: s, n, q, r, m, and i.

echo -n "bmrb_id,query_orf_subid,pdb_id,subject_orf_subid," > $blastFile
echo    "match_size,number_gaps,number_identities,query_orf_match_start" >> $blastFile

# testing:
#echo -n "4020,,1brv,," >> $blastFile
#echo    "32,32,32" >> $blastFile

echo "Combining a list of PDB NMR entries used for pre-filtering blast results"

echo $pdb_nmr_list | sed 's/ /\,/g' > $tmp_dir/nmr_entries.txt
# make sure to remove any values with " in them. Upsets the java csv parser.
foreach f ($list)
    echo "ripping $f"
    cat $f | \
        gawk -F',' -f $scripts_dir/getBlast -v file=$tmp_dir/nmr_entries.txt | \
        egrep -v '"'  >> \
        $blastFile
    if ( $status ) then
        echo "ERROR: couldn't transform file: " $f
        exit 1
    endif
end
