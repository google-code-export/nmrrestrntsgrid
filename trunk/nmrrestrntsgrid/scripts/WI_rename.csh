#!/bin/csh 
# Author: Jurgen F. Doreleijers @ Wed Feb 23 15:59:44 CST 2000
#
# TASK: enabling multiple models/files
# USE:  WI_rename.csh t|f t|f t|f xxxx.pdb
# EXAMPLE: WI_rename.csh t t t ../PDB/1brv.pdb
# ARGUMENTS:
#   do_logs
#   add_protons
#   do_write
#   pdb file name with directory
#
# NOTES:- pdb file can be specified with path name but the output files
#         are (over)written in the current working directory.
#       - assumes whatif is installed and the topology file location, defined
#         below, exists.
# OPTIONS
#       - see usage echoed when no arguments are given.
#
# Define the paths to the following programs:  
# joinpdb.
# The topology file to be used. Normally AND according to documentation at:
# http://swift.cmbi.kun.nl/whatif/chap07.html the extension of this file
# has to be FIL. 
#set topology_file = $BJ/WHATIF/run/TOPOLOGY.H
set topology_file = /home/vriend/whatif/dbdata/TOPOLOGY.H
# No need to change things below this line
###############################################################################


if ($#argv != 4 ) then
 goto usage
endif

# change the variable do_logs to f to get no logs.
set do_logs     = $1

# do we need atoms added? Set it to anything else than t to not add them.
set add_atoms   = $2

# do we need a pdb output file?
set do_write    = $3

# input file
set input_file  = $4

# do_logs
if ( !(( $do_logs == "t" ) || ( $do_logs == "f") ) ) then
 goto usage
endif

# add_protons
if ( !(( $add_atoms == "t" ) || ( $add_atoms == "f") ) ) then
 goto usage
endif

#do_write
if ( !(( $do_write == "t" ) || ( $do_write == "f") ) ) then
 goto usage
endif


set out = whatif.script
# Get the bare entry code for the pdb file.
set x   = $input_file:t:gr
set ext = $input_file:e

# Get the directory the pdb file is in.
set dir = $input_file:h
    
# Zip it where equal
if ( "$dir" == "$input_file" ) then
 set dir = ""
endif

set log_file = $x"_wi".log
# Delete the log file
if ( -e $log_file ) then
  \rm -f $log_file
endif

# Get a copy of a proton topology file
ln -f -s $topology_file TOPOLOGY.H

# Delete the wi script file
if ( -e $out ) then
  \rm -f $out
endif

# Check if input file exists
if ( ! -e $input_file ) then
 echo "ERROR: Aborting, file does not exist: $input_file"
 exit(2)
endif

echo "Trying to separate models from the PDB file"
splitpdb $input_file > /dev/null
set NOSPLIT = $status

# How many models are we handeling
if ( $NOSPLIT ) then
    # Single file
    
    # Is the file local already
    if ( $dir == "" ) then
    # Yes, local
       set was_copy = "f"
    else
    # No, not local
       if ( -e $x.$ext ) then
#         echo "the found dir is: $dir"
         echo "ERROR: Please delete local file $x.$ext first"
         exit(3)
       endif
#       echo "Make a temporary local copy of $x.$ext"
       set was_copy = "t"
       ln -s $input_file $x.$ext
    endif
    
    set list = $x.$ext
else
    # Multiple file
    set list = ( `\ls $x"_"[0-9][0-9][0-9].$ext` )

    if ( ! $#list ) then
      echo "ERROR: No pdb files anyway (1)"
      exit (4)
    endif
endif


if ( ! $#list ) then
  echo "ERROR No: pdb files anyway (2)"
  exit (5)
endif

set number_models = $#list

echo "Will transform $#list model(s)"

foreach pdb_file ( $list )
#   echo "WHAT IF will process PDB file " $pdb_file

   set z = $pdb_file:t:gr
   set outputPDBFile = $z"_wi".$ext
   
   # Removing files so WI will not ask for confirmation
   set delete_list = $z"_wi.$ext"
   
   if ( $do_logs == "t" ) then
     set delete_list = ( $delete_list $z.namchk.log $z.lista.log )
   endif

   foreach file ( $delete_list )
     if ( -e $file ) then
      echo "Deleting file: $file"
      \rm $file
     endif
   end

   # Generate WI script

   # Set WI options
   cat >> $out << EOD
# Truncating errors in a PDBOUT table                        
SETWIF 593 100                                               
# Should Q atoms be considered hydrogen atoms?               
SETWIF 1505 1                                                
# Read all models                                            
#SETWIF 847 1                                                 
# Not adding C-terminal O if missing                         
SETWIF 1071 1                                                
# We have an NMR structure (curiously set to No here)        
SETWIF 1503 0                                                
# IUPAC atom nomenclature                                    
SETWIF 142 1                                                 
# Cutoff for reporting in the INP* routines (*100)           
SETWIF 143 400
# General debug flag 
# Should prevent problems such as:
# > 1b9q and many others: broken backbone/ERROR reading DSSP file
# > 1ehj Zero length in torsion calculation                                               
SETWIF 1012 0
# default is 25; threshold *100 for JURRES
SETWIF 1306 9999
# Read the one model
getmol
$pdb_file
xxx
EOD

   ## Add hydrogens if missing
   if ( $add_atoms == "t" ) then
        cat >> $out << EOD
# Round the coordinates to 0.001 as in PDB files and correct any atom names again.
%ROUNDC        
#Save hydrogens that WI thinks are ok
JURSAV
# Deleting hydrogens
#%DELHYD TOT 0
# Correcting atoms without moving unaffected.
%CORALL NO
# Adding hydrogens
%ADDHYD TOT 0
# Next line not needed anymore...
#N
# Round the coordinates to 0.001 as in PDB files and correct any atom names again.
%ROUNDC        
#Restore the saved hydrogens that WI thought were ok. 
#The option will overwrite any existing hydrogens with the exact same IUPAC corrected name.
#setwif 1306 25 is standard for 0.25 Angstrom within which JURRES sill overwrite.
# when set to very large number: 999 it will overwrite all. 
JURRES
EOD
   endif
   
   # Start a log file for the name checking routine
   if ( $do_logs == "t" ) then
     echo "dolog"                                                      >> $out
     echo "$z.namchk.log"                                              >> $out
     echo "name check of $pdb_file"                                    >> $out
     echo "0"                                                          >> $out
     echo "time"                                                       >> $out
   endif

   # Do the actual name check
   echo "%namchk"                                                      >> $out
   # Finish the log file

   if ( $do_logs == "t" ) then
     echo "nolog"                                                      >> $out
   endif

   echo ""                                                             >> $out

   # Write the new PDB file
   if ( $do_write == "t" ) then
        cat >> $out << EOD
%makmol

$outputPDBFile
tot
0

EOD
   endif
   
   # Start a log file for the lista output
   if ( $do_logs == "t" ) then
        cat >> $out << EOD
dolog
$z.lista.log
lista of $pdb_file
0
time
lista all
nolog
EOD
   endif

   # Initialize the soup
   echo "%inisou"                                                      >> $out
   echo ""                                                             >> $out
   
end

echo "fullstop y"                                                      >> $out

# Run whatif with the script
$DIR_WHATIF/DO_WHATIF.COM script $out > $log_file


# Delete some junk
#\rm check.db pdbout.txt pdbout.tex WHATIF.FIG TOPOLOGY.FIL $out >& /dev/null

# Join the resulting pdb files to xxxx_wi.pdb
if ( $NOSPLIT ) then
  if ( $was_copy == "t" ) then  
#     echo "Removing local copy of the file $x.pdb"
     \rm -f $x.$ext
  endif
else
  # Delete the original list of files splitted
  \rm -f $list

   if ( $do_write == "t" ) then
      # Get the new list of files generated.
      set list = ( `\ls $x"_"[0-9][0-9][0-9]"_wi".$ext` )

      if ( ! $#list ) then
        echo "ERROR: No resulting pdb files anyway"
        exit (6)
      endif

      if ( $#list != $number_models ) then
        echo "ERROR: different number of resulting pdb files $#list was $number_models"
        exit (7)
      endif

      echo "Concatenating the individual models"
      joinpdb -o $x"_wi".$ext $list > /dev/null

      # Delete the new list of files generated
      \rm -f $list
   endif
   
endif

# Join the resulting namchk and lista log files
if ( $do_logs == "t" ) then
    cat $x*.lista.log  > $x"_all_lista".log
    cat $x*.namchk.log > $x"_all_namchk".log
    \rm -f $x*.lista.log $x*.namchk.log
endif

#\rm -f $out
#\rm -f PDBFILE* ALTERR.LOG check.db pdbout.t* WHATIF.FIG $out >& /dev/null
 
exit(0)



#####################
# usage block
#####################
usage:
    echo 'Usage: WI_rename.csh t|f t|f t|f pdb_file'
    echo ""
    echo "ERROR: Please supply three arguments;"
    echo "1) t or f for writting a log file"
    echo "2) t or f for adding missing protons"
    echo "3) t or f for writting a pdb file"
    echo "3) the pdb file name with or without path"
    exit (1)
    
    
#### JUNK
WHAT IF
WHAT IF nomenclature corrected on host: `hostname` by user: `whoami`
WHAT IF protons added true or false: $add_atoms
WHAT IF
0


