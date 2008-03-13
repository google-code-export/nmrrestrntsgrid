import os
urlDB            = 'http://tang.bmrb.wisc.edu/servlet_data/viavia/mr_mysql_backup/'
urlLists         = 'http://tang.bmrb.wisc.edu/wattos/lists/'

big_dir           = '/Users/jd/big'
workspace         = "/Users/jd/workspace"
    
base_dir         = os.path.join(big_dir,'docr','CloneWars','DOCR1000')
projectDirectory = os.path.join(big_dir,'docr','DOCR_big_tmp_','link')

results_dir      = os.path.join(base_dir,'Results')
csh_script_dir   = os.path.join(base_dir,'scripts')

dir_destRep      = os.path.join(workspace, 'all' )
dir_recoordRep   = os.path.join(workspace, 'recoordD' )
dir_ccpnRep      = os.path.join(workspace, 'ccpnD' )

urlDB2 = 'tobeset'

print "Read recoord.localConstants.py version 0.3.1"