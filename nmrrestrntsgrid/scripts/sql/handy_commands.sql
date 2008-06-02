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
mysql -h localhost -u wattos2 -p4I4KMU wattos2
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
