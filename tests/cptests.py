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
        
        # examples of tries 'n catches
        self.cpplambdaEqualTest("(try (int 5) (catch e  (int 6) e))", 5)
        self.cpplambdaEqualTest("(try (throw (apply Exception)) (catch e (int 6) (is e e)))", True)
        self.cpplambdaEqualTest("(for x (int 7) x)", 6)
        self.cpplambdaEqualTest("(for x (mklist (int 0) (int 1) (int 2) (int 3) ) x)", 3)
        self.cpplambdaEqualTest('(let ((x0 (int 0)) (x1 (int 1)) (x2 (int 2))) (mklist x0 x1 x2))', [0, 1, 2])

    def test_B(self):
        """Some tests of the import and global lookup mechanisms.
        """
        self.cpplambdaEqualTest('(import "plambda.actors.pyactor")',  True)
        self.cpplambdaStringEqualTest('(define Main plambda.actors.pyactor.Main)',  'Main')
        self.cpplambdaEqualTest('Main.myself',  None)
        self.cpplambdaEqualTest('(seq (apply Main "thenameofmyselfisme") (boolean True))',  True)
        self.cpplambdaEqualTest('(== Main.myself (getattr Main "myself"))', True)

    def test_C(self):
        """Simple tests of the primitive iterative data structures, tuple, list and dict.
        """
        self.cpplambdaEqualTest('(mktuple (int 1) (int 2) (int 3))', (1, 2, 3))
        self.cpplambdaEqualTest('(mklist (int 1) (int 2) (int 3))', [1, 2, 3])
        self.cpplambdaEqualTest('(mkdict "one" (int 1) "two" (int 2) "three" (int 3))', {'one': 1, 'two':2, 'three':3})
        self.cpplambdaEqualTest('(get (mktuple (int 1) (int 2) (int 3)) (int 0))', 1)
        self.cpplambdaEqualTest('(get (mklist (int 1) (int 2) (int 3)) (int 0))', 1)
        self.cpplambdaEqualTest('(get (mkdict "one" (int 1) "two" (int 2) "three" (int 3)) "three")', 3)
        self.cpplambdaEqualTest('(mklist)', [])
        self.cpplambdaEqualTest('(mktuple)', ())
        self.cpplambdaEqualTest('(mkdict)', {})


    def test_D(self):
        """Checks the availability of builtin functions.
        We are currently just targeting 2.7. Useful to
        see the edge cases. The clashes are because of our antrl4 parser. 
        The incantation at the top of this file is for the 'print' one to work. 
        """
        for key, value in pythonGlobals.iteritems():
            # clashes
            if key not in ('getattr', 'float', 'int', 'setattr'):
                self.cpplambdaEqualTest(key, value)
            # the global construct allows you to sidestep the clashes
            self.cpplambdaEqualTest('(global "{0}")'.format(key), value)

    

    def test_F(self):
        """Tests using a drone.
        """
        here = os.getcwd()
        self.cpplambdaEqualTest('(import "sys")', True)
        self.cpplambdaEqualTest('(import "os")', True)
        # have more ways of doing things in plambda than in jlambda
        self.cpplambdaStringEqualTest('(invoke os "getcwd")', here)
        self.cpplambdaStringEqualTest('(apply os.getcwd)', here)
        # make plambda find stuff in the tests directory
        self.cpplambdaEqualTest('(invoke sys.path "insert" (int 0) (apply os.getcwd))', None)
        self.cpplambdaEqualTest('(import "tests.drones.simple_drone")', True)
        self.cpplambdaStringEqualTest('(define SimpleDrone tests.drones.simple_drone.SimpleDrone) ', 'SimpleDrone')
        self.cpplambdaStringEqualTest('(define drone (apply SimpleDrone "droneZero"))', 'drone')
        self.cpplambdaEqualTest('drone.name', 'droneZero')
        self.cpplambdaEqualTest('(invoke drone "initialize" "2" "2" "666")', True)
        self.cpplambdaEqualTest('drone.x', 2)
        self.cpplambdaEqualTest('drone.y', 2)
        self.cpplambdaEqualTest('drone.e', 666)
        self.cpplambdaEqualTest('(invoke drone "mv" "E")', True)
        self.cpplambdaEqualTest('drone.x', 3)


    def test_G(self):
        letstr = '(let ((x (int 6)) (y (int 7)) (z (int 11)) (x (int 5))) (+ x ( + y  z)))'
        self.cpplambdaEqualTest(letstr, 23)
        letstr = '(let ((x (int 666))) (let ((x (int 6)) (y (int 7)) (z (int 11)) (x (int 5))) (+ x ( + y  z))) x )'
        self.cpplambdaEqualTest(letstr, 666)
        self.cpplambdaEqualTest('(let ((x (apply object)) (y x)) (is x y))', True) 
        self.cpplambdaEqualTest('(let ((x0 (int 0)) (x1 (int 1)) (x2 (int 2))) (mklist x0 x1 x2))', [0, 1, 2])
        
    def test_H(self):
        self.cpplambdaStringEqualTest('(define obj (apply object))', 'obj')
        self.cpplambdaEqualTest('(setuid obj "adefaultuid")', True)
        self.cpplambdaEqualTest('(is (fetch "adefaultuid") obj)', True) 
        self.cpplambdaEqualTest('(is (fetch (getuid obj)) obj)', True) 
        self.cpplambdaEqualTest('(setuid obj None)', True)
        self.cpplambdaEqualTest('(fetch "adefaultuid")', None)

    def test_I(self):
        self.cpplambdaEqualTest('(is (int 4) (int 4))', True)
        self.cpplambdaStringEqualTest('(define I (lambda (x) x))', 'I')
        self.cpplambdaEqualTest('(is (apply I I) I)', True)
        self.cpplambdaEqualTest('(apply I (int 4))', 4)
        self.cpplambdaEqualTest('(is I I)', True)
        self.cpplambdaEqualTest('(is (apply (apply I I) (apply I I)) I)', True)


    def test_J(self):
        self.cpplambdaEqualTest('(import "sys")', True)
        self.cpplambdaEqualTest('(import "os")', True)
        # make plambda find stuff in the tests directory
        self.cpplambdaEqualTest('(invoke sys.path "insert" (int 0) (apply os.getcwd))', None)
        self.cpplambdaEqualTest('(import "tests.kwargs")', True)
        self.cpplambdaStringEqualTest('(define kwargs tests.kwargs.kwargs)', 'kwargs')
        self.cpplambdaStringEqualTest('(define l0 (mklist (int 1) (int 2) (int 3)))', 'l0')
        self.cpplambdaStringEqualTest('(define d0 (mkdict "one" (int 1) "two" (int 2) "three" (int 3)))', 'd0')
        self.cpplambdaStringEqualTest('(kwapply kwargs l0 d0)', '(1, 2, 3) {one: 1, three: 3, two: 2}')

    def test_K(self):
        self.cpplambdaStringEqualTest('(define l0 (mklist (int 1) (int 2) (int 3)))', 'l0')
        self.cpplambdaStringEqualTest('(define d0 (mkdict "one" (int 1) "two" (int 2) "three" (int 3)))', 'd0')
        self.cpplambdaEqualTest('(modify l0 (int 0) "T")', None)
        self.cpplambdaStringEqualTest('(get l0 (int 0))', "T")
        self.cpplambdaEqualTest('(modify d0 "two" "T")', None)
        self.cpplambdaStringEqualTest('(get d0 "two")', "T")

    def test_L(self):
        self.cpplambdaEqualTest('(isnone None)', True)
        self.cpplambdaEqualTest('(isnone "str")', False)
        self.cpplambdaEqualTest('(isobject "str")', True)
        self.cpplambdaEqualTest('(isobject None)', False)
        self.cpplambdaEqualTest('(isobject (int 4))', True)
        self.cpplambdaEqualTest('(isint (int 4))', True)
        self.cpplambdaEqualTest('(isint (float 4))', False)
        self.cpplambdaEqualTest('(isfloat (int 4))', False)
        self.cpplambdaEqualTest('(isfloat (float 4))', True)


    def test_M(self):
        # hard to read but ...
        self.cpplambdaStringEqualTest('"23"', "23")
        self.cpplambdaStringEqualTest("'23'", "23")
        self.cpplambdaStringEqualTest("'\"'", '"')     # the backslash is for python not plambda
        self.cpplambdaStringEqualTest('"\'"', "'")     # the backslash is for python not plambda
        self.cpplambdaStringEqualTest('"\\\\"', "\\")  # the backslash is for python not plambda
        self.cpplambdaStringEqualTest("'\\\\'", "\\")  # the backslash is for python not plambda

    def test_N(self):
        # examples of how to circumnavigate name clashes
        self.cpplambdaEqualTest("(apply isinstance (int 21) (global 'int'))", True)
        self.cpplambdaEqualTest("(apply isinstance (float 21) (global 'float'))", True)


    def test_O(self):
        # examples of tries 'n catches
        self.cpplambdaEqualTest("(try (int 5) (catch e  (int 6) e))", 5)
        self.cpplambdaEqualTest("(try (throw (apply Exception)) (catch e  (is e e)))", True)
        self.cpplambdaEqualTest("(for x (int 7) x)", 6)
        self.cpplambdaEqualTest("(for x (mklist (int 0) (int 1) (int 2) (int 3) ) x)", 3)
        self.cpplambdaEqualTest("(import 'sys')", True)
        self.cpplambdaEqualTest("sys.path", sys.path)
        
    def test_P(self):
        fact = """
(define fact (n)
  (if (is n (int 0))
      (int 1)
    (* n (apply fact (- n (int 1))))))
        """
        self.cpplambdaStringEqualTest(fact, 'fact')
        self.cpplambdaEqualTest('(apply fact (int 10))', 3628800)
        self.cpplambdaEqualTest('(apply fact (int 15))', 1307674368000)
        self.cpplambdaEqualTest('(apply fact (int 20))', 2432902008176640000)
        self.cpplambdaEqualTest('(apply fact (int 30))', 265252859812191058636308480000000)
        self.cpplambdaEqualTest('(apply fact (int 40))', 815915283247897734345611269596115894272000000000)
        

        
if __name__ == "__main__":
    unittest.main()
