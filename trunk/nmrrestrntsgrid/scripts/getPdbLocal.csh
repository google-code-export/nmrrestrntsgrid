#!/bin/tcsh -f

# For simple copy from resource that misses rsync.
# E.g.
# $UJ/wattosTestingPlatform/pdb/data/structures/divided/mmCIF/br/1brv.cif.gz
source $0:h/settings.csh


# You should CHANGE THE NEXT THREE LINES to suit your local setup
set src=/Volumes/jd/wattosTestingPlatform/pdb
set dst=/Users/jd/wattosTestingPlatform/pdb

#set subl = ( 1brv )
#set subl = (`cat /Users/jd/entry_list_97.csv`)
set subl = (`cat $list_dir/bmrbPdbEntryList.csv`)

echo "Doing" $#subl "pdb entries"
foreach x ( $subl )
#   echo "Doing $x"
   set ch23 = ( `echo $x | cut -c2-3` )
   set subdirLoc = $dst/data/structures/divided/mmCIF/$ch23
   if ( ! -e $subdirLoc ) then
        echo "Creating dir: " $subdirLoc
        mkdir -p $subdirLoc
   endif

   # skip entries already present
   if ( -e $subdirLoc/$x.cif.gz ) then
#        echo "Skipping $x"
        continue
   endif

   \cp -pa  $src/data/structures/divided/mmCIF/$ch23/$x.cif.gz \
            $dst/data/structures/divided/mmCIF/$ch23

   if ( -e $subdirLoc/$x.cif.gz && ! -e $src/data/structures/all/mmCIF/$x.cif.gz ) then
        echo "linking to all dir"
        ln -s ../../divided/mmCIF/$ch23/$x.cif.gz $src/data/structures/all/mmCIF/$x.cif.gz
   endif
end

echo "Done with syncing PDB files for number of entries: $#subl"

