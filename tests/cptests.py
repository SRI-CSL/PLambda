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
        """Simple primitive data and if tests.
        """
        self.cps_plambdaEqualTest('(int 666)', 666)
        self.cps_plambdaEqualTest('(boolean False)', False)
        self.cps_plambdaEqualTest('(boolean cow)', False)
        self.cps_plambdaEqualTest('(boolean tRuE)', True)
        self.cps_plambdaEqualTest('(float 3.1459)',  3.1459)
        self.cps_plambdaEqualTest('(float 3.0)',  3)
        self.cps_plambdaEqualTest('(== (float 3.0) (int 3))',  True)
        self.cps_plambdaEqualTest('(< (float 3.1) (int 3))',  False)
        self.cps_plambdaEqualTest('(== (apply object) (apply object))',  False)
        self.cps_plambdaEqualTest('(if (boolean True) (int 7) (float 11))',  7)
        self.cps_plambdaEqualTest('(if (boolean False) (int 7) (float 11))',  11.0)
        self.cps_plambdaEqualTest('(if (boolean False) (int 7))',  None)
        self.cps_plambdaExceptionTest('(if (int 11) (int 7))',  PLambdaException('11 is not a boolean in conditional @stdin:1'))

    def test_B(self):
        """Some tests of the import and global lookup mechanisms.
        """
        self.cps_plambdaEqualTest('(import "plambda.actors.pyactor")',  True)
        self.cps_plambdaStringEqualTest('(define Main plambda.actors.pyactor.Main)',  'Main')
        self.cps_plambdaEqualTest('Main.myself',  None)
        self.cps_plambdaEqualTest('(seq (apply Main "thenameofmyselfisme") (boolean True))',  True)
        self.cps_plambdaEqualTest('(== Main.myself (getattr Main "myself"))', True)

    def test_C(self):
        """Simple tests of the primitive iterative data structures, tuple, list and dict.
        """
        self.cps_plambdaEqualTest('(mktuple (int 1) (int 2) (int 3))', (1, 2, 3))
        self.cps_plambdaEqualTest('(mklist (int 1) (int 2) (int 3))', [1, 2, 3])
        self.cps_plambdaEqualTest('(mkdict "one" (int 1) "two" (int 2) "three" (int 3))', {'one': 1, 'two':2, 'three':3})
        self.cps_plambdaEqualTest('(get (mktuple (int 1) (int 2) (int 3)) (int 0))', 1)
        self.cps_plambdaEqualTest('(get (mklist (int 1) (int 2) (int 3)) (int 0))', 1)
        self.cps_plambdaEqualTest('(get (mkdict "one" (int 1) "two" (int 2) "three" (int 3)) "three")', 3)
        self.cps_plambdaEqualTest('(mklist)', [])
        self.cps_plambdaEqualTest('(mktuple)', ())
        self.cps_plambdaEqualTest('(mkdict)', {})


    def test_D(self):
        """Checks the availability of builtin functions.
        We are currently just targeting 2.7. Useful to
        see the edge cases. The clashes are because of our antrl4 parser. 
        The incantation at the top of this file is for the 'print' one to work. 
        """
        for key, value in pythonGlobals.iteritems():
            # clashes
            if key not in ('getattr', 'float', 'int', 'setattr'):
                self.cps_plambdaEqualTest(key, value)
            # the global construct allows you to sidestep the clashes
            self.cps_plambdaEqualTest('(global "{0}")'.format(key), value)

    

    def test_F(self):
        """Tests using a drone.
        """
        here = os.getcwd()
        self.cps_plambdaEqualTest('(import "sys")', True)
        self.cps_plambdaEqualTest('(import "os")', True)
        # have more ways of doing things in plambda than in jlambda
        self.cps_plambdaStringEqualTest('(invoke os "getcwd")', here)
        self.cps_plambdaStringEqualTest('(apply os.getcwd)', here)
        # make plambda find stuff in the tests directory
        self.cps_plambdaEqualTest('(invoke sys.path "insert" (int 0) (apply os.getcwd))', None)
        self.cps_plambdaEqualTest('(import "tests.drones.simple_drone")', True)
        self.cps_plambdaStringEqualTest('(define SimpleDrone tests.drones.simple_drone.SimpleDrone) ', 'SimpleDrone')
        self.cps_plambdaStringEqualTest('(define drone (apply SimpleDrone "droneZero"))', 'drone')
        self.cps_plambdaEqualTest('drone.name', 'droneZero')
        self.cps_plambdaEqualTest('(invoke drone "initialize" "2" "2" "666")', True)
        self.cps_plambdaEqualTest('drone.x', 2)
        self.cps_plambdaEqualTest('drone.y', 2)
        self.cps_plambdaEqualTest('drone.e', 666)
        self.cps_plambdaEqualTest('(invoke drone "mv" "E")', True)
        self.cps_plambdaEqualTest('drone.x', 3)


    def test_G(self):
        letstr = '(let ((x (int 6)) (y (int 7)) (z (int 11)) (x (int 5))) (+ x ( + y  z)))'
        self.cps_plambdaEqualTest(letstr, 23)
        letstr = '(let ((x (int 666))) (let ((x (int 6)) (y (int 7)) (z (int 11)) (x (int 5))) (+ x ( + y  z))) x )'
        self.cps_plambdaEqualTest(letstr, 666)
        self.cps_plambdaEqualTest('(let ((x (apply object)) (y x)) (is x y))', True) 
        self.cps_plambdaEqualTest('(let ((x0 (int 0)) (x1 (int 1)) (x2 (int 2))) (mklist x0 x1 x2))', [0, 1, 2])
        
    def test_H(self):
        self.cps_plambdaStringEqualTest('(define obj (apply object))', 'obj')
        self.cps_plambdaEqualTest('(setuid obj "adefaultuid")', True)
        self.cps_plambdaEqualTest('(is (fetch "adefaultuid") obj)', True) 
        self.cps_plambdaEqualTest('(is (fetch (getuid obj)) obj)', True) 
        self.cps_plambdaEqualTest('(setuid obj None)', True)
        self.cps_plambdaEqualTest('(fetch "adefaultuid")', None)

    def test_I(self):
        self.cps_plambdaEqualTest('(is (int 4) (int 4))', True)
        self.cps_plambdaStringEqualTest('(define I (lambda (x) x))', 'I')
        self.cps_plambdaEqualTest('(is (apply I I) I)', True)
        self.cps_plambdaEqualTest('(apply I (int 4))', 4)
        self.cps_plambdaEqualTest('(is I I)', True)
        self.cps_plambdaEqualTest('(is (apply (apply I I) (apply I I)) I)', True)


    def test_J(self):
        self.cps_plambdaEqualTest('(import "sys")', True)
        self.cps_plambdaEqualTest('(import "os")', True)
        # make plambda find stuff in the tests directory
        self.cps_plambdaEqualTest('(invoke sys.path "insert" (int 0) (apply os.getcwd))', None)
        self.cps_plambdaEqualTest('(import "tests.kwargs")', True)
        self.cps_plambdaStringEqualTest('(define kwargs tests.kwargs.kwargs)', 'kwargs')
        self.cps_plambdaStringEqualTest('(define l0 (mklist (int 1) (int 2) (int 3)))', 'l0')
        self.cps_plambdaStringEqualTest('(define d0 (mkdict "one" (int 1) "two" (int 2) "three" (int 3)))', 'd0')
        self.cps_plambdaStringEqualTest('(kwapply kwargs l0 d0)', '(1, 2, 3) {one: 1, three: 3, two: 2}')

    def test_K(self):
        self.cps_plambdaStringEqualTest('(define l0 (mklist (int 1) (int 2) (int 3)))', 'l0')
        self.cps_plambdaStringEqualTest('(define d0 (mkdict "one" (int 1) "two" (int 2) "three" (int 3)))', 'd0')
        self.cps_plambdaEqualTest('(modify l0 (int 0) "T")', None)
        self.cps_plambdaStringEqualTest('(get l0 (int 0))', "T")
        self.cps_plambdaEqualTest('(modify d0 "two" "T")', None)
        self.cps_plambdaStringEqualTest('(get d0 "two")', "T")

    def test_L(self):
        self.cps_plambdaEqualTest('(isnone None)', True)
        self.cps_plambdaEqualTest('(isnone "str")', False)
        self.cps_plambdaEqualTest('(isobject "str")', True)
        self.cps_plambdaEqualTest('(isobject None)', False)
        self.cps_plambdaEqualTest('(isobject (int 4))', True)
        self.cps_plambdaEqualTest('(isint (int 4))', True)
        self.cps_plambdaEqualTest('(isint (float 4))', False)
        self.cps_plambdaEqualTest('(isfloat (int 4))', False)
        self.cps_plambdaEqualTest('(isfloat (float 4))', True)


    def test_M(self):
        # hard to read but ...
        self.cps_plambdaStringEqualTest('"23"', "23")
        self.cps_plambdaStringEqualTest("'23'", "23")
        self.cps_plambdaStringEqualTest("'\"'", '"')     # the backslash is for python not plambda
        self.cps_plambdaStringEqualTest('"\'"', "'")     # the backslash is for python not plambda
        self.cps_plambdaStringEqualTest('"\\\\"', "\\")  # the backslash is for python not plambda
        self.cps_plambdaStringEqualTest("'\\\\'", "\\")  # the backslash is for python not plambda

    def test_N(self):
        # examples of how to circumnavigate name clashes
        self.cps_plambdaEqualTest("(apply isinstance (int 21) (global 'int'))", True)
        self.cps_plambdaEqualTest("(apply isinstance (float 21) (global 'float'))", True)


    def test_O(self):
        # examples of tries 'n catches
        self.cps_plambdaEqualTest("(try (int 5) (catch e  (int 6) e))", 5)
        self.cps_plambdaEqualTest("(try (throw (apply Exception)) (catch e  (is e e)))", True)
        self.cps_plambdaEqualTest("(for x (int 7) x)", 6)
        self.cps_plambdaEqualTest("(for x (mklist (int 0) (int 1) (int 2) (int 3) ) x)", 3)
        self.cps_plambdaEqualTest("(import 'sys')", True)
        self.cps_plambdaEqualTest("sys.path", sys.path)
        
    def test_P(self):
        fact = """
(define fact (n)
  (if (is n (int 0))
      (int 1)
    (* n (apply fact (- n (int 1))))))
        """
        self.cps_plambdaStringEqualTest(fact, 'fact')
        self.cps_plambdaEqualTest('(apply fact (int 10))', 3628800)
        self.cps_plambdaEqualTest('(apply fact (int 15))', 1307674368000)
        self.cps_plambdaEqualTest('(apply fact (int 20))', 2432902008176640000)
        self.cps_plambdaEqualTest('(apply fact (int 30))', 265252859812191058636308480000000)
        self.cps_plambdaEqualTest('(apply fact (int 40))', 815915283247897734345611269596115894272000000000)
        

        
if __name__ == "__main__":
    unittest.main()
