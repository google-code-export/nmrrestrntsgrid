-- First whipe them out with the following commandline:
-- rm /tmp/*.csv

SELECT pdb_id FROM phase1 into OUTFILE '/tmp/nrg_phase1.csv';
SELECT pdb_id FROM phase2 into OUTFILE '/tmp/nrg_phase2.csv';
SELECT pdb_id FROM phase3 into OUTFILE '/tmp/nrg_phase3.csv';
SELECT pdb_id FROM phase4 into OUTFILE '/tmp/nrg_phase4.csv';

-- Entries dropped from phase 1 to 2 (none on april 21th).
SELECT pdb_id FROM phase1
where pdb_id not in ( select pdb_id from  phase2 )
order by pdb_id
into OUTFILE '/tmp/nrg_phase2lost.csv';

-- Entries dropped from phase 2 to 3
SELECT pdb_id FROM phase2
where pdb_id not in ( select pdb_id from  phase3 )
order by pdb_id
into OUTFILE '/tmp/nrg_phase3lost.csv';

SELECT pdb_id FROM amber into OUTFILE '/tmp/nrg_amber.csv';

-- Note that "OPTIONALLY ENCLOSED BY " can not be suplied by itself alone.
SELECT * FROM OverviewAll into OUTFILE '/tmp/overviewAll.csv'
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES  TERMINATED BY '\n';

SELECT pdb_id FROM perdocrbad into OUTFILE '/tmp/perdocrbad.csv';
SELECT pdb_id FROM perfredbad into OUTFILE '/tmp/perfredbad.csv';
SELECT pdb_id FROM violmaxbad into OUTFILE '/tmp/violmaxbad.csv';
SELECT pdb_id FROM violrmsbad into OUTFILE '/tmp/violrmsbad.csv';

SELECT pdb_id FROM DOCRFREDEntriesAll   into OUTFILE '/tmp/DOCRFREDEntriesAll.csv';
SELECT pdb_id FROM DOCRFREDEntries      into OUTFILE '/tmp/DOCRFREDEntries.csv';
SELECT pdb_id FROM DOCRFREDGoodies      into OUTFILE '/tmp/DOCRFREDGoodies.csv';
SELECT pdb_id FROM Set14DOCRFREDBaddies into OUTFILE '/tmp/Set14DOCRFREDBaddies.csv';

SELECT *      FROM complMoltypes into OUTFILE '/tmp/complMoltypes.csv'
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES  TERMINATED BY '\n';



SELECT *      FROM _Distance_constraint_surplus_percentages into OUTFILE '/tmp/_Distance_constraint_surplus_percentages.csv'
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES  TERMINATED BY '\n';

