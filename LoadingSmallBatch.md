# Entry set #

`1a24 1a4d 1afp 1ai0 1brv 1bus 1cjg 1hue 1ieh 1iv6 1kr8 2hgh 2k0e`

# PHASE - Prep #
Make sure you work under the development settings.

and check that your classpath starts with the correct jar with:
```
echo $CLASSPATH
/big/docr/workspace/wattos/lib/Wattos.jar....
```
If it's the one in not in workspace you need to change something caus that's production.

Now, empty the tables of the DEVELOPMENT database.

The production database is wattos1. The development is wattos1 but on a different machine (stella). The user name
is always the same as the database name.

Login to the mysql database to remove spurious entries:
```
mysql -h localhost -u wattos1 -p4I4KMS wattos1
```

BEFORE YOU CONTINUE, look at the nice data online in NRG we have in production and develop.
Make sure that after you do the next step only the development has been touched!
It takes about 2 weeks on a single processor to restore the production site completely!

To remove all:
```
mysql -u wattos1 -p4I4KMS  wattos1 < $WS/nmrrestrntsgrid/scripts/sql//db_create.sql
```

Then remove any DBFS files outside the mrannotator by hand.
```
cd /Users/jd/CloneWars/DB/mrgrid/bfiles/wattos1
\rm -rf *
```

# PHASE 1 Original #
One can copy the annotated .mr files from tang in /share/wattos/mr\_anno\_backup
to the in progress dir and do them one by one.

Type:
```
set x = 1a4d
scp /share/wattos/mr_anno_backup/$x.mr \
     /dumpzone/pdb/mr_anno_progress_nrg31
wsetup
mrannotator
```

When that gets old, do the bulk loading using a script in Wattos project/scripts:
```
cd '/Users/jd/CloneWars/DOCR1000/oceans12/bmrb/' # where .mr files are located.
```
I have another copy on tang:
`cd/big/jurgen/oceans12/bmrb`
Note the list of the random 100 resides in:
```
/big/jurgen/random100/list.csv
```

Then edit
```
$WS/wattos/scripts/load_db_raw.csh
```
and execute.

# PHASE 2 Parsed #

Assuming the above has been set.

Look up the script:
$WS/wattos/scripts/load\_db\_conversions.csh

Run the java command inside once to see if it works for one small entry (may
I suggest 1a24?). If it works for one it should work for all.
Note that even though the script is called something with 'conversions' it
results in the data being at the PHASE 2: Parsed.

# PHASE 3 and 4 - Converted and Filtered. #

Assuming the above has been set.
Look up the modified well-known scripts:
```
$WS/nmrrestrntsgrid/scripts/processDOCR_FRED.csh
$scripts_dir/weeklyDOCR_FRED.csh
```
(same dir)

Note: doGet (part of weeklyDOCR\_FRED) manually if you are doing a lot of entries.
#   if you need many (100+) do this step manually separate from this setup (getFilesFromGrid.csh)
You can edit getFilesFromGrid.csh so that you access everything at once.

First check again if you have the development settings for the nmrrestrntsgrid
project. The scripts\_dir variable now needs to point to $WS/nmrrestrntsgrid/scripts.
WS stands for the workspace directory on /big/docr.

Do:
```
echo $scripts_dir
```
and ensure it points to  point to $WS/nmrrestrntsgrid/scripts.

# NEW: #
The restraint files that are input to process\_DOCR\_FRED.csh need first to be put into place using the weekly script. In settings.csh there is a servletUrl to be edited before you try this on a different machine. Perhaps use the suggested
```
setenv servletUrl  'http://localhost:8080/NRG/MRGridServlet'
```
Then edit the line to reflect which entries you want to do such as:
```
set subl = (`cat $list_dir/list_baddies_2009-08-03.csv`)
```
The way you run it hasn't changed:
```
set x = 1a4d  ; $scripts_dir/processDOCR_FRED.csh $x |& tee $perEntry_dir/$x.log
cat $dir_star/$x/$x.log
```

Check he NRG results: http://restraintsgrid.bmrb.wisc.edu/NRG/MRGridServlet

Check in the usual way with the script weeklyDOCR\_FRED.csh.

## NB ##
  * Don't do the 'whole/weekly' set yet.
  * Recall that the script will fail with "No input STAR parsed restraints file:
```
/big/docr/NRG/restraint/unzipped/1a4d_rst.str
```

if they haven't been retrieved with the weekly script -first-.
  * The log file for the FC step is in $ccpn\_tmp\_dir/data/recoord/$x
  * Entry 2k0e takes the FC about 35 minutes if a cpu is available even after the ensemble is truncated to a max of 7500 residues total.
**Consider that the presetDict.py needs to be brought up to date.**

Now go ahead and try putting all 13 in. Five entries will fail yet.