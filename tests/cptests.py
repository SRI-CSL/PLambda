#!/usr/bin/env python

# iam: This is needed to stop python from treating 'print' as something special; rather than 
# just a builtin. Wonder how much of this hackery is in our future?
#
from __future__ import print_function

import unittest, os

from Testing import PLambdaTest

from plambda.eval.Globals import pythonGlobals


class plambdaTest(PLambdaTest):
    """Tests of the plambda language.
    """

    def test_A(self):
        """Simple primitive data tests.
        """
        self.cpplambdaEqualTest('(int 666)', 666)
        self.plambdaEqualTest('(boolean False)', False)
        self.plambdaEqualTest('(boolean cow)', False)
        self.plambdaEqualTest('(boolean tRuE)', True)
        self.plambdaEqualTest('(float 3.1459)',  3.1459)
        self.plambdaEqualTest('(float 3.0)',  3)
        self.plambdaEqualTest('(== (float 3.0) (int 3))',  True)
        self.plambdaEqualTest('(< (float 3.1) (int 3))',  False)
        self.plambdaEqualTest('(== (apply object) (apply object))',  False)


        
if __name__ == "__main__":
    unittest.main()
