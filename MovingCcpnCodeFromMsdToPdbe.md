# Introduction #

This doc describes how JFD made the changes requested by WV.

# RECOORD #

  * Do a cvs update on recoord. This will generate the new pdbe dir. Move the msd localConstants.py to it parallel.
  * Now remove the msd dir and update again to check.

# CCPN #
  * Same as above but the localConstants.py is in msd/adatah

Inside Eclipse checked the consistency of the imports.

# nmrrestrntsgrid #
  * I changed several strings msd to pdbe and checked in the [revision 168](https://code.google.com/p/nmrrestrntsgrid/source/detail?r=168).
