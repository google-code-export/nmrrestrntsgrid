--Queries for analyses used in paper NRG. First the definitions, followed by the results for table 1 in the NRG paper.


-- Table 1 row: NMR with restraints 4,411
DROP VIEW IF EXISTS DOCRFREDEntriesAll;
CREATE VIEW DOCRFREDEntriesAll AS
SELECT DISTINCT pdb_id
FROM wattos1.mrfile
order by pdb_id;

-- Table 1 row: With parsable restraints
DROP VIEW IF EXISTS DOCRFREDEntries;
CREATE VIEW DOCRFREDEntries AS
    SELECT DISTINCT pdb_id
    FROM wattos1.`mrblock` b, wattos1.`mrfile` f
    where b.mrfile_id=f.mrfile_id AND
    b.text_type='2-parsed' AND
    b.type = 'entry' AND
    b.subtype = 'full' AND
    b.item_count >=1;

-- Table 1 row: With parsed distance restraints
DROP VIEW IF EXISTS DOCRFREDEntriesDR;
CREATE VIEW DOCRFREDEntriesDR AS
    SELECT DISTINCT pdb_id
    FROM wattos1.`mrblock` b, wattos1.`mrfile` f
    where b.mrfile_id=f.mrfile_id AND
    text_type='2-parsed' AND
    type = 'distance' AND
    b.item_count >= 1;

-- Table 1 row: 'Good' set
DROP VIEW IF EXISTS DOCRFREDGoodies;
CREATE VIEW DOCRFREDGoodies AS
SELECT df.pdb_id
FROM DOCRFREDEntries df
where df.pdb_id not in ( select pdb_id from Set14DOCRFREDBaddies )
order by df.pdb_id;

-- Get counts of pdb entries per program
SELECT count(DISTINCT f.pdb_id), b.program
FROM wattos1.mrblock AS b, wattos1.mrfile AS f
WHERE b.mrfile_id=f.mrfile_id and (
    b.type='dipolar coupling' OR
    b.type='distance' OR
    b.type='dihedral angle'
)	AND
b.text_type = '1-original'
group by b.program
order by count(DISTINCT f.pdb_id);

-- Surplus analysis
DROP VIEW IF EXISTS _Distance_constraint_surplus_percentages;
CREATE VIEW _Distance_constraint_surplus_percentages AS
SELECT pdb_id,
        Constraint_surplus_count/Constraint_count as surplus,
        Constraint_redundant_count/Constraint_count as redundant,
        Constraint_double_count/Constraint_count as dubbel,
        Constraint_fixed_count/Constraint_count as fixed,
        Constraint_impossible_count/Constraint_count as impossible,
        Constraint_exceptional_count/Constraint_count as exceptional
from _Distance_constraint_surplus
where Constraint_count!=0 AND
    pdb_id not in ( select b.pdb_id from Set14DOCRFREDBaddies b );


DROP VIEW IF EXISTS RDC_Entries;

CREATE VIEW RDC_Entries AS
SELECT DISTINCT f.pdb_id
FROM wattos1.mrblock AS b, wattos1.mrfile AS f
WHERE b.mrfile_id=f.mrfile_id and text_type='3-converted-DOCR' and type='dipolar coupling'
order by f.pdb_id;

-- Get the entries that only have 1 type (1 or more entities of it)
DROP VIEW IF EXISTS moltypesOverview;

CREATE VIEW moltypesOverview AS
SELECT pdb_id,type,typescount
FROM moltypes
group by pdb_id
having count(*)=1
order by pdb_id;

-- Get the completeness per moltype/entries
DROP VIEW IF EXISTS complMoltypes;
CREATE VIEW complMoltypes AS
SELECT m.pdb_id,m.type,c.compl
FROM moltypesOverview m, _NOE_completeness_stats c
where m.pdb_id=c.pdb_id AND
    m.pdb_id not in ( select pdb_id from RDC_Entries ) and
    m.pdb_id not in ( select pdb_id from Set14DOCRFREDBaddies )
order by m.type,c.compl desc,m.pdb_id;

-- Average and occurancies on the above table.
DROP VIEW IF EXISTS complMoltypesStats;
CREATE VIEW complMoltypesStats AS
SELECT m.type, avg(c.compl), count(m.pdb_id)
FROM moltypesOverview m, _NOE_completeness_stats c
where m.pdb_id=c.pdb_id AND
    m.pdb_id not in ( select pdb_id from RDC_Entries ) and
    m.pdb_id not in ( select pdb_id from Set14DOCRFREDBaddies )
group by m.type
order by count(m.pdb_id) desc;


-- Fails for some weir reason:
-- ERROR 1054 (42S22): Unknown column 'p2.ITEM_COUNT' in 'order clause'

-- Table 1 rows: Sets 1-4 and Set Union
SELECT count(*) FROM perdocrbad; -- 419
SELECT count(*) FROM perfredbad; -- 317
SELECT count(*) FROM violmaxbad; -- 319
SELECT count(*) FROM violrmsbad; -- 264
select count(distinct pdb_id) from set12; -- 475
select count(distinct pdb_id) from set34; -- 382

select count(pdb_id) from DOCRFREDEntriesAll;      -- 4,411
select count(pdb_id) from DOCRFREDEntries;         -- 3,969
select count(pdb_id) from Set14DOCRFREDBaddies;    --   754
select count(pdb_id) from DOCRFREDGoodies;         -- 3,208
