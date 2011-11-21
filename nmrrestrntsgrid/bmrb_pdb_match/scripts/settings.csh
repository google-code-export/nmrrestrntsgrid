#!/bin/csh -f

# NOTE THAT THIS FILE IS NOT BEING USED ANYMORE!!

# Author: Jurgen F. Doreleijers @ Fri Apr  1 15:01:48 CST 2005

## Directory with this file
set base_dir        = $SJ/BMRB/Matches_BMRB_PDB
set scripts_dir     = $base_dir/scripts
set list_dir        = $base_dir/lists
set doc_dir         = $base_dir/documentation
set results_dir     = $base_dir/results

set viavia_url      = http://tang.bmrb.wisc.edu/servlet_data/viavia/
set mysql_url       = $viavia_url/mr_mysql_backup
set bmrb_pdb_url    = $viavia_url/bmrb_pdb_match

## Dir with the coordinate files.
set pdbbase_dir     = /dumpzone/pdb/pdb
set viavia_dir      = /var/www/servlet_data/viavia
# Dir with data in BMRB NMR Restraints Grid
set mr_backup_dir   = $viavia_dir/mr_mysql_backup
# Dir with public data from matching project.
set match_dir       = $viavia_dir/bmrb_pdb_match

set tmp_dir         = /tmp/matches_tmp_
set dir_star_files  = /website/ftp/pub/data/nmr-star

## File with the PDB entry codes for NMR entries
set pdb_mainFile = $list_dir/pdb_main.csv
## File with the PDB entry codes for NMR entries
set pdb_nmrFile = $list_dir/pdb_nmr.csv
## File with the PDB entry codes for NMR entries with MR files
set pdb_mrFile = $list_dir/pdb_mr.csv

# BMRB data
set bmrb_export_db_url  = "ftp://ftp.bmrb.wisc.edu/pub/data/export_db/"
#set bmrb_export_db_url  = "ftp://yola.bmrb.wisc.edu/pub/data/export_db/"
set bmrb_mainFile       = $list_dir/bmrb_main.csv
set bmrb_authorFile     = $list_dir/bmrb_author.csv
set bmrb_sequenceFile   = $list_dir/bmrb_sequence.csv
set bmrb_ligandFile     = $list_dir/bmrb_ligand.csv
set ets_pdbFile         = $list_dir/ets_pdb.csv
set ets_rcsbFile        = $list_dir/ets_rcsb.csv

# PDB data
set pdb_authorFile     = $list_dir/pdb_author.csv
set pdb_ligandFile     = $list_dir/pdb_ligand.csv
set pdb_modelFile      = $list_dir/pdb_model.csv


## List of target matches between BMRB and PDB entries
# Last number in the file means the overall score it should get.
# use 0 for higher priority in match.
#set overrideFile        = $doc_dir/override_manual.csv

# DO NOT CHANGE; they are defined to be in dir: ../result from $list_dir
# and have hard-coded names.
set scoreFile           = $results_dir/score.csv
set score_one2oneFile   = $results_dir/score_one2one.csv

# Blast bin results dir
set blastFile = $list_dir/blast.csv

## No changes below this line
##############################################################################
# Let's echo a couple of list counts.

set pdb_nmr_list    = (`cat $pdb_nmrFile        |gawk '{if (NR!=1) print}'`)
set pdb_mr_list     = (`cat $pdb_mrFile         |gawk '{if (NR!=1) print}'`)
set bmrb_main_list  = (`cat $bmrb_mainFile      |gawk '{if (NR!=1) print}'`)


