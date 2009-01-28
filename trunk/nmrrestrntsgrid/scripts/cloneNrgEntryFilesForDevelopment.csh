#!/bin/tcsh -f

############################################################################
#
# Gets all the entry files needed locally to develop with.
# 
############################################################################

# USE:  cloneNrgEntryFilesForDevelopment.csh [1brv]

#OR: set x = 1ai0  ; $scripts_dir/cloneNrgEntryFilesForDevelopment.csh $x  


#set subl = (  1j6t 1j6y 1jtw 1k1c 1kb7 1la8 1lae 1lfu 1m3v 1m8l 1m39 1mhi 1mhj 1mit 1mvg 1mvz 1naj 1nao 1nil 1nk2 1odp 1odq 1odr 1oef 1oeg 1omt 1omu 1op1 1opp 1p5o 1p6r 1p7e 1p7f 1pan 1peh 1pei )
set subl = (`cat $list_dir/list_baddies_2009-01-20.csv`)

# Get argument pdb code if it exists.
if ( $1 != "" ) then    
    set subl = (  `echo $1 | sed 's/,/ /'`  )
endif
cd $scripts_dir

echo "Getting all entry files for " $#subl "pdb entries"
foreach x ( $subl )
    echo "Doing $x"
    getMr.csh $x
    getMrAnnotated.csh $x
    getMmCif.csh $x
end

