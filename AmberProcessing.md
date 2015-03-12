# Introduction #

Amber coordinate files are needed for the order of the atoms in there determines the number of the atoms in the restraint lists in Amber.

# Details #

  * Get original Amber coordinate file from author.
  * Truncate to have just one model in this file. Everything from the line MODEL 2 goes.
  * Place this copy as $x.pdb ($x is the entry id in lower case; e.g. 1brv) in the directory the mrannotator will look for it. It's specified by the variable amber\_pdb\_dir and currently is: amber\_pdb\_dir                  :
/dumpzone/pdb\_external/amber\_pdb (on tang)
  * Perhaps remove spurious water like in 2l8m