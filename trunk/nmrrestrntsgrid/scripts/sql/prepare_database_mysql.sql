-- STEP BY STEP PROCEDURE FOR SETTING UP NEW DB

-- login with root password
--mysql -u root -p'\!Ecj%Y&R' mysql
-- The db isn't available anywhere but on the host itself so this posses no security problem.

-- Notes:
    --  # no escapes for any char but the first.
    -- no backslash escape '\' needed when using double quotes in windows.

drop database wattos1;

-- create it
create database wattos1;

use mysql;

-- creating the account 
CREATE USER 'wattos1'@'localhost'           ;
SET PASSWORD FOR 'wattos1'@'localhost'               = PASSWORD('4I4KMS');
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('');
update user set file_priv='Y' where user='wattos1';
update user set file_priv='Y' where user='root';

-- not sure where the next line belongs:
use wattos1;
GRANT ALL ON * TO 'wattos1'@'localhost';
GRANT ALL ON * TO 'root'@'localhost';

GRANT REPLICATION SLAVE ON *.* TO 'repl'@'localhost.localdomain' IDENTIFIED BY 'slavepass';

-- create the tables within
mysql -u wattos1 -p4I4KMS  wattos1 < $WS/wattos/scripts/sql/db_create.sql

-- OR load very fast! Dump from 1 database to the next.
mysqldump --opt -u root -p'\!Ecj%Y&R' wattos1 > $SJ/filetosaveto.sql
-- add if speed is needed to begining of file: SET FOREIGN_KEY_CHECKS=0;
-- takes only 4 seconds without optimalization though.
mysql -u wattos1 -p4I4KMS wattos1 < $SJ/filetosaveto.sql
and then copy the mrgrid data itself too
cd /big/jurgen/DB/mrgrid/bfiles
cp -rvfup wattos1/* wattos1
/* just a comment to end the previous command interpreted by jedit as a comment **/

-- More config
set global query_cache_size=16000000;
SHOW STATUS LIKE 'Qcache%';
SHOW VARIABLES LIKE 'have_query_cache';
SHOW VARIABLES LIKE 'query_cache%';