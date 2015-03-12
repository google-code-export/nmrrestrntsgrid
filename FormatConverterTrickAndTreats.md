# Introduction #

Probably good to start a list

# Interpreting the log files (courtesy of Wim) #

see the closed [issue 82](http://code.google.com/p/nmrrestrntsgrid/issues/detail?id=82&colspec=Milestone%20Priority%20ID%20Entry%20Component%20FC%20Type%20Status%20Owner%20Summar) for the discussion

The .summary file should give you enough information to do the linking. In the case of 2k0e (if it does not have a presetDict entry), you should first get these lines:
```
Number of atom strings read:                        1157
Number of CCPN resonances created from these:       1340

Percentage of CCPN resonances linked to atoms:       87.91%
```

The first two lines are more for my information, what you need to look at is the 'Percentage of...' line. This tells you how well the information from the constraints in the NMR-STAR file was 'linked' to atoms in the CCPN data model.

If all goes well, this is 100.0%
If it didn't link anything, this is 0.0%

So if an entry has 100.0% linked, then it's fine. If it's +98.0%, then usually some of the original names from the NMR-STAR file weren't recognized. If it is lower, then there are usually more serious problems.

In order to then link the data from the NMR-STAR file to the CCPN, you can use the information further down in the file

Under 'Unlinked data from original restraint file:' you find the chain and sequence codes from the NMR-STAR file, with the corresponding atom names and residue codes (if any).

Under 'Data on molecules in CCPN', you find information on the chains in CCPN.

In this case, I have the following. Unlinked data from original restraint file:
```
 Chain code ' '
  143      : HB
  181      : MN
  182      : MN
  183      : MN
  184      : MN
  201      : HA, HB#
... [truncated]

Data on molecules in CCPN:

 Chain code 'A'
  1 (Ala)...148 (Lys)

 Chain code 'B'
  151 (Ca): CA

 Chain code 'C'
  152 (Ca): CA

 Chain code 'D'
  153 (Ca): CA

 Chain code 'E'
  154 (Ca): CA
```


I assume the MN residues 181-184 correspond to the Ca chains in CCPN, not sure what residues 201-226 are in this case.

# Speed #
  * Reduce the number of models for testing
> > The fastest way to run the FC is to eliminate most of it's input anywho. In the $script\_dirs/wcf/ReadMmCifWriteNmrStar.wcf there is a setting for that to reduce the number to 7500 but better still; use 500 to be sure you get at least one model (Wattos isn't clever enough to not truncate to at least one). This way I saw the FC processing speed for entry 2hgh drop to an astounding 30 seconds on a macbook pro!

  * Reduce the number of models for testing (courtesy of Wim)
> > In python/recoord2/msd/linkNmrStarData.py just set the numModelsToRead variable inside the LinkNmrStarData
class. This could be useful for quicker testing (set it to 1 temporarily). For 1cjg with 11 models this improved the processing speed from 3'45 to 1'58 on the macbook pro Stella just playing some Doe Maar in the background. Not a huge improvement but everything helps.

  * Limit processing to all but the final write of the NMR-STAR file. (courtesy of Wim)
> > > ...  to test the conversion itself, I've now added a '-noWrite' option that you can pass into the [python/recoord2/msd/linkNmrStarData.py] script. The final NMR-STAR file will not be written, and should speed things up considerably when testing the conversion stage (the .summary file will still be generated).
> > In the NRG setup this can be passed by changing setting:
```
    set extraFCOptions      = ( -raise -force )
    to:
    set extraFCOptions      = ( -raise -force -noWrite )
```
> > For 1cjg with 1 model this improved the processing speed further from 1'58 to 1'48 on the macbook pro Stella now playing some Iron Maiden. So this seems to be a minor improvement.