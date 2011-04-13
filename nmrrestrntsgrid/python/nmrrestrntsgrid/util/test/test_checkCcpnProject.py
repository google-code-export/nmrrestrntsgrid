"""

Unit test execute as:
$dir_nrg_python/nmrrestrntsgrid/util/test/test_checkCcpnProject.py

"""
from nmrrestrntsgrid import nrgDirTestsData
from nmrrestrntsgrid.settings.localConstants import nrg_tmp_dir
from nmrrestrntsgrid.util.NTutils import * #@UnusedWildImport
from nmrrestrntsgrid.util.checkCcpnProject import checkCcpnProject
from nmrrestrntsgrid.util.disk import mkdirs
from nmrrestrntsgrid.util.forkoff import do_cmd
from shutil import rmtree
from unittest import TestCase
import unittest

class AllChecks(TestCase):

#    entryList = "1brv 1lcc_bad".split()
    entryList = "1lcc_bad".split()

    def test_checkCcpnProject(self):

        nrgDirTmpTest = os.path.join( nrg_tmp_dir, getCallerName() )
        mkdirs( nrgDirTmpTest )
        self.failIf(os.chdir(nrgDirTmpTest), msg =
            "Failed to change to test directory for files: " + nrgDirTmpTest)
        inputArchiveDir = os.path.join(nrgDirTestsData, "ccpn")

        for entryId in AllChecks.entryList:
            expectedBad = 'bad' in entryId

            if os.path.exists(entryId):
                NTmessage("Removing previous directory: %s" % entryId)
                rmtree(entryId)

            ccpnFile = os.path.join(inputArchiveDir, entryId + ".tgz")
            self.assertTrue( os.path.exists(ccpnFile))
            do_cmd("tar -xzf " + ccpnFile) # will extract to local dir.
            if os.path.exists('linkNmrStarData'):
                NTmessage("Renaming standard directory linkNmrStarData to entry: %s" % entryId)
                os.rename('linkNmrStarData', entryId)
            ccpnProject = checkCcpnProject( entryId )
            isBad = ccpnProject == None
            self.assertEquals( isBad, expectedBad )

            # end if
        # end for
    # end def
# end class

if __name__ == "__main__":
    unittest.main()