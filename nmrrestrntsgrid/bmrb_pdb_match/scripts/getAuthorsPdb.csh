#!/bin/csh
# Author: Jurgen F. Doreleijers @ Fri Apr  1 15:01:48 CST 2005
# Takes less than 5 minutes for ~4500 entries.
# Will also set subl variable list.
source $SJ/BMRB/Matches_BMRB_PDB/scripts/settings.csh

set mmCifDir = $pdbbase_dir/data/structures/all/mmCIF

## No changes below this line
##############################################################################

echo "Using all PDB NMR entries to be: $#pdb_nmr_list"

\rm $pdb_authorFile 
echo "pdb_id,author_family_name" > $pdb_authorFile
foreach x ( $pdb_nmr_list ) 
    echo -n "$x "
    set mmCifFile = $mmCifDir/$x.cif.Z
    if ( ! -e $mmCifFile ) then
        echo "WARNING: mmCIF file does not exist for entry: $x"
        continue
    endif    
    gunzip -c $mmCifFile |\
        gawk -f $scripts_dir/getAuthorsPdb -v entry_id=$x >>\
        $pdb_authorFile
    ## Can't check the status of gawk when piping with gunzip
    #if ( $status ) then
    #    echo "ERROR: couldn't extract authors from mmCIF file for entry: $x"
    #    exit 1
    #endif
end    

echo "\nDone"

