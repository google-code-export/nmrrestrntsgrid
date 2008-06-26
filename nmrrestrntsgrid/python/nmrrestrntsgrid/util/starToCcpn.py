"""
File requested by Jurgen to read in NMR-STAR file and create a CCPN project.
"""

import os, shutil

from memops.api import Implementation
from ccpnmr.format.converters.NmrStarFormat import NmrStarFormat
from ccpnmr.format.process.matchResonToMolSys import matchResonToMolSys

from memops.general.Io import saveProject

if __name__ == '__main__':

  inputNmrStarFile = '/Users/wim/workspace/stable/all/data/archives/bmrb/nmrRestrGrid/1a4d/joinedCoord.str'

  ccpnProjectPath = "test"
  ccpnProjectName = '1a4d'  
  ccpnProjectSavePath = os.path.join(ccpnProjectPath,ccpnProjectName)

  allChemCompDataPath = '/Users/wim/workspace/stable/all/data/allChemComps'
  
  #
  # Create project
  #
  
  ccpnProject = Implementation.MemopsRoot(name = ccpnProjectName)
  
  #
  # Read NMR-STAR file
  #
  
  nmrStarFormat = NmrStarFormat(ccpnProject, guiParent = None)
  entry = nmrStarFormat.readProject(inputNmrStarFile, version = '3.1', minimalPrompts = True, useOriginalChainCode = True, linkAtoms = False, chemCompPath = allChemCompDataPath)

  #
  # Run linkResonances
  #   
  
  keywds = {}
  
  strucGen = entry.findFirstStructureGeneration()
  resonances = strucGen.nmrConstraintStore.sortedFixedResonances()
 
  keywds['globalStereoAssign'] = True
  keywds['nmrConstraintStore'] = strucGen.nmrConstraintStore
  keywds['setSingleProchiral']    = True
  keywds['setSinglePossEquiv']    = True
  keywds['minimalPrompts']        = True
  keywds['useCommonNames']        = False
  keywds['useAmbiguity']          = True
  keywds['useLinkResonancePopup'] = False
  keywds['useEmptyNamingSystems'] = False
  
  # Use automapping in this case
  forceChainMappings = matchResonToMolSys(resonances,ccpnProject.findFirstMolSystem(),assignFormat = 'nmrStar')

  if forceChainMappings:
    keywds['forceChainMappings'] = forceChainMappings


  nmrStarFormat.linkResonances(**keywds)
  
  #
  # Write out the CCPN project
  #
  # Will remove existing project!
  # 
  
  if os.path.exists(ccpnProjectSavePath):
    shutil.rmtree(ccpnProjectSavePath)

  saveProject(ccpnProject, newPath = ccpnProjectSavePath)
