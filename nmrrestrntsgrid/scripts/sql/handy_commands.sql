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

alter table entry add column in_recoord BOOLEAN default 0;
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
