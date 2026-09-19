#!/usr/bin/env -S python -u

import sys
import unittest


class test_stub(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        """
        print("in SetUpClass")

    def test_stub_one(self):
        """
        """
        self.assertEqual(0, 0, "Something wrong with this test...")

    def test_stub_two(self):
        """
        """
        self.assertTrue(True, "Something wrong with this test...")

    def test_stub_three(self):
        """
        """
        self.assertEqual(3, 3, "Something wrong with this test...")

    def test_stub_four(self):
        """
        """
        self.assertEqual(4, 4, "Something wrong with this test...")

if __name__=='__main__':
    unittest.main()


