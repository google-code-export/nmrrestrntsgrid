#!/bin/tcsh -f

# Load common settings
source $SJ/BMRB/Matches_BMRB_PDB/scripts/settings.csh

#set stage = "remove"
set stage = "check"
######### NO CHANGES BELOW THIS LINE #############
#find /bmrb/ftp/pub/data/nmr-star -name "bmr*.str" -exec cp {} . \;

cd $SJ/quicky_unb_
set list = ( `find . -name "bmr*.str" | sort -n` )
#set list = bmr4400.str
echo "doing number of files: $#list"

if ( $stage == "remove" ) then
    foreach x ( $list )
        echo $x
        s2nmr -o $x.new remove_redundant_tags.str $x > /dev/null
        if ( $status ) then
            echo "ERROR: s2nmr failed"
        endif    
        if ( ! -e $x.new ) then
            echo "ERROR: no result file"
        endif
        if ( -z $x.new ) then
            echo "ERROR: empty result file"
        endif
        egrep -v "Could not find old tag" $x.err > $x.err.mod
        if ( ! -z $x.err.mod ) then
            echo "ERROR: bad error file"
        endif
    end
endif


if ( $stage == "check" ) then
    find . -name "bmr*.str"         | wc
    find . -name "bmr*.str.new"     | wc
    find . -name "bmr*.str.err"     | wc
    find . -name "bmr*.str.err.mod" | wc
    # count and check error sizes again.    
    find . -name "bmr*.str.err.mod" -exec ls -l {} \;     | sort -n +4 | tail
endif

if ( $stage == "rename" ) then
    foreach x ( $list )
        #echo $x
        mv $x       $x".org" 
        mv $x.new   $x
    end
endif

