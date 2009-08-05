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
        make sure it runs on all 4 tables. Ignore warnings for missing files:
        ~10 violations,645 assignment and the others.
-a1- Use Wattos.Utils.getMolTypes.py (needs a star api)
-b0- Create database for wattosAn: create database wattosAn;
-b- customize and run importExternalTablesWattosAn.sql:
    mysql -u root wattosAn < $scripts_dir/sql/importExternalTablesWattosAn.sql
-c- customize and run createWattosAn.sql (Yes do this -after- the previous step.)
    mysql -u root wattosAn < $scripts_dir/sql/createWattosAn.sql
-d- data/extract view: overviewall and other views to csv:
    sudo su
    rm /tmp/*.csv >& /dev/null
    # On nmr machine command takes a while to run.
    mysql -u root wattosAn < $scripts_dir/sql/exportTablesWattosAn.sql
    # Back on development machine again:
    scp -P 39676 jd@localhost-nmr:/tmp/\*.csv /Users/jd/Desktop/Werk/NRG_Paper/csv
-e- Import into excel in tab: "auto imported" -> "Right click" -> "Edit text import"
-f- Copy and paste the 5 columns from "auto imported" to SortedCriteria
-g- Order each of those columns in that tab only. The rest will be updated autom.


Completeness:

mysql> select * from complMoltypesStats;
+---------------------------------+------------------+-----------------+
| type                            | avg(c.compl)     | count(m.pdb_id) |
+---------------------------------+------------------+-----------------+
| polymer/polypeptide(L)          | 43.1308918517887 |            2321 |
| polymer/polyribonucleotide      | 34.1399999011647 |             110 |
| polymer/polydeoxyribonucleotide | 27.1847457077544 |              59 |
| polymer/unknown                 | 35.2000001271566 |               3 |
| polymer/polypeptide(D)          | 49.9000015258789 |               1 |
+---------------------------------+------------------+-----------------+


