"""
File requested by Jurgen to read in NMR-STAR file and create a CCPN project.

Execute like:
python -u $dir_nrg_python/nmrrestrntsgrid/util/starToCcpn.py [in out]
"""
from ccpnmr.format.converters.NmrStarFormat import NmrStarFormat
from memops.api import Implementation
from memops.general.Io import saveProject
from nmrrestrntsgrid.settings.localConstants import ccpn_tmp_dir
import sys
import os
import shutil


#allChemCompDataPath = '/Users/wim/workspace/stable/all/data/allChemComps'
allChemCompDataPath = os.path.join(ccpn_tmp_dir, 'data/allChemComps')
fcInputDir          = os.path.join(ccpn_tmp_dir, 'data/archives/bmrb/nmrRestrGrid')

if __name__ == '__main__':
    ccpnProjectPath     = "test"
    ccpnProjectName     = '1a4d'  
    inputNmrStarFile    = os.path.join(fcInputDir, ccpnProjectName, 'joinedCoord.str')
    ccpnProjectSavePath = os.path.join(ccpnProjectPath, ccpnProjectName)

    if len(sys.argv)>1:
        inputNmrStarFile = sys.argv[1]
        ccpnProjectSavePath = sys.argv[2]
  
    # Create project
    ccpnProject = Implementation.MemopsRoot(name = ccpnProjectName)
    
    # Read NMR-STAR file
    nmrStarFormat = NmrStarFormat(ccpnProject, guiParent = None)
    entry = nmrStarFormat.readProject(inputNmrStarFile, version = '3.1', minimalPrompts = True, 
                useOriginalChainCode = True, linkAtoms = False, chemCompPath = allChemCompDataPath)
    
    # Run linkResonances
    keywds = {}    
    strucGen = entry.findFirstStructureGeneration()
    
    keywds['globalStereoAssign']    = True
    keywds['nmrConstraintStore']    = strucGen.nmrConstraintStore
    keywds['setSingleProchiral']    = True
    keywds['setSinglePossEquiv']    = True
    keywds['minimalPrompts']        = True
    keywds['useCommonNames']        = False
    keywds['useAmbiguity']          = True
    keywds['useLinkResonancePopup'] = False
    keywds['useEmptyNamingSystems'] = False
    
    nmrStarFormat.linkResonances(**keywds)
    
    # Write out the CCPN project
    # Will remove existing project!
    if os.path.exists(ccpnProjectSavePath):
      shutil.rmtree(ccpnProjectSavePath)
    
    saveProject(ccpnProject, newPath = ccpnProjectSavePath)
    