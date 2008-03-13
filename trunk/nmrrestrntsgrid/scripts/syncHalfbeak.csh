#!/bin/csh 
# Author: Jurgen F. Doreleijers 
# Fri Jun  2 14:37:52 CDT 2006
#syncing between halfbeak work on /big and /big on tang called /bigtang on halfbeak.

#Needed because WHATIF doesn't work fast enough over nfs mounted drives.

# on halfbeak
# update files on tang only if they're newer on halfbeak perserving all priorities.
cp -rvup /big/jurgen/DB/mrgrid/bfiles/wattos2/* /bigtang/jurgen/DB/mrgrid/bfiles/wattos2
#and if needed use \ and -f and all files. 
\cp -rfvup /big/jurgen/* /bigtang/jurgen


delete from `mrfile`
where detail like '3%' or detail like '4%'
