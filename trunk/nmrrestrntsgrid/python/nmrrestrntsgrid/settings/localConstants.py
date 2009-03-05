from nmrrestrntsgrid.util.NTutils import NTdebug
from nmrrestrntsgrid.util.NTutils import NTmessage
import os


# Needs to map exactly to settings.csh

user_dir = os.getenv('UJ')
ccpn_tmp_dir = os.getenv('ccpn_tmp_dir')
scripts_dir = os.getenv('scripts_dir')
WS = os.path.join(user_dir, 'workspace34')
R = os.path.join(WS, 'recoord')
big_dir = os.path.join(user_dir, 'NRG')
results_dir = os.path.join(big_dir, 'Results')
dir_link = os.path.join(big_dir, 'link')
dir_star = os.path.join(big_dir, 'star')
ccpn_tmp_dir = os.path.join(user_dir,'ccpn_tmp')

urlDB2 = None

extraFCOptions = ['-raise','-force','-noGui']

NTdebug("using user_dir: [%s] " % user_dir)
NTdebug("using dir_link: [%s] " % dir_link)
NTmessage("Read nmrresrntsgrid.settings.localConstants.py version 0.4")