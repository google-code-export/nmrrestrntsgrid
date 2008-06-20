#!/bin/csh -f 
# Call by:
# $scripts_dir/combineSaveFrameTypesFromMultipleEntries.csh


set resultFile = $tmp_dir/result.str
set filterFile = $scripts_dir/filter_rules_keep_only_dc_atom.str
## No changes below
##################################################

\rm -r $resultFile >& /dev/null
cd $dir_restr_unzip

set list = (`find . -name "*.str" | sort `)
echo "Doing number of entries: $#list"
wsetup
set x = 1brv_rst.str
#foreach x ( $list )
    echo $x
    # Note that the next line was modified but not checked.
    java Wattos.Star.STARFilter $x $x.tmp $filterFile
    if ( $status ) then
        echo "ERROR $x in filtering"
#        continue
    endif
    cat $x.tmp >> $resultFile
#    rm $x.tmp
#end        

