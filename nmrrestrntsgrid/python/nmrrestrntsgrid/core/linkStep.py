from nmrrestrntsgrid.settings.localConstants import ccpn_tmp_dir
from nmrrestrntsgrid.settings.localConstants import dir_link
from nmrrestrntsgrid.settings.localConstants import dir_star
from nmrrestrntsgrid.settings.localConstants import extraFCOptions
from nmrrestrntsgrid.util.NTutils import NTdebug
from nmrrestrntsgrid.util.NTutils import NTerror
from recoord2.pdbe.linkNmrStarData import LinkNmrStarData #@UnresolvedImport
import shutil
import nmrrestrntsgrid
import os
import sys

NTerror("Code is not finished!")
def linkNmrStarData2(x):

    if x != '1brv':
        NTerror("just checking")
        return

    inputStarFile = x + "_join.str"
#    outputStarFile      = os.path.join(dir_star,x,x+"_merge.str")
#    mergeScriptFile     = os.path.join(R,"python/recoord2/pdbe/linkNmrStarData.py")
    fcInputDir = os.path.join(ccpn_tmp_dir, 'data/archives/bmrb/nmrRestrGrid', x)
    inputStarFileFullPath = os.path.join(dir_star, x, inputStarFile)
#    guess_file       = "guessLink.txt"

    os.chdir(dir_link)
    if os.path.exists(x):
        shutil.rmtree(x, 1)

    os.mkdir(x)
    os.chdir(x)

    if not os.path.exists(inputStarFileFullPath):
        NTerror("%s previous step produced no star file" % x)
        return

    if not os.path.exists(fcInputDir):
        os.mkdir(fcInputDir)

    fcInputFile = os.path.join(fcInputDir, 'joinedCoord.str')
    if os.path.exists(fcInputFile):
        os.unlink(fcInputFile)

    os.link(inputStarFileFullPath, fcInputFile) # TODO: check if os.link is appropriate instead of disk.copy(src, path) # us a real copy
    if not os.path.exists(fcInputFile):
        NTerror("%s failed to copy input for FC to: $fcInputDir" % x)
        return

    # Set the right project dir in the script
    # directly.

    # Can be handy for guessing later.
#    cmd = '%s/guessOffSet.csh %s %s' % ( scripts_dir, x, guess_file)
#    ec = ExecuteProgram( cmd )
#    ec.run()

    argv = [ None, x ] + extraFCOptions
    LinkNmrStarData(argv)
    return True

if __name__ == '__main__':

    nmrrestrntsgrid.verbosity = nmrrestrntsgrid.verbosityDebug

    x = '1brv'
    if len(sys.argv) > 1:
        x = sys.argv[1]
    NTdebug("Starting link for entry %s" % x)
    if not linkNmrStarData2(x):
        NTerror("Failed to linkNmrStarData2")