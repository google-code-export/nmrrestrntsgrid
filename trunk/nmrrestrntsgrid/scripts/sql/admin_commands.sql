SELECT distinct ( F.PDB_ID )
FROM mrblock AS B, mrfile AS F
WHERE B.mrfile_ID=F.mrfile_ID

DROP TABLE IF EXISTS duplicates;
CREATE TABLE tmp_table (   pdb_id CHAR(4));
select count(e.pdb_id) from entry e
where e.pdb_id IN ('1a24','1a4d','1aa3','1ac0','1afp','1ai0','1azj','1bbx','1bku','1brv','1bus','1c98','1cjg','1du9','1e41','1ew1','1fd6','1fjk','1ho0','1hu6','1hue','1hx4','1hx7','1ieh','1iv6','1iw4','1j5n','1j8z','1je4','1jmn','1jo1','1jor','1juu','1jwc','1k3g','1kb1','1kc4','1kr8','1kvi','1kyj','1l1p','1ld6','1ls4','1lux','1mke','1n0a','1nin','1nmr','1nwv','1nyb','1osw','1p7a','1pdt','1pik','1puq','1q0v','1r9u','1rkk','1rq6','1s4j','1sb6','1snl','1suy','1sym','1szy','1t1q','1t50','1t8j','1t9e','1tit','1tte','1u6v','1uwd','1vek','1x30','1xgc','1y4o','1y58','1y74','1yg3','1yhd','1yng','1zza','1zzf','2ai5','2aiy','2beg','2bgo','2bth','2btx','2c6b','2cqb','2d2p','2euy','2evz','2eze','2f3a','2fey','2fr9','2heq','2hgh','2hj8','2jm8','2jmg','2joe','2jpe','2jsk','2jsm','2jue','2k0e','2k1c','3ci2','3gb1','3gcc','3hsf','4ull');
-- Really weird why one can not use aliases for the table name here
-- The following didn't work with an alias e for entry:
DELETE FROM entry
WHERE pdb_id IN ('1a24','1a4d','1aa3','1ac0','1afp','1ai0' )
LIMIT 2;


-- Look for the todo list.
DROP TABLE IF EXISTS tmp_table;
CREATE TABLE tmp_table (   pdb_id CHAR(4));
--DELETE 
--FROM tmp_table;

-- entries done
insert into tmp_table ( pdb_id ) 
SELECT DISTINCT F.PDB_ID
FROM mrblock AS B, mrfile AS F
WHERE B.mrfile_ID=F.mrfile_ID AND TYPE='entry' AND PROGRAM='STAR' AND text_type LIKE '3-%';

SELECT DISTINCT PDB_ID 
into outfile '/tmp/entries_all_2008-08-21_todo.csv' 
FROM mrfile AS F
WHERE DETAIL LIKE '1-%' AND
PDB_ID NOT IN ( 
	SELECT PDB_ID
	FROM tmp_table
) ORDER BY PDB_ID;

