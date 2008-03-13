wsetup

/big/jurgen/RECOORD_NA/perEntry/1b4y

lns -s .
gawk -f $WATTOSSCRIPTSDIR/convert_star2pdb nonredun.str nonredun.pdb
splitpdb modelnum=1 nonredun.pdb  

# Next command doesn't give output when successfull.
# Creates nonredun_001.psf
pdb2psf nonredun_001.pdb


