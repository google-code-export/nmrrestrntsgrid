-- Code to create the views based on the wattos1 db.
DROP view IF EXISTS PERFREDTMP;
CREATE VIEW PERFREDTMP
    AS
SELECT F.PDB_ID, B.TEXT_TYPE, B.ITEM_COUNT
FROM wattos1.mrblock AS B, wattos1.mrfile AS F
WHERE B.mrfile_ID=F.mrfile_ID AND TYPE='entry' AND PROGRAM='STAR'
ORDER BY F.PDB_ID, B.TEXT_TYPE;

DROP view IF EXISTS PERFRED;
CREATE VIEW PERFRED
    AS
SELECT P1.PDB_ID AS PDB_ID, P1.ITEM_COUNT AS C_PARS, P2.ITEM_COUNT AS C_FILTER, P2.ITEM_COUNT/P1.ITEM_COUNT AS P_FILTER
FROM PERFREDTMP AS P1, PERFREDTMP AS P2
WHERE (((P1.PDB_ID)=P2.PDB_ID) AND ((P1.ITEM_COUNT)>0) AND ((P1.TEXT_TYPE)='2-parsed') AND ((P2.TEXT_TYPE)='4-filtered-FRED'))
ORDER BY P2.ITEM_COUNT/P1.ITEM_COUNT DESC;

DROP view IF EXISTS PERFREDBAD;
CREATE VIEW PERFREDBAD
    AS
SELECT PDB_ID
FROM PERFRED
WHERE P_FILTER<0.333333;

DROP view IF EXISTS PERDOCR;
CREATE VIEW PERDOCR
    AS
SELECT P1.PDB_ID AS PDB_ID, P1.ITEM_COUNT AS C_PARS, P2.ITEM_COUNT AS C_FILTER, P2.ITEM_COUNT/P1.ITEM_COUNT AS P_FILTER
FROM PERFREDTMP AS P1, PERFREDTMP AS P2
WHERE (((P1.PDB_ID)=P2.PDB_ID) AND ((P1.ITEM_COUNT)>0) AND ((P1.TEXT_TYPE)='2-parsed') AND ((P2.TEXT_TYPE)='3-converted-DOCR'))
ORDER BY P2.ITEM_COUNT/P1.ITEM_COUNT DESC;


DROP view IF EXISTS PERDOCRBad;
CREATE VIEW PERDOCRBAD
    AS
SELECT PDB_ID
FROM PERDOCR
WHERE P_FILTER<0.8;


DROP view IF EXISTS _Distance_constraint_stats_list_Query_Rms;
CREATE VIEW _Distance_constraint_stats_list_Query_Rms
    AS
SELECT _Distance_constraint_stats_list.pdb_id,
    Sqrt(Sum(Constraint_count*Viol_rms*Viol_rms)/Sum(Constraint_count)) AS WgtAvgRms
FROM _Distance_constraint_stats_list
GROUP BY _Distance_constraint_stats_list.pdb_id;

DROP view IF EXISTS _Distance_constraint_stats_list_Query_Max;
CREATE VIEW _Distance_constraint_stats_list_Query_Max
    AS
SELECT DISTINCTROW _Distance_constraint_stats_list.pdb_id,
Max(_Distance_constraint_stats_list.Viol_max) AS MaxOfViol_max
FROM _Distance_constraint_stats_list
GROUP BY _Distance_constraint_stats_list.pdb_id;



DROP view IF EXISTS violRmsBad;
CREATE VIEW violRmsBad
    AS
SELECT pdb_id, WgtAvgRms
FROM _Distance_constraint_stats_list_Query_rms
WHERE WgtAvgRms>0.25;


DROP view IF EXISTS violMaxBad;
CREATE VIEW violMaxBad
    AS
SELECT _Distance_constraint_stats_list_Query_Max.pdb_id,
        _Distance_constraint_stats_list_Query_Max.MaxOfViol_max
FROM   _Distance_constraint_stats_list_Query_Max
WHERE  _Distance_constraint_stats_list_Query_Max.MaxOfViol_max>2;


-- Get the counts of the unions of these 4 sets.
DROP view IF EXISTS set12;
CREATE VIEW set12 AS
SELECT d.pdb_id
from perDocrBad d
UNION
SELECT f.pdb_id
from perFredBad f;

DROP view IF EXISTS set34;
CREATE VIEW set34 AS
SELECT v1.pdb_id
from violMaxBad v1
UNION
SELECT v2.pdb_id
from violRmsBad v2;

DROP view IF EXISTS Set14DOCRFREDBaddies;
CREATE VIEW Set14DOCRFREDBaddies
    AS
SELECT d.pdb_id
from perDocrBad d
UNION
SELECT f.pdb_id
from perFredBad f
UNION
SELECT v1.pdb_id
from violMaxBad v1
UNION
SELECT v2.pdb_id
from violRmsBad v2;

-- Note in the below that using a NATURAL keyword instead of the ON clause
-- fails to pick up all the values because perFred and perDocr share
-- more than the one column name 'pdb_id' in common.
DROP view IF EXISTS overviewAll;
CREATE VIEW OverviewAll AS
SELECT
P.p_filter as perDocr,
F.p_filter as perFred,
S.pdb_id,
M.MaxOfViol_Max,
R.WgtAvgRms
FROM
((((wattos1.entry S
LEFT OUTER JOIN perDocr P ON S.pdb_id = P.pdb_id)
LEFT OUTER JOIN perFred F ON S.pdb_id = F.pdb_id)
LEFT OUTER JOIN _Distance_constraint_stats_list_Query_Max M ON S.pdb_id = M.pdb_id)
LEFT OUTER JOIN _Distance_constraint_stats_list_Query_rms R ON S.pdb_id = R.pdb_id)
ORDER BY S.pdb_id;

-- Get phase 1 entries
DROP view IF EXISTS phase1;
CREATE VIEW phase1 AS
SELECT distinct pdb_id
FROM wattos1.`mrblock` b, wattos1.`mrfile` f
where b.mrfile_id=f.mrfile_id AND
text_type='1-original';

-- Get phase 2 entries
DROP view IF EXISTS phase2;
CREATE VIEW phase2 AS
SELECT distinct pdb_id
FROM wattos1.`mrblock` b, wattos1.`mrfile` f
where b.mrfile_id=f.mrfile_id AND
text_type='2-parsed' AND
type = 'entry';

-- Get phase 3 entries
DROP view IF EXISTS phase3;
CREATE VIEW phase3 AS
SELECT distinct pdb_id
FROM wattos1.`mrblock` b, wattos1.`mrfile` f
where b.mrfile_id=f.mrfile_id AND
text_type='3-converted-DOCR' AND
type = 'entry';

-- Get phase 4 entries
DROP view IF EXISTS phase4;
CREATE VIEW phase4 AS
SELECT distinct pdb_id
FROM wattos1.`mrblock` b, wattos1.`mrfile` f
where b.mrfile_id=f.mrfile_id AND
text_type='4-filtered-FRED' AND
type = 'entry';

-- Amber phase 1 entries
DROP view IF EXISTS amber;
CREATE VIEW amber AS
SELECT distinct pdb_id
FROM wattos1.`mrblock` b, wattos1.`mrfile` f
where b.mrfile_id=f.mrfile_id AND
text_type='1-original' AND
program = 'AMBER';
