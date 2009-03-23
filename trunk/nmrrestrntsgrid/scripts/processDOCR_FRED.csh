#!/bin/csh -f
# Author: Jurgen F. Doreleijers
# Wed Dec 14 13:49:06 CST 2005
#
# TASK: Do all processing needed in order to go from parsed restraints
#       to files for the FRED database.
# USE:  processDOCR_FRED.csh [1brv]
#OR: set x = 1brv  ; $scripts_dir/processDOCR_FRED.csh $x |& tee $perEntry_dir/$x.log

#set subl = ( 1a4d 1a24 1afp 1ai0 1brv 1bus 1cjg 1hue 1ieh 1iv6 1kr8 2hgh 2k0e )

#set subl = ( 1a4d 1afp 1ai0 1brv 1bus 1cjg 1hue 1ieh 1iv6 1kr8 2hgh 2k0e )
#set subl = ( 108d 149d 170d 171d 17ra )

#set subl = ( 1a4d )
#set subl = (`cat $list_dir/list_baddies_2009-01-20.csv`)
#set subl = ( `cat  $list_dir/NMR_Restraints_Grid_entries_2008_02-14.txt`)
#set subl = ( `cat  $list_dir/nmr_list_parsed_2008-02-15.txt`)
#set subl = ( 1brv 2jnd 2jqs 2ofc 2pmc )

source $0:h/settings.csh


# Get argument pdb code if it exists.
if ( $1 != "" ) then
    set subl = (  $1  )
endif

set doReadMmCif         = 1
set doJoin              = 1
set doMerge             = 1 # Actually linking by FC.
set doAssign            = 1
set doSurplus           = 1
set doViolAnal          = 1
set doCompleteness      = 1
set doExportsForGrid    = 1
set doOrganizeForGrid   = 1
set doDumpInGrid        = 1
set doCleanFiles        = 0 # Keep this on for it does fill up > 100 G on > 4,000 entries

set interactiveProcessing = 1 # Set to zero to do production run but one for a very fast run.
# The largest entry 2k0e is completely reprocessed interactively in 2'30".

set extraWattosOptions  =
set extraFCOptions      = ( -raise -force )
#set extraFCOptions      = ( -raise -force -noWrite )
# Filter a small number of distance restraints out for FRED.
set dofilterTopViolations = 1

# E.g. to make it run without an X-server
set hasHead = 0

# No need to change things below this line
###############################################################################

# steps that are not really done anymore but are dealt with so that the setup stays consistent.
set regularProcessing = 1
set doAddMissingAtoms   = $regularProcessing
set doWHATIF            = $regularProcessing
set doNomenclature      = $regularProcessing
set doCoplanars         = $regularProcessing

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

# redefine wattos alias
# wsetup now done in ~/.cshrc of docr user.
#setenv WATTOSMEM 2g failed after updating OS FS to case sensitive
setenv WATTOSMEM 1500m
setenv woptions  "$extraWattosOptions -Xmx$WATTOSMEM"
alias wattos "java $woptions Wattos.CloneWars.UserInterface -at"
alias wjava  "java $woptions"

echo
echo "interactiveProcessing       interactive run is fast use zero for production            $interactiveProcessing"
echo "doReadMmCif       Converts PDB mmCIF to NMR-STAR with Wattos        -> XXXX_wattos.str $doReadMmCif"
echo "doJoin            Joins the parsed NMR-STAR rest with coor. Wattos    -> XXXX_join.str $doJoin"
echo "doMerge           Converts STAR to STAR with linkNmrStarData.py      -> XXXX_merge.str $doMerge"
#echo "doAddMissingAtoms Calculates any missing atoms                       -> XXXX_extra.str $doAddMissingAtoms"
#echo "doWHATIF          Changes nomenclature and hydrogen with WI                            $doWHATIF"
#echo "doNomenclature    Updates nomen. and hydrogen in STAR with Wattos    -> XXXX_nomen.str $doNomenclature"
echo "doAssign          Changes stereo assignments with Wattos            -> XXXX_assign.str $doAssign"
echo "doSurplus         Changes distance restraints with Wattos     ->   XXXX_nonsurplus.str $doSurplus"
echo "doViolAnal        Analyzes violation with Wattos                                       $doViolAnal"
echo "doCompleteness    Determines NOE completeness with Wattos                              $doCompleteness"
#echo "doCoplanars       Calculates coplanar base sets for nucleic acid structures            $doCoplanars"
echo "doExportsForGrid  Converts DOCR/FRED to CYANA and XPLOR for Grid                       $doExportsForGrid"
echo "doOrganizeForGrid Puts the results in a directory structure for Grid                   $doOrganizeForGrid"
echo "doDumpInGrid      Puts the files into Grid                                             $doDumpInGrid"
echo "doCleanFiles      Removes redundant files from fs                                      $doCleanFiles"
echo "Is there an X-server attached for possible questions:                                  $hasHead"
echo "Extra arguments FC                                                                     $extraFCOptions"
echo "PYTHONPATH:       $PYTHONPATH"
echo "CLASSPATH:        $CLASSPATH"
which wattos

echo "Doing" $#subl "pdb entries"
foreach x ( $subl )
   echo "Doing $x"
   set ch23 = ( `echo $x | cut -c2-3` )

    if ( $doReadMmCif ) then
        echo "  mmCIF"
        set script_file     = $wcf_dir/ReadMmCifWriteNmrStar.wcf
        set inputMmCifFile  = $CIFZ2/$ch23/$x.cif.gz
        set outputStarFile  = $x"_wattos".str
        set script_file_new = $x.wcf
        set log_file        = $x.log

        cd $dir_star
        if ( -e $x ) then
            \rm -rf $x
        endif
        mkdir $x
        cd $x

        if ( ! -e $inputMmCifFile ) then
            echo "ERROR: $x No input mmCIF file: $inputMmCifFile"
            continue
        endif
        set maxModels = 999
        if ( $interactiveProcessing ) then
        	set maxModels = 2
        endif
        sed     -e 's|INPUT_MMCIF_FILE|'$inputMmCifFile'|'   $script_file  |\
	        sed -e 's|MAX_MODELS|'$maxModels'|'                            |\
            sed -e 's|OUTPUT_STAR_FILE|'$outputStarFile'|' > $script_file_new
#        echo -n "DEBUG: "; date

        wattos < $script_file_new >& $log_file
        if ( $status ) then
            echo "ERROR $x Wattos script $script_file_new failed; not continueing"
            continue
        endif
#        echo -n "DEBUG: "; date

        grep --quiet ERROR $log_file
        if ( ! $status ) then
            echo "ERROR $x found erros in log file; not continueing; will now grep for ERROR again."
            grep ERROR $log_file
            continue
        endif

        \rm $script_file_new
        if ( ! -e $outputStarFile ) then
            echo "ERROR $x found no output star file $outputStarFile"
            continue
        endif
    endif


    if ( $doJoin ) then
        echo "  join"
        set inputStarCoorFile   = $x"_wattos".str
        set inputStarRestFile   = $dir_restr_unzip/$x"_rst".str
        set outputStarFile      = $x"_join".str
        set log_file            = $x"_join".log

        cd $dir_star
        if ( ! -e $x ) then
            echo "ERROR: $x No dir: $x"
            continue
        endif
        cd $x

        if ( ! -e $inputStarCoorFile ) then
            echo "ERROR: $x No input STAR coordinates file: $inputStarCoorFile"
            continue
        endif
        if ( ! -e $inputStarRestFile ) then
            echo "ERROR: $x No input STAR parsed restraints file: $inputStarRestFile"
            continue
        endif

#        echo -n "DEBUG: "; date
        wjava Wattos.Star.STARJoin $inputStarCoorFile $inputStarRestFile $outputStarFile >& $log_file
        if ( $status ) then
            echo "ERROR $x STARJoin; not continueing"
            continue
        endif
#        echo -n "DEBUG: "; date

        grep --quiet ERROR $log_file
        if ( ! $status ) then
            echo "ERROR $x found erros in log file; not continueing; will now grep for ERROR again."
            grep ERROR $log_file
            continue
        endif

        if ( ! -e $outputStarFile ) then
            echo "ERROR $x found no output star file $outputStarFile"
            continue
        endif
    endif


   if ( $doMerge ) then
        echo "  merge"
        set log_file            = $x"_merge".log
        set fc_entry_dir        = $ccpn_tmp_dir/data/recoord/$x
        set fcInputDir          = $ccpn_tmp_dir/data/archives/bmrb/nmrRestrGrid/$x
        set fc_log_file         = $fc_entry_dir/linkNmrStarData.log
        set fc_sum_file         = $fc_entry_dir/linkNmrStarData.summary
        set inputStarFile       = $x"_join".str
        set outputStarFile      = $dir_star/$x/$x"_merge".str
        set mergeScriptFile     = $R/python/recoord2/msd/linkNmrStarData.py
        set guess_file       = guessLink.txt

        cd $dir_link
        if ( -e $x ) then
            \rm -rf $x
        endif
        mkdir $x
        cd $x

        if ( ! -e $dir_star/$x/$inputStarFile  ) then
            echo "ERROR $x previous step produced no star file."
            continue
        endif
        if ( ! -e $fcInputDir ) then
        	mkdir -p $fcInputDir
        endif
        set fcInputFile = $fcInputDir/joinedCoord.str
        \cp -f $dir_star/$x/$inputStarFile $fcInputFile
        if ( ! -e $fcInputFile ) then
            echo "ERROR $x failed to copy input for FC to: $fcInputDir"
            continue
        endif
        # Set the right project dir in the script
        # directly.

        # Can be handy for guessing later.
        $scripts_dir/guessOffSet.csh $x |& tee $guess_file

#        echo -n "DEBUG: "; date
        python -u $mergeScriptFile $x $extraFCOptions >& $log_file
        if ( $status ) then
            echo "ERROR $x in $mergeScriptFile"
            echo "please check the log: $cwd/$log_file (it hasn't been copied to: $fc_sum_file yet because aborting entry at this point."
            continue
        endif
#        echo -n "DEBUG: "; date
        # Take a copy for ease of annotation together in this dir.
        \cp -f $fc_log_file $fc_sum_file .
        grep --quiet ERROR $log_file
        if ( ! $status ) then
            echo "ERROR $x found in merge log file; will now grep for ERROR again."
            grep ERROR $log_file
            continue
        endif

        set theCwd = $cwd
        cd $fc_entry_dir
        tar -cf - linkNmrStarData | gzip --fast > $x.tgz
        cd $theCwd

        set fcOutputFile = $fc_entry_dir/$x"_linked".str
        if ( ! -e $fcOutputFile  ) then
            echo "ERROR $x FC produced no star file."
            continue
        endif
        # keep the copy.
        \cp -f $fcOutputFile $outputStarFile

        ## Check validity without really filtering anything.
#        echo -n "DEBUG: "; date
        wjava Wattos.Star.STARFilter $outputStarFile $x"_nice".str . >& STARFilter.log
        if ( $status ) then
          echo "ERROR $x $mergeScriptFile produced no valid star file according to Wattos."
          continue
        endif
#        echo -n "DEBUG: "; date
        grep --quiet "ERR" STARFilter.log
        if ( ! $status ) then
          echo "ERROR $x Wattos reported an error in parsing/unparsing merge step STAR file.; will now grep for ERROR again."
          grep ERROR $log_file
          continue
        endif
        if ( ! -e $x"_nice".str ) then
          echo "ERROR $x Wattos produced no star file after merge step."
          continue
        endif
        # why not use a nice star file if the choice is there.
        \mv $x"_nice".str $outputStarFile
    endif


    if ( $doAddMissingAtoms ) then
#        echo "  skipping addMissingAtoms"
        set script_file     = $wcf_dir/AddMissingAtoms.wcf
        set inputStarFile   = $dir_star/$x/$x"_merge".str
        set outputStarFile  = $x"_extra".str
        set outputPDBFile   = $x"_extra".pdb
        set script_file_new = $x.wcf
        set log_file        = $x"_addMissingAtoms".log

        cd $dir_extra
        if ( -e $x ) then
            \rm -rf $x
        endif
        mkdir $x
        cd $x

        if ( ! -e $inputStarFile ) then
            echo "ERROR: $x No addMissingAtoms input star file: $inputStarFile"
            echo "ERROR: perhaps a previous phase was not done yet?"
            continue
        endif
        if ( 1 ) then
	        cp $inputStarFile $outputStarFile
        else
	        # writes star file with PDB file writing; automatically.
	        sed -e 's|OUTPUT_PDB_FILE|'$outputPDBFile'|'     $script_file |\
	        sed -e 's|INPUT_STAR_FILE|'$inputStarFile'|'       > $script_file_new

	        wattos < $script_file_new >& $log_file
	        if ( $status ) then
	            echo "ERROR $x Wattos addMissingAtoms script: $script_file_new failed"
	            continue
	        endif

	        if ( ! -e $outputPDBFile ) then
	            echo "ERROR $x found no PDB file $outputPDBFile"
	            continue
	        endif
	        \rm $script_file_new
	   endif
       if ( ! -e $outputStarFile ) then
		    echo "ERROR $x found no star file $outputStarFile"
		    continue
       endif
    endif


    ## Don't care when whatif crashes.
    if ( $doWHATIF ) then
#        echo "  skipping wi"
        if ( 0 ) then
	        set inputPDBFile   = $dir_extra/$x/$x"_extra".pdb
	        cd $dir_wi_all
	        if ( -e $x ) then
	            \rm -rf $x
	        endif
	        mkdir $x
	        cd $x

	        #\rm $x"_rename".log >& /dev/null
	        #\rm $x"_wi".pdb     >& /dev/null
	        #\rm -f $x.pdb       >& /dev/null
	        #if ( -e $pdbmod_dir/pdb$x.ent ) then
	        #    echo "DEBUG: $x using the PDB coordinates from the mod directory"
	        #    ln -s $pdbmod_dir/pdb$x.ent $x.pdb
	        #else
	        #    zcat $PDBZ2/$ch23/pdb$x.ent.gz > $x.pdb
	        #endif
	# ARGUMENTS:
	#   do_logs
	#   add_coordinates
	#   do_write
	#   pdb file name with directory

	        # Get the file locally because WI doesn't deal well with long path names.
	        ln -s $inputPDBFile $x.pdb
	        # What if needs to be fooled in thinking it has an input stream.
	        $scripts_dir/WI_rename.csh f f t $x.pdb < /dev/null >& $x"_rename".log
	        if ( $status ) then
	            echo "WARNING $x in whatif"
	            # continue
	        endif
	        grep --quiet ERROR $x"_rename".log
	        if ( ! $status ) then
	            echo "WARNING $x found in whatif log file"
	            # continue
	        endif
	        grep --quiet "No match" $x"_rename".log
	        if ( ! $status ) then
	            echo "WARNING $x found 'No match' in log file"
	            # continue
	        endif
	        if ( ! -e $x"_wi".pdb ) then
	            echo "WARNING $x found no WI pdb file"
	            # continue
	        endif
	        # \rm $x.pdb
        endif
    endif


    if ( $doNomenclature ) then
#        echo "  skipping nomen"
        # Nevertheless make sure that the expected output from this exists
        # for further down the pipe line.
        if ( 1 ) then
	        set script_file     = $wcf_dir/SetAtomNomenclatureToIUPAC.wcf
	        set inputStarFile   = $dir_extra/$x/$x"_extra".str
	        set inputPDBFile    = $dir_wi_all/$x/$x"_wi".pdb
	        set outputStarFile  = $x"_nomen".str
	        set script_file_new = $x.wcf
	        set log_file        = $x.log

	        cd $dir_nomen
	        if ( -e $x ) then
	            \rm -rf $x
	        endif
	        mkdir $x
	        cd $x

	        if ( ! -e $inputStarFile ) then
	            echo "ERROR: $x No nomen input star file: $inputStarFile"
	            continue
	        endif

	        cp $inputStarFile $outputStarFile
        else
	        if ( ! -e $inputPDBFile ) then
	            echo "WARNING: $x no input WI PDB file for entry: $inputPDBFile"
	            \cp -f $inputStarFile $outputStarFile
	        else
	            sed -e 's|OUTPUT_STAR_FILE|'$outputStarFile'|'   $script_file |\
	            sed -e 's|INPUT_STAR_FILE|'$inputStarFile'|'                  |\
	            sed -e 's|INPUT_PDB_FILE|'$inputPDBFile'|'       > $script_file_new

	            wattos < $script_file_new >& $log_file
	            if ( $status ) then
	                echo "WARNING $x Wattos rename script failed; not using rename"
	                \cp -f $inputStarFile $outputStarFile
	            else
	                grep --quiet ERROR $log_file
	                if ( ! $status ) then
	                    echo "WARNING $x found erros in log file; not using rename"
	                    \cp -f $inputStarFile $outputStarFile
	                endif
	            endif
	            \rm $script_file_new
	        endif
        endif
        if ( ! -e $outputStarFile ) then
            echo "ERROR $x found no star file $outputStarFile"
            continue
        endif
    endif



    # Check and correct stereospecific assignment of restraints
    if ( $doAssign ) then
        echo "  assign"
        set script_file      = $wcf_dir/CheckAssignment.wcf
        #set inputStarFile    = $dir_nomen/$x/$x"_nomen".str
        set inputStarFile    = $dir_star/$x/$x"_merge".str
        set outputStarFile   = $x"_assign".str
        set script_file_new  = $x.wcf
        set log_file         = $x.log

        cd $dir_assign
        if ( -e $x ) then
            \rm -rf $x
        endif
        mkdir $x
        cd $x

        if ( ! -e $inputStarFile ) then
            echo "ERROR: $x No FormatConverter input star file: $inputStarFile"
            continue
        endif
        # The flag disables any output; exit status will be zero when any match is found
        set containsLinkedDistances = 0
        grep --quiet "_Dist_constraint_tree.Constraint_ID" $inputStarFile
        if ( ! $status ) then
            set containsLinkedDistances = 1
        endif
        if ( $containsLinkedDistances ) then
            sed -e 's|OUTPUT_STAR_FILE|'$outputStarFile'|'     $script_file |\
            sed -e 's|INPUT_STAR_FILE|'$inputStarFile'|'     > $script_file_new

#	        echo -n "DEBUG: "; date
            wattos < $script_file_new >& $log_file
            if ( $status ) then
                echo "ERROR $x in Wattos assign script"
                continue
            endif
#            echo -n "DEBUG: "; date
            grep --quiet ERROR $log_file
            if ( ! $status ) then
                echo "ERROR $x found in assign log file; will now grep for ERROR again."
	            grep ERROR $log_file
                continue
            endif
            if ( ! -e $outputStarFile ) then
                echo "ERROR $x found no star file $outputStarFile"
                continue
            endif
            ## Check validity
            wjava Wattos.Star.STARFilter $outputStarFile $x"_tmp".str . >& STARFilter.log
            if ( $status ) then
                echo "ERROR $x Wattos assign step produced no valid star file according to Wattos."
                continue
            endif
            grep --quiet "ERR" STARFilter.log
            if ( ! $status ) then
                echo "ERROR $x Wattos reported an error in parsing/unparsing assign step STAR file."
                continue
            endif
            if ( ! -e $x"_tmp".str ) then
                echo "ERROR $x Wattos after Wattos assign produced no star file."
                continue
            endif
            \rm -f $x"_tmp".str
            \rm $script_file_new
        else
#            echo "DEBUG: ignoring assignment analysis because no distance constraints were found."
            cp $inputStarFile $outputStarFile
        endif
        if ( ! -e $outputStarFile ) then
            echo "ERROR $x found no star file $outputStarFile"
            continue
        endif

    endif


    # Remove surplus restraints
    if ( $doSurplus ) then
        echo "  surplus"
        set script_file      = $wcf_dir/GetNonSurplus.wcf
        set inputStarFile    = $dir_assign/$x/$x"_assign".str
        set outputStarFile   = $x"_nonsurplus".str
        set script_file_new  = $x.wcf
        set log_file         = $x.log

        cd $dir_surplus
        if ( -e $x ) then
            \rm -rf $x
        endif
        mkdir $x
        cd $x

        if ( ! -e $inputStarFile ) then
            echo "ERROR: $x No FormatConverter input star file: $inputStarFile"
            continue
        endif

        # The flag disables any output; exit status will be zero when any match is found
        set containsAssignedDistances = 0
        grep --quiet "_Dist_constraint_tree.Constraint_ID" $inputStarFile
        if ( ! $status ) then
            set containsAssignedDistances = 1
        endif
        if ( $containsAssignedDistances ) then
            set filterTopViolationsText = "#FILTER_TOP_VIOLATIONS"
            if ( $dofilterTopViolations ) then
                set filterTopViolationsText = ""
            endif
            sed -e 's|OUTPUT_STAR_FILE|'$outputStarFile'|'     $script_file |\
            sed -e 's|\#FILTER_TOP_VIOLATIONS|'$filterTopViolationsText'|'   |\
            sed -e 's|INPUT_STAR_FILE|'$inputStarFile'|'     > $script_file_new

#        	echo -n "DEBUG: "; date
            wattos < $script_file_new >& $log_file
            if ( $status ) then
                echo "ERROR $x in Wattos surplus script"
                continue
            endif
#	        echo -n "DEBUG: "; date
            grep --quiet ERROR $log_file
            if ( ! $status ) then
                echo "ERROR $x found in surplus log file; will now grep for ERROR again."
	            grep ERROR $log_file
                continue
            endif
            \rm -f $x"_tmp".str
            \rm $script_file_new
        else
            echo "DEBUG: ignoring surplus analysis because no distance constraints were found."
            #echo "DEBUG: Removing any dihedrals and RDCs from original."
            #set filterStarFile   = $scripts_dir/filter_rules_remove_dih_rdc.str
            #wjava Wattos.Star.STARFilter $inputStarFile $outputStarFile $filterStarFile >& STARFilter.log
            #if ( $status ) then
            #    echo "ERROR $x failed to remove nondist saveframes."
            #    continue
            #endif
            #grep --quiet "ERR" STARFilter.log
            #if ( ! $status ) then
            #    echo "ERROR $x Wattos reported an error in parsing/unparsing surplus step STAR file."
            #    continue
            #endif
            cp $inputStarFile $outputStarFile
        endif
        if ( ! -e $outputStarFile ) then
            echo "ERROR $x found no star file $outputStarFile"
            continue
        endif
    endif



    # Get violation analyses
    if ( $doViolAnal ) then
        echo "  viol"
        set script_file      = $wcf_dir/CalcConstrViolation.wcf
        set inputStarFile    = $dir_surplus/$x/$x"_nonsurplus".str
        set outputDistStarFile   = $x"_dist_viol".str
        set outputDihedStarFile  = $x"_dihed_viol".str
        set script_file_new  = $x.wcf
        set log_file         = $x.log

        cd $dir_viol
        if ( -e $x ) then
            \rm -rf $x
        endif
        mkdir $x
        cd $x

        if ( ! -e $inputStarFile ) then
            echo "ERROR: $x No FormatConverter input star file: $inputStarFile"
            continue
        endif

        sed -e 's|OUTPUT_DIST_STAR_FILE|'$outputDistStarFile'|'     $script_file |\
        sed -e 's|OUTPUT_DIHED_STAR_FILE|'$outputDihedStarFile'|' |\
        sed -e 's|INPUT_STAR_FILE|'$inputStarFile'|'     > $script_file_new

        wattos < $script_file_new >& $log_file
        if ( $status ) then
            echo "ERROR $x in Wattos violation script"
            continue
        endif

        grep --quiet ERROR $log_file
        if ( ! $status ) then
            echo "ERROR $x found in viol log file; will now grep for ERROR again."
            grep ERROR $log_file
            continue
        endif

        grep --quiet "_Dist_constraint_tree.Constraint_ID" $inputStarFile
        if ( ! $status ) then
	        if ( ! -e $outputDistStarFile ) then
	            echo "ERROR $x found no result file $outputDistStarFile"
	            continue
	        endif
	    endif

        grep --quiet "_Torsion_angle_constraint_list.ID" $inputStarFile
        if ( ! $status ) then
            if ( ! -e $outputDihedStarFile ) then
                echo "ERROR $x found no result file $outputDihedStarFile"
                continue
            endif
        endif

        \rm $script_file_new
    endif


    # Get completeness
    if ( $doCompleteness ) then
        echo "  compl"
        set script_file      = $wcf_dir/GetCompleteness.wcf
        set inputStarFile    = $dir_surplus/$x/$x"_nonsurplus".str
        set outputStarFile   = $x"_compl".str
        set outputBaseFile   = $x"_compl"

        set script_file_new  = $x.wcf
        set log_file         = $x.log

        cd $dir_compl
        if ( -e $x ) then
            \rm -rf $x
        endif
        mkdir $x
        cd $x

        if ( ! -e $inputStarFile ) then
            echo "ERROR: $x No FormatConverter input star file: $inputStarFile"
            continue
        endif

        # The --quiet flag disables any output; exit status will be zero when any match is found
        set containsNonSurplusDistances = 0
        grep --quiet "_Dist_constraint_tree.Constraint_ID" $inputStarFile
        if ( ! $status ) then
            set containsNonSurplusDistances = 1
        endif

        # Reducing time spend for entry (with 1 model)
        # 1brv from 6 to 3 seconds and for
        # 2hgh from 60 to 13 seconds.
        set maxDistanceCompleteness = 9.0
        if ( $interactiveProcessing ) then
        	set maxDistanceCompleteness = 4.0
        endif
        if ( $containsNonSurplusDistances ) then
            sed -e 's|OUTPUT_STAR_FILE|'$outputStarFile'|'     $script_file 				|\
            sed -e 's|INPUT_STAR_FILE|'$inputStarFile'|'                    				|\
            sed -e 's|MAX_DISTANCE_COMPLETENESS|'$maxDistanceCompleteness'|'             	|\
            sed -e 's|OUTPUT_FILE_BASE|'$outputBaseFile'|'     > $script_file_new

#	        echo -n "DEBUG: "; date
            wattos < $script_file_new >& $log_file
            if ( $status ) then
                echo "ERROR $x in Wattos completeness script"
                continue
            endif
#	        echo -n "DEBUG: "; date
            grep --quiet ERROR $log_file
            if ( ! $status ) then
                echo "ERROR $x found in compl log file; will now grep for ERROR again."
	            grep ERROR $log_file
                continue
            endif
            if ( ! -e $outputStarFile ) then
                echo "WARNING $x found no result file $outputStarFile"
                echo "WARNING $x perhaps due to no observable atoms in PDB file like for entry 8drh"
            endif
            \rm $script_file_new
        else
            echo "DEBUG: ignoring completeness analysis because no distance constraints were found."
        endif
    endif



    # Get base pairing and tripling etc.
    if ( $doCoplanars ) then
#        echo "  skipping coplanar"
        if ( 0 ) then
	        set script_file      = $wcf_dir/GetCoplanarBases.wcf
	        set inputStarFile    = $dir_surplus/$x/$x"_nonsurplus".str
	        set script_file_new  = $x.wcf
	        set log_file         = $x.log

	        cd $dir_coplanar
	        if ( -e $x ) then
	            \rm -rf $x
	        endif
	        mkdir $x
	        cd $x

	        if ( ! -e $inputStarFile ) then
	            echo "ERROR: $x No FormatConverter input star file: $inputStarFile"
	            continue
	        endif

	        # The flag disables any output; exit status will be zero when any match is found
	        set containsNA = 0
	        egrep --quiet "_Entity.Polymer_type +poly(deoxy)?ribonucleotide" $inputStarFile
	        if ( ! $status ) then
	            set containsNA = 1
	        endif
	        if ( $containsNA ) then
	            sed -e 's|INPUT_STAR_FILE|'$inputStarFile'|'       $script_file \
	                > $script_file_new
	            wattos < $script_file_new >& $log_file
	            if ( $status ) then
	                echo "ERROR $x after executing Wattos script file: $script_file"
	                continue
	            endif
	            grep --quiet ERROR $log_file
	            if ( ! $status ) then
	                echo "ERROR $x found in planar log file"
	                continue
	            endif
	            \rm $script_file_new
	        else
	#            echo "DEBUG: ignoring coplanars analysis because no NA were found."
            endif
        endif
    endif


    # Converts to XPLOR (and later others) formatted restraints and coordinates.
    if ( $doExportsForGrid ) then
        echo "  exportsForGrid"
        # FC exports
        set fc_entry_dir        = $ccpn_tmp_dir/data/recoord/$x
        # Wattos exports
        set script_file         = $wcf_dir/ExportForNRG.wcf
        set overallStatus = 0
        cd $dir_export
        if ( -e $x ) then
            \rm -rf $x
        endif
        mkdir $x
        cd $x

        set overallStatus = 0
        foreach fcExportFormat (  Cns Cyana )
	        # check if loop encountered a fatal error before.
	        if ( $overallStatus ) then
	            #echo "DEBUG: $x found error before in doExportsForGrid"
	            continue
	        endif

	        #echo "DEBUG: exporting $fcExportFormat"

            if ( ! -e $fcExportFormat ) then
            	mkdir $fcExportFormat
            endif

            # use absolute path for human user that sees the message.
            set fc_ScriptFile       = $R/python/recoord2/msd/"export"$fcExportFormat.py
            set fc_log_file         = $cwd/$fcExportFormat/$x"_fc_export_"$fcExportFormat.log

	        python -u $fc_ScriptFile $x "$fc_entry_dir/.." $fcExportFormat >& $fc_log_file
	        if ( $status ) then
	            echo "ERROR $x in $fc_ScriptFile"
                set overallStatus = 1
                continue
	        endif

	        grep --quiet ERROR $fc_log_file
	        if ( ! $status ) then
	           echo "ERROR $x found in $fc_log_file log file; will now grep for ERROR again."
	           grep ERROR $fc_log_file
	           set overallStatus = 1
	           continue
	        endif
        end


        # disable for testing.
        #foreach d ( )
        foreach d ( DOCR )
            set outputFileBase = $x"_"$d
            set inputFile     = $dir_nomen/$x/$x"_nomen".str
            if ( $d == "FRED" ) then
                set inputFile   = $dir_surplus/$x/$x"_nonsurplus".str
            endif
	        set script_file_new  = $outputFileBase.wcf
	        set log_file         = $outputFileBase.log
            sed -e 's|OUTPUT_XPLOR_FILE_BASE|'$outputFileBase'|' $script_file |\
            sed -e 's|INPUT_STAR_FILE|'$inputFile'|'       > $script_file_new

	        if ( ! -e $inputFile ) then
	            echo "ERROR: $x No input star file: $inputFile"
	            continue
	        endif

	        # Note that the Wattos generated restraint files are not put into NRG. The FC generated ones are used.
            wattos < $script_file_new >& $log_file
            if ( $status ) then
                echo "ERROR $x after executing Wattos script file: $script_file see log file: $log_file"
                set overallStatus = 1
                continue
            endif
            grep --quiet ERROR $log_file
            if ( ! $status ) then
                echo "ERROR $x found in export log file; will now grep for ERROR again."
	            grep ERROR $log_file
                set overallStatus = 1
                continue
            endif
            \rm $script_file_new
        end

#        echo -n "DEBUG: "; date
        if ( $overallStatus ) then
            echo "ERROR $x found in doExportsForGrid"
            continue
        endif
    endif

    # Organize the files for insertion into NMR Restraints Grid -AND- to wwPDB.
    # Add BMRB specific notes for DOCR/FRED NMR-STAR files.
    if ( $doOrganizeForGrid ) then
        echo "  gridOrganize"
#        echo -n "DEBUG: "; date
        set overallStatus = 0

        set wwPDB_dir_entry = $wwPDB_dir/$ch23/$x
        # Create directory with parents if needed
        mkdir -p $wwPDB_dir_entry
        # Remove any previous content for this entry.
        \rm -rf $wwPDB_dir_entry/* >& /dev/null

        # Create the STAR files with correct header.
        foreach d ( DOCR FRED wwPDB )
            #echo "Creating STAR file for $d"
            set dataFile      = "data_"$d"_restraints_with_modified_coordinates_PDB_code_"
            if ( $d == "wwPDB" ) then
            	set dataFile      = "data_wwPDB_remediated_restraints_file_for_PDB_entry_"
            endif

            set fileHeader    = $nrg_dir/data/change_comment_star_$d.txt
            set DBdir         = $dir_db/$d/$x
            if ( $d == "wwPDB" ) then
                # It's put into this location because it was most efficient to code but the wwPDB archive is not here!
                set DBdir         = $dir_db/wwPDBtmp/$x
            endif

            set outputFile    = $x"_project".str
            set inputFile     = $dir_nomen/$x/$x"_nomen".str
            if ( $d == "FRED" ) then
                set inputFile   = $dir_surplus/$x/$x"_nonsurplus".str
            endif

            ## NO CHANGES BELOW
            \rm -rf $DBdir >& /dev/null
            mkdir -p $DBdir
            cd $DBdir
            echo $dataFile$x                                  >  $outputFile
            echo                                              >> $outputFile
            sed -e 's|PDBCODE HERE|'$x'|' $fileHeader         >> $outputFile
            echo                                              >> $outputFile
            gawk -f $scripts_dir/stripDataNode   $inputFile   >> $outputFile

            ## Check validity
            wjava Wattos.Star.STARFilter $outputFile $x"_testRead".str . >& STARFilter.log
            if ( $status ) then
                echo "ERROR $x gridOrganize for database $d produced no valid star file according to Wattos."
                set overallStatus = 1
                continue
            endif
            grep --quiet "ERR" STARFilter.log
            if ( ! $status ) then
                echo "ERROR $x Wattos reported an error in parsing/unparsing gridOrganize step STAR file.; will now grep for ERROR again."
                grep ERROR STARFilter.log
                continue
            endif
            if ( ! -e $x"_testRead".str ) then
                echo "ERROR $x Wattos produced no star file at gridOrganize."
                set overallStatus = 1
                continue
            endif
            \rm -f $x"_testRead".str
        end

        # Gzip and copy the star file to wwPDB_dir_entry
        gzip -c $dir_db/wwPDBtmp/$x/$x"_project".str > $wwPDB_dir_entry/$x.str.gz
        \rm -rf $dir_db/wwPDBtmp/$x

        foreach d ( DOCR FRED )
            set DBdir         = $dir_db/$d/$x
            cd $DBdir

            set assignFile    =  $dir_assign/$x/assignment.str
            set surplusFile   = $dir_surplus/$x/surplus_summary.str
            set complFile     =   $dir_compl/$x/$x"_compl".str

            if ( $d == "DOCR" ) then
                # Get the Wattos generated XPLOR sequence files.
                cp $dir_export/$x/$x"_DOCR_"*.py .

                # only setting DOCR converted files.
	            set dataTypeList = (  dist                           hBond                          dihed               rdc )
	            set dataTypeList2 = ( _distance_general_distance_na_ _distance_HB_na_               _dihedral_na_na_    _dipolar_coupling_na_na_)
	            @ dataTypeNumber = 0
	            foreach dataType ( $dataTypeList )
	                #echo "DEBUG: working on dataType: " $dataType
	                @ dataTypeNumber ++
	                # name changed from Wattos: 1a4d_DOCR_dc_001.tbl to FC:
	                # Cns/1a4d.dist.1.tbl
	                # Cyana/1brv.dihed.1.aco

	#                set list = ( `find $dir_export/$x -name "$x\_$d\_$dataType*"` )
	                set list = ( `find $dir_export/$x -name "$x\.$dataType\.*"` )
	                foreach file ( $list )
	                    #echo "DEBUG: working on file: " $file

	#                   set number = ( `gawk -v f=$file:t:r 'BEGIN{f=substr(f,5);gsub(/[a-z_A-Z]/,"",f);printf("%d\n", f)}' /dev/null`)
	                    set number = ( `gawk -v f=$file:t:r 'BEGIN{split(f,a,".");printf("%s\n", a[3])}'                    /dev/null`)

	                    #echo "DEBUG: deduced number: " $number
	                    set extension = $file:e
	                    set fileNew = $x$dataTypeList2[$dataTypeNumber]$number.$extension
                        cp $file $fileNew
                        cp $file $wwPDB_dir_entry
	                    if ( $status ) then
	                        echo "ERROR $x failed to copy file $file to $fileNew."
	                        set overallStatus = 1
	                        continue
	                    endif
	                end
	            end
                set cyanaSeqFile = $dir_export/$x/Cyana/$x.seq
                if ( -e $cyanaSeqFile  ) then
                    set fileNew = $x"_sequence".seq
                    cp $cyanaSeqFile $fileNew
                    cp $cyanaSeqFile $wwPDB_dir_entry/$fileNew
                endif

	            ## Only create the ccpn project once.
	            cd $ccpn_tmp_dir/data/recoord/$x
	            #cd $dir_link/$x/ccpn
	            # Create a tgz copy that will not be deleted whereas the ccpn dir will.
	            tar czf $dir_link/$x/$x"_project".xml.tgz * > /dev/null
	            if ( $status ) then
	                echo "ERROR $x failed to tar xml files to $DBdir/$x"_project".xml.tgz"
	                set overallStatus = 1
	                continue
	            endif
	            cd $DBdir
	            ln -s $ccpn_tmp_dir/data/recoord/$x/$x.tgz $x"_project".xml.tgz
                cp $x"_project".xml.tgz $wwPDB_dir_entry/$x"_ccpn".tgz
            endif # db is DOCR


            # Allow absent files without complain
            if ( $d == "FRED" ) then
                cp -v $assignFile  $x"_assign".str     >& /dev/null
                cp -v $surplusFile $x"_surplus".str    >& /dev/null
                cp -v $complFile   $x"_compl".str      >& /dev/null
                set outputDistStarFile   = $dir_viol/$x/$x"_dist_viol".str
                set outputDihedStarFile  = $dir_viol/$x/$x"_dihed_viol".str
                cp -v $outputDistStarFile    .       >& /dev/null
                cp -v $outputDihedStarFile   .       >& /dev/null
            endif

        end
        if ( $overallStatus ) then
            echo "ERROR $x found in doOrganizeForGrid"
            continue
        endif
    endif

    # Insert the files into NMR Restraints Grid.
    if ( $doDumpInGrid ) then
        set log_file         = $dir_db/$x"_loadDB".log
        echo "  gridDump"
#        echo -n "DEBUG: "; date
        java -Xmx500m Wattos.Episode_II.MRInterloop >& $log_file << EOD
l
$dir_db
y
$x
n
EOD
        if ( $status ) then
            echo "ERROR $x failed to dump files to DOCR/FRED"
            continue
        endif
        grep --quiet ERROR $log_file
        if ( ! $status ) then
            echo "ERROR $x found in gridDump log file: $log_file; will now grep for ERROR again."
            grep ERROR $log_file
            continue
        endif
#        echo -n "DEBUG: "; date
    endif

    # Insert the files into the NMR Restraints Grid.
    if ( $doCleanFiles ) then

        # Remove redundant data if all went fine
        \rm -rf $dir_db/DOCR/$x
        \rm -rf $dir_db/FRED/$x
        \rm -rf $dir_link/$x/ccpn
        \rm -rf $ccpn_tmp_dir/data/recoord/$x/linkNmrStarData
        \rm -rf $dir_star/$x/*.str >& /dev/null
        \rm -rf $dir_assign/$x/*_assign.str >& /dev/null
        \rm -rf $dir_surplus/$x/*_nonsurplus.str >& /dev/null
    endif

    echo "  Finished $x"
end

echo "Finished"