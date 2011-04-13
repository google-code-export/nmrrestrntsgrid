#!/bin/tcsh -f
# execute like:
# $scripts_dir/getCcpnNrgDocr.csh 2kqu
source $0:h/settings.csh

#set inputUrlBase = http://nmr.cmbi.ru.nl/NRG-CING/input
set inputUrlBase = http://nmr.cmbi.ru.nl/NRG-CING/recoordSync
set outputDirBase = $D/NRG-CING/recoordSync
# Then copy manually to /Users/jd/workspace35/cing/Tests/data/ccpn or so

set subl = ( 1a4d 1a24 1afp 1ai0 1b4y 1brv 1bus 1c2n 1cjg 1d3z 1hkt 1hue 1ieh 1iv6 1jwe 1kr8 1otz 1v0e 2cka 2fws 2hgh 2jmx 2k0e 2kib 2kz0 2rop )

# Get argument pdb code if it exists.
if ( $1 != "" ) then
#    set subl = (  $1  )
    set subl = (  `echo $1 | sed 's/,/ /'g`  )
endif


echo "==>     DOING" $#subl "pdb entries"
foreach x ( $subl )
    echo "==>      DOING $x"
    set ch23 = ( `echo $x | cut -c2-3` )

    # set inputUrl = $inputUrlBase/$ch23/$x.tgz # in case of input dir
    set inputUrl = $inputUrlBase/$x/$x.tgz # on recoordSync
    set outputDir = $outputDirBase/$x
    if ( ! -e $outputDir ) then
        mkdir -p $outputDir
    endif

    cd $outputDir

    if ( -e $x.tgz ) then
        echo "Removing entry already present: $x"
        \rm -f $x.tgz
    endif

    wget --quiet $inputUrl
    if ( $status || ! -e $x.tgz  ) then
        echo "WARNING: not retrieved $x.tgz "
    endif


    if ( 0 ) then # DEFAULT: 0
        cp $x.tgz $CINGROOT/Tests/data/ccpn
    endif
end

echo "==> DONE with syncing PDB files for number of entries: $#subl"

