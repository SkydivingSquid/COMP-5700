import unittest
import sbom.info as sbom

class SbomTest(unittest.TestCase):

    def test_sbom_010_shouldReturnDeveloperName(self):
        myName = 'umphrda'
        self.assertIn(myName, sbom.info())