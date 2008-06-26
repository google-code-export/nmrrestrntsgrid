import os


# Needs to map exactly to settings.csh 

user_dir         = os.getenv('UJ')
ccpn_tmp_dir     = os.getenv('ccpn_tmp_dir')
scripts_dir      = os.getenv('scripts_dir')
workspace        = os.path.join(user_dir,'workspace')
big_dir          = os.path.join(user_dir,'NRG')
results_dir      = os.path.join(big_dir,'Results')
    
urlDB2 = None

print "DEBUG: using user_dir: [%s] " % user_dir
print "Read nmrresrntsgrid.settings.localConstants.py version 0.3.1"