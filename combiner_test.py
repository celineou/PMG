from cgitb import reset
from linecache import getline
import unittest
from csv_combiner import CSVCombiner
import pandas as pd

class testCases(unittest.TestCase):
    def test_checkFile2(self):
        file="./fixtures/empty.csv"
        result = CSVCombiner().checkFile(file)
        self.assertFalse(result)

    def test_checkFile3(self):
        file="./filedoesnotexist.csv"
        result = CSVCombiner().checkFile(file)
        self.assertFalse(result)

    def test_checkFile4(self):
        file="./fixtures/clothing.csv"
        result = CSVCombiner().checkFile(file)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
