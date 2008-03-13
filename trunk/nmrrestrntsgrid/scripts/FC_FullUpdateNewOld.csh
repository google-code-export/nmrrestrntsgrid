Tot nu toe gedaan:

# As wim:
[wim@tang ~/ccpn]$ pwd
/share2/wim/ccpn
[wim@tang ~/ccpn]$ chmod -R g+wrx *

# As jurgen:
/~/ source /Users/jd/CloneWars/DOCR1000/scripts/settings.csh
/~/ echo $base_dir/
/Users/jd/CloneWars/DOCR1000/
/~/ echo $CCPNMR_TOP_DIR
/share2/wim/ccpn/all
/~/ cd  $CCPNMR_TOP_DIR/data/ccp/chemComp/other

/~/ find $base_dir/chempCompUpdates/chemComps  -name "*.xml" -print -exec ln -sf {} . \;
/~/ find $base_dir/chempCompUpdates/chemComps2 -name "*.xml" -print -exec ln -sf {} . \;
/~/ cd $CCPNMR_TOP_DIR/data/ccp
/~/ \cp -rvf $base_dir/chempCompUpdates/chemCompCoord1/* chemCompCoord
/~/ echo $dir_python
/share2/wim/ccpn/all/python/recoord
/~/ cd $dir_python
/recoord/ find $base_dir/recoordUpdates  -name "*.py" -print -exec cp {} . \;
/Users/jd/CloneWars/DOCR1000/recoordUpdates/mergeStarFilesTest.py
/Users/jd/CloneWars/DOCR1000/recoordUpdates/localConstants.py

# FC starts up nicely.
/recoord/ alias fc 'python $CCPNMR_TOP_DIR/python/ccpnmr/format/gui/FormatConverter.py'
/recoord/ fc

