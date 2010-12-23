#!/bin/tcsh -f

source $0:h/settings.csh

set useVersion = "2" # DEFAULT 2. Switch to 3 in future.
set base_url = 'http://rest.bmrb.wisc.edu/bmrb/NMR-STAR2'
set target_dir = $bmrb_dir/2.1.1
if ( $useVersion == "3" ) then
    set target_dir = $bmrb_dir/3.0.8.34
    set base_url = 'http://www.bmrb.wisc.edu/ftp/pub/bmrb/entry_directories'
endif

set wgetLogFile     = "getBmrb_wget".log

set subl = ( 4020 4046 4047 4969 5317 7009 15072 20074 16995 11041 4046 5577 5576 5762 5801 5808 4491 5131 6113 7009 7008 15381 )
#set subl = ( `cat $CINGROOT/data/NRG/bmrbPdbMatch/bmrb.csv| gawk '{if (NR!=1) print}'` )

# Get argument bmrb code if it exists.
if ( $1 != "" ) then
    set subl = (  `echo $1 | sed 's/,/ /g'`  )
endif

echo "Doing" $#subl "bmrb entries"
foreach x ( $subl )
   echo "Doing $x"
   set digits12 = ( `echo $x | gawk '{ a = $1; printf "%02d\n", a%100}' `)
   set hashDir = $target_dir/$digits12
   if ( ! -e $hashDir ) then
        mkdir -p $hashDir
   endif

   set query = $base_url/$x
   if ( $useVersion == "3" ) then
       set query = $base_url/bmr$x/bmr$x"_3.str"
   endif

   set targetFile = $hashDir/"bmr$x.str"

   if ( -e $targetFile ) then
          echo "Skipping entry already present: $x"
          continue
   endif

    wget -v -o $wgetLogFile -O $targetFile "$query"
    if ( $status ) then
        echo "ERROR: failed to wget from url: $query"
#        exit 1
    endif
    if ( ! -e $targetFile ) then
        echo "ERROR: failed to find target file: $targetFile"
#        exit 1
    endif

    sleep 5
end

echo "Done with retrieving the BMRB entry"
