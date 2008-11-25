#!/bin/tcsh -f

# Load common settings
source $SJ/BMRB/Matches_BMRB_PDB/scripts/settings.csh

# Takes 45 wall clock seconds on halbeak (Pentium(R) 4 2.66GHz)
# for 4486 entries but that's when the disk access has been cached
# a couple of times.

# Process the data before:
# Take out from BMRB ligand codes the invalid ones and note them:
# 5715,Ni(II)    
# 4164,Ga+3
######### NO CHANGES BELOW THIS LINE #############

echo "Scanning for het groups"
cd $list_dir

echo "pdb_id,ligand_code" > $pdb_ligandFile
foreach x ( $pdb_nmr_list )
    if ( ! -e  $PDB/pdb$x.ent ) then
        echo "WARNING: missing PDB file for $x"
        continue
    endif
    gawk -f $scripts_dir/getLigandsPdb \
        -v entry_id=$x \
        $PDB/pdb$x.ent >> \
        $pdb_ligandFile    
    if ( $status ) then
        echo "ERROR scanning the PDB header for ligands"
        exit 1
    endif
end    


