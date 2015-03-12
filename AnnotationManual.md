# Introduction #

This wiki may contain the most up to date info on how to annotate the weekly entries.

The web page for the MRgrid:

_http://restraintsgrid.bmrb.wisc.edu/NRG/MRGridServlet_

# Environment Settings #

The development settings including what wsetup does are now initialized from the ~/.cshrc no need to do anything.

After this there should be rights jars included in the classpath.
To check that do:

`echo $CLASSPATH`

The first jar should be:

`/big/docr/workspace/wattos/lib/Wattos.jar`

# Annotation #

After setting the environment classpath, start annotation by executing:

`mrannotator`

Choose the place where you like to start your processing. After annotating, save and quit from Jedit. The parsing process will start. Check any possible errors at this parsing phase and fix the errors .

# Post Processing #

When the initial annotation is finished, this script is run:


Right now the process use only one model(the first model) during the conversion. This setting is in the processDOCR\_FRED.csh . The weeklyDOCR\_FRED.csh inherit such setting since it indirectly call the the processDOCR\_FRED.csh script.

The directory for these two scripts is:

`/big/docr/workspace/nmrrestrntsgrid/scripts`

There is alias for this directory is $script\_dir.



Check the output of the  weeklyDOCR\_FRED.csh.

The location of the settings (presetDict.py) for the new NRG is at:

```
/big/docr/workspace/recoordD/python/recoord2
```

There is a alias for this directory $P.


# Settings #

  * The settings for the new NRG can be modified at:
```
tang:/big/docr/workspace/recoordD/python/recoord2/presetDict.py 
```

There are files generated during the postprocessing.

The log file are at

```
/big/docr/NRG/link
```
The alias for this directory is:
```
$dir_link
```
the summary file is ###_merge.log_

There are traceback information in the log file.

Other files that are useful for looking for clues for setting to FC are:

atoms\_tmp.txt
guessLink.txt

link\_NMRStar.log (this file is not in the directory yet, it's need to be copied from CCPN dir)

The files link\_NMRStar.log from CCPN are at:

/big/docr/ccpn\_tmp/data/recoord/


It is the annotator's responsibility for sync-ing with the cvs.