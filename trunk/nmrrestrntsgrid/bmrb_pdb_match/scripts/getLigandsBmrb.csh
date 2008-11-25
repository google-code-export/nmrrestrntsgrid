#!/bin/csh
# Author: Jurgen F. Doreleijers @ Fri Apr  1 15:01:48 CST 2005

# Will also set subl variable list.
source $SJ/BMRB/Matches_BMRB_PDB/scripts/settings.csh
set file = "ligand.ascii.gz"

## No changes below this line
##############################################################################
cd $list_dir

wget -q "$bmrb_export_db_url/$file" 
if ( ! -e $file ) then
    echo "ERROR: couldn't get file: $file"
    echo "ERROR: from url dir: $bmrb_export_db_url"
    exit 1
endif

gunzip -f $file
set file = $file:r

echo "bmrb_id,ligand_code" > $bmrb_ligandFile
cat $file | \
    gawk -F'|' '/^[0-9]+\|data_/{printf "%s,%s\n", $2, $11}' | \
    sed -e 's/?//g' | \
    sed -e 's/   *//g' | \
    sed -e 's/,$/,?/g' | \
    sed -e 's/^data_//' | \
    sed -e 's/\,/ LONG_VALUE/g' |\
    sort -n |\
    sed -e 's/ LONG_VALUE/\,/g' >> \
    $bmrb_ligandFile
# The above does respectively in words:
    # Print 2 selected columns
    # Excise any ? 
    # Excise large whitespace blocks
    # Make lack of code but not lack of ligand evident by replacing empty value by a ?
    # Excise prefix of "data_"
    
    
    

