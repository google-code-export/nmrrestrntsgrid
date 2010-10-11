#!/bin/tcsh -f
# Author: Thomas Solomon
# Date:   November 1, 2002
# Updated by Kenneth J. Addess Jan 29,2004
# Updated by Chen, L. Nov 10, 2006
# Updated by Jurgen Doreleijers Thu Mar  5 10:30:45 CET 2009

source $0:h/settings.csh

set MIRRORDIR=$pdbbase_dir                         # your top level rsync directory
set RSYNC=rsync                                    # location of local rsync

set SERVER=rsync.wwpdb.org::ftp/
set PORT=33444
set USER_ID=anonymous
#set PASSWORD_FILE=$nrg_dir/passwordFilePdb.txt

#set subl = (`cat $list_dir/list_baddies_2009-01-20.csv`)
set subl = ( 1a4d 1a24 1afp 1ai0 1b4y 1brv 1bus 1cjg 1d3z 1hkt 1hue 1ieh 1iv6 1jwe 1kr8 2hgh 2k0e )

# Get argument pdb code if it exists.
if ( $1 != "" ) then
    set subl = (  `echo $1 | sed 's/,/ /g'`  )
endif


echo "Doing" $#subl "pdb entries"
foreach x ( $subl )
   echo "Doing $x"
   set ch23 = ( `echo $x | cut -c2-3` )
   set subdirLoc = $MIRRORDIR/data/structures/divided/mmCIF/$ch23
   if ( ! -e $subdirLoc ) then
        echo "Creating dir: " $subdirLoc
        mkdir -p $subdirLoc
   endif

    set localFile = $subdirLoc/$x.cif.gz
    if ( -e $localFile ) then
        continue
        #rm $localFile
    endif

   $RSYNC -rlpt -z --delete --port=$PORT \
#    --password-file=$PASSWORD_FILE \
    $USER_ID@$SERVER/data/structures/divided/mmCIF/$ch23/$x.cif.gz $localFile
end

echo "Done with syncing PDB mmCIF files for number of entries: $#subl"

