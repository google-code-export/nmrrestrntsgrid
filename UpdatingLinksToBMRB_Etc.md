# Introduction #

Each record in NRG can be linked to the above 3 databases.

# Updating #
As docr@grunt update the database fields:
```
/docr/ java -Xmx128m Wattos.Episode_II.MRUpdateLinksToExternalDBs $WS/nmrrestrntsgrid/bmrb_pdb_match/results
Opened sql connection:Wattos.Episode_II.SQL_Episode_II@375e9756
Reading relation : bmrb_main
Reading relation : pdb_main
Reading relation : score_many2one
All keys are valid
All keys are valid
Reading relation : recoord
All keys are valid
Reading relation : dress
All keys are valid
Checking fkc: ForeignKeyConstraint from relation: [score_many2one] at column: [bmrb_id] references relation: [bmrb_main] at column: [bmrb_id]
All keys are valid
Checking fkc: ForeignKeyConstraint from relation: [score_many2one] at column: [pdb_id] references relation: [pdb_main] at column: [pdb_id]
All keys are valid
Checking fkc: ForeignKeyConstraint from relation: [recoord] at column: [pdb_id] references relation: [pdb_main] at column: [pdb_id]
All keys are valid
Checking fkc: ForeignKeyConstraint from relation: [dress] at column: [pdb_id] references relation: [pdb_main] at column: [pdb_id]
All keys are valid
Cleared column: bmrb_id in entry table
Cleared column: in_recoord in entry table
Cleared column: in_dress in entry table
Updating BMRB links numbered: 1708
Updating links from relation recoord numbered: 543
Updating links from relation dress numbered: 100
All done
```