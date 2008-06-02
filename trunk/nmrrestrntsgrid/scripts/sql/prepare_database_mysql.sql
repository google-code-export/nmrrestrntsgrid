-- STEP BY STEP PROCEDURE FOR SETTING UP NEW DB

-- set root password
--mysql -u root password '\!Ecj'ETC   # no escapes for any char but the first.

-- Notes:
    -- no backslash escape '\' needed when using double quotes in windows.

-- create it
create database wattos3;

-- creating the account 
# Not needed anymore?
CREATE USER 'wattos3'@'localhost'               ;
CREATE USER 'wattos3'@'localhost.localdomain'   ;
CREATE USER 'wattos3'@'tang.bmrb.wisc.edu'      ;
CREATE USER 'wattos3'@'whelk.bmrb.wisc.edu'     ;
CREATE USER 'wattos3'@'anthozoan.bmrb.wisc.edu' ;
CREATE USER 'wattos3'@'zebrafish.bmrb.wisc.edu' ;
CREATE USER 'repl'@'whelk.bmrb.wisc.edu'        ;


SET PASSWORD FOR 'wattos3'@'localhost'               = PASSWORD('4I4KMS');
SET PASSWORD FOR 'wattos3'@'localhost.localdomain'   = PASSWORD('4I4KMS');
SET PASSWORD FOR 'wattos3'@'tang.bmrb.wisc.edu'      = PASSWORD('4I4KMS');
SET PASSWORD FOR 'wattos3'@'whelk.bmrb.wisc.edu'     = PASSWORD('4I4KMS');
SET PASSWORD FOR 'wattos3'@'anthozoan.bmrb.wisc.edu' = PASSWORD('4I4KMS');
SET PASSWORD FOR 'wattos3'@'zebrafish.bmrb.wisc.edu' = PASSWORD('4I4KMU');
SET PASSWORD FOR 'repl'@'whelk.bmrb.wisc.edu'        = PASSWORD('slavepass');
                                                    
GRANT ALL ON wattos3.* TO 'wattos3'@'localhost';
GRANT ALL ON wattos3.* TO 'wattos3'@'tang.bmrb.wisc.edu';
GRANT ALL ON wattos3.* TO 'wattos3'@'halfbeak.bmrb.wisc.edu';
GRANT ALL ON wattos3.* TO 'wattos3'@'whelk.bmrb.wisc.edu';
GRANT ALL ON wattos3.* TO 'wattos3'@'anthozoan.bmrb.wisc.edu';
GRANT ALL ON wattos3.* TO 'wattos3'@'zebrafish.bmrb.wisc.edu';
GRANT ALL ON wattos3.* TO 'wattos3'@'localhost.localdomain';             

use user;
update user set file_priv='Y' where user='wattos3';

GRANT REPLICATION SLAVE ON *.* TO 'repl'@'whelk.bmrb.wisc.edu'   IDENTIFIED BY 'slavepass';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'localhost.localdomain' IDENTIFIED BY 'slavepass';



-- create the tables within
-- type the following on the terminal
--
mysql -h tang.bmrb.wisc.edu -u wattos3 -p4I4KMS  wattos3 < "C:\Documents and Settings\jurgen.WHELK.000\workspace\Wattos\scripts\SQL\db_create.sql"
mysql -h localhost          -u wattos3 -p4I4KMS  wattos3 < "C:\Documents and Settings\jurgen.WHELK.000\workspace\Wattos\scripts\SQL\db_create.sql"
mysql -h localhost          -u wattos3 -p4I4KMS  wattos3 < /share/jurgen/db_create.sql
mysql -h localhost          -u wattos3 -p4I4KMS  wattos3 < /Users/jd/workspace/Wattos/scripts/sql/db_create.sql

-- OR load very fast! Dump from 1 database to the next.
mysqldump --opt -u root -p'\!Ecj%Y&R' wattos3 > $SJ/filetosaveto.sql
-- add if speed is needed to begining of file: SET FOREIGN_KEY_CHECKS=0;
-- takes only 4 seconds without optimalization though.
mysql -u wattos3 -p4I4KMS wattos3 < $SJ/filetosaveto.sql
and then copy the mrgrid data itself too
cd /big/jurgen/DB/mrgrid/bfiles
cp -rvfup wattos3/* wattos3
/* just a comment to end the previous command interpreted by jedit as a comment **/

-- More config
set global query_cache_size=16000000;
SHOW STATUS LIKE 'Qcache%';
SHOW VARIABLES LIKE 'have_query_cache';
SHOW VARIABLES LIKE 'query_cache%';




-- JUNK BELOW

# Setttings within Eclips db browser.
C:\Documents and Settings\jurgen.WHELK.000\workspace\Wattos\lib\mysql-connector-java-5.0.3-bin.jar
jdbc:mysql://localhost:3306/wattos3
com.mysql.jdbc.Driver