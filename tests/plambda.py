#!/usr/bin/env python

import unittest

from plam.visitor.Parser import parseFromString
from plam.plambda.Interpreter import Interpreter
from plam.plambda.PLambdaException import PLambdaException

from Testing import PLambdaTest


class plambdaTest(PLambdaTest):
    """Tests of the plambda language.
    """

    def testOne(self):
        self.plambdaEqualTest('(int 666)', 666)
        
    def testTwo(self):
        self.plambdaEqualTest('(boolean False)', False)
        
    def testThree(self):
        self.plambdaEqualTest('(float 3.1459)',  3.1459)

    def testFour(self):
        self.plambdaEqualTest('(import "plam.actors.pyactor")',  True)
        self.plambdaStringEqualTest('(define Main plam.actors.pyactor.Main)',  'Main')
        self.plambdaEqualTest('Main.myself',  None)
        self.plambdaEqualTest('(seq (apply Main "thenameofmyselfisme") (boolean True))',  True)
        self.plambdaEqualTest('(== Main.myself (getattr Main "myself"))', True)
       


        
if __name__ == "__main__":
    unittest.main()
