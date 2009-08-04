-- live results from filesystem.
DROP TABLE IF EXISTS _Distance_constraint_stats_list;
CREATE table _Distance_constraint_stats_list
(
    pdb_id                        CHAR(4),
    Sf_category                   VARCHAR(255),
--    Entry_ID                      INT,
--    ID                            INT,
    Constraint_list_ID            INT,
    Constraint_count              INT,
    Viol_count                    INT,
    Viol_total                    FLOAT,
    Viol_max                      FLOAT,
    Viol_rms                      FLOAT,
    Viol_average_all_restraints   FLOAT,
    Viol_average_violations_only  FLOAT,
    Cutoff_violation_report       FLOAT,
    dummy                         VARCHAR(255)
);
LOAD DATA LOCAL INFILE
    '/Users/jd/NRG/Results/weekly20090312/_Distance_constraint_stats_list_mySqlNulls.csv'
    INTO TABLE _Distance_constraint_stats_list
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES  TERMINATED BY '\n';


-- 786 Entries that failed 4 requirements for Gottingen poster.
--DROP TABLE IF EXISTS docrFredBaddies786;
--CREATE TABLE docrFredBaddies786 ( pdb_id CHAR(4) NOT NULL PRIMARY KEY);
--LOAD DATA LOCAL INFILE
--  '/Volumes/BMRB\;TANG/docr/CloneWars/DOCR1000/lists/setDocrFredBaddies786.csv'
--  INTO TABLE docrFredBaddies786
--  FIELDS TERMINATED BY ','
--  OPTIONALLY ENCLOSED BY '\"'
--  LINES  TERMINATED BY '\n';
--
---- Entries that have already been checked manually.
--DROP TABLE IF EXISTS docrFredBaddiesNotFixed;
--CREATE TABLE docrFredBaddiesNotFixed ( pdb_id CHAR(4) NOT NULL PRIMARY KEY);
--LOAD DATA LOCAL INFILE
--  '/Volumes/BMRB\;TANG/docr/CloneWars/DOCR1000/lists/setDocrFredBaddiesNotFixed.csv'
--  INTO TABLE docrFredBaddiesNotFixed
--  FIELDS TERMINATED BY ','
--  OPTIONALLY ENCLOSED BY '\"'
--  LINES  TERMINATED BY '\n';

DROP TABLE IF EXISTS _Distance_constraint_surplus;

CREATE table _Distance_constraint_surplus
(   pdb_id                        CHAR(4) NOT NULL PRIMARY KEY,
    Sf_category                   VARCHAR(255),
    Redundancy_threshold_pct        FLOAT,
    Update_original_constraints     VARCHAR(20),
    Only_filter_fixed               VARCHAR(20),
    Averaging_method                VARCHAR(20),
    Number_of_monomers_sum_average  INT,
    Constraint_count                INT,
    Constraint_surplus_count        INT,
    Constraint_nonsurplus_count     INT,
    Constraint_exceptional_count    INT,
    Constraint_double_count         INT,
    Constraint_impossible_count     INT,
    Constraint_fixed_count          INT,
    Constraint_redundant_count      INT,
    dummy1                          CHAR(1),
    dummy2                          CHAR(1),
    dummy3                          CHAR(1),
    dummy4                          CHAR(1)
    );

LOAD DATA LOCAL INFILE
    '/Users/jd/NRG/Results/weekly20090312/_Distance_constraint_surplus_mySqlNulls.csv'
    INTO TABLE _Distance_constraint_surplus
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES  TERMINATED BY '\n';

DROP TABLE IF EXISTS _Stereo_assign_list;
--18 COLUMNS
CREATE table _Stereo_assign_list
(
pdb_id                      CHAR(4),
Sf_category                 VARCHAR(255),
Triplet_count               INT,
Swap_count                  INT,
Swap_percentage             FLOAT,
Deassign_count              INT,
Deassign_percentage         FLOAT,
Model_count                 INT,
Total_e_low_states          FLOAT,
Total_e_high_states         FLOAT,
Crit_abs_e_diff             FLOAT,
Crit_rel_e_diff             FLOAT,
Crit_mdls_favor_pct         FLOAT,
Crit_sing_mdl_viol          FLOAT,
Crit_multi_mdl_viol         FLOAT,
Crit_multi_mdl_pct          FLOAT,
dum1          VARCHAR(255),
dum2          VARCHAR(255),
dum3          VARCHAR(255),
dum4          VARCHAR(255),
dum5          VARCHAR(255),
dum6          VARCHAR(255),
dum7          VARCHAR(255),
dum8          VARCHAR(255),
dum9          VARCHAR(255),
dum10         VARCHAR(255),
dum11         VARCHAR(255)
);

LOAD DATA LOCAL INFILE
    '/Users/jd/NRG/Results/weekly20090312/_Stereo_assign_list_mySqlNulls.csv'
    INTO TABLE _Stereo_assign_list
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES  TERMINATED BY '\n';




---- Remember it's generated by Wattos.Utils.getMolTypes.py
DROP TABLE IF EXISTS moltypes;
CREATE table moltypes
(   pdb_id                        CHAR(4) NOT NULL,
    type                          VARCHAR(255) NOT NULL,
    typescount                    INT NOT NULL,
    rescount                    INT NOT NULL
    );
LOAD DATA LOCAL INFILE
    '/Users/jd/moltypes.csv'
    INTO TABLE moltypes
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES  TERMINATED BY '\n';


DROP TABLE IF EXISTS _NOE_completeness_stats;
-- compl should be 12th.
CREATE table _NOE_completeness_stats
(
    pdb_id                        CHAR(4) NOT NULL PRIMARY KEY,
    dummy_2                       VARCHAR(255),
    dummy_3                       VARCHAR(255),
    dummy_4                       VARCHAR(255),
    dummy_5                       VARCHAR(255),
    dummy_6                       VARCHAR(255),
    dummy_7                       VARCHAR(255),
    dummy_8                       VARCHAR(255),
    dummy_9                       VARCHAR(255),
    dummy_10                       VARCHAR(255),
    dummy_11                      VARCHAR(255),
    compl                         FLOAT,
    dummy_13                      VARCHAR(255),
    dummy_14                      VARCHAR(255),
    dummy_15                      VARCHAR(255),
    dummy_16                      VARCHAR(255),
    dummy_17                      VARCHAR(255),
    dummy_18                      VARCHAR(255),
    dummy_19                      VARCHAR(255),
    dummy_20                      VARCHAR(255),
    dummy_21                      VARCHAR(255),
    dummy_22                      VARCHAR(255),
    dummy_23                      VARCHAR(255),
    dummy_24                      VARCHAR(255),
    dummy_25                      VARCHAR(255),
    dummy_26                      VARCHAR(255),
    dummy_27                      VARCHAR(255)
);

LOAD DATA LOCAL INFILE
    '/Users/jd/NRG/Results/weekly20090312/_NOE_completeness_stats_mySqlNulls.csv'
    INTO TABLE _NOE_completeness_stats
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES  TERMINATED BY '\n';


--DROP TABLE IF EXISTS rcsb_id_with_mr;
--CREATE table rcsb_id_with_mr
--(   rcsb_id                       CHAR(10) NOT NULL PRIMARY KEY
--);
--
--LOAD DATA LOCAL INFILE
--  '/Users/jd/NRG/Results/weekly20090312/rcsb_id_with_mr.csv'
--  INTO TABLE rcsb_id_with_mr
--  FIELDS TERMINATED BY ','
--  OPTIONALLY ENCLOSED BY '\"'
--  LINES  TERMINATED BY '\n';
--
--DROP TABLE IF EXISTS rcsb_pdb_id;
--CREATE table rcsb_pdb_id
--(   rcsb_id                       CHAR(10) NOT NULL PRIMARY KEY,
--    pdb_id                        CHAR(4) NOT NULL
--);
--
--LOAD DATA LOCAL INFILE
--  '/Users/jd/NRG/Results/weekly20090312/rcsb_pdb_id.csv'
--  INTO TABLE rcsb_pdb_id
--  FIELDS TERMINATED BY ','
--  OPTIONALLY ENCLOSED BY '\"'
--  LINES  TERMINATED BY '\n';
--
