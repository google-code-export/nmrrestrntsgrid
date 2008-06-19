Doc for how to load a small batch of entries (e.g. oceans12)


1a4d 1a24 1afp 1ai0 1brv 1bus 1cjg 1hue 1ieh 1iv6 1kr8 2hgh 2k0e

One can copy the annotated .mr files from tang in /share/wattos/mr_anno_backup
to the in progress dir and do them one by one.

set x = 1a4d
scp jurgen@tang.bmrb.wisc.edu:/share/wattos/mr_anno_backup/$x.mr \
     /Users/jd/wattosTestingPlatform/Wattos/mr_anno_progress
     
wsetup
mrannotator

When that gets old, do the bulk loading using a script in Wattos project/scripts:
cd '/Users/jd/CloneWars/DOCR1000/oceans12/bmrb/' # where .mr files are located.

$WS/wattos/scripts/load_db_raw.csh

