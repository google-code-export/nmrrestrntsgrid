This directory contains the results of the scoring program (Wattos).

All target links between BMRB and NMR PDB entries are scored and written to
score.csv. The other four score files contain targets that fulfill the
requirements (they have an overall score of less than 9) and can be considered
valid links.

To link from PDB to BMRB entries use: score_many2one.csv. 
To link from BMRB to PDB entries use: score_one2many.csv.

I.e. to link from BMRB to PDB it is probably ok to link from different BMRB
entries to the same PDB entry occasionally. If you don't want that then you
should use the one 2 one version of the scoring file (score_one2one.csv). If you
want to use all the links possible from either side use score_many2many.csv.

Deliverables (at the time of writing, June 9th, 2005)

CSV file name     #elements Description
--------------------------------------------------------------------------------
score             32,140    All target scores.
score_many2many     2098    Scores less than 9.
score_many2one      1525    Entries of BMRB origin may occur multiple times.
score_one2many      1439    Entries of PDB origin may occur multiple times.
score_one2one       1285    Only targets in which both sides of the target occur
                            only once.

