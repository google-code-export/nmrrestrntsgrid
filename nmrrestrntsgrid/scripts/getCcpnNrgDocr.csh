#!/bin/tcsh -f
# execute like:
# $scripts_dir/getCcpnNrgDocr.csh 2kqu
source $0:h/settings.csh

set inputUrlBase = http://nmr.cmbi.ru.nl/NRG-CING/data
set outputDirBase = $D/NRG-CING/recoordSync
# Then copy manually to /Users/jd/workspace35/cing/Tests/data/ccpn or so

set subl = ( 2kqu )

# Get argument pdb code if it exists.
if ( $1 != "" ) then
#    set subl = (  $1  )
    set subl = (  `echo $1 | sed 's/,/ /'g`  )
endif


echo "==>     DOING" $#subl "pdb entries"
foreach x ( $subl )
    echo "==>      DOING $x"
    set ch23 = ( `echo $x | cut -c2-3` )

	set inputUrl = $inputUrlBase/$ch23/$x/$x.tgz
	set outputDir = $outputDirBase/$x
	if ( ! -e $outputDir ) then
		mkdir -p $outputDir
	endif

	cd $outputDir

	if ( -e $x.tgz ) then
		echo "Removing entry already present: $x"
		\rm -f $x.tgz
	endif

	wget $inputUrl
    if ( $status ) then
        echo "ERROR: failed wget for $x"
        continue
    endif

	if ( 1 ) then
		cp $x.tgz $CINGROOT/Tests/data/ccpn
    endif
end

echo "==> DONE with syncing PDB files for number of entries: $#subl"

