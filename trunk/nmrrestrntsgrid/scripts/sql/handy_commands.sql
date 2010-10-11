SHOW VARIABLES LIKE '%query_cache%';
SHOW STATUS LIKE '%qcache%';
SHOW DATABASES;
USE JFDPLAY;
SHOW TABLES;
DESCRIBE bmrb_main;

-- don't remove the ibdata file in the data dir because for innodb it contains
-- the actual data itself too.
SHOW WARNINGS;

mysql -uroot mysql < /path/to/fill_help_tables.sql
mysql -h localhost -u wattos1 -p4I4KMS wattos1
-- or within
source /path/to/fill_help_tables.sql

-- usefull for dumping database in sql commands creating the tables
-- and text files for the actual data.
mysqldump --tab=c:\jurgen\mysqldump --opt jfdplay
-- then use repetively:
LOAD DATA INFILE 'file_name.txt'
INTO TABLE tbl_name

-- show optimizers results
explain select ...

alter table entry add column res_count INTEGER default NULL;
alter table entry add column in_dress   BOOLEAN default 0;
alter table mrblock add column item_count INTEGER default NULL;

-- login as root on mysql:
-- type the following on the terminal using mysql to generate pass.
# done: /usr/bin/mysqladmin -u root password '\!Ecj ...ETC
mysql -u root -p'\!...

--You can test the MySQL daemon with the benchmarks in the 'sql-bench' directory:
cd /usr/share/sql-bench ; run-all-tests
--but needs DBD module for perl installed first; not done.

-- Operate the server instance
/etc/init.d/mysql restart
-- will read the installed /etc/my.cnf

query_cache_type 0; off, 1; all, 2; only when specified.
C:\Program Files\MySQL\MySQL Server 4.1

-- Windows:
mysql -uroot -p"aevj%" mysql -- Etc. just note how double quotes like to be used under Windows,
-- no escaping special characters needed.


-- Find viable entries for RECOORD. Just one criteria.
select e.pdb_id from entry e
where e.pdb_id IN (
   select f.pdb_id from `mrblock` m, mrfile f
   where m.mrfile_id = f.mrfile_id AND
   m.text_type = '2-parsed'  AND (
   m.type = 'distance' OR
   m.type = 'dihedral angle' OR
   m.type = 'dipolar'
   )
)

-- Find doubly counted entries.
create table virtual_table AS
select b.text_type, f.pdb_id, b.item_count from `mrblock` b, mrfile f
where f.mrfile_id=b.mrfile_id AND
( b.text_type like "3%" OR b.text_type like "4%" ) AND
b.subtype = "full" AND b.program="STAR"

select *, (v2.item_count - v1.item_count) AS d from `virtual_table` v1, `virtual_table` v2
where v1.pdb_id=v2.pdb_id AND
v1.text_type LIKE "3%" AND
v2.text_type LIKE "4%" AND
v1.item_count < v2.item_count
order by v1.pdb_id ASC

-- find entries in db but not having "2-parsed  STAR    entry   full" Used to be 1 on 7/21/06
-- These might very well be obsoleted entries like 1nj7 or amber entry that failed to be done right.
select e.pdb_id from entry e
where e.pdb_id NOT IN (
   select f.pdb_id from `mrblock` m, mrfile f
   where m.mrfile_id = f.mrfile_id AND
   m.text_type LIKE '4%'  AND
   m.program = 'STAR' AND
   m.type = 'entry' AND
   m.subtype = 'full' AND
   m.format = 'n/a'
)

delete from entry e
where e.pdb_id = '1a42';



-- get entries that aren't in FRED yet at a certain cutoff
select distinct pdb_id from mrfile
where detail like '1%' AND
pdb_id not in (
    select distinct f.pdb_id from mrfile f
    where f.detail like '4%'
) AND
pdb_id != '9'
order by pdb_id


INSERT INTO entry ( entry_id, pdb_id ) VALUES ( 2, '1brv' );

INSERT INTO entry (entry_id, pdb_id) VALUES ( 1009, '1brv');


INSERT INTO mrfile (
mrfile_id,
entry_id,
detail,
pdb_id,
date_modified
) VALUES (
1,
1,
'detail',
'1brv',
{TIMESTAMP '2004-06-15 04:43:26'}
);

INSERT INTO mrblock (
mrblock_id,
mrfile_id,
position,
program,
type,
subtype,
format,
text_type,
line_count,
date_modified,
other_prop,
dbfs_id,
file_extension,
md5_sum
) VALUES (
1,
1,
4,
'program',
'type',
'subtype',
'format',
'text_type',
9,
SYSDATE,
'no other prop',
3,
'tgz',
'060a8849c50c0440917a8713902a29bb'
)


DELETE FROM mrblock
WHERE dbfs_id IN ( 5, 3 );





-- With parsable restraints
SELECT count(*) FROM `mrblock`
where item_count >=1 AND
text_type='2-parsed' AND
type = 'entry' AND
subtype = 'full';

-- With distance restraints
SELECT count(distinct pdb_id)
FROM `mrblock` b, `mrfile` f
where b.mrfile_id=f.mrfile_id AND
text_type='2-parsed' AND
type = 'distance' AND
item_count >= 1; ()


-- unreleased MR files
select count(*) from unreleasedMREntriesPDB;


INSERT INTO entry ( entry_id, pdb_id ) VALUES ( 2, '1brv' );

INSERT INTO entry (entry_id, pdb_id) VALUES ( 1009, '1brv');


INSERT INTO mrfile (
mrfile_id,
entry_id,
detail,
pdb_id,
date_modified
) VALUES (
1,
1,
'detail',
'1brv',
{TIMESTAMP '2004-06-15 04:43:26'}
);

INSERT INTO mrblock (
mrblock_id,
mrfile_id,
position,
program,
type,
subtype,
format,
text_type,
line_count,
date_modified,
other_prop,
dbfs_id,
file_extension,
md5_sum
) VALUES (
1,
1,
4,
'program',
'type',
'subtype',
'format',
'text_type',
9,
SYSDATE,
'no other prop',
3,
'tgz',
'060a8849c50c0440917a8713902a29bb'
)


DELETE FROM mrblock
WHERE dbfs_id IN ( 5, 3 );




-- Random
SELECT count(DISTINCT f.pdb_id), b.text_type, b.type
FROM wattos1.mrblock AS b, wattos1.mrfile AS f
WHERE b.mrfile_id=f.mrfile_id and (
    b.type='dipolar coupling' OR
    b.type='distance' OR
    b.type='dihedral angle'
)
group by b.text_type, b.type
order by b.text_type, b.type;

-- Get the programs involved.
SELECT count(DISTINCT f.pdb_id), b.program
FROM wattos1.mrblock AS b, wattos1.mrfile AS f
WHERE b.mrfile_id=f.mrfile_id AND
      b.text_type = '1-original' AND
      b.program != 'MR format' AND
      b.program != 'n/a' AND
      b.program != 'unknown'
group by b.program
order by count(DISTINCT f.pdb_id) desc, b.program;


-- Get the
DROP VIEW IF EXISTS stereoGroupPercentage;
CREATE VIEW stereoGroupPercentage AS
SELECT r.pdb_id,s.Triplet_count/r.rescount as percTriplet
FROM residueCount r, _Stereo_assign_list s
where r.pdb_id=s.pdb_id
order by percTriplet asc;

-- Get the unreleased Rutgers PDB entries with MR files
DROP VIEW IF EXISTS unreleasedMREntriesPDB;

CREATE VIEW unreleasedMREntriesPDB AS
SELECT p.pdb_id
FROM rcsb_id_with_mr m, rcsb_pdb_id p
where m.rcsb_id=p.rcsb_id and
p.pdb_id not in ( select pdb_id from DOCRFREDEntries);

-- JUNK follows.
-- SELECT * FROM `mrblock` where file_name LIKE '1brv%';


-- Get the number of residues per entry
DROP VIEW IF EXISTS residueCount;
CREATE VIEW residueCount AS
SELECT m.pdb_id,sum(m.rescount) AS rescount
FROM moltypes m
group by m.pdb_id
order by rescount;

    program                        VARCHAR(255)     NOT NULL,
    type                           VARCHAR(255)     NOT NULL,
    subtype                        VARCHAR(255)     NOT NULL,
    format                         VARCHAR(255)     NOT NULL,

-- Get counts of pdb entries per program
SELECT count(*), b.program, b.type, b.subtype, b.format
FROM wattos1.mrblock AS b
WHERE (
    b.type!='dipolar coupling'
)   AND
b.text_type = '1-original'
group by b.program, b.type, b.subtype, b.format
order by count(*) desc;


select * from mrblock where program = 'Wattos' and format = 'dihedral angle';