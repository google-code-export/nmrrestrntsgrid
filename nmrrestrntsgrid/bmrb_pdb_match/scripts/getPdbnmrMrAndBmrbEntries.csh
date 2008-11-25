#!/bin/tcsh -f

# Load common settings
source $SJ/BMRB/Matches_BMRB_PDB/scripts/settings.csh

set ocaUrl          = "http://oca.ebi.ac.uk/oca-bin/ocaids"
set ocaUrlNmr       = $ocaUrl"?dat=dep&ex=nmr&m=du"
set ocaUrlAll       = $ocaUrl"?dat=dep&ex=any&m=du"
set gridUrl         = "http://www.bmrb.wisc.edu/servlet_data/viavia/mr_mysql_backup/entry.txt"

# The PDB all update retrieve from OCA takes 4 sekonds on their end for Query
# and overall it takes 67 seconds. The other updates are much faster. Total 
# time take was 81 seconds once.
set do_pdbnmr_update    = 1
set do_pdball_update    = 1
set do_pdbmr_update     = 1
set do_bmrb_update      = 1

# How long may I take
set max_cpu_time = 600
######### NO CHANGES BELOW THIS LINE #############

limit cputime $max_cpu_time
cd $list_dir

if ( $do_pdbnmr_update ) then
    set tmpFile = $pdb_nmrFile:r".html"
    wget -q -O $tmpFile "$ocaUrlNmr" 
    if ( $status ) then
        echo "ERROR: couldn't download from url: $ocaUrlNmr"
        exit 1
    endif
    
    echo "pdb_id" > $pdb_nmrFile
    # The sort -u isn't needed I believe.
    cat $tmpFile | \
        gawk '/^[0-9]/{print tolower($1)}' | \
        sort -u >>\
        $pdb_nmrFile       
    
    if ( $status ) then
        echo "ERROR: couldn't convert data"
        exit 1
    endif
    
    if ( -z  $pdb_nmrFile ) then  
        echo "ERROR: created an empty result file."
        exit 1
    endif
    
    set list = ( `cat $pdb_nmrFile` )
    echo "Got number of PDB NMR entries from OCA: $#list"
    if ( $#list < 3000 | $#list > 9999 ) then  
        echo "ERROR: Number of NMR PDB entries has to be in range: [3000,9999]."
        exit 1
    endif
    \rm $tmpFile
endif
 

if ( $do_pdball_update ) then
    set tmpFile = $pdb_mainFile:r".html"
    wget -q -O $tmpFile "$ocaUrlAll" 
    if ( $status ) then
        echo "ERROR: couldn't download from url: $ocaUrlAll"
        exit 1
    endif
    
    echo "pdb_id" > $pdb_mainFile
    # The sort -u isn't needed I believe.
    cat $tmpFile | \
        gawk '/^[0-9]/{print tolower($1)}' | \
        sort -u >>\
        $pdb_mainFile       
    
    if ( $status ) then
        echo "ERROR: couldn't convert data"
        exit 1
    endif
    
    if ( -z  $pdb_mainFile ) then  
        echo "ERROR: created an empty result file."
        exit 1
    endif
    
    set list = ( `cat $pdb_mainFile` )
    echo "Got number of all PDB entries from OCA: $#list"
    if ( $#list < 30000 | $#list > 99990 ) then  
        echo "ERROR: Number of all PDB entries has to be in range: [30000,99999]."
        exit 1
    endif
    \rm $tmpFile
endif


if ( $do_pdbmr_update ) then
    set tmpFile = $pdb_mrFile:r".html"
    wget -q -O $tmpFile "$gridUrl"
    if ( $status ) then
        echo "ERROR: couldn't download from url: $gridUrl"
        exit 1
    endif
    
    echo "pdb_id" > $pdb_mrFile
    # The sort -u isn't needed I believe.
    cat $tmpFile | \
        gawk '{print $3}' | \
        sort -u >>\
        $pdb_mrFile       
    
    if ( $status ) then
        echo "ERROR: couldn't convert data"
        exit 1
    endif
    
    if ( -z  $pdb_mrFile ) then  
        echo "ERROR: created an empty result file."
        exit 1
    endif
    
    set list = ( `cat $pdb_mrFile` )
    echo "Got number of PDB MR entries from NMR Restraints Grid: $#list"
    if ( $#list < 2000 | $#list > 9999 ) then  
        echo "ERROR: Number of PDB entries with MR files has to be in range: [3000,9999]."
        exit 1
    endif
    \rm $tmpFile
endif


if ( $do_bmrb_update ) then
    set file = "depsindb.ascii.gz"
    wget -q "$bmrb_export_db_url/$file" 
    if ( ! -e $file ) then
        echo "ERROR: couldn't get file: $file"
        echo "ERROR: from url dir: $bmrb_export_db_url"
        exit 1
    endif
    
    gunzip -f $file
    set file = $file:r
    
    echo "bmrb_id" > $bmrb_mainFile
    cat $file | \
        gawk -F'|' '{print $1}' | \
        sed -e 's/   *//g' | \
        sed -e 's/^data_//' | \
        sort -n >> \
        $bmrb_mainFile

    set list = ( `cat $bmrb_mainFile` )
    echo "Got number of BMRB entries from BMRB export database: $#list"
    if ( $#list < 3000 | $#list > 9999 ) then  
        echo "ERROR: Number of BMRB entries has to be in range: [3000,9999]."
        exit 1
    endif
    
endif        
    

