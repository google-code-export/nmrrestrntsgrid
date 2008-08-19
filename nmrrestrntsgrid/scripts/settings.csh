#!/bin/csh -f
# Author: Jurgen F. Doreleijers 
# Fri Apr  1 15:01:48 CST 2005 Initiated
# Thu Mar 13 09:21:34 CET 2008 Modified to work under sf.net project

# when testing new locations will be used 1 for true only 0 for false
#setenv testing  1

# TODO: remove these lines when debugging is done.
# some get inhereted by the production setup that is still the default.
unset nrg_project    
unset base_dir       
unset pdbbase_dir    
unset tmp_dir        
unset big_dir        
unset WS             
unset W              
unset nrg_dir        
unset CCPNMR_TOP_DIR 
unset ccpn_tmp_dir   
unset scripts_dir 
unset big_dir     
unset dir_star         
unset dir_link         
unset dir_compl        
unset dir_coplanar     
unset dir_viol         
unset dir_surplus      
unset dir_assign       
unset dir_wi_all       
unset dir_nomen        
unset dir_extra        
unset dir_export       
unset dir_db           
unset dir_restraint    
unset dir_restr_unzip  
unset dir_recoord_na   
unset dir_python   
unset perEntry_dir
unset results_dir

# next line requires gawk to be installed.
set measahost = (`hostname|gawk -F'[.]' '{print tolower($1)}'`)

# Host name based locals SECTION I (there is a section II below).
if ( $measahost == "stella" ) then
    echo "DEBUG in NRG settings.csh; Now on $HOST which is the development default."
endif

if ( $measahost == "tang" ) then
    echo "DEBUG in NRG settings.csh; Now on $HOST which will be the production setup."
    setenv UJ           /big/docr
	setenv WS           $UJ/workspace                     # Common to all projects currently.
else
    setenv WS           $UJ/workspace34
endif


if ( $measahost == "swoft" ) then
    echo "DEBUG in settings.csh; Now on swoft"
    setenv tmp_dir         ~jurgen/tmp
    setenv big_dir         ~jurgen/tmp/DOCR_big_tmp_
    setenv pdbbase_dir     ~/PDB_rem/ftp.ebi.ac.uk/pub/databases/rcsb/pdb-remediated
endif

# Development settings; other locals need to be setenv below. Can be overiden by next section
setenv nrg_project        nmrrestrntsgrid
setenv pdbbase_dir        $UJ/wattosTestingPlatform/pdb     # For PDB and mmCIF formatted entries data.
setenv mr_anno_progress_dir $UJ/wattosTestingPlatform/Wattos/mr_anno_progress # mrannotator
setenv tmp_dir            $UJ/tmp                           #
setenv big_dir            $UJ/NRG                           # NRG data large in size.
setenv W                  $WS/wattos                        # Wattos install
setenv nrg_dir            $WS/$nrg_project                  # For NRG project code.
setenv CCPNMR_TOP_DIR     $WS/ccpn 
setenv ccpn_tmp_dir       $UJ/ccpn_tmp                      # Temporary location for FC data.

# CING, and RECOORD
setenv C                  $WS/cing
setenv R                  $WS/recoord
setenv P                  $R/python/recoord2

setenv servletUrl  'http://localhost/NRG/MRGridServlet'

# Host name based locals SECTION II (see section I). These are modifications.
if ( $measahost == "tang" ) then
#    setenv CCPNMR_TOP_DIR     /big/wim/workspace/all 
#    setenv R                  /big/wim/workspace/recoord 
    setenv pdbbase_dir        /dumpzone/pdb/pdb
    setenv servletUrl  'http://tang.bmrb.wisc.edu/NRG/MRGridServlet' 
endif
if ( $measahost == "stella" ) then
    echo "DEBUG in NRG settings.csh; Now on $HOST which is the development default."
endif
                       
## Directory with this file
setenv scripts_dir      $nrg_dir/scripts
setenv wcf_dir          $scripts_dir/wcf 
setenv list_dir         $big_dir/lists
setenv results_dir      $big_dir/Results
setenv perEntry_dir     $results_dir/perEntry
setenv dir_nrg_python   $nrg_dir/python
#setenv DIR_WHATIF   /home/vriend/whatif
setenv PDBZ2        $pdbbase_dir/data/structures/divided/pdb
setenv CIFZ2        $pdbbase_dir/data/structures/divided/mmCIF

################################################################################
# More or less temp files.
setenv dir_star         $big_dir/star
setenv dir_link         $big_dir/link
setenv dir_compl        $big_dir/completeness
setenv dir_coplanar     $big_dir/coplanar
setenv dir_viol         $big_dir/viol
setenv dir_surplus      $big_dir/surplus
setenv dir_assign       $big_dir/assign
setenv dir_wi_all       $big_dir/wi/all
setenv dir_nomen        $big_dir/nomen
setenv dir_extra        $big_dir/extra
setenv dir_export       $big_dir/export
setenv dir_db           $big_dir/db
setenv dir_restraint    $big_dir/restraint
setenv dir_restr_unzip  $big_dir/restraint/unzipped
setenv dir_recoord_na   $big_dir/recoord_na

# perhaps do the below once.
#mkdir -p $dir_star $dir_link $dir_compl $dir_coplanar $dir_viol $dir_surplus $dir_assign $dir_wi_all $dir_nomen $dir_db $dir_restraint $dir_restr_unzip $dir_extra

setenv dir_pdb_status   $pdbbase_dir/data/status 
              
## No changes below this line. Except special case of Wim's 'all'.
##############################################################################
# Wattos.
setenv PYTHONPATH   $W/python

# recoord (needs to preceed ccpn because both have a msd package.)
setenv PYTHONPATH   ${PYTHONPATH}:$R/python;

# restrntsgrid
setenv PYTHONPATH   ${PYTHONPATH}:${dir_nrg_python}

# ccpn/recoord with api 
setenv PYTHONPATH   ${PYTHONPATH}:$CCPNMR_TOP_DIR/python

# CING
if ( -e $C/cing.csh ) then
    source $C/cing.csh
endif

# Wattos
alias wsetup        'setenv WATTOSROOT $W; source $W/scripts/wsetup'
# FormatConverter
alias fc            'python $CCPNMR_TOP_DIR/python/ccpnmr/format/gui/FormatConverter.py'
