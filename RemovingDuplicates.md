# Introduction #

The mrannotator sometimes starts to show:
```
ERROR: There are duplicates in database: [2kg8]
ERROR: Unique list of them: [2kg8]
Then the db is messed up with a duplicate.
```

# Details #

Remove it by taking the entry out of db:
```
mrannotator
Annotate from mirror(m), in progress(i), database(d)?
*d*
Possible entries include:[108d, 149d, 170d, 171d, 17ra, 1a03, 1a1p, 1a1t, 1a24, 1a2i, 1a2s, 1a3p, 1a4d, 1a51, 1a57, 1a5e, 1a5j, 1a60, 1a6x, 1a7f]
Annotate one entry(y) or consecutive entries(n)? (y/n): *y*
Give entry code (e.g.: 108d) to annotate: *2kg8*

Get the MR file_id from the pdb code and detail value.
WARNING: in MRAnnotate.annotateEntry
ERROR: WARNING: got more mrfile ids for pdb entry code:2kg8
ERROR: WARNING: will just use the first one
Copy the MR file from the database.
Writing file: /dumpzone/pdb/mr_anno_progress_nrg31/2kg8.mr
Removing all the files associated with this PDB entry from the database.
The number of entries deleted              : 1
X11 connection rejected because of wrong authentication.
STDERR>X connection to localhost:11.0 broken (explicit kill or server shutdown).
ERROR: in MRAnnotate.annotateEntry found:
ERROR: Error editing this entry. Please remove temporary files
ERROR: Skipping this entry.
Start over? (y/n): n
```