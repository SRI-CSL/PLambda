#!/usr/bin/env python

import unittest

from plam.visitor.Parser import parseFromString
from plam.plambda.Interpreter import Interpreter
from plam.plambda.PLambdaException import PLambdaException

from Testing import PLambdaTest


class plambdaTest(PLambdaTest):
    """Tests of the plambda language.
    """

    def test_A(self):
        """Simple primitive data tests.
        """
        self.plambdaEqualTest('(int 666)', 666)
        self.plambdaEqualTest('(boolean False)', False)
        self.plambdaEqualTest('(boolean cow)', False)
        self.plambdaEqualTest('(boolean tRuE)', True)
        self.plambdaEqualTest('(float 3.1459)',  3.1459)
        self.plambdaEqualTest('(float 3.0)',  3)
        self.plambdaEqualTest('(== (float 3.0) (int 3))',  True)

    def test_B(self):
        self.plambdaEqualTest('(import "plam.actors.pyactor")',  True)
        self.plambdaStringEqualTest('(define Main plam.actors.pyactor.Main)',  'Main')
        self.plambdaEqualTest('Main.myself',  None)
        self.plambdaEqualTest('(seq (apply Main "thenameofmyselfisme") (boolean True))',  True)
        self.plambdaEqualTest('(== Main.myself (getattr Main "myself"))', True)

    def test_C(self):
        """Simple tests of the primitive data structures, tuple, list and dict.
        """
        self.plambdaEqualTest('(mktuple (int 1) (int 2) (int 3))', (1, 2, 3))
        self.plambdaEqualTest('(mklist (int 1) (int 2) (int 3))', [1, 2, 3])
        self.plambdaEqualTest('(mkdict "one" (int 1) "two" (int 2) "three" (int 3))', {'one': 1, 'two':2, 'three':3})
        self.plambdaEqualTest('(get (mktuple (int 1) (int 2) (int 3)) (int 0))', 1)
        self.plambdaEqualTest('(get (mklist (int 1) (int 2) (int 3)) (int 0))', 1)
        self.plambdaEqualTest('(get (mkdict "one" (int 1) "two" (int 2) "three" (int 3)) "three")', 3)


        
if __name__ == "__main__":
    unittest.main()
