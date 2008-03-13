"""
Show a molecule every hour.
"""
__author__    = "$Author$"
___date__     = "$Date$"

import os
# BMRB specific
import jfdutils
src_dir                 = '/export/condor/condor/DOCR_big_tmp_/wi/Proton_Check/all'
#src_dir                 = '/export/condor/condor/DOCR_big_tmp_/wattos/all'
good_entry_list_file    = '/Users/jd/CloneWars/DOCR1000/lists/list_step_1.csv'

# No changes below this line.
##########################################################################

true = 1
false = 0


###############################################################################
## Always nice to have a main:

if __name__ == '__main__':

    good_entry_list = {}
    jfdutils.read_entries( good_entry_list_file, false, good_entry_list)
        
    
    os.chdir(src_dir)
    fileList = os.listdir('.')
    fileList.sort()
    print "DEBUG: Found number of files: ", len(fileList)
    
    for file in fileList:
        #print "DEBUG: Looking at file: " + file
        entryPartF = file[0:4]
        #print "DEBUG: Looking at entryPartF: " + entryPartF
        if ( not good_entry_list.has_key(entryPartF)):
            print "Removing: " + file
            #os.unlink(file)

