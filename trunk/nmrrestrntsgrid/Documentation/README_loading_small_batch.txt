Doc for how to load a small batch of entries (e.g. oceans12)

1a4d 1a24 1afp 1ai0 1brv 1bus 1cjg 1hue 1ieh 1iv6 1kr8 2hgh 2k0e

********************************************************************************
PHASE - Prep
********************************************************************************
Make sure you work under the development settings. Execute:

swNRG31

and check that your classpath starts with the correct jar with:

wsetup
echo $CLASSPATH
/big/docr/workspace/wattos/lib/Wattos.jar....

If it's the one in /share you need to change something caus that's production.


Now, empty the tables of the DEVELOPMENT database.

The production database is wattos2. The development is wattos1. The user name
is always the same as the database name.

Login to the mysql database to remove spurious entries:
mysql -h localhost -u wattos1 -p4I4KMS wattos1

BEFORE YOU CONTINUE, look at the nice data online in NRG we have in production and develop.
Make sure that after you do the next step only the development has been touched!
It takes a long time before I can restore the production site completely. Perhaps
as much as a week!
 
-- To remove all:
delete from entry;

********************************************************************************
PHASE I parsed
********************************************************************************
One can copy the annotated .mr files from tang in /share/wattos/mr_anno_backup
to the in progress dir and do them one by one.

Type:
set x = 1a4d
scp jurgen@tang.bmrb.wisc.edu:/share/wattos/mr_anno_backup/$x.mr \
     /Users/jd/wattosTestingPlatform/Wattos/mr_anno_progress
     
wsetup
mrannotator

When that gets old, do the bulk loading using a script in Wattos project/scripts:
cd '/Users/jd/CloneWars/DOCR1000/oceans12/bmrb/' # where .mr files are located.
I have another copy in tang: /big/jurgen/oceans12/bmrb
$WS/wattos/scripts/load_db_raw.csh


********************************************************************************
PHASE II Converted
********************************************************************************

Assuming the above has been set.

Look up the script:
$WS/wattos/scripts/load_db_conversions.csh

Run the java command inside once to see if it works for one small entry (may
I suggest 1a24?). If it works for one it should work for all.


