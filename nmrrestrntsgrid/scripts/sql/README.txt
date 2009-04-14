This directory contains database related files used by Wattos.

Content files           Description
------------------------+-------------------------------------------------------
README.txt              This file.
analysesPaper.sql       Analysis on WattosAn database for paper DOCR2
createWattosAn.sql      Creates a database for analysis of the NMR Restraint Grid db.
importExternalTablesWattosAn.sql Imports relevant external tables.
wattosAn.clay           Clay related file for modeling databases.


Notes:
-a- customize and run $scripts_dir/getSTARinfo.csh
        make sure it runs on all 4 tables
-b- customize and run importExternalTablesWattosAn.sql:
    mysql -u root wattosAn < $WS/nmrrestrntsgrid/scripts/sql/importExternalTablesWattosAn.sql
-c- customize and run createWattosAn.sql (Yes do this -after- the previous step.)
    mysql -u root wattosAn < $WS/nmrrestrntsgrid/scripts/sql/createWattosAn.sql
-d- data/extract view: overviewall to csv in eclipse (command line below seems to fail on OS permissions).
    rm /Users/jd/Desktop/Werk/NRG_Paper/overviewAll.csv
    mysql -u root wattosAn < $WS/nmrrestrntsgrid/scripts/sql/exportTablesWattosAn.sql    
-e- Import into excel in tab: "auto imported" -> "Right click" -> "Edit text import"
-f- Copy and paste the 5 columns from "auto imported" to SortedCriteria
-g- Order each of those columns in that tab only. The rest will be updated autom.

Still needed?
??-6- use excel to add column: =IF(AND(AND(A4>=0.8,B4>=0.3333),AND(D4<=2,E4<=0.25)),1,"")

