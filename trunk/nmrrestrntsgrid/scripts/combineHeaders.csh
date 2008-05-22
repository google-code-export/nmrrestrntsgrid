#!/bin/csh -f

set resultFile = headers.str

## No changes below
##################################################

\rm -r $tmp_dir/$resultFile >& /dev/null
cd $tmp_dir_big_all
set list = (`find . -name "[1-9][0-9a-z][0-9a-z][0-9a-z]_iu.str" | sort `)
echo "Doing number of BMRB entries: $#list"
foreach x ( $list )
    echo $x
    # Note that the next line was modified but not checked.
    gawk -v str="^save_conformer_family_coord_set" -f $scriptDir/getHeader.gawk \
        $tmp_dir_big_all/$x >> $tmp_dir/$resultFile
end        

\mv $tmp_dir/$resultFile $results_dir
