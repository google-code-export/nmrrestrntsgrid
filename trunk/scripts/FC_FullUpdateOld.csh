#!/bin/csh 
# Author: Jurgen F. Doreleijers 
# Thu Jun 1 13:51:19 CDT 2006
## No changes below
# $scripts_dir/FC_FullUpdate.csh

set manualCommitDone = 0
# Remove any involved file and directory to be completely restored by CVS update. It's best to
# do this only after a manual step of adding/deleting/commiting all that was good to cvs first.
set fullUpdate  = 1
# Add the chemcomps (needed when fullUpdate  = 1)
set addChemComp = 1
# Add updates to recoord not in CVS.
set addRecoord  = 1
# No changes below this line
########################################################



echo "Clean up some"
cd $CCPNMR_TOP_DIR
echo "Removing old pyc files"
find . -name "*.pyc" -exec rm {} \;

echo "Commit some in RECOORD"
if ( ! -e $dir_python ) then
    mkdir -p $dir_python
endif

# Local things are kept local.
cp -uv $dir_python/localConstants.py           $base_dir/recoordUpdates
cp -uv $dir_python/localConstants.py           $base_dir/recoordUpdates
# Omit the CVS dir if any.
cp -uv $base_dir/Python/recoord/PDBmod/*       $base_dir/PDBmodUpdates

# todo manually.
# cvs -d :pserver:jurgen_bmrb.wisc.edu@cvsebi.ebi.ac.uk:/ebi/cvs/recoord commit -m "JFD mods" presetDict.py guessOffset.py CloneWars.py
cvs -d :pserver:jurgen_bmrb.wisc.edu@cvsebi.ebi.ac.uk:/ebi/cvs/recoord diff


echo "Clean up some"
cd $CCPNMR_TOP_DIR
if ( $fullUpdate ) then
    if ( ! $manualCommitDone ) then
        echo "ERROR: make sure to commit all that was good to cvs first"
        exit 1
    endif
    echo "WARNING: removing complete previous install"
    \rm -rf ccpn recoord
else
    echo "Removing old pyc files"
    find . -name "*.pyc" -exec rm {} \;
endif

# Update CCPN; password connect doesn't work yet automatically.
cd $CCPNMR_TOP_DIR
if ( $fullUpdate ) then
    echo "Checking out ccpn files"
    cvs -z3 -d :pserver:jurgenfd@ccpn.cvs.sourceforge.net:/cvsroot/ccpn co -r branch2 ccpn
else
    echo "Updating ccpn files"
    cvs -z3 -d :pserver:jurgenfd@ccpn.cvs.sourceforge.net:/cvsroot/ccpn update -r branch2 ccpn
endif
echo "Making Python API"
python $CCPNMR_TOP_DIR/ccpn/python/memops/scripts_v2/makePython.py

# Update RECOORD
cd $CCPNMR_TOP_DIR
if ( $fullUpdate ) then
    echo "Checking out RECOORD files"
    cvs -d :pserver:jurgen_bmrb.wisc.edu@cvsebi.ebi.ac.uk:/ebi/cvs/recoord co recoord
else
    echo "Updating RECOORD files"
    cvs -d :pserver:jurgen_bmrb.wisc.edu@cvsebi.ebi.ac.uk:/ebi/cvs/recoord update
endif 

if ( $addChemComp ) then
    echo "Add the many chemcomps too by: (takes an hour)"
    cd  $CCPNMR_TOP_DIR/ccpn/data/ccp/chemComp/other
    find $base_dir/chempCompUpdates/chemComps  -name "*.xml" -print -exec cp {} . \;
    find $base_dir/chempCompUpdates/chemComps2 -name "*.xml" -print -exec cp {} . \;
    cd $CCPNMR_TOP_DIR/ccpn/data/ccp
    \cp -rvf $base_dir/chempCompUpdates/chemCompCoord1/* chemCompCoord
endif

if ( $addRecoord ) then
    echo "Add updates to recoord not in CVS."
    cd $dir_python
    find $base_dir/recoordUpdates  -name "*.py" -print -exec cp {} . \;
    cd $CCPNMR_TOP_DIR/recoord
    if ( ! -e PDBmod ) then
        mkdir PDBmod
    endif
    \cp -v $base_dir/PDBmodUpdates/* PDBmod
    
endif    

    

