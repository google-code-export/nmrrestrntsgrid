"""
Presetdict: contains presets for entries to make them run automatically
Explanations (below the entry code layer!!):
------------
  'duplicateResonances': {'x': ['A','B']}, # Keywords for duplicating restraints from chain x to chains a and b.
  'linkResonances': {
    'keywds': {	                 # Keywords send to linkResonances script
      'forceChainMappings': [[' ',' ',1,0]],   # Chain mapping: [chainCode, formatChainCode, firstSeqId, offset]                	            
      'forceDefaultChainMapping': 1,  # Use if default chain mapping is correct
                                      # Only works if one CCPN chain, one format chain present!
      'useLinkResonancePopup': 0,     # Use if you do not want the resonance-atom popups to show up                	
      'useIupacMatching': 1           # Use if you want to match to IUPAC names (CAREFUL: only use if certain that no overlap occurs)
      'specificResNameMappings': ' .119.ZN': ' .200.ZN' # see entry 2ffw
      },                	                   
    'run': 2                          # Use to run linkResonances multiple times
    }
"""

moreHelp1="""
More help from code: ccpnmr\format\converters\DataFormat.py  #IOkeywords

Directly pasted from code: ccpnmr\format\process\linkResonances.py #run

    globalStereoAssign   0    (default) Do not assume anything about stereospecific assignment 
                         1    Assume that all prochiral atoms have been stereospecifically
                              assigned.
	         
    setSingleProchiral   None  (default) Do not assume anything on the status of single
                               prochiral atoms (e.g. ASP HB2, but no info on HB3)
                   	     0     Assume that for single prochiral atoms the other prochiral
                   	           atom carries exactly the same information
                   	     1     Assume that for single prochiral atoms the other prochiral
                   	           atom is not known - information is not copied
	         
    setSinglePossEquiv   None  (default) Do not assume anything on the status of single
                               possibly equivalent atoms (e.g. PHE HD1, but no info on HD2)
                   	     0     Assume that for single possibly equivalent atoms the other
                   	           atom is equivalent
                   	     1     Assume that for single possibly equivalent atoms the other
                   	           atom is not equivalent
    
    useCommonNames       0      (default) Do not use 'common names' information
                         1      Translate 'common names' information; this will translate
                   	            commonly mistyped atom names using their expected meaning
                         -1     Ignore 'common names'; this will not link any
                   	            atoms listed as common names.
    
    useAmbiguity         0      (default) Do not use ambiguity name information
                         1      Translate ambiguous names; this will translate ambiguous
                   	            atom names (e.g. HG* for THR) using their expected meaning
                         -1     Ignore ambiguous names; this will not link any
	                               atoms listed as common names.
    
    useIupacMatching     0      (default) Do not use IUPAC names for mapping in addition
                                to selected naming system
                         1      Use IUPAC names for mapping: if no match is found using
	                               the selected naming system the IUPAC names will be tried,
	                               but ONLY if there is no chemAtomSet for the match found
	                               (this is to avoid problem with HB2/HB3 type mapping).
                         2      Use IUPAC names for mapping: if no match is found using
	                               the selected naming system the IUPAC names will be tried,
	                               and will always be applied if a match found.
    
    useLinkResonancePopup   1   (default) If no match was found, ask which atom(s) the
                                resonance corresponds to
	                           0   Do not try to match resonances to atoms if no match was found
         
    forceShiftMerge         0   (default) Uses interaction to determine which chemical
                                shift value is correct when ambiguous.
                            1   Will automatically merge ambiguous shift values.
    
    fixSingleAtoms          0   Will not try to find out if an unrecognized atom set (e.g. HG# for LEU)
                                is available as single atom (HG in this case)
                            1   (default) Will reset unrecognized atom sets to single atom if relevant (e.g. HG# to HG for LEU)
    
    Advanced keyword use (for full automation only - use with care):
    
    forceChainMappings          Default None. Can be set to a Python dictionary so that
                                chains are mapped automatically.
    
    forceDefaultChainMapping    Default None. Can be set to 1 to use the default chain
                                mapping (works only for 1 CCPN chain, 1 format chain)
    
    addNameMappings             Default None. Can be set to a dictionary so that some
                                atom names will be mapped automatically (similar to
	                               useAmbiguity or useCommonNames set to 1)
             
    specificResNameMappings     Default None. Can be set to a dictionary so that resNames
                                are automatically changed (e.g. ' .1.H' to ' .1.HN')
    
    formatChainCodes            Default None. Can be set to a dictionary
                                to copy/change the original format chain code
	                               to new/existing chain codes (can be necessary for multimers, ...)
    
    useResLinkMapping           Default 1. Set to 0 if stored resonance link mappings should
                                not be used.
    
    useSingleProchiralMapping   Default 0. Set to 1 if stored single prochiral atom
                                settings should not be used.
    
    useSinglePossEquivMapping   Default 0. Set to 1 if stored single possible equivalent atom
                                settings should not be used.
                                
    autoConnectStereo           Default 1. Set to 0 if unlinked ambiguous resonances should not
                                be automatically connected based on atom names to existing stereospecific
                                resonances.
"""


presetDict = {

#
# Monomers
#

'1a6x': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1a57': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ah9': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1aj3': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1apq': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1b1v': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1bu9': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1bvm': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1b75': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ba4': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1b22': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },


'1b64': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1bbn': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1bct': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1bjb': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1bcn': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1beg': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1bjx': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1bla': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1blr': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1blj': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1bsh': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ckv': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ckw': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'ILE': [['HB*','HB'],['HD*','HD1*'],['HD','HD1*']]} 
      }
    }
  },

'1cej': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1cky': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ckz': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ck7': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1cmf': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1cmg': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1cmz': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1afi': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ',' ',1,0],[' ','MER',2,0]]
      }
    }
  },

'1ajw': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ak6': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ',' ',2,0]],
      'addNameMappings':  {'ILE': [['HD#','HD1*']]} 
      }
    }
  },

'1ak7': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ',' ',2,0]],
      'addNameMappings':  {'ILE': [['HD#','HD1*']]}
      }
    }
  },

'1b2t': {
    
  'linkResonances': {
    'keywds': {
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2
      }
    }
  },

'1bf0': {
    
  'linkResonances': {
    'keywds': {
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2
      }
    }
  },

'1bf9': {
    
  'linkResonances': {
    'keywds': {
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2
      }
    }
  },

'1bgk': {
    
  'linkResonances': {
    'keywds': {
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2
      }
    }
  },

'1b4r': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,7]],
      'specificResNameMappings': {' .8.HN': ' .8.HT*'}
      }
    }
  },

'1bfi': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1bh4': {

  'linkResonances': {
   'keywds': {
      'forceChainMappings': [[' ',' ',1,-3]]
      }
    }
  },
  
'1bqz': {
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {
          'ALA': [['HB\#','HB*']],
          'ARG': [['HB\#','HB*'],['HG\#','HG*'],['HD\#','HD*']],
          'ASN': [['HD2\#','HD2*']],
          'ASP': [['HB\#','HB*']],'PHE': [['HB\#','HB*'],['HD\#','HD*']],
          'GLN': [['HB\#','HB*'],['HE2\#','HE2*'],['HG\#','HG*']],
          'GLU': [['HB\#','HB*'],['HG\#','HG*']],
          'GLY': [['HA\#','HA*']],
          'HIS': [['HB\#','HB*']],
          'ILE': [['HG1\#','HG1*'],['HD1\#','HD1*'],['HG2\#','HG2*']],
          'LEU': [['HB\#','HB*'],['HD1\#','HD1*'],['HD2\#','HD2*'],['HD\#','HD*']],
          'LYS': [['HB\#','HB*'],['HE\#','HE*'],['HG\#','HG*'],['HD\#','HD*']],
          'MET': [['HB\#','HB*'],['HG\#','HG*']],
          'PRO': [['HB\#','HB*'],['HD\#','HD*'],['HG\#','HG*']],
          'SER': [['HB\#','HB*']],
          'THR': [['HB\#','HB'],['HG2\#','HG2*'],['HG\#','HG2*','HG1']],
          'TYR': [['HB\#','HB*'],['HD\#','HD*'],['HE\#','HE*']],
          'VAL': [['HG1\#','HG1*'],['HG2\#','HG2*']],
      }
    }
   }
  },


'1cz4': {

  'comment': "Has THR HG+ (in ambiguitydict?)",

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1cw5': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1cwx': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1cey': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1cz5': {

  'comment': "Has THR HG+ (in ambiguitydict?)",

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1d1d': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1c7v': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1c7w': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1d1r': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },


'1d3z': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1d5v': {
  
  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1d8b': {

  'linkResonances': {
   'keywds': {
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2, 
      'forceChainMappings': [['A',' ',1,10]]
      }
    }
  },

'1cfe': {

  'linkResonances': {
   'keywds': {
      'forceChainMappings': [[' ',' ',1,0]]
      }
    }
  },

'1d8z': {
  
  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'ILE': [['HD#','HD1*']]}
      }
    }
  },

'1d9s': {
  
  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1dc2': {
  
  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1dc7': {
  
  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
  
'1dcj': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1doq': {

  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,16]]
      }
    }
  },

'1du2': {

  'comment': """
 Has lots of H instead of HN - using useIupacMatching = 2
 Has THR QG2 (to HG2*), VAL QG1,QG2 (to HG1*,HG2* stereo)
 ASN QD2 (to HD2*), LEU QQD (to HD*), ALA QB (to HB*),
 GLY HA1 (to HA3 stereo), ILE QG1,QD2 (to HG1*, HD2*),
 LEU QD1,QD2 (to HD1*,HD2* stereo), VAL QQG (to HG*)
   """,

  'linkResonances': {
   'keywds': {
      'useIupacMatching': 2, 
      'namingSystem': 'DIANA',
      'forceDefaultChainMapping': 1
      }
    }
  },

'1du9': {

  'comment': "Has VAL OT# (not linked - in ambiguityDict?)",

  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,0]]
      }
    }
  },

'1dv5': {
  
  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1dx7': {

  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'TRP': [['HD+','HD1']]}
      }
    }
  },

'1e17': {

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1e3y': {

  'comment': 'Has TRP HE3#,HZ2#,HZ3# (to HE3,HZ2,HZ3)', 

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'TRP': [['HE3#','HE3'],['HZ2#','HZ2'],['HZ3#','HZ3']]}
      }
    }
  },

'1e41': {

  'comment': 'Has TRP HE3#,HZ2#,HZ3# (to HE3,HZ2,HZ3)', 

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'TRP': [['HE3#','HE3'],['HZ2#','HZ2'],['HZ3#','HZ3']]}
      }
    }
  },

'1e5b': {

  'comment': 'Has ASN HD++ (not linked)',
  
  },

'1e5c': {

  'comment': 'Has ASN HD++ (not linked)',
  
  },

'1e8l': {

  'comment': 'Has ASN HG2 (not linked)',
  
  },

'1e8r': {

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
  
'1e9k': {

  'comment': 'Has THR HG1# (not linked)',
  
  },

'1e9t': {

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ef5': {

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

  

'1ehx': {
  
  'comment': "Has ILE HD2, HD3 (not linked)",

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1eiw': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ckr': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1c49': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1eo1': {
  #has HN* 1 Met for H*
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'specificResNameMappings': {' .1.HN*': ' .1.HT*'}
      }
    }
  },

'1eot': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1eph': {

  'comment': "has ARG HE#",
  
  'linkResonances': {
   'keywds': {
      #'useLinkResonancePopup': 0   
      }
    }
  },

'1epj': {

  'comment': "has ARG HE#",
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      #'useLinkResonancePopup': 0  
      }
    }
  },

'1eq0': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1eq3': {

  'comment': "restraint 35 not in pdb",
	
  'linkResonances': {
    'keywds': {                     
      'forceChainMappings': [['A',' ',1,35]],
      'specificResNameMappings': {' .36.HN': ' .36.HT*'}
      }
    }
  },

'1eww': {
	
  'linkResonances': {
    'keywds': {
      'forceDefaultChainMapping': 1,
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1n1u': {
	
  'linkResonances': {
    'keywds': {                     
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1nb1': {
	
  'linkResonances': {
    'keywds': {                     
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1nbj': {
	
  'linkResonances': {
    'keywds': {                     
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1eza': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1idi': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1idl': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'2eza': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ezo': {

  'comment': "restraint 0 not in pdb",
  	
  'linkResonances': {
    'keywds': {                     
      'forceChainMappings': [['A',' ',1,0]]
      }
    }
  },

'1ezp': {

  'comment': "restraint 0 not in pdb",
	
  'linkResonances': {
    'keywds': {                     
      'forceChainMappings': [['A',' ',1,0]] 
      }
    }
  },

'1ezt': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ezy': {
	
  'linkResonances': {
    'keywds': {                     
      'forceChainMappings': [['A',' ',1,0]] 
      }
    }
  },

'1f16': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1fad': {
  
  'linkResonances': {
   'keywds': {
       'forceChainMappings': [['A',' ',5,-4]]  
      }
    }
  },

'1f2h': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1   
      }
    }
  },


'1f43': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',12,0]] 
      }
    }
  },

'1f7e': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1   
      }
    }
  },

'1f7m': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'SER': [['HG#','HG']]}
      }
    }
  },

'1fcl': {

  'comment': "useIupacMatching = 2 does no harm, is xplor entry",
  
  'linkResonances': {
   'keywds': {
      'useIupacMatching': 2, 
      'addNameMappings':  {'VAL': [['HG#+','HG*']],'LEU': [['HD#+','HD*']],'THR': [['HG#+','HG1','HG2*']]}
      }
    }
  },

'1fdm': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [[' ','SEG1',7,0],[' ',' ',2,0]] 
      }
    }
  },

'1fex': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1   
      }
    }
  },

'1fht': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'PHE': [['HN*','HN']],'TYR': [['HN*','HN']],'ILE': [['HD*','HD1*']]}
      }
    }
  },

'1fjd': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1   
      }
    }
  },

'1fmm': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1, 
      'addNameMappings':  {'ILE': [['HD*','HD1*'],['HD#','HD1*'],['HB*','HB'],['HB#','HB'],]} 
      }
    }
  },

'1fo7': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',36,89]] 
      }
    }
  },

'1fow': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1   
      }
    }
  },

'1fr0': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1   
      }
    }
  },

'1fry': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1   
      }
    }
  },

'1fuw': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'MET': [['HN*','HN']],'ILE': [['HB*','HB'],['HD*','HD1*']],'THR': [['HB*','HB']],'VAL': [['HB*','HB']] } 
      }
    }
  },

'1fwp': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1fzt': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1gjs': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1gyz': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1g10': {
  
  'comment': "useIupacMatching = 2 does no harm, is xplor entry",

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'useIupacMatching': 2  
      }
    }
  },
 
'1g11': {
  
  'comment': "useIupacMatching = 2 does no harm, is xplor entry",

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'useIupacMatching': 2  
      }
    }
  },

'1g2t': {
  
  'linkResonances': {
   'keywds': {
      'addNameMappings':  {'THR': [['HB*','HB']],'VAL': [['HB*','HB']],'ILE': [['HD#','HD1*'],['HB*','HB']],'TRP': [['HD#','HD1']]}
      }
    }
  },

'1g2s': {
  
  'linkResonances': {
   'keywds': {
      'addNameMappings':  {'THR': [['HB*','HB']],'VAL': [['HB*','HB']],'ILE': [['HD#','HD1*'],['HB*','HB']],'TRP': [['HD#','HD1']]}
      }
    }
  },


'1g4f': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1hg6': {
  
  'linkResonances': {
   'keywds': {
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1g6e': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1h2o': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1g6m': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1gb4': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1g6j': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1g91': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },


'1g9l': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ga3': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',6,0],['A','IL13',2,0]] 
      }
    }
  },

'1gd3': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1gd4': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1gd5': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1gdf': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1gh5': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1gh9': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ghj': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ghk': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ghu': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1go1': {
  
  'comment': "error in pdb, residue 0 does not exist, seem correct:4,-3",

  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',3,-2]],
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2   
      }
    }
  },

'1fho': {
  
  'linkResonances': {
   'keywds': {
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2,
      'forceDefaultChainMapping': 1
      }
    }
  },

'1gw3': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1gxe': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1gxg': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1h0z': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1h3z': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1h40': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1h7d': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1h7j': {
  
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1h95': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
 
'1hdl': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
 
'1heh': {
  
  'linkResonances': {
   'keywds': {
      'addNameMappings':  {'PRO': [['HG++','HG*']]} 
      }
    }
  },

'1hej': {
  
  'linkResonances': {
   'keywds': {
      'addNameMappings':  {'PRO': [['HG++','HG*']]} 
      }
    }
  },

'1hfg': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
 
'1hn6': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'specificResNameMappings': {' .436.HN': ' .436.HT*'}
      }
    }
  },
 
'1ho2': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,0]] 
      }
    }
  },

'1ho7': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,0]] 
      }
    }
  },

'1hp9': {
   
  'linkResonances': {
   'keywds': {
      # 'useCommonNames': 0
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'ASN': [['HD#','HD2*']],'ARG': [['HE#','HE']]},
      #'useLinkResonancePopup': 0
      }
    }
  },
 
'1hpw': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
 
'1hqb': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
 
'1hs7': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
 
'1hx7': {
  
  'linkResonances': {
   'keywds': {
      'addNameMappings':  {'ASN': [['HD23','HD22']]},
      'forceDefaultChainMapping': 1
      }
    }
  },

'1hy8': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,5]],
      'specificResNameMappings': {' .6.HN': ' .6.HT*'}
      }
    }
  },

'1hz3': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ivm': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
 
'1i11': {
   
  'comment': "useIupacMatching = 2 does no harm, is xplor entry",

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'useIupacMatching': 2 
      }
    }
  },

'1i42': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
 
'1i5j': {
   
  'comment': "useIupacMatching = 2 does no harm, is xplor entry",

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'VAL': [['QQG','HG*']],'LEU': [['QQD','HD*']],'GLY': [['QA','HA*']]}, 
      'useIupacMatching': 2  
      }
    }
  },

'1iba': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ib9': {
   
  'linkResonances': {
   'keywds': {
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },
 
'1ich': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
 
'1ieh': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
 
'1iez': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'PHE': [['HB1#','HB3']],'PHE': [['HB2#','HB2']]} 
      }
    }
  },


'1i2u': {
   
  'linkResonances': {
   'keywds': {
     #'useCommonNames': 0,
      'addNameMappings':  {'ALA': [['QB','HB*']],'VAL': [['QG1','HG1*']],'VAL': [['QG2','HG2*']],'THR': [['QG2','HG2*']],'LEU': [['QD1','HD1*']],'LEU': [['QD2','HD2*']],'ILE': [['QG2','HG2*']],} 
      }
    }
  },

'1i2v': {
   
  'linkResonances': {
   'keywds': {
      #'useCommonNames': 0,
      'addNameMappings':  {'ALA': [['QB','HB*']],'VAL': [['QG1','HG1*'],['QG2','HG2*']],'THR': [['QG2','HG2*']],'LEU': [['QD1','HD1*'],['QD2','HD2*']],'ILE': [['QG2','HG2*'],['QD','HD1*']]} 
      }
    }
  },



'1ifw': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
 
'1ig6': {
  
  'comment': "Has DYANA specificResName mapping",

  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,12]],
      'specificResNameMappings': {' .13.HN': ' .13.HT*'} 
      }
    }
  },

'1igl': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },
 
'1iio': {
  
  'comment': "error in pdb: no residue 0, does not exist in coordinate list",

  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',7,-3],['A','m865',8,-3]],
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2,
      #'useLinkResonancePopup': 1 # contains lots of errors
      }
    }
  },

'1b5n': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1bno': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1d8v': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1fyj': {
   
  'linkResonances': {
   'keywds': {
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1ed7': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'specificResNameMappings': {' .655.HN': ' .655.HT*'}
      }
    }
  },

'1brv': {   
  'readCoordinates': {
    'keywds': {
      'addNameMappings':  {'ALL': [['1H','H1'],['2H','H2']]} 
      }
    },

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'specificResNameMappings': {'1.171.HN1': '1.171.HN*'}
      }
    }
  },

'1bqv': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1bo0': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1bnb': {
   
  'comment': "consistent error",

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'ILE': [['HD*','HD1*'],['HB*','HB']]}
      }
    }
  },
 
'1il6': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1imq': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1iox': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ip0': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ip9': {
   
  'linkResonances': {
   'keywds': {
      # 'useCommonNames': 0
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'THR': [['HB#','HB']],'ILE': [['HB#','HB'],['HD#','HD1*']],'ASN': [['HD#','HD2*']],'GLN': [['HE#','HE2*']]} 
      }
    }
  },

'1ipg': {
   
  'linkResonances': {
   'keywds': {
     # 'useCommonNames': 0
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'THR': [['HB#','HB']],'ILE': [['HB#','HB'],['HD#','HD1*']],'ASN': [['HD#','HD2*']],'GLN': [['HE#','HE2*']]} 
      }
    }
  },

'1irz': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1itl': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'LYS': [['HB1#','HB3']]} 
      }
    }
  },

'1iwc': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1iwf': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1iyg': {   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1iyu': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1iy6': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1iyy': {
   
  'comment': "CB# does not exist for CYS",

  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'CYS': [['CB#','CB']],'ILE': [['HN*','H*']]} 
      }
    }
  },

'1j0t': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',2,0]] 
      }
    }
  },

'1j6q': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1j6y': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1j7m': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1j7q': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1j7r': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1j8c': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      #'useCommonNames' : 0
      'addNameMappings':  {'ILE': [['HB#','HB'],['HD#','HD1*']],'ASN': [['HD#','HD2*']],'GLN': [['HE#','HE2*']]} 
      }
    }
  },

'1jas': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jc6': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jcu': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jqr': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jdq': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1je3': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jfj': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jfn': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jh3': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jhb': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ji8': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jjg': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jjr': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jnj': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jo5': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1joo': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jor': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jr6': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jrj': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jsb': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jt8': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
   }
  },

'1jvr': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jwe': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jw3': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jw2': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jxc': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jyg': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jyt': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1jzu': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',5,0],['A','PEPT',4,0]] 
      }
    }
  },

'1iqs': {
   
  'linkResonances': {
   'keywds': {
    # 'useCommonNames' : 0,
      'addNameMappings':  {'THR': [['HB','HB*']],'ILE': [['HB','HB*'],['HD*','HD1*']],'ASN': [['HD*','HD2*']],'GLN': [['HE*','HE2*']]} 
      }
    }
  },

'1iqo': {
   
  'linkResonances': {
   'keywds': {
    # 'useCommonNames' : 0,
      'addNameMappings':  {'THR': [['HB','HB*']],'ILE': [['HB','HB*'],['HD*','HD1*']],'ASN': [['HD*','HD2*']],'GLN': [['HE*','HE2*']]} 
      }
    }
  },

'1k0s': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',2,0]],
      'forceDefaultChainMapping': 1
      }
    }
  },

'1k18': {
   
  'linkResonances': {
   'keywds': {
      'addNameMappings':  {'ILE': [['HN*','H*']]}  
      }
    }
  },

'1k19': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      # 'useCommonNames': 0,
      'addNameMappings':  {'ILE': [['HD*','HD1*']],'ASN': [['HD*','HD2*']],'GLN': [['HE*','HE2*']]} 
      }
    }
  },

'1k1c': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1k1v': {
  
  'comment': "Has resonances preceding and following sequence from PDB.",

  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,23]] 
      }
    }
  },

'1k1z': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,  #has lots of hd1% etc, and hb2/3, forced to be xplor
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2   
      }
    }
  },


'1k3j': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1kbs': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1k7b': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1k8b': {
  
  'linkResonances': {
   'keywds': {'specificResNameMappings': {' .39.HN': ' .39.HT*'},
      'forceChainMappings': [['A',' ',1,38]]
      
      }
    }
  },

'1k8h': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1k8m': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1k8o': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1kdf': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1kft': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1kgm': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1khm': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1kik': {
   
  'linkResonances': {
   'keywds': {
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2,
      'specificResNameMappings': {' .64.HN': ' .64.HT*'}
      }
    }
  },

'1kj0': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1kma': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1kkg': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,0]],
      }
    }
  },

'1kkd': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',3,-2]],
      }
    }
  },

'1klr': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,30]],
      }
    }
  },

'1kmd': {
   
  'linkResonances': {
   'keywds': {
      'addNameMappings':  {'GLY': [['HA2*','HA2']]}  
      }
    }
  },

'1kn7': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1kot': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1koy': {
  
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,18]],
      'addNameMappings':  {'ILE': [['HD#','HD1*']]} 
      }
    }
  },

'1kq8': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1krw': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ks0': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1ktm': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1kx6': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1l1i': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1l1p': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1pfl': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1l3g': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,1],['A','MBP1',3,1]] 
      }
    }
  },

'1l3y': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1l7b': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1l7y': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ldl': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ldr': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1lg4': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,23]] 
      }
    }
  },

'1lgl': {
   
  'linkResonances': {
   'keywds': {
      #'addNameMappings':  {'GLY': [['O','O*']]}  
      }
    }
  },

'1liz': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1lkj': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1lm0': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ls4': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1m7t': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1mit': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1m12': {
   
  'linkResonances': {
   'keywds': {
      'useIupacMatching': 2
      }
    }
  },

'1m2e': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1m2f': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1maj': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1m3b': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1m3c': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1m3a': {
   
  'linkResonances': {
   'keywds': {
      'specificResNameMappings': {' .135.HN': ' .135.H*'}
      }
    }
  },

'1kjs': {
   
  'linkResonances': {
   'keywds': {
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1m30': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1m39': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1m94': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1qhk': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',2,5]],
      'addNameMappings':  {'TYR': [['HB1*','HB1']],'LYS': [['HB2*','HB2']],'ILE': [['HD*','HD1*']]} 
      }
    }
  },

'1m9g': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1qk6': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,0]] 
      }
    }
  },

'1qkf': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1mg8': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1qkh': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1mjd': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1qnd': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,0]] 
      }
    }
  },

'1mk3': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'ALA': [['HB##','HB*']],'THR': [['HG#2','HG2*']]}  
      }
    }
  },

'1mke': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1qu5': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1qxf': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1mm4': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1mm5': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1r63': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [[' ',' ',1,0]] 
      }
    }
  },

'1mnl': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1roo': {
   
  'linkResonances': {
   'keywds': {
      'addNameMappings':  {'LYS': [['QB','HB*']],'GLY': [['QA','HA*']]}  
      }
    }
  },

'1mot': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1rot': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1sdf': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1sh1': {
   
  'comment': "is dyana entry, but names are messed up",

  'linkResonances': {
   'keywds': {
      'addNameMappings':  {'PRO': [['QPD','HD*']],'LEU': [['QPB','HB*'],['QQD','HD*']],'GLY': [['QPA','HA*']],'SER': [['QPB','HB*']],'CYS': [['QPB','HB*']],'ASN': [['QPB','HB*']],'TRP': [['QPB','HB*']],'GLU': [['QPG','HG*'],['QPB','HB*']],'LYS': [['QPB','HB*'],['QPD','HD*'],['QPE','HE*']],'TYR': [['QPB','HB*']],'ASP': [['QPB','HB*']]},
      'namingSystem': 'XPLOR',
      #'useLinkResonancePopup': 0
      }
    }
  },



'1mph': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [[' ',' ',2,0]] 
      }
    }
  },

'1mpz': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1mzk': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',3,0]] 
      }
    }
  },

'1spy': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1sso': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1sut': {

  'comment': "Is discover entry",
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'ARG': [['HB','HB*'],['HD','HD*'],['HH','HH*']],'PRO': [['HB','HB*']],'LYS': [['HB','HB*']],'GLN': [['HB','HB*']],'ILE': [['HD1','HD1*']]},
      }
    }
  },

'1suh': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [[' ',' ',3,0]] 
      }
    }
  },

'1tbd': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1txa': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'specificResNameMappings': {' .1.HN': ' .1.HT*',' .2.HN#': ' .2.HN'},
      'addNameMappings':  {'THR': [['NH','N']],'LYS': [['NH','N']],'CYS': [['NH','N']],'TYR': [['NH','N']],'TRP': [['NH','N']],'ASP': [['NH','N']],'GLY': [['NH','N']],'ALA': [['NH','N']]}
      }
    }
  },

'1n3g': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1n6z': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1n4t': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1n4i': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1tih': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'ARG': [['HH**','HH*']],'ILE': [['H***','H']]},
      'useIupacMatching': 2
      }
    }
  },

'1n91': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1n9d': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1tit': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [[' ',' ',10,-7]] 
      }
    }
  },

'1tnn': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1nct': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [[' ',' ',9,-8]] 
      }
    }
  },

'1ojg': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',1,21]] 
      }
    }
  },

'1tof': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1nfa': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },


'1ni7': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1u2f': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },


'1nj7': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'namingSystem': 'DIANA',
      'addNameMappings':  {'ARG': [['HH1','HH1*']]}
      }
    }
  },

##'1cou': {
##   
##  'linkResonances': {
##   'keywds': {
##      'forceDefaultChainMapping': 1,
##      'namingSystem': 'DIANA', 
##      'addNameMappings':  {
##        'GLU': [['HB+','HB*'],['HB-','HB*'],['HG+','HG*'],['HG-','HG*']],
##                           'LYS': [['HB+','HB*'],['HB-','HB*'],['HD+','HD*'],['HD-','HD*']],
##                           'TYR': [['HB+','HB*'],['HB-','HB*'],['HD','HD*'],['HE','HE*']],
##                           'ASP': [['HB+','HB*'],['HB-','HB*']],
##                           'SER': [['HB+','HB*'],['HB-','HB*']],
##                           'CYS': [['HB+','HB*'],['HB-','HB*']],
##                           'GLY': [['HA+','HA*'],['HA-','HA*']]
##                           }
##      }
##    }
##  },



'1ugl': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'namingSystem': 'XPLOR', #has lots of hd1% etc, and hb2/3, forced to be xplor
      'useIupacMatching': 2   
      }
    }
  },

'1nm7': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A',' ',8,301]] 
      }
    }
  },

'1uxc': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1nmr': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1nmv': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1no8': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'namingSystem': 'DIANA',
      'addNameMappings':  {'GLY': [['HA3','HA1']]} 
      }
    }
  },

'1vhp': {
   
  'linkResonances': {
   'keywds': {
      'addNameMappings':  {'TYR': [['HDE*','HE*']]}
      }
    }
  },

'1vih': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'specificResNameMappings': {' .6.HN': ' .6.HT*'}
      }
    }
  },

'1nr3': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1nwb': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1nwv': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'ILE': [['HD1','HD11'],['HD2','HD12'],['HD3','HD13']]},
      #'useLinkResonancePopup': 0
      }
    }
  },

'1nxi': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1kul': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1kun': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ny4': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1ny9': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1n6v': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1n6u': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1nyn': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1nzp': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'ILE': [['HD#','HD1*']]}
      
      }
    }
  },

'1o1w': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1o78': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1o8t': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1o8r': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1oef': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'2vik': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1oeg': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },


'1og7': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2   
      }
    }
  },

'1ohm': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2   
      }
    }
  },

'1ohn': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2   
      }
    }
  },

'1ahl': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2   
      }
    }
  },



'1onb': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1op1': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1oq3': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1or5': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1orx': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1p1t': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },


'1pbu': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1plo': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1pms': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1pn5': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1pux': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1q27': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'GLN': [['HB1*','HB1'],['HB2*','HB2']],'LEU': [['HB1*','HB1'],['HB2*','HB2']]}
      }
    }
  },

'1q59': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1qbf': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'THR': [['HG++','HG1','HG2*']],'TYR': [['H+','H']]}
      }
    }
  },

'1wkt': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1xna': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'2cpb': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'2cjn': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'addNameMappings':  {'ILE': [['HD#','HD1*']],'GLN': [['HE#','HE2*']]} 
      }
    }
  },

'2ezh': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'2ezl': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'2hfh': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'2igg': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'2igh': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'2ktx': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'2lfb': {
	
  'linkResonances': {
    'keywds': {                     
      'forceChainMappings': [[' ',' ',1,0]]
      }
    }
  },

'2mob': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'2pta': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'2r63': {
	
  'linkResonances': {
    'keywds': {                     
      'forceChainMappings': [[' ',' ',1,0]]
      }
    }
  },

'2sob': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'2u1a': {
   
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [[' ',' ',2,0]],
      'addNameMappings':  {'ARG': [['HH++','HH*']]} 
      }
    }
  },

'3ci2': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'3cti': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'3nla': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },



#
# Multimers
#
'1a7f': {

  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',2,0],['B','B',1,0]]
      }
    }
  },

'1aze': {

  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1',1,0,"A"],['B','1',1,0,"B"]]  #codes with 1A and 1B
      }
    }
  },

'1rtn': {

  #'duplicateResonances': {' ': ['a','b']},
  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {
      'formatChainCodes': {' ': ['a','b']}, 
      'forceChainMappings': [['A','a',1,0],['B','b',1,0]] 
      }
    }
  },

'1r2a': {

  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','a',2,0],['B','b',2,0],['A','A',3,0],['B','B',3,0]] 
      }
    }
  },

'1qmc': {

  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,218],['B','B',1,218]],
      }
    },

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',2,218],['B','B',2,218]] 
      }
    }
  },




'1aq5': {
    
  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0],['C','C',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
      'forceChainMappings': [['A','A',6,0],['B','B',6,0],['C','C',6,0]]
      }
    }
  },
   
'1b4c': {

  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,-1],['B','B',1,-1]],
      }
    },

  'linkResonances': {
    'keywds': {                     
      'forceChainMappings': [['A','sbm1',1,-1],['B','sbm2',1,-1]]
      }  
    }	
  },
   
'1cir': {

  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,40]],
      }
    },


  'linkResonances': {
    'keywds': {                    
      'forceChainMappings': [['A',' ',1,19],['B',' ',1,59]],   
      #'useLinkResonancePopup': 0
      }
    }
  },

'1cop': {

  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['D','D',1,0],['E','E',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
      'forceChainMappings': [['D','D',1,0],['E','E',1,0]]  
      }
    }
  },

'1cqg': {
    
  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,58]],
      }
    },

  'linkResonances': {
    'keywds': {                    
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,105]]
      }
    }
  },

'1cq0': {

  'linkResonances': {
    'keywds': {                    
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1dcz': {

  'linkResonances': {
    'keywds': {                    
      'specificResNameMappings': {' .47.HN': ' .47.HT*'}
      }
    }
  },

'1dd2': {

  'linkResonances': {
    'keywds': {                    
      'specificResNameMappings': {' .47.HN': ' .47.HT*'}
      }
    }
  },

'1df6': {

  'linkResonances': {
    'keywds': {                    
      'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1dp3': {

  'linkResonances': {
    'keywds': {                    
      'specificResNameMappings': {' .2.HN': ' .2.HT*'}
      }
    }
  },

'1d5g': {

  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
      'forceChainMappings': [['A','A',1,0],['B','B',2,0]]   
      }
    }
  },

'1d7q': {

  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,14],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,14],['B',' ',4,0]],   
      #'useLinkResonancePopup': 0     
      }
    }
  },

'1dbd': {

  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
      'forceChainMappings': [['A','A',3,0],['B','B',3,0]]   
      }
    }
  },

'1dom': { #ok

  'duplicateResonances': {' ': ['MCP1','MCP2']},   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {
      #'formatChainCodes': {' ': ['MCP1','MCP2']},                  
      'forceChainMappings': [['A','MCP1',1,0],['B','MCP2',1,0]]   
      }
    }
  },

'1dum': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',2,0],['B','B',2,0]]   
      }
    }
  },

'1e52': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',8,0],['B','B',8,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',8,0],['B','B',8,0]]  
      }
    }
  },

'1e91': {

  'duplicateResonances': {' ': ['PAH2','MAD1']},
     
  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]]
      }
    },

  'linkResonances': {
    'keywds': {
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2,
      'forceChainMappings': [['A','PAH2',4,0],['B','MAD1',1,200]]  
      }
    }
  },

'1eci': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,0],['B',' ',1,40]] 
      }
    }
  },

'1ejp': { #ok

  'duplicateResonances': {' ': ['A','B']},                   
      
  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]] 
      }
    }
  },

'1ejq': { #ok

  'duplicateResonances': {' ': ['A','B']},       

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]] 
      }
    }
  },

'1ev0': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,30],['B','B',1,30]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','AAAA',1,30],['B','AAAB',1,30]]   
      }
    }
  },

'1exe': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','1',1,0],['B','1',1,100]]   
      }
    }
  },

'1f22': {
##Created chain 'A', start seqCode 1, end seqCode 68, molecule 'CYTOCHROME C7'...
##Created chain 'B', start seqCode 69, end seqCode 69, molecule 'HEME C'...
##Created chain 'C', start seqCode 70, end seqCode 70, molecule 'HEME C'...
##Created chain 'D', start seqCode 71, end seqCode 71, molecule 'HEME C'...

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','A',1,68],['C','A',1,69],['D','A',1,70]],
      }
    },

  #'linkResonances': {
  #  'keywds': {                     
  #   'forceChainMappings': [['C','CAD',2,0],['I','ICAD',8,0]]
  #    }
  #  }
  },

'1f2r': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['C','C',1,0],['I','I',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['C','CAD',2,0],['I','ICAD',8,0]]
      }
    }
  },

'1f3c': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','CHA1',1,0],['B','CHA2',1,0]]
      }
    }
  },

'1f95': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0],['C','C',1,0],['D','D',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','CHA1',1,0],['B','CHA2',1,0],['C','CHA3',1,0],['D','CHA4',1,0]] 
      }
    }
  },

'1f96': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0],['C','C',1,0],['D','D',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','CHA1',1,0],['B','CHA2',1,0],['C','CHA3',1,0],['D','CHA4',1,0]] 
      }
    }
  },


'1g1e': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,5],['B','B',1,294]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,5],['B',' ',1,294]]
      }
    }
  },

'1gjz': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,-2],['B','B',1,-2]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','a',3,0],['B','b',3,0]]
      }
    }
  },

'1h0t': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','Z',1,0],['B','ZSPA',1,0]]
      }
    }
  },

'1hqi': {

  'linkResonances': {
    'keywds': {                     
       'formatChainCodes': {' ': ['P2']},
       'forceChainMappings': [[' ','P2',1,0]]
      }
    }
  },

'1h3h': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,15],['B','B',1,75]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','SH3',1,15],['B','SLP',1,75]]
      }
    }
  },

'1h8b': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',3,-2],['B','B',9,-2]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','ef34',6,-2],['B','zr7',10,-2]]
      }
    }
  },

'1hi7': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',1,0],['B','B',1,0]]
      }
    }
  },

'1hiq': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',2,0],['B',' ',1,100]]
      }
    }
  },

'1his': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',2,0],['B',' ',1,100]]
      }
    }
  },

'1hit': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,0],['B',' ',1,100]]
      }
    }
  },

'1hrj': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','a',1,101],['B','b',1,201]]
      }
    }
  },

'1hs5': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','a',1,0],['B','b',1,0],['A','A',3,0],['B','B',4,0]]
      }
    }
  },

'1hue': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','1',1,0],['B','1',1,90]]
      }
    }
  },

'1i5h': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['B','B',1,604],['W','W',1,449]],
      }
    },

  'linkResonances': {
    'keywds': {
      'formatChainCodes': {'BP2': ['B']},  
      'forceChainMappings':  [['B','B',2,604],['W','W',3,449]]
      #'forceChainMappings': [['B','B',2,604],['B','BP2',2,604],['W','W',3,449]]
      }
    }
  },

'1idg': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,180]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,0],['B',' ',2,180]]
      }
    }
  },

'1idh': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,180]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,0],['B',' ',2,180]]
      }
    }
  },

'1ihq': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,0],['B',' ',1,138]]
      }
    }
  },

'1ihv': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,218],['B','B',1,218]],
      }
    },

  #'linkResonances': {
  #  'keywds': {                     
  #   'forceChainMappings': [['C','CAD',2,0],['I','ICAD',8,0]]
  #    }
  #  }
  },

'1isk': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',2,0],['B',' ',2,300]]
      }
    }
  },

'1j9i': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',1,0],['B','B',1,0]]
      }
    }
  },

'1jgn': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',2,0],['B','B',1,0]]
      }
    }
  },


'1jh4': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',7,0],['B','B',5,0]]
      }
    }
  },

'1jmq': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,4],['P','P',1,50]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','1',1,4],['P','2',1,0]]
      }
    }
  },

'1k2h': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','sam1',1,0],['B','sam2',1,0]],
     'addNameMappings':  {'ILE': [['HD#','HD1*']]} 
      }
    }
  },

'1k3m': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','1',1,0],['B','1',1,21]]
      }
    }
  },

'1k4u': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['P','P',1,358],['S','S',1,454]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['P','PRRC',2,358],['S','SH3C',2,454]]
      }
    }
  },

'1ka7': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,274]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','SAP',2,0],['B','PEP',4,0]]
      }
    }
  },

'1kal': {

  'linkResonances': {
    'keywds': {                     
     'specificResNameMappings': {' .1.HN': ' .1.HT*'}
      }
    }
  },

'1kc4': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,177]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,0],['B',' ',2,177]]
      }
    }
  },

'1klc': {

  'comment': "Has OT# for Ser",

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,0],['B',' ',1,200]]
      }
    }
  },

'1klq': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,10],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,10],['B',' ',1,0]]
      }
    }
  },

'1kup': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,11]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',1,0],['B','B',1,11]]
      }
    }
  },

'1kuz': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,11]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',1,0],['B','B',1,11]]
      }
    }
  },

'1l2z': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,62]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',6,0],['B',' ',3,62]]
      }
    }
  },

'1l4w': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,179]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,0],['B',' ',1,179]],
     'addNameMappings':  {'THR': [['HB*','HB']],'VAL': [['HB*','HB']],'LEU': [['HG*','HG']],'TRP': [['HD*','HD1']],'ARG': [['HE*','HE']]}
      }
    }
  },

'1ljz': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,179]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,0],['B',' ',1,179]],
     'addNameMappings':  {'THR': [['HB*','HB']],'VAL': [['HB*','HB']],'LEU': [['HG*','HG']],'TRP': [['HD*','HD1']],'ARG': [['HE*','HE']]}
      }
    }
  },

'1lkq': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','1',1,0],['B','1',1,21]]
      }
    }
  },

'1lr1': {
    
  'duplicateResonances': {' ': ['A','B']},

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',5,-4],['B','B',5,-4]],
      }
    },

  'linkResonances': {
    'keywds': {                     
      'forceChainMappings': [['A','A',5,-4],['B','B',5,-4]]
      }
    }
  },

'1m4p': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',2,0],['B','B',1,204]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',2,0],['B',' ',1,204]]
      }
    }
  },

'1mhi': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','acha',2,0],['B','bcha',1,0]]
      }
    } 
  },

'1mhj': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','acha',1,0],['B','bcha',1,0]]
      }
    } 
  },

'1mpe': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0],['C','C',1,0],['D','D',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','a',1,0],['B','b',1,0],['C','c',1,0],['D','d',1,0]]
      }
    } 
  },

'1mq1': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0],['C','C',1,0],['D','D',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','a',1,0],['B','b',1,0],['C','c',1,91],['D','d',1,91]]
      }
    } 
  },

'1mv4': {
    
  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,247],['B','B',1,247]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',2,0],['B',' ',2,137]]
      }
    } 
  },

'1n7t': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,300]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',1,0],['B','B',1,300]]
      }
    } 
  },

'1ng7': {

  'duplicateResonances': {'a': ['a','b']},

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','a',2,0],['B','b',2,0]]
      }
    } 
  },

'1ntc': {
    
  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,378],['B','B',1,378]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','a',21,0],['B','b',21,0]]
      }
    } 
  },

'1olg': {
    
  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,318],['B','B',1,318],['C','C',1,318],['D','D',1,318]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',2,0],['B','B',2,0],['C','C',2,0],['D','D',2,0]]
      }
    } 
  },

'1om2': {   

  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',2,0],['B',' ',4,121]]
      }
    } 
  },

'1oo9': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,82],['B','B',1,300]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',15,82],['B',' ',2,300]]
      }
    } 
  },

'1pfm': {

  'readCoordinates': {
	
    'keywds': {
      'forceChainMappings': [['A','A',1,2],['B','B',1,2],['C','C',1,2],['D','D',1,2]],
      }
    },

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',4,0],['B','B',4,0],['C','C',4,0],['D','D',24,0]] 
      }
    }
  },


'1pfs': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]]
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','a',1,0],['B','b',1,0],['A',' ',1,0],['B',' ',1,0]]
      }
    } 
  },


#'1pik': {   
#
#  'linkResonances': {
#    'keywds': {                     
#     'forceChainMappings': [['D','ESPR',1,20],['A','ESPR',1,21],[' ','ESPR',1,22],['B','ESPR',1,23],['C','ESPR',1,24],['G','ESPR',1,25],['E','DNA1',1,0],['F','DNA2',1,10]]
#      }
#    } 
#  },

'1q0w': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,254],['B','B',1,0]]
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','UIM',1,254],['B','UBI',1,0]]
      }
    } 
  },

'1q6a': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,200]]
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',2,0],['B',' ',2,200]],
     'addNameMappings':  {'CYS': [['HB1#','HB1']]} 
      }
    } 
  },

'1q6b': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,200]]
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',2,0],['B',' ',2,200]],
     'addNameMappings':  {'CYS': [['HB1#','HB1']]} 
      }
    } 
  },

'1qnk': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,4],['B','B',1,4]]
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,4],['B',' ',1,204]]
      }
    } 
  },

'1qp6': { #ok   

  'duplicateResonances': {' ': ['A2DA','A2DB']},
  
  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]]
      }
    },

  'linkResonances': {
    'keywds': {                     
     #'formatChainCodes': {' ': ['A2DA','A2DB']},
     'forceChainMappings': [['A','A2DA',1,0],['B','A2DB',1,0]]
      }
    } 
  },

'1nla': { #ok

  'duplicateResonances': {' ': ['a','b']},

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','a',5,0],['B','b',5,0]]
      }
    } 
  },

'1qrj': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,15]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',7,0],['B',' ',1,15]]
     
      }
    } 
  },

'1qtg': { #ok

  'duplicateResonances': {' ': ['A','B']},

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {
     'forceChainMappings': [['A','A',7,0],['B','B',7,0]]
      }
    } 
  },

'1rpr': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','ROPA',2,0],['B','ROPB',18,0]]
      }
    } 
  },

'1sym': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,-1],['B','B',1,-1]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','a',1,-1],['B','b',1,-1]]
      }
    } 
  },

'1uwo': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',2,-1],['B','B',2,-1]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','a',2,-1],['B','b',2,-1]]
      }
    } 
  },

'1vkt': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','1',1,0],['B','1',1,21]]
      }
    } 
  },

'1wtu': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',2,0],['B',' ',2,500]]
      }
    } 
  },

'1xgl': {  

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,0],['B',' ',1,21]]
      }
    } 
  },

'1xoo': {
   
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1
      }
    }
  },

'1zxa': {  

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','AN1',17,-8],['B','AN2',18,-8]]
      }
    } 
  },

'2bgf': {   

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',1,0],['B','B',1,0]]
      }
    } 
  },


'2ezo': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0],['C','C',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','a',1,0],['B','b',1,0],['C','c',1,0]]
      }
    } 
  },

'2ezx': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]]
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',2,0],['B','B',2,0]]
      }
    } 
  },

'2ezy': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]]
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',2,0],['B','B',2,0]]
      }
    } 
  },

'2hiu': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]]
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,0],['B',' ',1,21]]
      }
    } 
  },

'2il8': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',2,0],['B','B',2,0]]
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A','A',4,0],['B','B',4,0]]
      }
    } 
  },

'1afo': { #ok

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,61],['B','B',1,61]]
      }
    },

  'linkResonances': {
    'keywds': {
      'formatChainCodes': {'*': ['a','b']}, # cross terms!
      'forceChainMappings': [['A','a',1,61],['B','b',1,61]]
     }
    } 
  },

'3eza': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]]
      }
    },

  'linkResonances': {
    'keywds': {                     
     'forceChainMappings': [['A',' ',1,0],['B',' ',1,300]]
      }
    } 
  },


#
# New 2005 (Wim Vranken, EBI. Previous is Aart Nederveen)
#

# 149d: checked, problems with atom names are due to errors in PDB file!

'171d': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,12]]
      }
    }
  },

'1a1t': {   

  'linkResonances': {
    'keywds': {
      # ZN is mapped to CYS sequence codes for resonances -resetting.
      'specificResNameMappings': {' .28.ZN': ' .56.ZN',' .49.ZN': ' .57.ZN'}
      }
    }
  },

'1a24': {   

  'linkResonances': {
    'keywds': {
      # Several obvious resets... also 'ILE': [['HG#','HG1#']],?? Could also be HG2#...
      'addNameMappings':  {'THR': [['HB#','HB'],['HG#','HG2#']],'LEU': [['HG#','HG']],'PHE': [['HZ*','HZ']] }
      }
    }
  },

'1a2i': {   

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [[' ',' ',1,0],['A',' ',1,107],['B',' ',1,108],['C',' ',1,109]]
      }
    },

  'linkResonances': {
    'keywds': { # The HEC resonances have to be mapped individually... have same numbering as normal residues and not really easy way to handle this differently.
                # TODO: still have to map the atom names themselves - no match with MSD naming system currently.
      'forceChainMappings': [[' ',' ',1,0],['A',' ',1,107],['B',' ',1,108],['C',' ',1,109],['D',' ',1,110]],
      'specificResNameMappings': {' .105.HA62': ' .111.HA62',
                                  ' .105.HA63': ' .111.HA63',
                                  ' .105.HA72': ' .111.HA72',
                                  ' .105.HA73': ' .111.HA73',
                                  ' .105.HAM':  ' .111.HAM',
                                  ' .105.HB62': ' .111.HB62',
                                  ' .105.HB63': ' .111.HB63',
                                  ' .105.HB72': ' .111.HB72',
                                  ' .105.HB73': ' .111.HB73',
                                  ' .105.HBM':  ' .111.HBM',
                                  ' .105.HDM':  ' .111.HDM',
                                  ' .105.HGM':  ' .111.HGM',
                                  ' .105.HT2A': ' .111.HT2A',
                                  ' .105.HT4A': ' .111.HT4A',
                                  ' .105.QM1':  ' .111.QM1',
                                  ' .105.QM3':  ' .111.QM3',
                                  ' .105.QM5':  ' .111.QM5',
                                  ' .105.QM8':  ' .111.QM8',
                                  ' .105.QT2':  ' .111.QT2',
                                  ' .105.QT4':  ' .111.QT4',
                                  ' .33.HA62': ' .108.HA62',
                                  ' .33.HA63': ' .108.HA63',
                                  ' .33.HA72': ' .108.HA72',
                                  ' .33.HA73': ' .108.HA73',
                                  ' .33.HAM':  ' .108.HAM',
                                  ' .33.HB62': ' .108.HB62',
                                  ' .33.HB63': ' .108.HB63',
                                  ' .33.HB72': ' .108.HB72',
                                  ' .33.HB73': ' .108.HB73',
                                  ' .33.HBM':  ' .108.HBM',
                                  ' .33.HDM':  ' .108.HDM',
                                  ' .33.HGM':  ' .108.HGM',
                                  ' .33.HT2A': ' .108.HT2A',
                                  ' .33.HT4A': ' .108.HT4A',
                                  ' .33.QM1':  ' .108.QM1',
                                  ' .33.QM3':  ' .108.QM3',
                                  ' .33.QM5':  ' .108.QM5',
                                  ' .33.QM8':  ' .108.QM8',
                                  ' .33.QT2':  ' .108.QT2',
                                  ' .33.QT4':  ' .108.QT4', 
                                  ' .51.HA62': ' .109.HA62',
                                  ' .51.HA63': ' .109.HA63',
                                  ' .51.HA72': ' .109.HA72',
                                  ' .51.HA73': ' .109.HA73',
                                  ' .51.HAM':  ' .109.HAM',
                                  ' .51.HB62': ' .109.HB62',
                                  ' .51.HB63': ' .109.HB63',
                                  ' .51.HB72': ' .109.HB72',
                                  ' .51.HB73': ' .109.HB73',
                                  ' .51.HBM':  ' .109.HBM',
                                  ' .51.HDM':  ' .109.HDM',
                                  ' .51.HGM':  ' .109.HGM',
                                  ' .51.HT2A': ' .109.HT2A',
                                  ' .51.HT4A': ' .109.HT4A',
                                  ' .51.QM1':  ' .109.QM1',
                                  ' .51.QM3':  ' .109.QM3',
                                  ' .51.QM5':  ' .109.QM5',
                                  ' .51.QM8':  ' .109.QM8',
                                  ' .51.QT2':  ' .109.QT2',
                                  ' .51.QT4':  ' .109.QT4', 
                                  ' .82.HA62': ' .110.HA62',
                                  ' .82.HA63': ' .110.HA63',
                                  ' .82.HA72': ' .110.HA72',
                                  ' .82.HA73': ' .110.HA73',
                                  ' .82.HAM':  ' .110.HAM',
                                  ' .82.HB62': ' .110.HB62',
                                  ' .82.HB63': ' .110.HB63',
                                  ' .82.HB72': ' .110.HB72',
                                  ' .82.HB73': ' .110.HB73',
                                  ' .82.HBM':  ' .110.HBM',
                                  ' .82.HDM':  ' .110.HDM',
                                  ' .82.HGM':  ' .110.HGM',
                                  ' .82.HT2A': ' .110.HT2A',
                                  ' .82.HT4A': ' .110.HT4A',
                                  ' .82.QM1':  ' .110.QM1',
                                  ' .82.QM3':  ' .110.QM3',
                                  ' .82.QM5':  ' .110.QM5',
                                  ' .82.QM8':  ' .110.QM8',
                                  ' .82.QT2':  ' .110.QT2',
                                  ' .82.QT4':  ' .110.QT4'
                                  
                                  }
      }
    }
    
  },

'1a7i': {

  'readCoordinates': {
    'keywds': {
      'forceChainMappings': [[' ',' ',8,],['A',' ',1,0],['B',' ',1,0]]
      }
    }
  },

'1a8n': {

  'duplicateResonances': {' ': ['DNA1','DNA2']},   

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','DNA1',1,0],['B','DNA2',1,0]]
      }
    }
  },

'1a8w': {

  'duplicateResonances': {' ': ['DNA1','DNA2']},   

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','DNA1',1,0],['B','DNA2',1,0]]
      }
    }
  },

'1a93': {   

  'linkResonances': {
    'keywds': {
      'specificResNameMappings': {'a.10.HD1*': 'a.10.HD2','a.15.HB': 'a.15.HB*','a.27.HG2*': 'a.27.HG','b.12.HG*': 'b.12.HG2*'}
      }
    }
  },


'1aa3': {   

  'linkResonances': {
    'keywds': {
      'specificResNameMappings': {' .300.HA#': ' .300.HA',' .306.HG#': ' .306.HG2#'}
      }
    }
  },

'1aa9': {   

  'linkResonances': {
    'keywds': {
      # Several obvious resets... problems with ASP OD#, ILE HG# and THR HG1#
      'addNameMappings':  {'LEU': [['HG#','HG']],'VAL': [['HB#','HB']],'HIS': [['HD#','HD2'],['HE#','HE1']] }
      }
    }
  },

'1abz': {   

  'linkResonances': {
    'keywds': {
      'specificResNameMappings': {' .0.H2+': ' .0.H2_*',' .0.H3+': ' .0.H3_*',' .38.HN+': ' .38.HN',' .39.HN+': ' .39.HN_*'}
      }
    }
  },

'1ac0': {   

  'linkResonances': {
    'keywds': {
      'addNameMappings':  {'PRO': [['HA#','HA']],'GLC': [['H61','H6_1'],['H62','H6_2']]},
      'forceChainMappings': [[' ', ' ', 1, 508], ['A', 'BCD1', 1, 0], ['B', 'BCD2', 1, 0]]
      }
    }
  },

'1acz': {   

  'linkResonances': { 
    'keywds': {
      'forceChainMappings': [[' ',' ',1,508],['A','BCD1',1,0],['B','BCD2',1,0]]
      }
    }
  },

'1ad7': {   

  'linkResonances': {
    'keywds': {
      'addNameMappings':  {'GLY': [['HA','HA*']]},
      'specificResNameMappings': {'1.2.HG': '1.2.HG*'}
      }
    }
  },

'1af8': {   

  'linkResonances': {
    'keywds': {
      'specificResNameMappings': {' .78.HD2*': ' .78.HD1*'}
      }
    }
  },

'1afj': {   

  'linkResonances': {
    'keywds': { # HG not mapped, but not really a problem!
      'forceChainMappings': [[' ',' ',1,0],[' ','MER',1,0]]
      }
    }
  },

'1aft': {   

  'linkResonances': {
    'keywds': {
      'specificResNameMappings': {' .0.HA*': ' .0.H_*'}
      }
    }
  },

'1ag7': {   

  'linkResonances': {
    'keywds': {
      'addNameMappings':  {'HYP': [['HD11','HD21'],['HD12','HD22']]},
      'specificResNameMappings': {' .28.HB1': ' .28.HB'}
      }
    }
  }, 

'1ah1': {   # Has some serious sequence jumps...

  'linkResonances': {
    'keywds': { # HG not mapped, but not really a problem!
      'forceChainMappings': [[' ', ' ', 1, -1],[' ', ' ', 66, 1],[' ', ' ', 106, 2],['A',' ',1,131],['B',' ',1,135]]
      }
    }
  },

'1ai0': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ','wat1',1,0],['A','wat2',1,0],      # Water
                             ['B','phe1',1,0],['C','phe2',1,0],      # Phenol
                             ['D','phe3',1,0],['E','phe4',1,0],
                             ['F','phe5',1,0],['G','phe6',1,0],
                             ['H','acha',1,0],['N','bcha',1,0],      # Insulin
                             ['I','ccha',1,0],['O','dcha',1,0],      # Insulin
                             ['J','echa',1,0],['P','fcha',1,0],      # Insulin
                             ['K','gcha',1,0],['Q','hcha',1,0],      # Insulin
                             ['L','icha',1,0],['R','jcha',1,0],      # Insulin
                             ['M','kcha',1,0],['S','lcha',1,0],      # Insulin
                             ['T', 'zn1', 1, 0], ['U', 'zn2', 1, 0]] # Zn
      }
    }
  },

'1aiy': {

  'comment': "Mapping was adjusted after switching to mergeSTARFilesTest.py because the chains were arranged differently.",

##Created chain ' ', start seqCode 9, end seqCode 9, molecule 'Molecule1'...
##Created chain 'A', start seqCode 10, end seqCode 10, molecule 'Molecule1'...
##Created chain 'B', start seqCode 3, end seqCode 3, molecule 'PHENOL'...
##Created chain 'C', start seqCode 4, end seqCode 4, molecule 'PHENOL'...
##Created chain 'D', start seqCode 5, end seqCode 5, molecule 'PHENOL'...
##Created chain 'E', start seqCode 6, end seqCode 6, molecule 'PHENOL'...
##Created chain 'F', start seqCode 7, end seqCode 7, molecule 'PHENOL'...
##Created chain 'G', start seqCode 8, end seqCode 8, molecule 'PHENOL'...
##Created chain 'H', start seqCode 1, end seqCode 21, molecule 'R6 INSULIN HEXAMER (chain A)'...
##Created chain 'I', start seqCode 1, end seqCode 21, molecule 'R6 INSULIN HEXAMER (chain A)'...
##Created chain 'J', start seqCode 1, end seqCode 21, molecule 'R6 INSULIN HEXAMER (chain A)'...
##Created chain 'K', start seqCode 1, end seqCode 21, molecule 'R6 INSULIN HEXAMER (chain A)'...
##Created chain 'L', start seqCode 1, end seqCode 21, molecule 'R6 INSULIN HEXAMER (chain A)'...
##Created chain 'M', start seqCode 1, end seqCode 21, molecule 'R6 INSULIN HEXAMER (chain A)'...
##Created chain 'N', start seqCode 1, end seqCode 30, molecule 'R6 INSULIN HEXAMER (chain B)'...
##Created chain 'O', start seqCode 1, end seqCode 30, molecule 'R6 INSULIN HEXAMER (chain B)'...
##Created chain 'P', start seqCode 1, end seqCode 30, molecule 'R6 INSULIN HEXAMER (chain B)'...
##Created chain 'Q', start seqCode 1, end seqCode 30, molecule 'R6 INSULIN HEXAMER (chain B)'...
##Created chain 'R', start seqCode 1, end seqCode 30, molecule 'R6 INSULIN HEXAMER (chain B)'...
##Created chain 'S', start seqCode 1, end seqCode 30, molecule 'R6 INSULIN HEXAMER (chain B)'...
##Created chain 'T', start seqCode 1, end seqCode 1, molecule 'ZINC ION'...
##Created chain 'U', start seqCode 2, end seqCode 2, molecule 'ZINC ION'...

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ','wat1',1,0],['A','wat2',1,0],      # Water
                             ['B','phe1',1,0],['C','phe2',1,0],      # Phenol
                             ['D','phe3',1,0],['E','phe4',1,0],
                             ['F','phe5',1,0],['G','phe6',1,0],
                             ['H','acha',1,0],['N','bcha',1,0],      # Insulin
                             ['I','ccha',1,0],['O','dcha',1,0],      # Insulin
                             ['J','echa',1,0],['P','fcha',1,0],      # Insulin
                             ['K','gcha',1,0],['Q','hcha',1,0],      # Insulin
                             ['L','icha',1,0],['R','jcha',1,0],      # Insulin
                             ['M','kcha',1,0],['S','lcha',1,0],      # Insulin
                             ['T', 'zn1', 1, 0], ['U', 'zn2', 1, 0]] # Zn
      }
    }
  },

'1aj1': {   

  'linkResonances': {
    'keywds': {
      'namingSystem': 'MSI',
      'addNameMappings':  {'ABA': [['HB','HB*'],['HG2*','HG*']]},
      'specificResNameMappings': {'1.19.HBR': '1.19.HB_2','1.19.HBS': '1.19.HB_1','1.19.HN': '1.19.HN_1'}
      }
    }
  },

'1aj4': {   

  'linkResonances': {
    'keywds': { # Also map .16.OD2 to .16.OE1??
      'specificResNameMappings': {' .154.HD2': ' .154.HD2*',
                                  'CA1.1.CAL': 'A.1.CA',
                                  'CA2.1.CAL': 'B.1.CA',
                                  'CA3.1.CAL': 'C.1.CA'}
      }
    }
  },


##'1ajy': {
##
##  'duplicateResonances': {' ': ['A','B']},   
##
##  'linkResonances': {
##    'keywds': {
##      'forceChainMappings': [['A','A',1,29],['B','B',1,29],      # Protein
##                             ['A','a',1,29],['B','b',1,29],      # Protein
##                             ['C','A',1,100],['C','a',1,100],    # Zn
##                             ['D','A',1,101],['D','a',1,101],    # Zn
##                             ['E','B',1,100],['E','b',1,100],    # Zn
##                             ['F','B',1,101],['F','b',1,101]]    # Zn
##      }
##    }
##  },


'1al9': { # TODO: still problems with atom names HET grps

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0],  # DNA
                             ['B', ' ', 1, 6],  # DNA
                             ['C', ' ', 1, 16], # het grps
                             ['D', ' ', 1, 14]] # het grps
      }
    }
  },

'1amd': { # TODO: still problems with atom names HET grps

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0],  # DNA
                             ['B', ' ', 1, 6],  # DNA
                             ['C', ' ', 1, 12], # het grps
                             ['D', ' ', 1, 19]] # het grp
      }
    }
  },

'1ao9': { # TODO has insertion codes

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ','1',1,0] ]
      }
    }
  },

'1ap8': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['A',' ',1,0],      # Protein
                             [' ',' ',1,213],[' ',' ',1,213] ] # Het group
      }
    }
  },

##'1aps': {
##
##  'linkResonances': {
##    'keywds': {
##      'forceChainMappings': [[' ',' ',2,0]]
##      }
##    }
##  },
  
'1aqq': {   

  'linkResonances': {
    'keywds': {
      'specificResNameMappings': {' .9.AG': 'A.1.AG',
                                  ' .14.AG': 'B.1.AG',
                                  ' .20.AG': 'C.1.AG',
                                  ' .26.AG': 'D.1.AG',
                                  ' .30.AG': 'E.1.AG',
                                  ' .36.AG': 'F.1.AG',
                                  ' .38.AG': 'G.1.AG'}
      }
    }
  },

'1aqr': {   

  'linkResonances': {
    'keywds': {
      'specificResNameMappings': {' .9.CU': 'A.1.CU',
                                  ' .14.CU': 'B.1.CU',
                                  ' .20.CU': 'C.1.CU',
                                  ' .26.CU': 'D.1.CU',
                                  ' .30.CU': 'E.1.CU',
                                  ' .36.CU': 'F.1.CU',
                                  ' .38.CU': 'G.1.CU'}
      }
    }
  },
  
'1aqs': {   

  'linkResonances': {
    'keywds': {
      'namingSystem': 'XPLOR',
      'specificResNameMappings': {' .9.CU': 'A.1.CU',
                                  ' .14.CU': 'B.1.CU',
                                  ' .20.CU': 'C.1.CU',
                                  ' .26.CU': 'D.1.CU',
                                  ' .30.CU': 'E.1.CU',
                                  ' .36.CU': 'F.1.CU',
                                  ' .38.CU': 'G.1.CU'}
      }
    }
  },

'1as5': {   

  'linkResonances': {
    'keywds': {
      'namingSystem': 'MSI'
      }
    }
  },

'1at4': { # TODO has insertion codes

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ','1',1,0] ]
      }
    }
  },

'1atx': {

  'readCoordinates': {
    'keywds': {
      'addNameMappings':  {'ALL': [['3HB','1HB'],['3HE','1HE'],['3HG1','1HG1']]} 
      }
    }
  },
  
### TODO 1au5: has atom name problems
##
##'1au6': { # TODO has atom name problems (see 1au5)
##
##  'linkResonances': {
##    'keywds': {
##      'forceChainMappings': [['A', ' ', 1, 0], ['B', ' ', 1, 8], [' ', ' ', 1, 16]]
##      }
##    }
##  },

'1ax7': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,13]]
      }
    }
  },

'1axl': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,11]]
      }
    }
  },

'1axp': { # TODO has insertion codes for chain B

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1',1,0]]
      }
    }
  },

'1axu': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,11]]
      }
    }
  },

'1ay3': {  # TODO this looks like one molecule, connected by 'other' residue...

  'readCoordinates': {
    'keywds': {
      'addNameMappings':  {'GLU': [['OD1','OE1']]} 
      }
    },

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1',1,2],['B','1',1,0],['C','1',1,3]]
      }
    }
  },

'1b3p': {

  'duplicateResonances': {' ': ['DNA1','DNA2']},

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','DNA1',1,0],['B','DNA2',1,0]]
      }
    }
  },

# TODO: 1b5k atom naming problems for HET grp.

'1b6y': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','STR1',1,0],['B','STR2',1,0]]
      }
    }
  },

'1b9r': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],[' ',' ',1,105]]
      }
    }
  },
 
'1bbx': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,12],['C','C',1,0],['D','D',1,0],['B','b',5,12]]
      }
    }
  },

'1bc6': {  

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ', ' ', 1, 0], ['A', ' ', 1, 77], ['B', ' ', 1, 78]]
      }
    }
  },

'1bd6': {  

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ', ' ', 1, 0], ['A', ' ', 1, 77], ['B', ' ', 1, 78]]
      }
    }
  },

'1bcb': {  

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1',1,0],['B','1',1,6],['C','1',1,12]]
      }
    }
  },

'1bfw': {  # TODO: 1 molecule, but D-amino acids AND inverse numbering - toughie
           # this linkResonances mapping is not correct! Is one molecule, but is being split up...

  'readCoordinates': {
    'keywds': {
      'addNameMappings':  {'ALL': [['1HN','HN2'],['HOD','HD2']]} 
      }
    },

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ',' ',1,158],[' ',' ',2,156],[' ',' ',3,154]]
      }
    }
  },

'1bfy': {  

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ', ' ', 1, 54], ['A', ' ', 1, 0]]
      }
    }
  },

'1bm6': {  

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ', 'CGS2', 1, 2], 
                             ['A', 'CGS2', 1, 1], 
                             ['B', 'IONS', 1, 257], 
                             ['C', 'IONS', 1, 258], 
                             ['D', 'CGS2', 1, 0], 
                             ['E', 'SLNA', 1, 82], 
                             ['F', 'IONS', 1, 255], 
                             ['G', 'IONS', 1, 256]]
      }
    }
  },
  
'1bp8': {

  'readCoordinates': {
    'keywds': {
      'addNameMappings':  {'ALL': [['1H3M',"1H3'"],['2H3M',"2H3'"],['3H3M',"3H3'"],['C3M',"C3"]]} 
      }
    }
  },

'1bqx': {  

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0], ['B', ' ', 1, 77], ['C', ' ', 1, 78]]
      }
    }
  },

'1buf': {  # TODO: not sure about ' ' code mapping... other molecule?

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1buf_amber001',1,0],['A',' ',1,0],
                             ['B','1buf_amber002',1,6],['B',' ',1,6]]
      }
    }
  },

'1bve': { 

  'linkResonances': {
    'keywds': {
      'addNameMappings':  {'DMP': [['H201',"H20_1"],['H202',"H20_2"],['H271',"H27_1"],['H272',"H27_2"],
                                   ['H301',"H30_1"],['H302',"H30_2"],['H601',"H60_1"],['H602',"H60_2"],
                                   ['H701',"H70_1"],['H702',"H70_2"],['H771',"H77_1"],['H772',"H77_2"]]}, 
      'forceChainMappings': [['A', ' ', 1, 0], ['B', ' ', 1, 100], ['C', ' ', 1, 322]]
      }
    }
  },

'1bwe': {  

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0], ['B', ' ', 1, 77], ['C', ' ', 1, 78]]
      }
    }
  },

'1bwt': {  

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1bwt_amber001',5,0],['A',' ',1,0],
                             ['B','1bwt_amber002',5,10],['B',' ',1,10]]
      }
    }
  },

'1bxd': {  

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ', ' ', 1, 450], ['A', ' ', 1, 289]]
      }
    }
  },

'1byv': {  # TODO has insertion code 1G (for seqCode 300 residue?)

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ', '1', 1, 32], ['A', '1', 1, 0], ['B', '1', 1, 299]]
      }
    }
  },

# TODO: 1bzb: has insertion codes for sugars

'1c6s': {  # TODO problems with atom names HEME group

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ', 'CYTO', 1, 0], [' ', ' ', 1, 0], ['A', 'HEME', 1, 0]]
      }
    }
  },

'1cfa': {  # TODO problems with atom names HEME group

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 2, 0], ['A', 'SEMI', 2, 0], ['B', ' ', 1, 71], ['B', 'SEMI', 1, 71]]
      }
    }
  },

'1ccf': {

  'readCoordinates': {
    'keywds': {
      'addNameMappings':  {'GLN': [['HE2',"1HE2"]], 'ASP': [['HB',"QB"]]} 
      }
    }
  },

'1cfp': {  # TODO check if this is OK

  'duplicateResonances': {' ': ['a','b']},

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','a',1,-1],
                             ['B','b',1,-1]]
      }
    }
  },

'1cqo': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,10]]
      }
    }
  },

'1cyz': { # TODO: problems with chains/residue matching and atom names

  'linkResonances': {
    'keywds': {
      'forceChainMappings':  [[' ', ' ', 1, 11], ['A', ' ', 1, 25], ['B', ' ', 1, 0], ['C', ' ', 1, 15]]
      }
    }
  },

'1d2l': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 45], ['B', ' ', 1, 0]]
      }
    }
  },

'1d6d': {

  'readCoordinates': {
    'keywds': {
      'addNameMappings':  {'G': [['HO3',"HO3*"]]} 
      }
    }
  },

'1daq': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ', ' ', 1, 83], ['A', ' ', 1, 95], ['B', ' ', 1, 0]]
      }
    }
  },

'1dav': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ', ' ', 1, 83], ['A', ' ', 1, 95], ['B', ' ', 1, 0]]
      }
    }
  },

##'1dhh': {
##
##  'linkResonances': {
##    'keywds': {
##      'forceChainMappings': [['A',' ',1,0],['B',' ',1,9]]
##      }
##    }
##  },

'1dip': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',1,-1],
                             ['B','B',1,-1]]
      }
    }
  },

'1djd': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['B','1DNA',1,0],
                             ['C','2DNA',1,11]]
      }
    }
  },

'1dl4': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1DNA',1,0],
                             ['B','2DNA',1,11]]
      }
    }
  },

'1dlz': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],
                             ['B',' ',1,1]]
      }
    }
  },

##'1drn': { 
##
##  'linkResonances': {
##    'keywds': {
##      'forceChainMappings': [['A',' ',1,0],
##                             ['B',' ',1,9]]
##      }
##    }
##  },

'1eio': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0]]
      }
    }
  },

'1eka': {  # TODO TODO INSERTION CODES

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1',1,0]]# Problem: codes 1B, 2B, ... for chain B!,['B','1',1,0]]
      }
    }
  },

'1ekd': {  # TODO TODO INSERTION CODES

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1',1,0]]# Problem: codes 1B, 2B, ... for chain B!,['B','1',1,0]]
      }
    }
  },

'1f8p': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',3,0]]
      }
    }
  },

'1fre': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ',' ',1,0]]
      }
    }
  },

'1fzp': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',8,0]]
      }
    }
  },

'1gjx': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',13,0]]
      }
    }
  },

'1go0': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',5,98]]
      }
    }
  },

'1gtc': {  # TODO TODO INSERTION CODES

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1',1,0]]# Problem: codes 1B, 2B, ... for chain B!,['B','1',1,0]]
      }
    }
  },


'1hbw': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','a',5,49],
                             ['B','b',5,49]]
      }
    }
  },


'1hze': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],
                             ['B','B',1,0],
                             [' ','RIBA',1,97]]  # TODO: also chain 'C' RIBOFLAVINE, but no restraints?
      }
    }
  },

'1i18': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],
                             ['B','B',1,0],
                             [' ','RIBA',1,97]]  # TODO: also chain 'C' RIBOFLAVINE, but no restraints?
      }
    }
  },

'1i7v': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1DNA',1,0],
                             ['B','2DNA',1,11]]
      }
    }
  },


'1ibi': { 

  'linkResonances': {
    'keywds': {
      'addNameMappings':  {'TYR': [['CG1',"CG"]]},
      'forceChainMappings': [['A',' ',1,81],['A','PEPT',1,81]]
      }
    }
  },

'1icy': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',4,0]]
      }
    }
  },

'1ilp': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1',1,0] # TODO PROBLEMS WITH INSERTION CODES, and mapping not clear
                             ]
      }
    }
  },

'1imu': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',4,0]]
      }
    }
  },

'1jar': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',2,0]]
      }
    }
  },

'1jkn': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','P',2,0],[' ','A',1,0]]
      }
    }
  },

'1jo1': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','DNA1',1,0],['B','DNA2',1,0],['C','DRG1',1,0],['D','DRG2',1,0]]
      }
    }
  },

'1jsa': { # Has Ca ions
  'comment':
"""
Created chain ' ', start seqCode 500, end seqCode 500, molecule 'CALCIUM ION'...
Created chain 'A', start seqCode 501, end seqCode 501, molecule 'CALCIUM ION'...
Created chain 'B', start seqCode 0, end seqCode 201, molecule 'RECOVERIN'...

Needs first residue number in PDB file modified to zero to be sequential.
Noted by Wim to EBI PDB annotators.
""",
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['B', ' ', 1, 0], [' ', ' ', 1, 499], ['A', ' ', 1, 500]]
      }
    }
  },

##'1ju7': { 
##
##  'linkResonances': {
##    'keywds': {
##      'forceChainMappings': [['A', ' ', 1, 0],['A', 'HIST', 1, 0]]
##      }
##    }
##  },

'1juu': { # TODO: B actually has insertion codes (1B, 2B, ..) in its numbering

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', '1', 1, 0], ['B', '1', 1, 11]]
      }
    }
  },

##'1jwc': { 
##
##  'linkResonances': {
##    'keywds': {
##      'forceChainMappings': [['A', ' ', 1, 0],['A', 'HIST', 1, 0]]
##      }
##    }
##  },

'1jy6': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',12,0],['B',' ',12,200]]
      }
    }
  },

'1jy9': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',2,0]]
      }
    }
  },

'1jzp': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0]]
      }
    }
  },

'1k09': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', 'M1', 2, 0],['B', 'M2', 2, 0]]
      }
    }
  },

'1k0t': { # TODO Still some problems with FE/SE constraints (not handled)

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 80], ['B', ' ', 1, 81], ['C', ' ', 1, 0]]
      }
    }
  },

'1k43': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0]]
      }
    }
  },

'1k5w': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 499], ['B', ' ', 1, 500], ['C', ' ', 1, 269]]
      }
    }
  },

'1kdx': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',2,585],['B',' ',1,118]]
      }
    }
  },
  
# TODO 1kkv: has insertion codes
# TODO 1kmr: has insertion codes

'1krx': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 124], ['B', ' ', 1, 0]]
      }
    }
  },
  
# TODO 1kqe: has modified amino acids, atom name problems

'1kwj': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,68],['C',' ',1,69],['D',' ',1,70]]
      }
    }
  },

'1kvj': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 84], ['B', ' ', 1, 0]]
      }
    }
  },

'1kvz': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',3,0]]
      }
    }
  },

'1kyj': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, -1], ['B', ' ', 1, 6], ['C', ' ', 1, 9], ['D', ' ', 1, 12]]
      }
    }
  },

'1l1v': {  #TODO insertion codes mapping!
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1',1,0],['B','2',1,16]]
      }
    }
  },

'1la3': {

  'linkResonances': { # A is Ca ion
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 500], ['B', ' ', 1, 0]]
      }
    }
  },

'1laq': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,13]]
      }
    }
  },

'1las': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,13]]
      }
    }
  },
  
# TODO: 1lcm, modified peptide, atom names badly matched

'1lfu': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', 'A', 1, 0], ['B', 'A', 1, 14], ['P', 'P', 1, 0]]
      }
    }
  },

'1lmv': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', 'a', 1, 0], ['B', 'b', 1, 0],['A', 'A', 1, 0], ['B', 'B', 1, 0]]
      }
    }
  },

'1lpw': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', 'a', 1, 0], ['B', 'b', 1, 0],['A', 'A', 1, 0], ['B', 'B', 1, 0]]
      }
    }
  },

'1m0j': { # Includes some resonances for sequence bit before what is in the PDB 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 100], ['B', ' ', 1, 101],['C', ' ', 1, 102],['D', ' ', 1, 7]]
      }
    }
  },

'1m4o': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ', ' ', 1, 179], ['A', ' ', 1, 0]]
      }
    }
  },

'1m9l': {

  'comment': 'Has insertion codes',
  
  },

'1mak': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ',' ',2,0]]
      }
    }
  },

'1mdi': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 200], ['B', ' ', 1, 201], ['C', ' ', 1, 202], ['D', ' ', 1, 203], ['E', ' ', 1, 204], ['F', ' ', 1, 205], ['G', ' ', 1, 105], ['H', ' ', 1, 0]]
      }
    }
  },

'1me0': { 

  'linkResonances': {
    'keywds': {
      'namingSystem': 'XPLOR',
      'forceChainMappings': [['A', ' ', 1, 0]]
      }
    }
  },

'1mp7': { 

  'linkResonances': {
    'keywds': {
      'namingSystem': 'XPLOR',
      'forceChainMappings': [['A', ' ', 1, 0], [' ', ' ', 1, 10]]
      }
    }
  },

'1mtg': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0], ['B', ' ', 1, 6], ['C', ' ', 1, 20]]
      }
    }
  },

# TODO 1muv: has insertion codes
# TODO 1mv1: has insertion codes
# TODO 1mv2: has insertion codes
# TODO 1mv6: has insertion codes
  
'1mwn': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['X','pep1',1,0],
                             ['Y','pep2',1,0],
                             ['E','sbt1',1,-1],
                             ['F','sbt2',1,-1],
                             ['A','cap1',1,0],  #CA
                             ['B','cap2',1,0],  #CA
                             ['C','cat1',1,0],  #CA
                             ['D','cat2',1,0]   #CA
                            ]
      }
    }
  },
  
# TODO: 1mxk, has atom name problems

##'1n53': { 
##
##  'linkResonances': {
##    'keywds': {
##      'forceChainMappings': [['A',' ',1,0],['B',' ',1,16]]
##      }
##    }
##  },

'1nao': { # Has atom name problems

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,9]]
      }
    }
  },

'1nev': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,10],['A','a',1,0],['B','b',1,10]]
      }
    }
  },
  
'1nvl': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['A','ACBP',1,0],[' ','PCOA',1,0],['B','PCOA',1,2]]
      }
    }
  },
  
'1nvo': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',2,-1],['B',' ',2,99]]
      }
    }
  },

'1ny8': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',8,0]]
      }
    }
  },

'1o4x': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',8,0],['B',' ',6,200],['C',' ',1,300],['D',' ',1,319]]
      }
    }
  },

'1oqp': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',3,92],['B',' ',2,238]]
      }
    }
  },

'1p7e': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',2,0]]
      }
    }
  },

'1p7f': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',2,0]]
      }
    }
  },

'1pik': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','DNA1',1,0],['B','DNA2',1,10],['C','ESPR',1,20]]
      }
    }
  },

'1q38': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',11,0]]
      }
    }
  },

'1qvx': { # Mapping from looking at structure in viewer... should be OK

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',6,9]]
      }
    }
  },

'1rfl': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',3,0]]
      }
    }
  },

'1s37': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', 'DNA1', 1, 0], ['B', 'DNA2', 1, 0]]
      }
    }
  },

'1s6d': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',4,0]]
      }
    }
  },

'1s6i': { 

  'comment': "Has some to-residue constraints (chain code 'I')",
  
  },

'1s9l': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['A','1',1,0],
                             ['B',' ',1,100],['B','1',1,100],
                             ['C',' ',1,200],['C','1',1,200],
                             ['D',' ',1,300],['D','1',1,300]] 
      }
    }
  },

'1saa': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1',1,0]]  # TODO chain B matches insertion codes!!
      }
    }
  },

'1ss3': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',2,0]]
      }
    }
  },

'1sxd': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',4,163]]
      }
    }
  },

'1sxm': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ',' ',1,0]]
      }
    }
  },

'1sy8': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1',1,0],['A','2',1,0]]  # TODO chain B matches insertion code B!!
      }
    }
  },

'1t4x': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,6]]
      }
    }
  },

'1te4': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',29,-20]]
      }
    }
  },

'1tne': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,6],['C',' ',1,3],['D',' ',1,9]]
      }
    }
  },

'1ttn': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',24,0]]
      }
    }
  },

'1txp': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,50],['C',' ',1,100],['D',' ',1,150]]
      }
    }
  },

'1umt': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','1',1,0]]
      }
    }
  },

'1vrc': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',3,0],['B','B',3,0],['C','C',2,200],['D','D',2,200]]
      }
    }
  },

'1vrv': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',2,10]]
      }
    }
  },

'1wib': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',9,0]]
      }
    }
  },

'1wvk': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',45,0]]
      }
    }
  },

'1x9v': { # TODO there is also a ' ' chainCode on format side - check what that is.

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','VPR1',3,51],['B','VPR2',3,51]]
      }
    }
  },

'1xkm': { # TODO this is probably not right - have to recheck...

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',2,0],['B',' ',1,22],['C',' ',2,47],['D',' ',1,70]]
      }
    }
  },

'1xnt': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',2,0]]
      }
    }
  },

'1xq8': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',2,0]]
      }
    }
  },

'1xv3': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',23,0]]
      }
    }
  },

'1xx0': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',13,223]]
      }
    }
  },

'1yl9': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,1]]
      }
    }
  },

'1ysy': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',4,0]]
      }
    }
  },

'1zbj': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0]]
      }
    }
  },

'1zgu': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]]
      }
    }
  },


'1zzf': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','a',1,0],['B','b',1,0],['A','A',1,0],['B','B',1,0]]
      }
    }
  },

'2a00': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',21,295],[' ','ANP',1,0]]
      }
    }
  },

'2b6g': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',39,-38],['B',' ',1,100]]
      }
    }
  },

'2baf': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0]]
      }
    }
  },

'2bjc': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',2,0],['A',' ',2,0],['B','A',2,100],['B',' ',2,100],['C','C',1,0],['D','C',1,100]]
      }
    }
  },

'2cpm': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',8,0]]
      }
    }
  },

'2cqe': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',8,0]]
      }
    }
  },

'2cqn': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',8,0]]
      }
    }
  },

'2ezw': { 

  'linkResonances': {
    'keywds': {
      'formatChainCodes': {' ': ['A','B']},  # cross terms! TODO is this working?
      'forceChainMappings': [['A','A',1,0],['A','a',1,0],['B','B',1,0],['B','b',1,0]]
      }
    }
  },

'2few': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',49,0],['B',' ',7,374]]
      }
    }
  },

'2fj6': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['A','A',1,0]]
      }
    }
  },

'2fws': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 599], ['B', ' ', 1, 649], ['C', ' ', 1, 370]]
      }
    }
  },

'3ctn': {

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ','CA2',1,0],['A','CA3',1,0],['B',' ',1,85]]
      }
    }
  },

'4ull': { # TODO: this is probably not correct...

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [[' ','VT1',5,0],[' ','VT2',5,0],[' ','VT3',5,0],[' ','VT4',5,0],[' ','VT5',5,0]]
      }
    }
  },

#
# JURGEN MAPPINGS BELOW
#

'1rjj': { 
  # JFD first tries at adding something:
  ## Modelled after 1dom
  ## The internal names for the chains are a and b.
  ## The external names are ' ' or A and B for restrains
  ##    and A and B for the PDB coordinates.
  #'duplicateResonances': {' ': ['a','b']},

  'readCoordinates': {
    'keywds': {
      ##
      'forceChainMappings': [['A','A',1,0],['B','B',1,0]],
      }
    },

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,300]]
      }
    } 
  },

'1b4y': {
  # Results:
  #   large violations on lower bounds because of sum averaging method.
  #   e.g. model 12 :25@Q2* :26@Q7 has distance: 5.55 center averaged and lowerbound: 5.5
  #   in sum averaging the distance is only: 3.947 so violated by 1.5 Ang.
  #   When run with center averaging the max violation is only 0.6 and it is an upp violation.
  #
  ## The PDB numbers: 17-26,  1-16, 27-30
  ## In CCPN numbers:  1-10, 11-26, 27-30 
  ## Restraints are a little more complex.
  # ^PDB numbers range
  #       ^CCPN numbers start at
  #          ^ Offset (ccpn-pdb)
  #            ^ PDB chain ids
  # 17-22  1 -16  S3
  # 23-26  7 -16  L2
  # 1-6   11  10  S1 (strand)
  # 7-10  17  10  L1 (loop)
  # 11-16 21  10  S2
  # 27-30 27   0   T (tail)  
##  'readCoordinates': { Not needed because FC takes sequence from SEQ records in PDB file.
##    'keywds': {
##      #[chainCode, formatChainCode, firstSeqId, offset]
##      'forceChainMappings': [
##        ['A','A', 1, 16],
##        ['A','A',11,-10],
##        ['A','A',27,  0]
##      ]
##    }      
##  },
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A','S3',  1, 16],
        ['A','L2',  7, 16],
        ['A','S1', 11,-10],
        ['A','L1', 17,-10],
        ['A','S2', 21,-10],
        ['A','T',  27,  0]
      ],
      'addNameMappings':  {
# Note that the ORIGINAL residue names should be used and not: DA, DG, DC.
        'A': [["HN*", 'H6*'],["HN'", 'H6*'],["HN''", 'H6*'],["HN'*", 'H6*']],
        'G': [["HN*", 'H2*'],["HN'", 'H2*'],["HN''", 'H2*'],["HN'*", 'H2*']],
        'C': [["HN*", 'H4*'],["HN'", 'H4*'],["HN''", 'H4*'],["HN'*", 'H4*']]
        }                                                        
   } 
  }
 },
'1zfs': { 
##  'readCoordinates': { 
##    'keywds': {
##      'forceChainMappings': [
##        ['A','A',1,0],
##        ['B','B',1,0],
##        ['C',' ',1,100],
##        ['C',' ',1,101],
##        ['C',' ',1,102],
##        ['C',' ',1,103]
##        ]
##      }
##    },
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['D','sam1',1,0],
        ['E','sam2',1,0],
        [' ','cap1',1,0],
        ['A','cap2',1,0],
        ['B','cat1',1,0],
        ['C','cat2',1,0]
        ]    
      }
    } 
  },
'2ff0': { 
  # Found matching residues through the series of Cys:
  # Restraints: 27,30,44,47
  # SEQRES       4, 7,21,24
  # So there's a diff of 23.
  # note occurances of both: segid SF1 and segid "SF1 "
  # but FC will automatically truncate that from the restraints.
  # Note that there are still >1000 error messages in the merge log but
  # majority of restraints are mapped.
  'linkResonances': { 
    'keywds': {
      'forceChainMappings': [
        ['C','SBS',1,15], # CTGTGGCCCTGAGCC
        ['A','SF1',1,23], ## protein
        ['B','SBS',1,0], # GGCTCAGGGCCACAG
        ['D','ZN2',1,0], # seqCode 1001, molecule 'ZINC ION'
        ['E','ZN2',1,1]  # seqCode 1002, molecule 'ZINC ION'
        ]    
      }
    } 
  },
'1x26': { 
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['B',' ',1,11], # molecule '5'-D(*CP*AP*TP*TP*CP*AP*GP*TP*TP*AP*G)-3''
        ['A',' ',1,0],  # molecule '5'-D(*CP*TP*AP*AP*CP*AP*GP*AP*AP*TP*G)-3''...
        [' ',' ',1,23], # 24, molecule 'N~3~-{3-[(7-METHYL-1,8-NAPHTHYRIDIN-2-YL)AMINO]-3-OXOPROPYL}-N~1~-[(7-OXO-7,8-'...
        ['C',' ',1,24]  # 25, molecule 'N~3~-{3-[(7-METHYL-1,8-NAPHTHYRIDIN-2-YL)AMINO]-3-OXOPROPYL}-N~1~-[(7-OXO-7,8-'...
        ], 
      'addNameMappings':  {
        'T': [["H2'","H2'"],["H2''","H2''"],["H7#", 'M7']],
        'A': [["H2'","H2'"],["H2''","H2''"]],
        'C': [["H2'","H2'"],["H2''","H2''"]],
        'G': [["H2'","H2'"],["H2''","H2''"]]        
        }
    # Wim, why did the below didn't fix the problem with the h2' and h2''.
##      'namingSystem': 'XPLOR', ## Forces the names in the restraint lists to be read as xplor names
##      'useIupacMatching': 2    ## Allows 'additional' matching on iupac names.
    }
  }
  },
'1znu': { ## First ~8 residues are numbered last. found with Wim's help.
  'linkResonances': {
    'keywds': { ## Improved from FCs output:   Final mapping: [['A', ' ', 8, 112]]
      'forceChainMappings': [['A',' ',1,112],['A',' ',1,141]]
      }}
  },
'2ffw': {
  'linkResonances': {
##Created chain 'A', start seqCode 87, end seqCode 164, molecule 'MIDLINE-1'...
##Created chain ' ', start seqCode 200, end seqCode 200, molecule 'ZINC ION'...
##Created chain 'B', start seqCode 201, end seqCode 201, molecule 'ZINC ION'...
    
    'keywds': { ## Improved from FCs output:   Final mapping:
                          # [[' ', ' ', 1, 88], ['A', ' ', 1, 86], ['B', ' ', 1, 89]]
      'forceChainMappings': [['A',' ',1,86],['B',' ',1,200],[' ',' ',1,199]],
      'specificResNameMappings': {' .119.ZN': ' .200.ZN',
                                  ' .134.ZN': ' .201.ZN'}      }
  }
  },
'2gov': {
  # Asked author for distance restraints for this one and entry 2gow.
  # Created chain 'A', start seqCode -4, end seqCode 190, molecule 'HEME-BINDING PROTEIN 1'...
  # Matched from dihedral restraints sequence pro 17, trp 18, gln 19.
                          # seqres records        22      etc.
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, -5]]
      }
  }
},
'2gow': { # Asked author for distance restraints for this one and entry 2gow.
  # Created chain 'A', start seqCode -4, end seqCode 190, molecule 'HEME-BINDING PROTEIN 1'...
  # Matched from distance restraints sequence 5 VPA..
                          # seqres records  13  etc.
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, -8]]
      }
  }
},
## From the restraint file:
##!     1  2  3  4  5     6  7  8  9  10
##! 5'- C  G  C  A  T[6-4]T  A  C  G  C -3' : 64TT strand
##! 3'- G  C  G  T  A     G  T  G  C  G -5' : CPGA strand
##!     20 19 18 17 16    15 14 13 12 11
##Created chain 'A', start seqCode 1, end seqCode 10, molecule 'DNA (5'-D(*CP*GP*CP*AP*(HYD)TP*+TP*AP*CP*GP*C)- DNA (5'-D(*CP*GP*CP*AP*(HYD)TP'...
##Created chain 'B', start seqCode 11, end seqCode 20, molecule 'DNA (5'-D(*GP*CP*GP*TP*GP*AP*TP*GP*CP*G)-3')'...
##Created chain 'C', start seqCode 5, end seqCode 5, molecule 'HYDROXY GROUP'...
'1cfl': { 
 'linkResonances': {
    'keywds': {
##      'forceChainMappings': [['A', '64TT', 1, 0], ['B', 'CPGA', 1, 10]]
      'addNameMappings':  {
        'T': [["1H2'","H2'"],["2H2'","H2''"],["#H5M", 'M7']],
        'A': [["1H2'","H2'"],["2H2'","H2''"]],
        'C': [["1H2'","H2'"],["2H2'","H2''"]],
        'G': [["1H2'","H2'"],["2H2'","H2''"]]        
        }
      }
  }
 },
'1m9o': { # restraints: cys: 15,24,30, same for seqres.
  # correction from: Final mapping: [[' ', ' ', 1, 6], ['A', ' ', 6, -1]]
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0]]
      }
  }
},
#  FC Final mapping: [['A', ' ', 1, 27], ['B', ' ', 15, 11]]
#Created chain 'A', start seqCode 169, end seqCode 169, molecule '4'-HYDROXYCINNAMIC ACID'...
#Created chain 'B', start seqCode 13, end seqCode 125, molecule 'PHOTOACTIVE YELLOW PROTEIN'...
'1xfq': { # note unique NOE ass; 
  # HA2  -> GLY 29,35,37, | matches at offset 12
  # HG12 -> ILE 31
  # HD21 -> ASN 43
  # Put this logic in guessOffset.py callable by guessOffSet.csh.
  # Large violations of >4Ang. still present:
#170 2  22 ASP HB2  2  99 LYS HB2  5.300 . 6.000 9.880 8.798 10.741  4.741  6 20  [*****+-*************]  1 1
  # weird because in the stereo ass. analysis results the largest viol. is only .219 for
  # the 2 triplets involved; is it a ambi?
  #
  # Not linked residue 69 which is 169 ligand perhaps?
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [['B', ' ', 1, 12]]
      }
  }
},
#Created chain 'A', start seqCode 1, end seqCode 8, molecule 'DNA (5'-D(*GP*AP*CP*AP*TP*AP*GP*C)-3''...
#Created chain 'B', start seqCode 9, end seqCode 17, molecule 'PEPTIDE NUCLEIC ACID PEPTIDE NUCLEIC ACID'...
#  Warning: Did not map CCPN chain codes ['B']
#  Warning: Did not map resonance chain codes ['S2']
#  Final mapping: [['A', 'S1', 1, 0]]
'1pdt': { 
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','S1',1,0],['B','S2',1,8]]
      }
    } 
  },

#Created molecule HISTONE ACETYLTRANSFERASE PCAF (molType protein, 118 chemComps)
#Created chain 'A', start seqCode 715, end seqCode 832, molecule 'HISTONE ACETYLTRANSFERASE PCAF'...
'1zs5': { 
  'comment': "A bug in FC (FC161) leads to pdb2STAR to fail.",
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','PROT',1,0]]
      }
    } 
  },
#Created molecule HYPOTHETICAL PROTEIN YNR034W-AP (molType protein, 120 chemComps)
#Created chain 'A', start seqCode -21, end seqCode 98, molecule 'HYPOTHETICAL PROTEIN YNR034W-AP'...
#No idea why this map is needed for FC fails without it.
#'2grg': { 
#  'linkResonances': {
#    'keywds': {
#      'forceChainMappings': [['A',' ',1,0]]
#      }
#    } 
#  },
#Created molecule CADMIUM ION (molType other, 1 chemComps)
##Created molecule METALLOTHIONEIN-3 (molType protein, 37 chemComps)
##Created chain 'A', start seqCode 69, end seqCode 69, molecule 'CADMIUM ION'...
##Created chain 'B', start seqCode 70, end seqCode 70, molecule 'CADMIUM ION'...
##Created chain 'C', start seqCode 71, end seqCode 71, molecule 'CADMIUM ION'...
##Created chain 'D', start seqCode 72, end seqCode 72, molecule 'CADMIUM ION'...
##Created chain 'E', start seqCode 32, end seqCode 68, molecule 'METALLOTHIONEIN-3'...
'2f5h': { 
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['E',' ',1,31]]
      }
    } 
  },

#Created molecule U1 SMALL NUCLEAR RIBONUCLEOPROTEIN A (molType protein, 127 chemComps)
#Created chain 'A', start seqCode 53, end seqCode 76, molecule 'U1 SMALL NUCLEAR RIBONUCLEOPROTEIN A'...
'2a3j': { 
   'readCoordinates': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0]],
      }
    },
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0]]
      }
    } 
  },
##Created molecule HYPOTHETICAL 24.6 KDA PROTEIN IN ILV2-ADE17 HYPOTHETICAL 24.6 KDA PROTEIN IN I (molType protein, 77 chemComps)
##Created molecule HYPOTHETICAL 25.2 KDA PROTEIN IN AFG3-SEB2 HYPOTHETICAL 25.2 KDA PROTEIN IN AF (molType protein, 98 chemComps)
##Created chain 'B', start seqCode 137, end seqCode 213, molecule 'HYPOTHETICAL 24.6 KDA PROTEIN IN ILV2-ADE17 HYPOTHETICAL 24.6 KDA PROTEIN IN I'...
##Created chain 'A', start seqCode 155, end seqCode 221, molecule 'HYPOTHETICAL 25.2 KDA PROTEIN IN AFG3-SEB2 HYPOTHETICAL 25.2 KDA PROTEIN IN AF'...
##  Final mapping: [['A', 'AN1', 10, 123], ['B', 'AN2', 20, 136]]
## That's actually to right mapping. The merge step still fails but it's probably not the mapping problem?
'2fv4': { 
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', 'AN1', 1, 123], ['B', 'AN2', 1, 136]]
      }
    } 
  },
'2axk': { 
 'linkResonances': {
    'keywds': {
##      'namingSystem': 'XPLOR-IUPAC', # Entry uses HB3s etc. but also HG1%. Defined a new Aqua map for it.
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2
      }
    } 
  },
##'2frw': {  # Authors didn't submit first 15 residues for seqres eventhough there are a few restraints for them.
##  },
'2g1g': { 
 'linkResonances': {
    'keywds': {
       'addNameMappings':  {
        'T6A': [
          ["CRG", "C15"],
          ["H2''","H2'"],
          ["H5'", "H5'_1"],
          ["H5''","H5'_2"],
          ["HRA", "H12"],
          ["HRB", "H14"],
          ],
        'C': [
          ["H2''","H2'"],
          ["H3''","H3'"],
          ],
        'A': [["H2''","H2'"]], # by request of authors. Otherwise mapped to HO2' which is silly
        'G': [["H2''","H2'"]],
        'T': [["H2''","H2'"]],
        'U': [["H2''","H2'"]],
     }
    } 
  }
 },
'2auv': { 
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [['B', ' ', 1, 0]]
      }
    } 
  },
'2fey': { 
 'linkResonances': {
    'keywds': {
       'addNameMappings':  {
        'C': [["H2''","H2'"]],
        'A': [["H2''","H2'"]], # Otherwise mapped to HO2' which is rare
        'G': [["H2''","H2'"]],
        'T': [["H2''","H2'"]],
        'U': [["H2''","H2'"]],
     }
    } 
  }
 },
'2aje': { 
 'linkResonances': {
    'keywds': {
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2
      }
    } 
  },
'2ge2': { 
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', 'SEG1', 1, 0],['B', 'SEG2', 1, 0],['A', 'AAF1', 1, -11]]
      }
    } 
  },
##Created molecule RNA 3UTR (molType RNA, 30 chemComps)
##Created molecule U1A 102 (molType protein, 101 chemComps)
##Created chain 'B', start seqCode 19, end seqCode 50, molecule 'RNA 3UTR'...
##Created chain 'A', start seqCode 1, end seqCode 101, molecule 'U1A 102'...
'1aud': { 
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', 'A102', 1, 0],
        ['A', ' ',    1, 0],
        ['B', 'str1', 1, 18],
        ['B', 'str1', 13, 20]],
      'addNameMappings':  {
# Note that the ORIGINAL residue names should be used and not: DA, DG, DC.
        'A': [["H2''","H2'"],["HN*", 'H6*'],["HN'", 'H6*'],["HN''", 'H6*'],["HN'*", 'H6*']],
        'G': [["H2''","H2'"],["HN*", 'H2*'],["HN'", 'H2*'],["HN''", 'H2*'],["HN'*", 'H2*']],
        'C': [["H2''","H2'"],["HN*", 'H4*'],["HN'", 'H4*'],["HN''", 'H4*'],["HN'*", 'H4*']],
        'U': [["H2''","H2'"]]
     }
# Based on restraints ranges:
##Rst: str1  19   .   H1 -  30   .  H1' diff  11 ch.range  12
##Rst: str1  33   .  H1' -  50   .  H1' diff  17 ch.range  30
##Restraint    SEQRS Offset
##A102  38 GLN .   .   .
##A102  72 GLN .   .   .
##str1  19   G B   1  18
##str1  20   G B   2  18
##str1  21   C B   3  18
##str1  23   G B   5  18
##str1  25   G B   7  18
##str1  27   C .   .   .
##str1  28   C .   .   .
##str1  35   G B  15  20
##str1  36   G B  16  20
##str1  38   C B  18  20
##str1  46   C B  26  20
##str1  48   G B  28  20
##str1  49   C .   .   .
##str1  50   C .   .   .
      }
    } 
  },
##Created chain 'B', start seqCode 99, end seqCode 104, molecule '6-MER PEPTIDE FROM BREAKPOINT CLUSTER REGION 6-MER PEPTIDE FROM BREAKPOINT CLU'...
##Created chain 'A', start seqCode 1, end seqCode 93, molecule 'AFADIN'...
'2ain': { 
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', 'A', 1, 0],
        ['B', 'B', 1, 98]],
      }
    } 
  },
##Created molecule INTERLEUKIN-1*BETA (/NMR$, MINIMIZED AVERAGE STRUCTURE) (molType protein, 153 chemComps)
##Created molecule Molecule1 (molType other, 1 chemComps)
##Created chain ' ', start seqCode 1, end seqCode 153, molecule 'INTERLEUKIN-1*BETA (/NMR$, MINIMIZED AVERAGE STRUCTURE)'...
##Created chain 'A', start seqCode 1, end seqCode 1, molecule 'Molecule1'...
##Created chain 'B', start seqCode 2, end seqCode 2, molecule 'Molecule1'...
##Created chain 'C', start seqCode 3, end seqCode 3, molecule 'Molecule1'...
##Created chain 'D', start seqCode 4, end seqCode 4, molecule 'Molecule1'...
##Created chain 'E', start seqCode 5, end seqCode 5, molecule 'Molecule1'...
##Created chain 'F', start seqCode 6, end seqCode 6, molecule 'Molecule1'...
##Created chain 'G', start seqCode 7, end seqCode 7, molecule 'Molecule1'...
##'6i1b': { 
##   'readCoordinates': {
##    'keywds': {
##      'forceChainMappings': [
##        [' ',' ',1,0],
##        ['A','A',1,0]
##        ],
##      }
##    },
## 'linkResonances': {
##    'keywds': {
##      'forceChainMappings': [
##        [' ', ' ', 1, 0],
##        ['A', ' ', 1, 0],
##        ['B', ' ', 1, 1],
##        ['C', ' ', 1, 2],
##        ['D', ' ', 1, 3],
##        ['E', ' ', 1, 4],
##        ['F', ' ', 1, 5],
##        ['G', ' ', 1, 6]
##        ],
##      }
##    } 
##  },
# No settings needed apparently although I don't understand why these
# settings would not work.
'1fzx': { 
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, 0],
        ['B', ' ', 1, 12],
        ['A', 'ATRA', 1, 0], # For dihedrals.
        ['B', 'ATRB', 1, 12]
        ],
      }
    } 
  },
'1g14': { 
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, 0],
        ['B', ' ', 1, 12],
        ['A', 'A5TR', 1, 0], # For dihedrals.
        ['B', 'T5TR', 1, 12]
        ],
      }
    } 
  },
'2akl': { 
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, -22]
        ],
      }
    } 
  },

##Restraint ranges
##Rst:    .  26   .   HA -  55   .   HA diff  29 ch.range  30
##
##Rst:    A  26   .   HN -  26   .   HN diff   0 ch.range   1
##Rst:    A  28   .   HN -  34   .   HN diff   6 ch.range   8
##Rst:    A  37   .    O -  54   .  HB1 diff  17 ch.range  26
##
##Rst:    B  26   .    O -  32   .   HN diff   6 ch.range   7
##Rst:    B  34   .    O -  34   .    O diff   0 ch.range   8
##Rst:    B  38   .  HD# -  38   .  HD# diff   0 ch.range   9
##Rst:    B  40   .  HE# -  41   .  HB# diff   1 ch.range  11
##Rst:    B  45   . HD2# -  45   . HD2# diff   0 ch.range  12
##
##Rst:    D  50   .  HD# -  50   .  HD# diff   0 ch.range   1
##
##Rst:    a  27   .  HD# -  27   .  HD# diff   0 ch.range   1
##Rst:    a  29   .   HB -  29   .   HB diff   0 ch.range   2
##Rst:    a  34   .   HN -  34   .   HN diff   0 ch.range   3
##
##Rst:    b  27   .   HA -  27   .   HA diff   0 ch.range   1
##Rst:    b  29   .   HA -  29   .   HA diff   0 ch.range   2
##Rst:    b  31   .   HA -  31   .   HA diff   0 ch.range   3
##Rst:    b  33   .  HD# -  33   .  HD# diff   0 ch.range   4

'1pet': { 
  'duplicateResonances': {' ': ['A','B','C','D']},
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', 'A', 1, 24],
        ['B', 'B', 1, 24],
        ['C', 'C', 1, 24],
        ['D', 'D', 1, 24],

        ['A', 'a', 1, 24],
        ['B', 'b', 1, 24],
        ['C', 'c', 1, 24],
        ['D', 'd', 1, 24]
        ],
      }
    } 
  },
##Created molecule 101-MER (molType None, 101 chemComps)
##Created molecule GAG POLYPROTEIN (molType protein, 56 chemComps)
##Created molecule ZINC ION (molType other, 1 chemComps)
##
##Created chain 'B', start seqCode 276, end seqCode 376, molecule '101-MER'...
##Created chain 'A', start seqCode 1, end seqCode 56, molecule 'GAG POLYPROTEIN'...
##Created chain ' ', start seqCode 57, end seqCode 57, molecule 'ZINC ION'...
##  Final mapping: [[' ', ' ', 1, 51], ['B', ' ', 1, 275]]
'1u6p': { 
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, 0],   # protein
        ['B', ' ', 1, 275], # RNA 101 mer
##        [' ', ' ', 1, 0]   # zinc incorporated with CYS of protein.
        ],
      }
    } 
  },
'2hfv': { 
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, 0]
        ],  
# Author was kind enought to provide updated file with IUPAC naming after request.     
##      'addNameMappings':  {
##        'ALA':   [["HB",    "MB"]],
##        'ARG':   [["HB",    "QB"],["HG",    "QG"], ["HD",    "QG"]],
##        'ASN':   [["HB",    "QB"],["HD2",   "QD"]],
##        'ASP':   [["HB",    "QB"]],
##        'GLN':   [["HB",    "QB"],["HG",    "QG"]],
##        'GLU':   [["HB",    "QB"],["HG",    "QG"]],
##        'GLY':   [["HA",    "QA"]],
##        'HIS':   [["HB",    "QB"]],
##        'ILE':   [["HD1",   "MD"], ["HG1",   "QG"], ["HG2",   "MG"]],
##        'LEU':   [["HB",    "QB"], ["HD",    "QD"], ["HD1",   "MD1"], ["HD2",   "MD2"]],
##        'MET':   [["HB",    "QB"], ["HG",    "QG"]],
##        'PRO':   [["HB",    "QB"], ["HG",    "QG"], ["HD",    "QD"]],
##        'SER':   [["HB",    "QB"]],
##        'THR':   [["HG2",   "MG"]],
##        'VAL':   [["HG1",   "MG1"], ["HG2",   "MG2"]],
##      }
    },
  }
 },
'1x2u': { 
  'comment': "Simple duplex",
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, 0],
        ['B', ' ', 1, 12]
        ],  
    },
  }
 },
'1x2x': { 
  'comment': "Simple duplex",
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, 0],
        ['B', ' ', 1, 12]
        ],  
    },
  }
 },
'2ga7': {
  'comment':
"""
Created chain 'A', start seqCode 178, end seqCode 178, molecule 'COPPER (I) ION'...
Created chain 'B', start seqCode 1, end seqCode 90, molecule 'COPPER-TRANSPORTING ATPASE 1'...
""",
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 178, 178], # Not needed I suppose.
        ['B', ' ', 1, 0]
        ],  
    },
  }
 },
'2fq0': {
  'comment':
"""
Created chain 'A', start seqCode 137, end seqCode 137, molecule '4'-PHOSPHOPANTETHEINE'...
Created chain 'B', start seqCode 1, end seqCode 79, molecule 'ACYL CARRIER PROTEIN'...
""",
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 137, 137], # Not needed I suppose.
        ['B', ' ', 1, 0]
        ],  
    },
  }
 },
'2fq2': {
  'comment':
"""
Created chain 'A', start seqCode 137, end seqCode 137, molecule '4'-PHOSPHOPANTETHEINE'...
Created chain 'B', start seqCode 1, end seqCode 79, molecule 'ACYL CARRIER PROTEIN'...
""",
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 137, 137], # Not needed I suppose.
        ['B', ' ', 1, 0]
        ],
    },
  }
 },
'2gut': {
  'linkResonances': {
    'keywds': {
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2  # does no harm, is xplor entry
    },
  }
 },
'2adl': {
  'comment':
"""
Created chain 'A', start seqCode 1, end seqCode 72, molecule 'CCDA'...
Created chain 'B', start seqCode 101, end seqCode 172, molecule 'CCDA'...
""",
  'linkResonances': {    
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, 0], # Not needed I suppose.
        ['B', ' ', 1, 100]
        ],
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2,  # does no harm, is xplor entry
      'addNameMappings':  {
        'THR':   [["HG##",   "HG2*"]], # This shouldn't be needed in Xplor system, right Wim?
      }
    }
  }
 },
'2ayj': { 
  'comment':
"""
Created chain 'A', start seqCode 1, end seqCode 56, molecule '50S RIBOSOMAL PROTEIN L40E'...
Created chain ' ', start seqCode 57, end seqCode 57, molecule 'ZINC ION'...
""",
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, 0]
        ],
      }
    } 
  },
'2hh8': {
  'comment':
"""
Why aren't the H correctly translated but the HN are?
""",
  'linkResonances': {    
    'keywds': {
      'namingSystem': 'XPLOR',
      'useIupacMatching': 2,  # does no harm, is xplor entry
    }
  }
 },
'2h3s': {
  'comment':
"""
Created chain 'B', start seqCode 11, end seqCode 35, molecule 'Molecule2'...
Created chain 'A', start seqCode 1, end seqCode 9, molecule 'PANCREATIC HORMONE'...
""",
  'linkResonances': {    
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, 0],
        ['B', ' ', 1, 10]
        ],
    }
  }
 },
'2h3t': {
  'comment':
"""
See 2h3s
""",
  'linkResonances': {    
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, 0],
        ['B', ' ', 1, 10]
        ],
    }
  }
 },
'2h4b': {
  'comment':
"""
Created chain 'C', start seqCode 11, end seqCode 35, molecule 'Molecule2'...
Created chain 'D', start seqCode 11, end seqCode 35, molecule 'Molecule2'...
Created chain 'A', start seqCode 1, end seqCode 9, molecule 'PANCREATIC HORMONE'...
Created chain 'B', start seqCode 1, end seqCode 9, molecule 'PANCREATIC HORMONE'...
""",
  'linkResonances': {    
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, 0],
        ['B', ' ', 1, 100],
        ['C', ' ', 1, 10],
        ['D', ' ', 1, 110]
        ],
    }
  }
 },
'17ra': { 
 'linkResonances': {
    'keywds': {
       'addNameMappings':  {
        'C': [["H2''","H2'"]],
        'A': [["H2''","H2'"]], # Otherwise mapped to HO2' which doesn't exist in RNA as this molecule is.
        'G': [["H2''","H2'"]],
        'T': [["H2''","H2'"]],
        'U': [["H2''","H2'"]],
     }
    } 
  }
 },
'1aff': {
  'comment':
"""
Created chain 'A', start seqCode 1, end seqCode 4, molecule 'QUADRUPLEX DNA (5'-D(TP*AP*GP*G)-3')'...
Created chain 'B', start seqCode 1, end seqCode 4, molecule 'QUADRUPLEX DNA (5'-D(TP*AP*GP*G)-3')'...
Created chain 'C', start seqCode 1, end seqCode 4, molecule 'QUADRUPLEX DNA (5'-D(TP*AP*GP*G)-3')'...
Created chain 'D', start seqCode 1, end seqCode 4, molecule 'QUADRUPLEX DNA (5'-D(TP*AP*GP*G)-3')'...

homo tetramer of 4 residues with restraints for single molecule numbered 1-8. I don't know if FC
can handle it; pretty complex.
""",
  'duplicateResonances': {' ': ['A','B','C','D'] },                   
  'linkResonances': {    
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, 0],
        ['B', ' ', 1, 4]
        ],
    }
  }
 },
'1ajl': { 
 'linkResonances': {
    'keywds': {
       'addNameMappings':  {
        'C': [["H2''","H2'"]],
        'A': [["H2''","H2'"]], # Otherwise mapped to HO2' which doesn't exist in RNA as this molecule is.
        'G': [["H2''","H2'"]],
        'T': [["H2''","H2'"]],
        'U': [["H2''","H2'"]],
     }
    } 
  }
 },
'1ajt': { 
 'linkResonances': {
    'keywds': {
       'addNameMappings':  {
        'C': [["H2''","H2'"]],
        'A': [["H2''","H2'"]], # Otherwise mapped to HO2' which doesn't exist in RNA as this molecule is.
        'G': [["H2''","H2'"]],
        'T': [["H2''","H2'"]],
        'U': [["H2''","H2'"]],
     }
    } 
  }
 },
'1aju': { 
  'comment':
"""
The sequence in the restraints doesn't match the coordinate section in an easy way.

Created chain 'B', start seqCode 47, end seqCode 47, molecule 'ARGININE'...
Created chain 'A', start seqCode 16, end seqCode 46, molecule 'TRANS ACTIVATING REGION RNA'...
  Final mapping: [['A', ' ', 1, 16]]

But my code gave:
Triplet matches
Restraint    SEQRS Offset
   .  16   G A   1  15
   .  17   G A   2  15
   .  18   C A   3  15
   .  19   C .   .   .
   .  21   G A   1  20
   .  26   G A  10  16
   .  27   A A  11  16
   .  28   G A   2  26
   .  29   C A  13  16
   .  36   G A  20  16
   .  37   C A  21  16
   .  39   C A  23  16
   .  41   C A  14  27
   .  43   G A   1  42
   .  44   G A   2  42
   .  45   C .   .   .
   .  46   C .   .   .
""",
 'linkResonances': {
    'keywds': {
      'forceChainMappings': [
        ['A', ' ', 1, 16],
        ['B', ' ', 1, 46]
        ],
       
    } 
  }
 },

'1ajy': {
  'comment':
"""
Created molecule PUT3 (molType protein, 71 chemComps)
Created molecule ZINC ION (molType other, 1 chemComps)
Created chain 'A', start seqCode 30, end seqCode 100, molecule 'PUT3'...
Created chain 'B', start seqCode 30, end seqCode 100, molecule 'PUT3'...
Created chain 'C', start seqCode 101, end seqCode 101, molecule 'ZINC ION'...
Created chain 'D', start seqCode 102, end seqCode 102, molecule 'ZINC ION'...
Created chain 'E', start seqCode 101, end seqCode 101, molecule 'ZINC ION'...
Created chain 'F', start seqCode 102, end seqCode 102, molecule 'ZINC ION'...
""",
  'duplicateResonances': {' ': ['A','B']},   

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A','A',1,29],['B','B',1,29],      # Protein
                             ['A','a',1,29],['B','b',1,29],      # Protein
                             ['C','A',1,100],['C','a',1,100],    # Zn
                             ['D','A',1,101],['D','a',1,101],    # Zn
                             ['E','B',1,100],['E','b',1,100],    # Zn
                             ['F','B',1,101],['F','b',1,101]]    # Zn
      }
    }
  },

'1al5': {
  'comment':
"""
# TODO has insertion codes in discover restraints
""",
  },

'1amb': {
  'comment':
"""
Restraints use non-numbers for distances

Created molecule DAUNOMYCIN (molType other, 3 chemComps)
Created molecule DNA (5'-D(*AP*CP*GP*TP*AP*CP*GP*T)-3') DNA (5'-D(*AP*CP*GP*TP*AP*CP*GP*T)-3') (molType DNA, 8 chemComps)
Created molecule Molecule2 (molType other, 2 chemComps)
Created chain 'C', start seqCode 17, end seqCode 20, molecule 'DAUNOMYCIN'...
Created chain 'A', start seqCode 1, end seqCode 8, molecule 'DNA (5'-D(*AP*CP*GP*TP*AP*CP*GP*T)-3') DNA (5'-D(*AP*CP*GP*TP*AP*CP*GP*T)-3')'...
Created chain 'B', start seqCode 9, end seqCode 16, molecule 'DNA (5'-D(*AP*CP*GP*TP*AP*CP*GP*T)-3') DNA (5'-D(*AP*CP*GP*TP*AP*CP*GP*T)-3')'...
Created chain 'D', start seqCode 19, end seqCode 20, molecule 'Molecule2'...
  Final mapping: [[' ', ' ', 1, 0]]
""",
  'duplicateResonances': {' ': ['A','B']}
  },
'1anr': { 
 'linkResonances': {
    'keywds': {
       'addNameMappings':  {
        'C': [["H2''","H2'"]],
        'A': [["H2''","H2'"]], # Otherwise mapped to HO2' which doesn't exist in RNA as this molecule is.
        'G': [["H2''","H2'"]],
        'T': [["H2''","H2'"]],
        'U': [["H2''","H2'"]],
     }
    } 
  }
 },

 '1aps': {
  'comment':
"""
$SJ/BMRB/97entries/atomlib for an overview for 97 entries' atom libs:
S:\jurgen\older\pdb-nmr\data_paper_allg\1aps\1aps.notes for info on problem violations.
""",
  'linkResonances': {
    'keywds': { 
      'forceChainMappings': [[' ',' ',2,0]],
##       'addNameMappings':  { # Disgeo from Aqua
##'ACE': [ ["CA","CA"], ["HA3","HA3"], ["HA1","HA1"], ["HA2","HA2"], ["C","C"], ["O","O"], ["N","N"], ["H","H"]],
##'ALA': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB1"], ["HB2","HB2"], ["HB3","HB3"], ["QB","MB"], ["N","N"], ["H","H"]],
##'ARG': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG1","HG2"], ["HG2","HG3"], ["CD","CD"], ["HD1","HD2"], ["HD2","HD3"], ["NE","NE"], ["HE","HE"], ["CZ","CZ"], ["NH1","NH1"], ["HH11","HH11"], ["HH12","HH12"], ["NH2","NH2"], ["HH21","HH21"], ["HH22","HH22"], ["QB","QB"], ["QG","QG"], ["QD","QD"], ["QH1","QH1"], ["QH2","QH2"], ["QH","QZ"], ["N","N"], ["H","H"], ["CA","CA"]],
##'ASN': [ ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["OD1","OD1"], ["ND2","ND2"], ["HD21","HD21"], ["HD22","HD22"], ["QB","QB"], ["QD2","QD"], ["N","N"], ["H","H"]],
##'ASP': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["OD1","OD1"], ["OD2","OD2"], ["HD2","HD2"], ["QB","QB"], ["N","N"]],
##'CYS': [ ["CA","CA"], ["H","H"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["SG","SG"], ["HG","HG"], ["QB","QB"], ["N","N"], ["H","H"]],
##'GLN': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG1","HG2"], ["HG2","HG3"], ["CD","CD"], ["OE1","OE1"], ["NE2","NE2"], ["HE21","HE21"], ["HE22","HE22"], ["QB","QB"], ["QG","QG"], ["QE2","QE"], ["N","N"], ["H","H"]], 
##'GLU': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG1","HG2"], ["HG2","HG3"], ["CD","CD"], ["OE1","OE1"], ["OE2","OE2"], ["HE2","HE2"], ["QB","QB"], ["QG","QG"], ["N","N"], ["H","H"]],
##'GLY': [ ["CA","CA"], ["HA1","HA2"], ["HA2","HA3"], ["C","C"], ["O","O"], ["QA","QA"], ["N","N"], ["H","H"]],
##'HIS': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["ND1","ND1"], ["HD1","HD1"], ["CD2","CD2"], ["HD2","HD2"], ["CE1","CE1"], ["HE1","HE1"], ["NE2","NE2"], ["HE2","HE2"], ["QB","QB"], ["N","N"], ["H","H"]], 
##'ILE': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB","HB"], ["CG1","CG1"], ["HG11","HG12"], ["HG12","HG13"], ["CG2","CG2"], ["HG21","HG21"], ["HG22","HG22"], ["HG23","HG23"], ["CD1","CD1"], ["HD11","HD11"], ["HD12","HD12"], ["HD13","HD13"], ["QG1","QG"], ["QG2","MG"], ["QD1","MD"], ["N","N"], ["H","H"]],
##'LEU': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG","HG"], ["CD1","CD1"], ["HD11","HD11"], ["HD12","HD12"], ["HD13","HD13"], ["CD2","CD2"], ["HD21","HD21"], ["HD22","HD22"], ["HD23","HD23"], ["QB","QB"], ["QD1","MD1"], ["QD2","MD2"], ["QQD","QD"], ["N","N"], ["H","H"]],
##'LYS': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG1","HG2"], ["HG2","HG3"], ["CD","CD"], ["HD1","HD2"], ["HD2","HD3"], ["CE","CE"], ["HE1","HE2"], ["HE2","HE3"], ["NZ","NZ"], ["HZ1","HZ1"], ["HZ2","HZ2"], ["HZ3","HZ3"], ["QB","QB"], ["QG","QG"], ["QD","QD"], ["QE","QE"], ["QZ","QZ"], ["N","N"], ["H","H"]],
##'MET': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG1","HG2"], ["HG2","HG3"], ["SD","SD"], ["CE","CE"], ["HE1","HE1"], ["HE2","HE2"], ["HE3","HE3"], ["QB","QB"], ["QG","QG"], ["QE","ME"], ["N","N"], ["H","H"]],
##'PHE': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["CD1","CD1"], ["HD1","HD1"], ["CD2","CD2"], ["HD2","HD2"], ["CE1","CE1"], ["HE1","HE1"], ["CE2","CE2"], ["HE2","HE2"], ["CZ","CZ"], ["HZ","HZ"], ["QB","QB"], ["QD","QD"], ["QE","QE"], ["QR","QR"], ["N","N"]],
##'PRO': [ ["CA","CA"], ["HA","HA"], ["CD","CD"], ["HD1","HD2"], ["HD2","HD3"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG1","HG2"], ["HG2","HG3"], ["QB","QB"], ["QG","QG"], ["QD","QD"], ["N","N"], ["H","H"]], 
##'SER': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["OG","OG"], ["HG","HG"], ["QB","QB"], ["N","N"]],
##'THR': [ ["CA","CA"], ["H","H"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["OG1","OG1"], ["HB","HB"], ["HG1","HG1"], ["CG2","CG2"], ["HG21","HG21"], ["HG22","HG22"], ["HG23","HG23"], ["QG2","MG"], ["N","N"]],
##'TRP': [ ["CA","CA"], ["H","H"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["CD1","CD1"], ["NE1","NE1"], ["CE2","CE2"], ["CD2","CD2"], ["HD1","HD1"], ["HE1","HE1"], ["CE3","CE3"], ["HE3","HE3"], ["CZ3","CZ3"], ["HZ3","HZ3"], ["CH2","CH2"], ["HH2","HH2"], ["CZ2","CZ2"], ["HZ2","HZ2"], ["QB","QB"], ["N","N"]],
##'TYR': [ ["CA","CA"], ["H","H"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["CD1","CD1"], ["HD1","HD1"], ["CE1","CE1"], ["HE1","HE1"], ["CZ","CZ"], ["OH","OH"], ["HH","HH"], ["CE2","CE2"], ["HE2","HE2"], ["CD2","CD2"], ["HD2","HD2"], ["QB","QB"], ["QD","QD"], ["QE","QE"], ["QR","QR"], ["N","N"], ["H","H"]],
##'VAL': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB","HB"], ["CG1","CG1"], ["HG11","HG11"], ["HG12","HG12"], ["HG13","HG13"], ["CG2","CG2"], ["HG21","HG21"], ["HG22","HG22"], ["HG23","HG23"], ["QG1","MG1"], ["QG2","MG2"], ["QQG","QG"]],
##},
      
       'addNameMappings':  { # Disman from Aqua
'ACE': [ ["CA","CA"], ["HA3","HA3"], ["HA1","HA1"], ["HA2","HA2"], ["C","C"], ["O","O"], ["N","N"], ["H","H"]], 
'ALA': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB1"], ["HB2","HB2"], ["HB3","HB3"], ["QB","MB"], ["N","N"], ["H","H"]],
'ARG': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG1","HG2"], ["HG2","HG3"], ["CD","CD"], ["HD1","HD2"], ["HD2","HD3"], ["NE","NE"], ["HE","HE"], ["CZ","CZ"], ["NH1","NH1"], ["HH11","HH11"], ["HH12","HH12"], ["NH2","NH2"], ["HH21","HH21"], ["HH22","HH22"], ["QB","QB"], ["QG","QG"], ["QD","QD"], ["QH1","QH1"], ["QH2","QH2"], ["QH","QZ"], ["N","N"], ["H","H"]], 
'ASN': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["OD1","OD1"], ["ND2","ND2"], ["HD21","HD21"], ["HD22","HD22"], ["QB","QB"], ["QD2","QD"], ["N","N"], ["H","H"]],
'ASP': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["OD1","OD1"], ["OD2","OD2"], ["HD2","HD2"], ["QB","QB"], ["N","N"]], 
'CYS': [ ["CA","CA"], ["H","H"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["SG","SG"], ["HG","HG"], ["QB","QB"], ["N","N"], ["H","H"]],
'GLN': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG1","HG2"], ["HG2","HG3"], ["CD","CD"], ["OE1","OE1"], ["NE2","NE2"], ["HE21","HE21"], ["HE22","HE22"], ["QB","QB"], ["QG","QG"], ["QE2","QE"], ["N","N"], ["H","H"]],
'GLU': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG1","HG2"], ["HG2","HG3"], ["CD","CD"], ["OE1","OE1"], ["OE2","OE2"], ["HE2","HE2"], ["QB","QB"], ["QG","QG"], ["N","N"], ["H","H"]],
'GLY': [ ["CA","CA"], ["HA1","HA2"], ["HA2","HA3"], ["C","C"], ["O","O"], ["QA","QA"], ["N","N"], ["H","H"]], 
'HIS': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["ND1","ND1"], ["HD1","HD1"], ["CD4","CD2"], ["HD4","HD2"], ["CE2","CE1"], ["HE2","HE1"], ["NE3","NE2"], ["HE3","HE2"], ["QB","QB"], ["N","N"], ["H","H"]], 
'ILE': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB","HB"], ["CG1","CG1"], ["HG11","HG12"], ["HG12","HG13"], ["CG2","CG2"], ["HG21","HG21"], ["HG22","HG22"], ["HG23","HG23"], ["CD1","CD1"], ["HD11","HD11"], ["HD12","HD12"], ["HD13","HD13"], ["QG1","QG"], ["QG2","MG"], ["QD1","MD"], ["N","N"], ["H","H"]],
'LEU': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG","HG"], ["CD1","CD1"], ["HD11","HD11"], ["HD12","HD12"], ["HD13","HD13"], ["CD2","CD2"], ["HD21","HD21"], ["HD22","HD22"], ["HD23","HD23"], ["QB","QB"], ["QD1","MD1"], ["QD2","MD2"], ["QQD","QD"], ["N","N"], ["H","H"]],
'LYS': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG1","HG2"], ["HG2","HG3"], ["CD","CD"], ["HD1","HD2"], ["HD2","HD3"], ["CE","CE"], ["HE1","HE2"], ["HE2","HE3"], ["NZ","NZ"], ["HZ1","HZ1"], ["HZ2","HZ2"], ["HZ3","HZ3"], ["QB","QB"], ["QG","QG"], ["QD","QD"], ["QE","QE"], ["QZ","QZ"], ["N","N"], ["H","H"]],
'MET': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG1","HG2"], ["HG2","HG3"], ["SD","SD"], ["CE","CE"], ["HE1","HE1"], ["HE2","HE2"], ["HE3","HE3"], ["QB","QB"], ["QG","QG"], ["QE","ME"], ["N","N"], ["H","H"]],
'PHE': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG1","CG"], ["CD2","CD1"], ["HD2","HD1"], ["CD6","CD2"], ["HD6","HD2"], ["CE3","CE1"], ["HE3","HE1"], ["CE5","CE2"], ["HE5","HE2"], ["CZ4","CZ"], ["HZ4","HZ"], ["QB","QB"], ["QR","QR"], ["N","N"]],
'PRO': [ ["CA","CA"], ["HA","HA"], ["CD","CD"], ["HD1","HD2"], ["HD2","HD3"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG","CG"], ["HG1","HG2"], ["HG2","HG3"], ["QB","QB"], ["QG","QG"], ["QD","QD"], ["N","N"], ["H","H"]],
'SER': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["OG","OG"], ["HG","HG"], ["QB","QB"], ["N","N"]], 
'THR': [ ["CA","CA"], ["H","H"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["OG1","OG1"], ["HB","HB"], ["HG1","HG1"], ["CG2","CG2"], ["HG21","HG21"], ["HG22","HG22"], ["HG23","HG23"], ["QG2","MG"], ["N","N"]],
'TRP': [ ["CA","CA"], ["H","H"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG3","CG"], ["CD2","CD1"], ["NE1","NE1"], ["CE8","CE2"], ["CD9","CD2"], ["HD2","HD1"], ["HE1","HE1"], ["CE4","CE3"], ["HE4","HE3"], ["CZ5","CZ3"], ["HZ5","HZ3"], ["CH6","CH2"], ["HH6","HH2"], ["CZ7","CZ2"], ["HZ7","HZ2"], ["QB","QB"], ["N","N"]],
'TYR': [ ["CA","CA"], ["H","H"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB1","HB2"], ["HB2","HB3"], ["CG1","CG"], ["CD2","CD1"], ["HD2","HD1"], ["CE3","CE1"], ["HE3","HE1"], ["CZ4","CZ"], ["OH","OH"], ["HH","HH"], ["CE5","CE2"], ["HE5","HE2"], ["CD6","CD2"], ["HD6","HD2"], ["QB","QB"], ["QR","QR"], ["N","N"], ["H","H"]],
'VAL': [ ["CA","CA"], ["HA","HA"], ["C","C"], ["O","O"], ["CB","CB"], ["HB","HB"], ["CG1","CG1"], ["HG11","HG11"], ["HG12","HG12"], ["HG13","HG13"], ["CG2","CG2"], ["HG21","HG21"], ["HG22","HG22"], ["HG23","HG23"], ["QG1","MG1"], ["QG2","MG2"], ["QQG","QG"]],
}    
    
    }
    }
  },
'1arj': { 
 'linkResonances': {
    'keywds': {
       'addNameMappings':  {
        'C': [["H2''","H2'"]],
        'A': [["H2''","H2'"]], # Otherwise mapped to HO2' which doesn't exist in RNA as this molecule is.
        'G': [["H2''","H2'"]],
        'T': [["H2''","H2'"]],
        'U': [["H2''","H2'"]],
     }
    } 
  }
 },

'1drn': {
  'comments': """DNA/RNA HYBRID REGION, D(GGAGA)R(UGAC)/D(GTCATCTCC)
  residues 6-9 have O2' (are RNA) and thus have no H2''
  they might have to be specified individually but FC hasn't got poly type right so
  that might have to be fixed first.
  """,
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],
                             ['B',' ',1,9]]
      },
       'addNameMappings':  {
        'C': [["H2''","H2'"]],
        'A': [["H2''","H2'"]], # Otherwise mapped to HO2' which doesn't exist in RNA as this molecule is.
        'G': [["H2''","H2'"]],
        'T': [["H2''","H2'"],["H5#","H7*"]],
        'U': [["H2''","H2'"]],
     }    
    }
  },

'1ju7': { 

  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0],['A', 'HIST', 1, 0]],
       'addNameMappings':  {
        'C': [["H2''","H2'"]],
        'A': [["H2''","H2'"]], # Otherwise mapped to HO2' which doesn't exist in RNA as this molecule is.
        'G': [["H2''","H2'"]],
        'T': [["H2''","H2'"]],
        'U': [["H2''","H2'"]],
     }    
      }
    }
  },
'1jwc': { 
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0],['A', 'HIST', 1, 0]],
       'addNameMappings':  {
        'C': [["H2''","H2'"]],
        'A': [["H2''","H2'"]], # Otherwise mapped to HO2' which doesn't exist in RNA as this molecule is.
        'G': [["H2''","H2'"]],
        'T': [["H2''","H2'"]],
        'U': [["H2''","H2'"]],
     }    
      }
    }
  },
'1n53': { 
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,16]],
       'addNameMappings':  {
        'C': [["H2''","H2'"]],
        'A': [["H2''","H2'"]], # Otherwise mapped to HO2' which doesn't exist in RNA as this molecule is.
        'G': [["H2''","H2'"]],
        'T': [["H2''","H2'"]],
        'U': [["H2''","H2'"]],
     }    
      }
    }
  },
# Next is a block of settings for HO2' problem for entries who's only problem it is.
'1atv':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1atw':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1biv':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1dxn':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1eor':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1esh':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1f5u':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1f6x':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1f6z':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1f78':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1f79':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1f7f':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1f7g':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1f7h':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1f7i':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1f84':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1f85':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1fmn':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1hlx':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1i3x':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1i3y':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1i4c':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1j4y':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1jzc':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1kaj':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1kis':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1kka':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1kpy':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1kpz':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1ldz':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1nbr':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1p5m':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1p5n':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1p5o':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1p5p':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1rnk':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1s34':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1t28':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1tob':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1txs':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1ull':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1uts':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'1z31':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'2a9x':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'2awq':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},
'2b7g':{'linkResonances':{'keywds':{'addNameMappings':{'C':[["H2''","H2'"]],'A':[["H2''","H2'"]],'G':[["H2''","H2'"]],'T':[["H2''","H2'"]],'U':[["H2''","H2'"]]}}}},

'1au5': { 
  'linkResonances': {
    'keywds': {
       'addNameMappings':  {
        'C': [["H2D","H2''"],["H5D","H5''"]],
        'A': [["H2D","H2''"],["H5D","H5''"]],
        'G': [["H2D","H2''"],["H5D","H5''"]],
        'T': [["H2D","H2''"],["H5D","H5''"]],
        'U': [["H2D","H2''"],["H5D","H5''"]],                                 }    
      }
    }
  },


'1au6': {
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0], ['B', ' ', 1, 8], [' ', ' ', 1, 16]],
       'addNameMappings':  {
        'C': [["H2D","H2''"],["H5D","H5''"]],
        'A': [["H2D","H2''"],["H5D","H5''"]],
        'G': [["H2D","H2''"],["H5D","H5''"]],
        'T': [["H2D","H2''"],["H5D","H5''"]],
        'U': [["H2D","H2''"],["H5D","H5''"]],
      }
    }
  },
},

'1bah': {   
  'linkResonances': {
    'keywds': {
      'useIupacMatching': 2,    ## Allows 'additional' matching on iupac names.
       'addNameMappings':  {
        'ABA': [["HN","H"]],
      }
    }
    }
  },

'1cjg': {
  'linkResonances': {
    'keywds': {
       'addNameMappings':  {
        'A': [["H5':H5''","H5'*"],["O*P","OP1"],["H61:H62","H6*"]],
        'T': [["H5':H5''","H5'*"],["O*P","OP1"],["H51:H53","H7*"]],
        'G': [["H5':H5''","H5'*"],["O*P","OP1"],["H21:H22","H2*"]],
        'C': [["H5':H5''","H5'*"],["O*P","OP1"],["H41:H42","H4*"]],
      }
    }
    }
  },


'2b6f': {
 'comments': """
Created chain ' ', start seqCode 1, end seqCode 1, molecule 'ADENOSINE-5'-TRIPHOSPHATE'...
Created chain 'A', start seqCode 2, end seqCode 2, molecule 'MAGNESIUM ION'...
Created chain 'B', start seqCode 17, end seqCode 137, molecule 'SULFIREDOXIN'...
  Final mapping: [[' ', ' ', 1, 25], ['A', ' ', 1, 29], ['B', ' ', 1, 16]]
  """,
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['B', ' ', 1, 16]], # Only part with restraints but why doesn't FC work
      # without it because it found the same thing by itself.
    }
  },
},

'1bwg': {
  'comments': """""",
  'linkResonances': {
    'keywds': {
       'addNameMappings':  {
        'T':  [["H5M*","H7*"]] # residue name of input.
      }
    }
    }
  },

'1cou': {
  'comments': """Note that e.g. Leu QD isn't matched to QD when using useIupacMatching
  Need to use single * for it then as in HD* and not HD** which would still be more logical.
  """, 
  'linkResonances': {
   'keywds': {
      'forceDefaultChainMapping': 1,
      'useIupacMatching': 2,    ## Allows 'additional' matching on iupac names.
      'namingSystem': 'DIANA', 
      'addNameMappings':  {
        'ALA': [],
        'ARG': [['HB+','HB*'],['HB-','HB*'],['HG+','HG*'],['HG-','HG*']], 
        'ASN': [['HB+','HB*'],['HB-','HB*'],['HD2+','HD2*'],['HD2-','HD2*']], 
        'ASP': [['HB+','HB*'],['HB-','HB*']],  
        'CYS': [['HB+','HB*'],['HB-','HB*']], 
        'GLN': [['HB+','HB*'],['HB-','HB*'],['HG+','HG*'],['HG-','HG*'],['HE2+','HE2*'],['HE2-','HE2*']],
        'GLU': [['HB+','HB*'],['HB-','HB*'],['HG+','HG*'],['HG-','HG*']],
        'GLY': [['HA+','HA*'],['HA-','HA*']],
        'HIS': [['HB+','HB*'],['HB-','HB*']], 
        'ILE': [['HG1+','HG1*'],['HG1-','HG1*'],['MD1','HD1*'],['MG2','HG2*']],
        'LEU': [['HB+','HB*'],['HB-','HB*'],['MDX','HD*'],['MDY','HD*'],['QD','HD*']], 
        'LYS': [['HB+','HB*'],['HB-','HB*'],['HG+','HG*'],['HG-','HG*'],['HD+','HD*'],['HD-','HD*']],
        'MET': [['HB+','HB*'],['HB-','HB*'],['HG+','HG*'],['HG-','HG*'],['ME','HE*']],
        'PHE': [['HB+','HB*'],['HB-','HB*'],['HD','HD*'],['HE','HE*']],
        'PRO': [['HB+','HB*'],['HB-','HB*'],['HG+','HG*'],['HG-','HG*'],['HD+','HD*'],['HD-','HD*']],
        'SER': [['HB+','HB*'],['HB-','HB*']],
        'THR': [["MG2","HG2*" ],["MG","HG2*"]],
        'TRP': [['HB+','HB*'],['HB-','HB*']], 
        'TYR': [['HB+','HB*'],['HB-','HB*'],['HD','HD*'],['HE','HE*']],
        'VAL': [['QG','HG*'],],
        }
      }
    }
  },

'2hgh': {
  'comments': """special interest entry for RECOORD_NA
Created chain 'B', start seqCode 1, end seqCode 55, molecule '55-MER'...
Created chain 'A', start seqCode 104, end seqCode 190, molecule 'TRANSCRIPTION FACTOR IIIA'...
Created chain 'C', start seqCode 191, end seqCode 191, molecule 'ZINC ION'...
Created chain 'D', start seqCode 192, end seqCode 192, molecule 'ZINC ION'...
Created chain 'E', start seqCode 193, end seqCode 193, molecule 'ZINC ION'...
  Final mapping: [['A', ' ', 1, 103], ['B', ' ', 1, 0], ['C', ' ', 1, 55], ['D', ' ', 1, 56], ['E', ' ', 1, 57]]

Restraints:
.           107  CYSZ ZN   
.           137  CYSZ ZN   
.           164  CYSZ ZN
RDCS use a different numbering scheme than the distance restraints do for the protein TF3A.
   57    TYR     HN    57    TYR      N    -20.887      1.000  1.00 2 offset 55
   58    VAL     HN    58    VAL      N    -19.245      1.000  1.00 3
   59    CYS     HN    59    CYS      N      2.645      1.000  1.00 4
...
  139    CYS     HN   139    CYS      N    -12.587      1.000  1.00 84
  140    HIS     HN   140    HIS      N     18.789      1.000  1.00 85
  141    GLN     HN   141    GLN      N     11.948      1.000  1.00 86
  """,
  'linkResonances': {
   'keywds': {
      'namingSystem': 'DIANA', 
      'useIupacMatching': 2,    ## Allows 'additional' matching on iupac names.
      'forceChainMappings': [['A', ' ', 1, 103],
                             ['B', ' ', 1, 0],
                             ['C', ' ', 1, 190],
                             ['D', ' ', 1, 191],
                             ['E', ' ', 1, 192]],
      'specificResNameMappings': {
        # first column original name
        # second column name before forceChainMappings
                                  ' .107.ZN': ' .191.ZN',
                                  ' .137.ZN': ' .192.ZN',
                                  ' .164.ZN': ' .193.ZN'
                                  }
      }
    }
  },

'2adn': {# this helps for the THR, change the above to follow suit.
  # Wim, whitout settings this works fine except for the THR.
  # When I specify the THR setting and I don't specify the forcechainmappings it fails to
  # map anything!
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0],
                             ['B', ' ', 1, 100]],
      'addNameMappings':  { 'THR': [["HG##","HG2#"]] }
   }
  }
},

'2b1o': {
  'comments': """
Created chain ' ', start seqCode 1, end seqCode 1, molecule 'CALCIUM ION'...
Created chain 'A', start seqCode 2, end seqCode 2, molecule 'CALCIUM ION'...
Created chain 'B', start seqCode 3, end seqCode 3, molecule 'CALCIUM ION'...
Created chain 'C', start seqCode 2, end seqCode 213, molecule 'CALCIUM-DEPENDENT CELL ADHESION MOLECULE-1'...
  Warning: Did not map CCPN chain codes ['A', 'B']
  Final mapping: [[' ', ' ', 1, 0], ['C', ' ', 1, 1]]
""",
  'linkResonances': {
   'keywds': {
     # first column is ccpn
     # second column is original
      'forceChainMappings': [
        ['C', ' ', 1, 1],
        [' ', 'A', 1, 0],
        ['A', 'B', 1, 0],
        ['B', 'C', 1, 0]],
      'specificResNameMappings': {
                                  ' .1.CA': 'A.1.CA', # changes name at input level
                                  ' .2.CA': 'B.1.CA',
                                  ' .3.CA': 'C.1.CA'
                                  },  
   }
  }  
},

'2hv4': {
    'comments': """Residue zero is skipped in sequential count.
Created chain 'A', start seqCode -5, end seqCode 103, molecule 'CYTOCHROME C ISO-1'...
Created chain 'B', start seqCode 104, end seqCode 104, molecule 'HEME C'...
  Final mapping: [['A', ' ', 1, -5], ['B', ' ', 1, 103]]

Triplet matches
Restraint    SEQRS Offset
   .  -4 GLU A   2  -6
   .  -3 PHE A   3  -6
   .  -2 LYS .   .   .
   .  -1 ALA .   .   .
   .   1 GLY A   6  -5
   .   2 SER A   7  -5  
  """,
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A', ' ', 1, -6],
                             ['A', ' ', 6, -5],
                             ['B', ' ', 1, 103]],
   }
  }
},

'2ixy': {
  'linkResonances': {
   'keywds': {
       'addNameMappings':  {
##        'A': [["H2'1","H2'"]],
##        'T': [["H2'1","H2'"]],
##        'G': [["H2'1","H2'"]],
##        'C': [["H2'1","H2'"]],
##        'U': [["H2'1","H2'"]]
        'ALL': [["H2'1","H2'"]] # Works for linking too now.
      }
   }
  }
},

'1dft': {
    'comments': """
Created chain ' ', start seqCode 31, end seqCode 31, molecule 'CADMIUM ION'...
Created chain 'A', start seqCode 32, end seqCode 32, molecule 'CADMIUM ION'...
Created chain 'B', start seqCode 33, end seqCode 33, molecule 'CADMIUM ION'...
Created chain 'C', start seqCode 1, end seqCode 30, molecule 'METALLOTHIONEIN-1'...
  Final mapping: [[' ', ' ', 1, 9], ['A', ' ', 1, 12], ['C', ' ', 1, 0]]
""",
  'linkResonances': {
    'keywds': {                    
      'forceChainMappings': [
        ['C', ' ', 1, 0] # No restraints for the Cd anyway.
        ]
      }
    }
  },

'1dgo': {
  'comments': """""",
  'linkResonances': {
    'keywds': {
       'addNameMappings':  {
        'T':  [["H5M1","H7*"],
               ["H5M2","H7*"],
               ["H5M3","H7*"]]
      }
    }
    }
  },

'1dhh': {
  'linkResonances': {
    'keywds': {
      'forceChainMappings': [['A',' ',1,0],['B',' ',1,9]],
      'addNameMappings':{'C':[["H2''","H2'"]],
                         'A':[["H2''","H2'"]],
                         'G':[["H2''","H2'"]],
                         'T':[["H2''","H2'"],["H5#","H7*"]],
                         'U':[["H2''","H2'"]]
                         }
    }
  }
},

'1dox': {
  'comments': """
Created molecule FERREDOXIN [2FE-2S] (molType protein, 96 chemComps)
Created molecule Molecule1 (molType other, 1 chemComps)

Created chain ' ', start seqCode 1, end seqCode 96, molecule 'FERREDOXIN [2FE-2S]'...
Created chain 'A', start seqCode 97, end seqCode 97, molecule 'Molecule1'...

  Final mapping: [[' ', ' ', 1, 0], ['A', ' ', 1, 96]]
Not mapped:
' .97.S#' and
' .97.FE#'  
"""  
},

'1dsj': {
  'comments': """
Created chain ' ', start seqCode 50, end seqCode 50, molecule 'VPR PROTEIN'...
Created chain 'A', start seqCode 50, end seqCode 76, molecule 'VPR PROTEIN_2'...
  Final mapping: [['A', ' ', 5, 45]]
Triplet matches
Restraint    SEQRS Offset
   .  51 GLY     3  48
but the trick is that chain a starts with seqres 2! and not 1 ACE.  
  """, 
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A', ' ', 1, 49]],
      }
    }
},

'1e0a': {
  'comments': """
Created molecule G25K GTP-BINDING PROTEIN, PLACENTAL ISOFORM (GP), G25K GTP-BINDING PROTEIN, PL (molType protein, 184 chemComps)
Created molecule MAGNESIUM ION (molType other, 1 chemComps)
Created molecule Molecule1 (molType other, 1 chemComps)
Created molecule PHOSPHOAMINOPHOSPHONIC ACID-GUANYLATE ESTER (molType other, 1 chemComps)
Created molecule SERINE/THREONINE-PROTEIN KINASE PAK-ALPHA (molType protein, 46 chemComps)
Created chain 'A', start seqCode 1, end seqCode 184, molecule 'G25K GTP-BINDING PROTEIN, PLACENTAL ISOFORM (GP), G25K GTP-BINDING PROTEIN, PL'...
Created chain 'B', start seqCode 186, end seqCode 186, molecule 'MAGNESIUM ION'...
Created chain 'C', start seqCode 187, end seqCode 187, molecule 'Molecule1'...
Created chain 'D', start seqCode 188, end seqCode 188, molecule 'Molecule1'...
Created chain 'E', start seqCode 185, end seqCode 185, molecule 'PHOSPHOAMINOPHOSPHONIC ACID-GUANYLATE ESTER'...
Created chain 'F', start seqCode 73, end seqCode 118, molecule 'SERINE/THREONINE-PROTEIN KINASE PAK-ALPHA'...
"""
  },

'2bzb': {
  'linkResonances': {
   'keywds': {
       'addNameMappings':  {
        'ALL': [["HN","H"]] 
      }
   }
  }
},

'2c0s': {
  'linkResonances': {
   'keywds': {
       'addNameMappings':  {
        'ALL': [["H","H"]]
      }
   }
  }
},

'2hkb': {
  'comments': """
Created chain 'A', start seqCode 1, end seqCode 12, molecule '5'-D(*CP*TP*CP*GP*GP*CP*GP*CP*CP*AP*TP*C)-3''...
Created chain 'B', start seqCode 13, end seqCode 24, molecule '5'-D(*GP*AP*TP*GP*GP*CP*GP*CP*CP*GP*AP*G)-3''...
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0],['B', ' ', 1, 12]],
    }
  }
},

'2hkc': {
  'comments': """
Created chain 'A', start seqCode 1, end seqCode 12, molecule '5'-D(*CP*TP*CP*GP*GP*CP*GP*CP*CP*AP*TP*C)-3''...
Created chain 'B', start seqCode 13, end seqCode 24, molecule '5'-D(*GP*AP*TP*GP*GP*CP*GP*CP*CP*GP*AP*G)-3''...
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0],['B', ' ', 1, 12]],
    }
  }
},

'1egf': {
# 1egf: has ASN HDE,HDZ, TYR CG1,CZ4, HIS HD4, GLN HEE,HEZ, TRP HD2,HH6,HZ7 (not linked)
# jfd added a couple more. Wim, why isn't HE1 linked, is it not defined in ccpn for trp?
  'linkResonances': {
   'keywds': {
      'namingSystem': 'DIANA',
      'addNameMappings':  {
                           'ALL': [['HB1','HB3']],
                           'ARG': [['HD1','HD3'],['HG1','HG3']],
                           'ASN': [['HDE','HD21'],['HDZ','HD22']],
                           'GLN': [['HEE','HE21'],['HEZ','HE22'],['HG1','HG3']],
                           'HIS': [['HD4','HD2'],['HEZ','HE22']], 
                           'ILE': [['HG1','HG12'],['HG2','HG13'],['QD','HD1*']],
                           'PRO': [['HD1','HD3'],['HG1','HG3']],
                           'THR': [['QG','HG2*']],
                           'TRP': [['HD2','HD1'],['HD2','HD1'],['HE1','HE1'],['HH6','HH2'],['HZ7','HZ2']],
                           'TYR': [['CG1','CG'],['CZ4','CZ']],
                           }
      }
    }
  },

'1fls': {
  'comments': """
Created chain ' ', start seqCode 168, end seqCode 168, molecule 'CALCIUM ION'...
Created chain 'A', start seqCode 1, end seqCode 165, molecule 'COLLAGENASE-3'...
Created chain 'B', start seqCode 169, end seqCode 169, molecule 'N-HYDROXY-2-[(4-METHOXY-BENZENESULFONYL)-PYRIDIN-3-YLMETHYL-AMINO]-3-METHYL-BE'...
Created chain 'C', start seqCode 166, end seqCode 166, molecule 'ZINC ION'...
Created chain 'D', start seqCode 167, end seqCode 167, molecule 'ZINC ION'...
  Final mapping: [[' ', ' ', 1, 69], ['A', ' ', 2, -1]]
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0]],
    }
  }
},

'1fm1': {
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0]],
    }
  }
},

'1fmh': {
  'comments': """
Created molecule GENERAL CONTROL PROTEIN GCN4 (molType None, 33 chemComps)
Created molecule Molecule2 (molType None, 33 chemComps)
Created chain 'A', start seqCode 0, end seqCode 32, molecule 'GENERAL CONTROL PROTEIN GCN4'...
Created chain 'B', start seqCode 0, end seqCode 32, molecule 'Molecule2'...
  Final mapping: [['A', ' ', 1, 0], ['B', ' ', 2, 30]]
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A', ' ', 1, -1], ['B', ' ', 1, 30]],
    }
  }
},

'1hdj': {
  'comments': """
Created molecule HUMAN HSP40 (molType protein, 77 chemComps)
Created chain ' ', start seqCode 0, end seqCode 76, molecule 'HUMAN HSP40'...  
  Final mapping: [[' ', ' ', 4, -4]]
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [[' ', ' ', 1, -1]],
    }
  }
},

'2fyl': {
  'comments': """
  haddock entry
Created chain 'A', start seqCode 17, end seqCode 97, molecule 'ALPHA-2-MACROGLOBULIN RECEPTOR-ASSOCIATED ALPHA-2-MACROGLOBULIN RECEPTOR-ASSOC'...
Created chain ' ', start seqCode 83, end seqCode 83, molecule 'CALCIUM ION'...
Created chain 'B', start seqCode 84, end seqCode 84, molecule 'CALCIUM ION'...
Created chain 'C', start seqCode 1, end seqCode 82, molecule 'LOW-DENSITY LIPOPROTEIN RECEPTOR-RELATED PROTEIN LOW-DENSITY LIPOPROTEIN RECEP'...
  Final mapping: [[' ', 'B', 1, 27], ['A', 'B', 1, 13], ['C', 'B', 21, -19]]
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [[' ', 'B', 1, 82], 
                             ['B', 'B', 1, 83], 
                             ['C', 'B', 1, 0]]
    }
  }
},

'2hym': {
  'comments': """
  haddock entry
Created chain 'B', start seqCode 1, end seqCode 165, molecule 'INTERFERON ALPHA-2'...
Created chain 'A', start seqCode 1, end seqCode 212, molecule 'SOLUBLE IFN ALPHA/BETA RECEPTOR'...
  Final mapping: []
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A', 'A', 1, 0], 
                             ['B', 'B', 1, 0]]
    }
  }
},
'2i94': {
  'comments': """
Created chain ' ', start seqCode 500, end seqCode 500, molecule 'CALCIUM ION'...
Created chain 'A', start seqCode 501, end seqCode 501, molecule 'CALCIUM ION'...
Created chain 'B', start seqCode 1, end seqCode 202, molecule 'RECOVERIN'...
Created chain 'C', start seqCode 1, end seqCode 25, molecule 'RHODOPSIN KINASE'...
  Final mapping: [[' ', 'A', 1, 96], ['A', 'A', 1, 97], ['C', 'A', 1, 22]]
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [[' ', 'A', 1, 499], 
                             ['A', 'A', 1, 500], 
                             ['B', 'A', 1, 0],
                             ['C', 'B', 1, 0],
                             ]
    }
  }
},
'2j5h': {
  'comments': """
Created chain 'A', start seqCode 0, end seqCode 40, molecule 'TERATOCARCINOMA-DERIVED GROWTH FACTOR'...
  Final mapping: []
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A', ' ', 1, -1]]
    }
  }
},
'1ayk': {
  'comments': """
Created chain ' ', start seqCode 172, end seqCode 172, molecule 'CALCIUM ION'...
Created chain 'A', start seqCode 1, end seqCode 169, molecule 'COLLAGENASE'...
Created chain 'B', start seqCode 170, end seqCode 170, molecule 'ZINC ION'...
Created chain 'C', start seqCode 171, end seqCode 171, molecule 'ZINC ION'...
  Final mapping: [['B', 'ZN1', 1, 0], ['C', 'ZN2', 1, 0]]
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0]]
    }
  }
},
'1ckk': {
  'comments': """
Created chain 'A', start seqCode 151, end seqCode 151, molecule 'CALCIUM ION'...
Created chain 'B', start seqCode 152, end seqCode 152, molecule 'CALCIUM ION'...
Created chain 'C', start seqCode 153, end seqCode 153, molecule 'CALCIUM ION'...
Created chain 'D', start seqCode 154, end seqCode 154, molecule 'CALCIUM ION'...
Created chain 'E', start seqCode 1, end seqCode 148, molecule 'CALMODULIN'...
Created chain 'F', start seqCode 1, end seqCode 26, molecule 'RAT CA2+/CALMODULIN DEPENDENT PROTEIN KINASE'...
  Final mapping: [['A', 'A', 1, 3], ['B', 'A', 1, 21], ['C', 'A', 1, 22], ['D', 'A', 1, 23]]
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['E', 'A', 1, 0],
                             ['F', 'B', 1, 0]]
    }
  }
},
'1diu': {
  'comments': """
Created chain ' ', start seqCode 1, end seqCode 162, molecule DIHYDROFOLATE REDUCTASE
Created chain 'A', start seqCode 1, end seqCode 1, molecule 'Molecule1'
  Final mapping: [['A', '1', 1, 6]]
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [[' ', '1', 1, 0]]
    }
  }
},
'1dt7': {
  'comments': """
Created chain 'A', start seqCode 114, end seqCode 114, molecule 'CALCIUM ION'...
Created chain 'B', start seqCode 115, end seqCode 115, molecule 'CALCIUM ION'...
Created chain 'C', start seqCode 116, end seqCode 116, molecule 'CALCIUM ION'...
Created chain 'D', start seqCode 117, end seqCode 117, molecule 'CALCIUM ION'...
Created chain 'X', start seqCode 92, end seqCode 113, molecule 'CELLULAR TUMOR ANTIGEN P53'...
Created chain 'Y', start seqCode 92, end seqCode 113, molecule 'CELLULAR TUMOR ANTIGEN P53'...
Created chain 'E', start seqCode 0, end seqCode 91, molecule 'S100 CALCIUM-BINDING PROTEIN'...
Created chain 'F', start seqCode 0, end seqCode 91, molecule 'S100 CALCIUM-BINDING PROTEIN'...
  Final mapping: [['A', 'pep1', 1, 6], ['A', 'pep2', 1, 6], ['B', 'pep1', 1, 7], ['B', 'pep2', 1, 7]]
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['E', 'sbm1', 1, -1], 
                             ['F', 'sbm2', 1, -1], 
                             ['X', 'pep1', 1, 0], 
                             ['Y', 'pep2', 1, 0]]
    }
  }
},

'1fpw': {
  'comments': """
Created chain 'A', start seqCode 500, end seqCode 500, molecule 'CALCIUM ION'...
Created chain 'B', start seqCode 501, end seqCode 501, molecule 'CALCIUM ION'...
Created chain 'C', start seqCode 502, end seqCode 502, molecule 'CALCIUM ION'...
Created chain 'D', start seqCode 1, end seqCode 190, molecule 'CALCIUM-BINDING PROTEIN NCS-1'...
   Final mapping: [['A', ' ', 1, 95], ['B', ' ', 1, 96], ['C', ' ', 1, 139]]
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['D', ' ', 1, 0], 
                             ['A', ' ', 1, 499], 
                             ['B', ' ', 1, 500], 
                             ['C', ' ', 1, 501]]
    }
  }
},

'1gpx': {
  'comments': """
Created chain ' ', start seqCode 107, end seqCode 107, molecule 'GALLIUM (III) ION'...
Created chain 'A', start seqCode 1, end seqCode 106, molecule 'PUTIDAREDOXIN'...
  Final mapping: [[' ', ' ', 1, 33]]
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A', ' ', 1, 0]]
    }
  }
},

'1hm1': {
  'comments': """
Created chain 'A', start seqCode 1, end seqCode 11, molecule 'FAPY ADDUCT OF AFLATOXIN B1 MODIFIED DNA DUPLEX (chain A)'...
Created chain 'B', start seqCode 12, end seqCode 20, molecule 'FAPY ADDUCT OF AFLATOXIN B1 MODIFIED DNA DUPLEX (chain B)'...
  Final mapping: [['B', '1DNA', 1, 4]]
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['A', '1DNA', 1, 0],
                             ['B', '2DNA', 1, 10]
                             ]
    }
  }
},
'1hov': {
  'comments': """
Created chain 'A', start seqCode 167, end seqCode 167, molecule 'CALCIUM ION'...
Created chain 'B', start seqCode 168, end seqCode 168, molecule 'CALCIUM ION'...
Created chain 'C', start seqCode 1, end seqCode 163, molecule 'MATRIX METALLOPROTEINASE-2'...
Created chain ' ', start seqCode 800, end seqCode 800, molecule 'N-{4-[(1-HYDROXYCARBAMOYL-2-METHYL-PROPYL)-(2-MORPHOLIN-4-YL-ETHYL)-SULFAMOYL]'...
Created chain 'D', start seqCode 165, end seqCode 165, molecule 'ZINC ION'...
Created chain 'E', start seqCode 166, end seqCode 166, molecule 'ZINC ION'...
  Final mapping: [[' ', ' ', 1, 56], ['A', ' ', 1, 72], ['B', ' ', 1, 108], ['D', ' ', 1, 146]]
what a nonsensical automatic mapping
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [['C', ' ', 1, 0]]
    }
  }
},
'1hrj': {
  'comments': """
Created chain 'A', start seqCode 1, end seqCode 68, molecule 'HUMAN REGULATED UPON ACTIVATION NORMAL T-CELL HUMAN REGULATED UPON ACTIVATION '...
Created chain 'B', start seqCode 1, end seqCode 68, molecule 'HUMAN REGULATED UPON ACTIVATION NORMAL T-CELL HUMAN REGULATED UPON ACTIVATION '...
No  Final mapping
""",
  'linkResonances': {
   'keywds': {
      'forceChainMappings': [
                             ['A', ' ', 1, 101],
                             ['B', ' ', 1, 201],
                             ]
    }
  }
},

'2p5j': {
  'comments': """
  Final mapping: [['A', ' ', 1, 0]]
""",
  'linkResonances': {
    'keywds': {
      'addNameMappings':{
            'LEU': [ ["QB","HB*"], ["QD1","HD1*"], ["QD2","HD2*"], ["QQD","HD*"] ],
            'VAL': [ ["HG21","HG2*"], ["HG22","HG2*"], ["HG23","HG2*"], ["QG1","HG1*"], ["QG2","HG2*"], ["QQG","HG*"]],
        },
      }
    }
  },

}
print "Read recoord.presetDict version blabla with", len(presetDict.keys()), "keys"
