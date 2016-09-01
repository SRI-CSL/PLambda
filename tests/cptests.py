#!/usr/bin/env python

# iam: This is needed to stop python from treating 'print' as something special; rather than 
# just a builtin. Wonder how much of this hackery is in our future?
#
from __future__ import print_function

import unittest, os

from Testing import PLambdaTest

from plambda.eval.Globals import pythonGlobals
from plambda.eval.Interpreter import PLambdaException
from plambda.eval.Closure import Closure


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
        self.cpplambdaEqualTest('(== (- (int 3)) (int -3))',  True)
        self.cpplambdaEqualTest('(== (- (int 0) (int 3)) (int -3))',  True)
        self.cpplambdaEqualTest('(< (float 3.1) (int 3))',  False)
        self.cpplambdaEqualTest('(== (apply object) (apply object))',  False)
        self.cpplambdaEqualTest('(if (boolean True) (int 7) (float 11))',  7)
        self.cpplambdaEqualTest('(if (boolean False) (int 7) (float 11))',  11.0)
        self.cpplambdaEqualTest('(if (boolean False) (int 7))',  None)
        self.cpplambdaExceptionTest('(if (int 11) (int 7))',  PLambdaException('11 is not a boolean in conditional @stdin:1'))
        self.cpplambdaEqualTest('(seq (int 666))', 666)
        self.cpplambdaEqualTest('(seq (int 661) (int 662) (int 663) (int 666))', 666)
        self.cpplambdaClassTest('(lambda (x y z) z)', Closure)
        self.cpplambdaEqualTest('(mktuple (int 1) (int 2) (int 3))', (1, 2, 3))
        self.cpplambdaEqualTest('(mklist (int 1) (int 2) (int 3))', [1, 2, 3])
        self.cpplambdaEqualTest('(mkdict "one" (int 1) "two" (int 2) "three" (int 3))', {'one': 1, 'two':2, 'three':3})
        self.cpplambdaEqualTest('(get (mktuple (int 1) (int 2) (int 3)) (int 0))', 1)
        self.cpplambdaEqualTest('(get (mklist (int 1) (int 2) (int 3)) (int 0))', 1)
        self.cpplambdaEqualTest('(get (mkdict "one" (int 1) "two" (int 2) "three" (int 3)) "three")', 3)
        self.cpplambdaEqualTest('(mklist)', [])
        self.cpplambdaEqualTest('(mktuple)', ())
        self.cpplambdaEqualTest('(mkdict)', {})
        self.cpplambdaEqualTest('(and)', True)
        self.cpplambdaEqualTest('(or)', False)
        self.cpplambdaEqualTest('(and (boolean True) (boolean True) (boolean True))', True)
        self.cpplambdaEqualTest('(or (boolean False) (boolean True))', True)
        here = os.getcwd()
        self.cpplambdaEqualTest('(import "sys")', True)
        self.cpplambdaEqualTest('(import "os")', True)
        # have more ways of doing things in plambda than in jlambda
        self.cpplambdaStringEqualTest('(invoke os "getcwd")', here)
        self.cpplambdaStringEqualTest('(apply os.getcwd)', here)
        self.cpplambdaEqualTest('(define foo (int 11))', 'foo')
        
        self.cpplambdaEqualTest('(import "plambda.actors.pyactor")',  True)
        self.cpplambdaStringEqualTest('(define Main plambda.actors.pyactor.Main)',  'Main')
        self.cpplambdaEqualTest('Main.myself',  None)
        self.cpplambdaEqualTest('(seq (apply Main "thenameofmyselfisme") (boolean True))',  True)
        self.cpplambdaEqualTest('(== Main.myself (getattr Main "myself"))', True)
        # examples of tries 'n catches
        self.cpplambdaEqualTest("(try (int 5) (catch e  (int 6) e))", 5)
        self.cpplambdaEqualTest("(try (throw (apply Exception)) (catch e (int 6) (is e e)))", True)
        self.cpplambdaEqualTest("(for x (int 7) x)", 6)
        self.cpplambdaEqualTest("(for x (mklist (int 0) (int 1) (int 2) (int 3) ) x)", 3)
        self.cpplambdaEqualTest('(let ((x0 (int 0)) (x1 (int 1)) (x2 (int 2))) (mklist x0 x1 x2))', [0, 1, 2])
        
        

        
if __name__ == "__main__":
    unittest.main()
