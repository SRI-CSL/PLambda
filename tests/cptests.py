#!/usr/bin/env python

# iam: This is needed to stop python from treating 'print' as something special; rather than 
# just a builtin. Wonder how much of this hackery is in our future?
#
from __future__ import print_function

import unittest, os

from Testing import PLambdaTest

from plambda.eval.Globals import pythonGlobals
from plambda.eval.Interpreter import PLambdaException


class plambdaTest(PLambdaTest):
    """Tests of the plambda language.
    """

    def test_A(self):
        """Simple primitive data tests.
        """
        self.cpplambdaStringEqualTest('"ThisIsAString"', "ThisIsAString")
        self.cpplambdaEqualTest('(int 666)', 666)
        self.cpplambdaEqualTest('(boolean False)', False)
        self.cpplambdaEqualTest('(boolean cow)', False)
        self.cpplambdaEqualTest('(boolean tRuE)', True)
        self.cpplambdaEqualTest('(float 3.1459)',  3.1459)
        self.cpplambdaEqualTest('(float 3.0)',  3)
        self.cpplambdaEqualTest('(== (float 3.0) (int 3))',  True)
        self.cpplambdaEqualTest('(< (float 3.1) (int 3))',  False)
        self.cpplambdaEqualTest('(== (apply object) (apply object))',  False)
        self.cpplambdaEqualTest('(if (boolean True) (int 7) (float 11))',  7)
        self.cpplambdaEqualTest('(if (boolean False) (int 7) (float 11))',  11.0)
        self.cpplambdaEqualTest('(if (boolean False) (int 7))',  None)
        self.cpplambdaExceptionTest('(if (int 11) (int 7))',  PLambdaException('11 is not a boolean in conditional @stdin:1'))


        
if __name__ == "__main__":
    unittest.main()
