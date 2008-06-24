#!/bin/csh -f 
# Author: Jurgen F. Doreleijers 
# Fri Jun  2 14:37:52 CDT 2006
# Script for guessing offset between seqres and restraint file.
# Use: set x=6i1b; $scripts_dir/guessOffSet.csh $x

  # Put this logic in guessOffset.py callable by guessOffSet.csh.
  # It's a semi-automatic way of doing things but much faster
  # than counting all by a human.
  # Todo:- add NAs (more characteristic cs atoms)
  #      - enable multiple models.
  #      - fix suspected gross errors for entry 1zs5
set atom_file   = atoms_tmp.txt
set seqres_file = seqres_tmp.txt
set res_file    = res_tmp.txt

###################################################################
## No changes below

# Get argument pdb code if it exists.
if ( $1 != "" ) then
    set x = (  $1  )
else 
    echo "ERROR: need to give entry code"    
endif

cd $dir_link/$x
egrep "^SEQRES" $x.pdb > $seqres_file
# First strip the quotes off any value, assuming this will not change the column count.
# Then uppercase all
sed 's/\. *\"\(.*\)\"/\. \1/g' restraints.star |\
    gawk '/_Dist_constraint.Auth_atom_ID/{f=1;next}/stop_/{f=0}{if(f==1 && (NF>4))printf ("%-4s %10s %5s %-5s\n", $(NF-3), $(NF-2), $(NF-1), $(NF))}'|\
    sort -u | sort -n -k 1.1 -k 2.2 > $atom_file
# todo; add the atoms from the dihedral and rdc restraints.
#gawk '/_Torsion_angle_constraint.Constraints_ID/{f=1;next}/stop_/{f=0}{if(f==1 && (NF>4))printf ("%-4s %10s %5s %-5s\n", $(NF-3), $(NF-2), $(NF-1), $(NF))}' \
#    restraints.star | sort -u > $atom_file

python $R/python/guessOffset.py $seqres_file $atom_file 

echo "Start guessing."



