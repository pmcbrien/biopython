# Copyright 2013 Lenna X. Peterson. All rights reserved.
#
# This code is part of the Biopython distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

"""Unit test for Bio.PDB.DSSP which need the binary tool.

See also test_PDB.py for dependency free DSSP tests.
"""

import subprocess
import unittest


from Bio import MissingExternalDependencyError
from Bio.PDB import PDBParser
from Bio.PDB import DSSP

# Check if DSSP is installed
try:
    subprocess.check_call(["dssp", "-h"])
except OSError:
    raise MissingExternalDependencyError(
        "Install dssp if you want to use it from Biopython.")


class DSSP_test(unittest.TestCase):
    """Test DSSP module"""

    def test_DSSP(self):
        """Test DSSP generation from PDB"""
        p = PDBParser()
        pdbfile = "PDB/2BEG.pdb"
        model = p.get_structure("2BEG", pdbfile)[0]
        dssp = DSSP(model, pdbfile)
        self.assertEqual(len(dssp), 130)


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)