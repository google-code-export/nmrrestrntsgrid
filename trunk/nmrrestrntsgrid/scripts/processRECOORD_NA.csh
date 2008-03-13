#!/bin/csh 
# Author: Jurgen F. Doreleijers 
# Wed Dec 14 13:49:06 CST 2005
#
# TASK: Do all processing needed for RECOORD
# USE:  processRECOORD_NA.csh [1b4y]
#OR: set x = 2hgh  ; $scripts_dir/processRECOORD_NA.csh $x |& tee $UJ/CloneWars/RECOORD_NA/perEntry/$x.log 
# Dependencies:
#       python, xplor (in path for xplor-nih), Wattos, aqua, etc. 

#exit 1
set subl = ( 1b4y )

#set subl = ( $sublF )
# Get argument pdb code if it exists.
if ( $1 != "" ) then
    set subl = (  $1  )
endif

set doSetupPSF          = 1
                          
set extraWattosOptions  = 
set extraFCOptions      = ( -raise )

# E.g. to make it run without an X-server
set hasHead = 0
if ( $hasHead ) then
    # Check head.
    if ( ! $?DISPLAY ) then
        echo "ERROR: Empty head"
        exit 1
    endif
else
    set extraWattosOptions = ( $extraWattosOptions -Djava.awt.headless=true )
    set extraFCOptions     = ( $extraFCOptions -noGui  )
    # -force option doesn't work with mergeStarFilesTest
endif     
# No need to change things below this line
###############################################################################

# redefine wattos alias
wsetup
setenv woptions  "$extraWattosOptions -Xmx$WATTOSMEM"
alias wattos "java $woptions Wattos.CloneWars.UserInterface -at"
alias wjava  "java $woptions"

echo "doSetupPSF        Create a XXXX.psf for xplor-nih                          -> XXXX.psf $doSetupPSF"               
echo "Is there an X-server attached for possible questions:                                  $hasHead"
echo "Extra arguments FC                                                                     $extraFCOptions"
echo "PYTHONPATH:       $PYTHONPATH"                
echo "CLASSPATH:        $CLASSPATH"                
which wattos

echo "Doing" $#subl "pdb entries"
foreach x ( $subl )
    echo "Doing $x"
    if ( $doSetupPSF ) then
        echo "  setup PSF"
        set log_file         = $x"_psf".log

        cd $dir_recoord_na
        if ( ! -e $x ) then
            mkdir $x
        endif
        cd $x
        # Convert FRED STAR file to PDB.
        ln -sf $dir_link/$x/nonredun.str 1xxx.str
        
        set script_file     = $scripts_dir/WriteEntryXplor.wcf
        set inputStarFile   = 1xxx.str
        set log_file        = $x"_setupPsf".log
                                   
        if ( ! -e $inputStarFile ) then
            echo "ERROR: $x No input star file: $inputStarFile"
            continue
        endif

        echo "      creating xplor input"
        wattos < $script_file >& $log_file
        if ( $status ) then
            echo "ERROR $x Wattos $script_file failed"
            continue
        else
            grep --quiet ERROR $log_file
            if ( ! $status ) then
                echo "ERROR $x found erros in log file"
            endif
        endif
        
        
        
        # TODO: write an xplor statement for selecting na residues that db setup needs
        echo "      creating xplor psf"
        pyXplor $dir_xplor/python/wattos2xplor.py 1xxx >>& $log_file
        if ( $status ) then
            echo "ERROR 1xxx in pdb2psf"
            continue
        endif
        grep ERR $log_file | head
        # if ( ! $status ) then
            # echo "ERROR 1xxx found in log file"
            # continue
        # endif
        if ( ! -e 1xxx.psf) then
            echo "ERROR 1xxx no psf file created"
            continue
        endif               
        if ( ! -e 1xxx_extended.pdb) then
            echo "ERROR 1xxx no 1xxx_extended.pdb created"
            continue
        endif               

    endif
    
    if ( $doSetupSystemRECOORD ) then
        # Make sure all expected files are present even if that means empty.
        touch 1xxx_xplor_dc.tbl        
        (cat 1xxx_xplor_dc_*.tbl > 1xxx_xplor_dc.tbl) >& /dev/null
        
        touch 1xxx_xplor_dihedral.tbl
        (cat 1xxx_xplor_di_*.tbl > 1xxx_xplor_dihedral.tbl) >& /dev/null
        
        touch 1xxx_plane.inp
        echo "vector identify (store9) (resid 1:26 or resid 28:33)">1xxx_xplor_na_selection.inp
        # Note that the RDCs will be dealt with per list.
        pyXplor $dir_xplor/python/setupSystemRECOORD.py |& tee setupSystemRECOORD.log
    endif
    
    if ( $doSetupAnneal ) then
        pyXplor $dir_xplor/python/annealRECOORD.py |& tee annealRECOORD.log
    endif
    
    echo "  Finished $x"
end

echo "Finished"
   
exit 0


# Notes todo:
- e.g. 2hgh
B chain in ccpn is listed as entity 1 in ccpn and nmrstar. Reported as FC179
for zn i want to add something like:
http://www.bmrb.wisc.edu/data_library/timedomain/1/bmr6682/analysis/9valid/TOP_ZINC.PRO
- rename the residue from zinc to zn though as in pdb.
Using PREsidue ZINF from there 3 times:

/2hgh_001/C/C/ZN`1/ZN
/2hgh_001/B/B/CYS`9/SG
/2hgh_001/B/B/CYS`4/SG
/2hgh_001/B/B/HIS`22/NE2
/2hgh_001/B/B/HIS`26/NE2

/2hgh_001/D/D/ZN`1/ZN
/2hgh_001/B/B/CYS`34/SG
/2hgh_001/B/B/CYS`39/SG
/2hgh_001/B/B/HIS`52/NE2
/2hgh_001/B/B/HIS`56/NE2

/2hgh_001/E/E/ZN`1/ZN
/2hgh_001/B/B/HIS`85/NE2
/2hgh_001/B/B/HIS`80/NE2
/2hgh_001/B/B/CYS`67/SG
/2hgh_001/B/B/CYS`61/SG

# Can be extracted probably by writing a little pymol macro or a huge java snippet.

# Junk
        # Following needs to be revised
        echo "      creating pdb file for fun"
        gawk -f $WATTOSSCRIPTSDIR/convert_star2pdb 1xxx.str 1xxx.pdb >>& $log_file
        if ( $status ) then
            echo "ERROR $x in convert_star2pdb"
            continue
        endif

        echo "      splitpdb" 
        splitpdb modelnum=1 1xxx.pdb  >>& $log_file
        if ( $status ) then
            echo "ERROR $x in splitpdb"
            continue
        endif
        if ( ! -e 1xxx"_001".pdb) then
            \cp -f 1xxx.pdb 1xxx"_001".pdb 
        endif
        \rm 1xxx.pdb
