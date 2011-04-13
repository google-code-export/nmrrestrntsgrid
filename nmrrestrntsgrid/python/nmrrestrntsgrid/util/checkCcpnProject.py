# Execute like e.g.:
# python -u $dir_nrg_python/nmrrestrntsgrid/util/checkCcpnProject.py ccpnPath

from memops.api.Implementation import ApiError
from memops.general.Io import loadProject
from nmrrestrntsgrid.util.NTutils import * #@UnusedWildImport

def checkCcpnProject( ccpnFile ):
    "Return None on error"
    ccpnProject = loadProject(ccpnFile, showWarning = None)
    try:
        ccpnProject.checkAllValid()
    except ApiError:
        NTtracebackWarning()
        NTwarning("Failed ccpnProject.checkAllValid which can be normal.")
        ccpnProject = None
    return ccpnProject

def printWarning(title, message):
    pass

if __name__ == '__main__':
    ccpnProject = checkCcpnProject( sys.argv[1] )
    if ccpnProject == None:
        sys.exit(1)