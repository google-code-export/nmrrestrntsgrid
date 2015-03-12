Dear Sirs I want to analyze different NMR models according to the amount of restraints per residues that they have. As you noted in your article the data in the PDB are not annotated in a standard form and are therefore very hard to read by computer. Is it possible to use your site (http://www.bmrb.wisc.edu/), to insert a list of pdb entries and receive the number of constraints for each entry in a standardized file? If so please direct me regarding how it is done. Thanks

# Here's one way of doing this: #

http://nmrrestrntsgrid.googlecode.com/files/restraintsPerResidueFiles.zip

**A) get the number of restraints per entry from the NMR Restraints Grid:
  1. Goto: http://www.bmrb.wisc.edu/servlets/MRGridServlet
  1. Select "3-converted-DOCR" for stage; submit for an update
  1. Select the number on the row: "entry full" under column: "STAR". At the moment this is ~3145.
  1. Per entry a row is listing the number of restraints under the column header: "item\_count". Select: [to zip file containing files for each block.](Save.md) above the table. This will download the actual data (>1 Gb) but also a small csv file (attached) with the meta data and some documentation.**

**B) Get the size of the molecular assembly from the PDB:
  1. Goto: http://www.rcsb.org/pdb/Welcome.do
  1. Select "Search"/Advanced Search on the left paneling.
  1. Select the options for experimental technique as per attached giffie and "Evaluate Query"
  1. Select "Tabulate"/"Custom Report" and within select only " Chain Length" then "Create report"
  1. Then again "Create report" to get a csv file as attached.**

**C) Import both csv files in a database such as MS Access to do the logical combinations. See attached results xls file for the outcome.**

Note that:
  1. the sequence in the PDB is often longer than for which coordinates and restraints were reported for.
  1. You might consider doing a more full interpretation of the data based on the NMR-STAR files.
  1. You might also want to consider using the restraint count from FRED as it excludes more junk.
  1. E.g the restraints per residue of PDB\_ID SumOfchainLength? ITEM\_COUNT perRes 1VND 77 14560 189.09 are mostly non-NOEs so it's arguable for them to be included.
  1. For 545 monomeric protein entries in RECOORD the number you're looking for is also available online;just google for it. We're in the process of extending that database to most of the >3,500 entries with restraints now.