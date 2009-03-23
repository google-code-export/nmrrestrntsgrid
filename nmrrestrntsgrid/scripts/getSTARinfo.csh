#!/bin/csh -f 
# Author: Jurgen F. Doreleijers 
# Wed Dec 14 13:49:06 CST 2005
#
# TASK: Retrieves info from star files as far as they're not in db already.
# USE:  $scripts_dir/getSTARinfo.csh
#       AND repeat for each term to do.  
source $0:h/settings.csh

set run_id          = weekly20070517
set DUMP_DIR        = /var/www/servlet_data/viavia/mr_mysql_backup
set list            = ( `gawk '{print $3}'  $DUMP_DIR/entry.txt |sort` )
#set list = ( 1brv )
#No changes below
################

if ( ! -e $results_dir/$run_id ) then
    mkdir $results_dir/$run_id
endif
cd $results_dir/$run_id
echo "Compiling results in directory: $cwd"
echo "Using entries: $#list"

echo "Getting info from STAR files"
set termList            = ( _Distance_constraint_stats_list _Stereo_assign_list             _Distance_constraint_surplus    _NOE_completeness_stats     )
set colCountList        = ( 12                              25                              17                              25                          )
set dirSpecList         = ( $dir_viol                       $dir_assign                     $dir_surplus                    $dir_compl                  )
set fileSpecAddList     = ( "_viol".str                     assignment.str                  surplus_summary.str             "_compl".str                )
set useXList            = ( 1                               0                               0                               1                           )

echo "Doing termList $termList"
@ count = 0
foreach t ( $termList ) 
#set t = _NOE_completeness_stats
#set count = 4
    @ count ++
    echo "Doing term $t"
    set csvfile = $t.csv
    set colCount = $colCountList[$count]
    \rm -rf $csvfile >& /dev/null
    foreach x ( $list )
        
        set strfile =     $dirSpecList[$count]/$x/$fileSpecAddList[$count]
        if ( $useXList[$count] ) then
            set strfile = $dirSpecList[$count]/$x/$x$fileSpecAddList[$count]
        endif
        
        if ( -e $strfile ) then
            egrep "^ *$t.* *" $strfile | \
                gawk -v x=$x -v c=$colCount \
                '{i=0;printf("\"%s\",",x);while(i<c){printf("%s,",$2);i++;getline};printf"\n"}' \
                >> $csvfile
        else 
            echo "WARNING: no star file: $strfile"
        endif
    end
    sed 's/,\.,/,\\N,/g' $csvfile > $t"_mySqlNulls".csv
end

exit 0

# Get molecular types.
set csvfile = molTypes.csv
\rm -rf $csvfile >& /dev/null
foreach x ( $list )
    set strfile = $dirSpecList[$count]/$x/$fileSpecAddList[$count]
    if ( $useXList[$count] ) then
        set strfile = $dirSpecList[$count]/$x/$x$fileSpecAddList[$count]
    endif
    
    if ( -e $strfile ) then
        egrep "^ *$t.* *" $strfile | \
            gawk -v x=$x -v c=$colCount \
            '{i=0;printf("\"%s\",",x);while(i<c){printf("%s,",$2);i++;getline};printf"\n"}' \
            >> $csvfile
    else 
        # echo "WARNING: no star file: $strfile"
    endif
end
sed 's/,\.,/,\\N,/g' $csvfile > $t"_mySqlNulls".csv
_Entity.Pol_type     polyribonucleotide


