# Introduction #

The installation on grunt is now maintained by Chris. $WS points to the workspace. The projects are named ccpn and recoord.

# How to #

  * complete refresh of the recoord archive
```
    cd $WS
    cvs -z3 -d :pserver:jurgen_bmrb.wisc.edu@cvsebi.ebi.ac.uk:/ebi/cvs/recoord checkout recoord    
    # or just update:
    cd $WS
    cvs update recoord
    There is a problem with using absolute paths in the cvs update command.
```
Then, also localize with a file: /big/docr/workspace/recoord/python/msd/adatah/localConstants.py containing:
```
http://nmrrestrntsgrid.googlecode.com/files/localConstants.py
```


  * Complete refresh of the ccpn sourceforge svn archive
```
    # Goto the workspace
    cd $WS
    # Remove any previous install if needed.
    \rm -r ccpn
    # Only login once this info will be saved. Need to have developer access otherwise syncing is delayed a lot. How to do this is described best at the sf.net site. You need to setup shared keys.
    # Check out stable reversion:
    svn checkout https://ccpn.svn.sourceforge.net/svnroot/ccpn/branches/stable/ccpn -r HEAD --depth=infinity --force
    Then link in the chem comps:
    cd ccpn
    ln -s /big/docr/ccpn-chemcomp .

    # If you only need to update you can do:
    svn update $WS/ccpn
    # At the time of writing it returns a message: 'At revision 5977'
```

  * regenerate the ccpn data model in/by python:
```
    python -u $CCPNMR_TOP_DIR/python/memops/scripts_v2/makePython.py
```


  * get info from NMR Restraints Grid for running FC on for example 1brv.
```
    set x = 1brv
    #python -u $WS/recoordD/python/recoord2/msd/getAllInfo.py $x -force 
    # not using recoordD anymore
    python -u $WS/recoord/python/recoord2/msd/getAllInfo.py $x -force 
    This will put the data in: .../data/archives
        bmrb/nmrRestrGrid/1brv and
        pdb
```

  * run FC:
```
    #python -u $WS/recoordD/python/recoord2/msd/linkNmrStarData.py $x -noGui -force -raise
    python -u $WS/recoord/python/recoord2/msd/linkNmrStarData.py $x -noGui -force -raise
```
> > This will put data in: .../data/recoord/$x

  * run FC on the above for export to CYANA.
```
    #python -u $WS/recoordD/python/recoord2/bmrb/export2Cyana.py $x -noGui -force -raise
   # python -u $WS/recoord/python/recoord2/bmrb/export2Cyana.py $x -noGui -force -raise - outdated
    python -u $WS/recoord/python/recoord2/msd/exportCyana.py $x in_directory out_directory  
```
> > This will put data in: .../data/recoord/$x

  * document:
```
python $CCPNMR_TOP_DIR/python/ccpnmr/format/help/createLinkResonancesParametersDoc.py
python $CCPNMR_TOP_DIR/python/ccpnmr/format/help/createFormatConverterParametersDoc.py
```