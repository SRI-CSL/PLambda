#!/usr/bin/env python

# iam: This is needed to stop python from treating 'print' as something special; rather than 
# just a builtin. Wonder how much of this hackery is in our future?
#
from __future__ import print_function

import unittest, os, sys

from Testing import PLambdaTest

from plambda.eval.Globals import pythonGlobals
from plambda.eval.Interpreter import PLambdaException
from plambda.eval.Closure import Closure


class plambdaTest(PLambdaTest):
    """Tests of the plambda language.
    """


    def test_I(self):
        self.cpplambdaEqualTest('(is (int 4) (int 4))', True)
        self.cpplambdaStringEqualTest('(define I (lambda (x) x))', 'I')
#        self.cpplambdaEqualTest('(is (apply I I) I)', True)
        self.cpplambdaEqualTest('(apply I (int 4))', 4)
        self.cpplambdaEqualTest('(is I I)', True)
#        self.cpplambdaEqualTest('(is (apply (apply I I) (apply I I)) I)', True)
        
        

        
if __name__ == "__main__":
    unittest.main()
