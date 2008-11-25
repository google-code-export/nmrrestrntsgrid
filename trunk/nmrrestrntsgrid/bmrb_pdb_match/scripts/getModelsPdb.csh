#!/bin/tcsh -f

# Load common settings
source $SJ/BMRB/Matches_BMRB_PDB/scripts/settings.csh

# Takes 170 wall clock seconds on halbeak (Pentium(R) 4 2.66GHz)
# for 4486 entries but that's when the disk access has been partially cached
######### NO CHANGES BELOW THIS LINE #############

echo "Scanning for models"
cd $list_dir

echo "pdb_id,model_count_type" > $pdb_modelFile
foreach x ( $pdb_nmr_list )
    echo -n $x" "
    if ( ! -e  $PDB/pdb$x.ent ) then
        echo "WARNING: missing PDB file for $x"
        continue
    endif
    gawk -f $scripts_dir/getModelsPdb \
        -v entry_id=$x \
        $PDB/pdb$x.ent >> \
        $pdb_modelFile    
    if ( $status ) then
        echo "ERROR scanning the PDB file for models"
        exit 1
    endif
end    


