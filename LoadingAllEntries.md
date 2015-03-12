# Notes #

Taking diffs on the mr files annotated and originals and using that in Nijmegen to reconstruct the annotations.

# patched versions #
> jurgen@tang.bmrb.wisc.edu:/share/wattos/mr\_anno\_backup/$x.mr


Edit/run:
$WS/wattos/scripts/load\_db\_raw.csh

check the log for errors.
E.g. JFD saw:
```
Reading file: ./1go0.mr as a textual file.
Read 0 lines.
Doing: splitToBlocks
DEBUG: Split text into 0 blocks
DEBUG: Check: checkBlockCount
ERROR: in DBMRFile.checkBlockCount found:
ERROR: Number of blocks found: 0
ERROR: Expected a positive number of blocks
DEBUG: Check: checkBlockTypes
DEBUG: Check: checkBlockEmptiness
ERROR: Found one or more errors by checking.
ERROR: in MRInterloop.loadEntry found:
ERROR: Checks not successful.
```

Also check these suspicious entries:
```
jd:nmr/~/ l $mr_anno_progress_dir | sort -n --key=5 | head
-rw-------     1 jd  jd            0 Mar 20 13:19 1go0.mr
-rw-------     1 jd  jd            0 Mar 20 13:20 1m9o.mr
total 8567976
drwxr-xr-x    10 jd  jd          340 Mar 20 13:54 ../
-rw-------     1 jd  jd          617 Mar 20 13:19 1ccf.mr
-rw-------     1 jd  jd          733 Mar 20 13:19 1e0n.mr
-rw-------     1 jd  jd         2254 Mar 20 13:19 1ftt.mr
-rw-------     1 jd  jd         3510 Mar 20 13:20 1pjd.mr
-rw-r--r--@    1 jd  jd         6148 Nov 29  2007 .DS_Store
-rw-------     1 jd  jd         6526 Mar 20 13:21 2h3o.mr
```

  * 1go0 is [issue 194](https://code.google.com/p/nmrrestrntsgrid/issues/detail?id=194)
  * 1m9o is fixed now because it was 1m9O (capital O)
  * 1ccf is [issue 195](https://code.google.com/p/nmrrestrntsgrid/issues/detail?id=195)

Get them with getMrAnnotated.csh from tang.