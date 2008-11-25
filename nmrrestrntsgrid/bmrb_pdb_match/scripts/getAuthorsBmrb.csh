#!/bin/csh
# Author: Jurgen F. Doreleijers @ Fri Apr  1 15:01:48 CST 2005

# Will also set subl variable list.
source $SJ/BMRB/Matches_BMRB_PDB/scripts/settings.csh
set file = "entrycitauthors.ascii.gz"

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

echo "bmrb_id,author_family_name" > $bmrb_authorFile
cat $file | \
    gawk -F'|' '{gsub(/\,/,"");printf "%s,%s\n", $2, $6}' | \
    sed -e 's/   *//g' | \
    sed -e 's/^data_//' | \
    sed -e 's/\,/ LONG_VALUE/g' |\
    sort -n |\
    sed -e 's/ LONG_VALUE/\,/g' >> \
    $bmrb_authorFile
    
# The above does respectively in words:
    # Print 2 selected columns
    # Excise large whitespace blocks
    # Excise prefix of "data_"


