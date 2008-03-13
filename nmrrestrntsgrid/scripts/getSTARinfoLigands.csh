#!/bin/csh 
# Author: Jurgen F. Doreleijers 
# Wed Dec 14 13:49:06 CST 2005
#
# TASK: Retrieves info from star files as far as they're not in db already.
# USE:  $scripts_dir/getSTARinfo.csh
  


set run_id          = weekly20061228
set DUMP_DIR        = /var/www/servlet_data/viavia/mr_mysql_backup
set list            = ( `gawk '{print $3}'  $DUMP_DIR/entry.txt |sort` )
#set list = ( 2hgh )
#No changes below
################

if ( ! -e $results_dir/$run_id ) then
    mkdir $results_dir/$run_id
endif
cd $results_dir/$run_id
echo "Compiling results in directory: $cwd"
echo "Using entries: $#list"

echo "Getting info from STAR files"
#set termList = ( _Distance_constraint_stats_list _Stereo_assign_list _Distance_constraint_surplus _NOE_completeness_stats  )
#set fileSpecAddList = ( "_compl".str "_viol".str )

set termList            = ( _Entity.Seq            )
set colCountList        = ( 1                              25                              17                      16                      25 )
set dirSpecList         = ( $dir_link                       $dir_assign                     $dir_surplus            $dir_compl )
set fileSpecAddList     = ( "_full".str                     assignment.str                  surplus_summary.str     "_compl".str  )
set useXList            = ( 1                               0                               0                       1  )

@ count = 0
foreach t ( $termList ) 
    @ count ++
    echo "Doing term $t"
    set csvfile = $t.csv
    set colCount = $colCountList[$count]
    \rm -rf $csvfile >& /dev/null
    foreach x ( $list )
        
        set strfile = $dirSpecList[$count]/$x/$fileSpecAddList[$count]
        if ( $useXList[$count] ) then
            set strfile = $dirSpecList[$count]/$x/$x$fileSpecAddList[$count]
        endif
        
        if ( -e $strfile ) then
            egrep "_Entity.Seq " $strfile | egrep "X" | \
                gawk -v x=$x -v c=$colCount \
                '{printf("\"%s\",",x);printf("%s\n",$2)}' \
                >> $csvfile
        else 
            # echo "WARNING: no star file: $strfile"
        endif
    end
    sed 's/,\.,/,\\N,/g' $csvfile > $t"_mySqlNulls".csv
end

