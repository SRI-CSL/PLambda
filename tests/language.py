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
        """Simple primitive data and if tests.
        """
        self.plambdaEqualTest('(int 666)', 666)
        self.plambdaEqualTest('(boolean False)', False)
        self.plambdaEqualTest('(boolean cow)', False)
        self.plambdaEqualTest('(boolean tRuE)', True)
        self.plambdaEqualTest('(float 3.1459)',  3.1459)
        self.plambdaEqualTest('(float 3.0)',  3)
        self.plambdaEqualTest('(float fud)',  0.0)
        self.plambdaEqualTest('(int fud)',  0)
        self.plambdaEqualTest('(boolean fud)',  False)
        self.plambdaEqualTest('(/ (int 4) (int 2))',  2)
        self.plambdaEqualTest('(== (float 3.0) (int 3))',  True)
        self.plambdaEqualTest('(< (float 3.1) (int 3))',  False)
        self.plambdaEqualTest('(< (float 3.1) (int 3))',  False)
        self.plambdaEqualTest('(== (apply object) (apply object))',  False)
        self.plambdaEqualTest('(if (boolean True) (int 7) (float 11))',  7)
        self.plambdaEqualTest('(if (boolean False) (int 7) (float 11))',  11.0)
        self.plambdaEqualTest('(if (boolean False) (int 7))',  None)
        self.plambdaExceptionTest('(if (int 11) (int 7))',  PLambdaException('11 is not a boolean in conditional @stdin:1'))
        self.plambdaExceptionTest('(/ (int 4) (int 0))',  PLambdaException('11 is not a boolean in conditional @stdin:1'))


    def test_B(self):
        """Some tests of the import and global lookup mechanisms.
        """
        self.plambdaEqualTest('(import "plambda.actors.pyactor")',  True)
        self.plambdaStringEqualTest('(define Main plambda.actors.pyactor.Main)',  'Main')
        self.plambdaEqualTest('Main.myself',  None)
        self.plambdaEqualTest('(seq (apply Main "thenameofmyselfisme") (boolean True))',  True)
        self.plambdaEqualTest('(== Main.myself (getattr Main "myself"))', True)

    def test_C(self):
        """Simple tests of the primitive iterative data structures, tuple, list and dict.
        """
        self.plambdaEqualTest('(mktuple (int 1) (int 2) (int 3))', (1, 2, 3))
        self.plambdaEqualTest('(mklist (int 1) (int 2) (int 3))', [1, 2, 3])
        self.plambdaEqualTest('(mkdict "one" (int 1) "two" (int 2) "three" (int 3))', {'one': 1, 'two':2, 'three':3})
        self.plambdaEqualTest('(get (mktuple (int 1) (int 2) (int 3)) (int 0))', 1)
        self.plambdaEqualTest('(get (mklist (int 1) (int 2) (int 3)) (int 0))', 1)
        self.plambdaEqualTest('(get (mkdict "one" (int 1) "two" (int 2) "three" (int 3)) "three")', 3)
        self.plambdaEqualTest('(mklist)', [])
        self.plambdaEqualTest('(mktuple)', ())
        self.plambdaEqualTest('(mkdict)', {})


    def test_D(self):
        """Checks the availability of builtin functions.
        We are currently just targeting 2.7. Useful to
        see the edge cases. The clashes are because of our antrl4 parser. 
        The incantation at the top of this file is for the 'print' one to work. 
        """
        for key, value in pythonGlobals.iteritems():
            # clashes
            if key not in ('getattr', 'float', 'int', 'setattr'):
                self.plambdaEqualTest(key, value)
            # the global construct allows you to sidestep the clashes
            self.plambdaEqualTest('(global "{0}")'.format(key), value)

    

    def test_F(self):
        """Tests using a drone.
        """
        here = os.getcwd()
        self.plambdaEqualTest('(import "sys")', True)
        self.plambdaEqualTest('(import "os")', True)
        # have more ways of doing things in plambda than in jlambda
        self.plambdaStringEqualTest('(invoke os "getcwd")', here)
        self.plambdaStringEqualTest('(apply os.getcwd)', here)
        # make plambda find stuff in the tests directory
        self.plambdaEqualTest('(invoke sys.path "insert" (int 0) (apply os.getcwd))', None)
        self.plambdaEqualTest('(import "tests.drones.simple_drone")', True)
        self.plambdaStringEqualTest('(define SimpleDrone tests.drones.simple_drone.SimpleDrone) ', 'SimpleDrone')
        self.plambdaStringEqualTest('(define drone (apply SimpleDrone "droneZero"))', 'drone')
        self.plambdaEqualTest('drone.name', 'droneZero')
        self.plambdaEqualTest('(invoke drone "initialize" "2" "2" "666")', True)
        self.plambdaEqualTest('drone.x', 2)
        self.plambdaEqualTest('drone.y', 2)
        self.plambdaEqualTest('drone.e', 666)
        self.plambdaEqualTest('(invoke drone "mv" "E")', True)
        self.plambdaEqualTest('drone.x', 3)


    def test_G(self):
        letstr = '(let ((x (int 6)) (y (int 7)) (z (int 11)) (x (int 5))) (+ x ( + y  z)))'
        self.plambdaEqualTest(letstr, 23)
        letstr = '(let ((x (int 666))) (let ((x (int 6)) (y (int 7)) (z (int 11)) (x (int 5))) (+ x ( + y  z))) x )'
        self.plambdaEqualTest(letstr, 666)
        self.plambdaEqualTest('(let ((x (apply object)) (y x)) (is x y))', True) 
        self.plambdaEqualTest('(let ((x0 (int 0)) (x1 (int 1)) (x2 (int 2))) (mklist x0 x1 x2))', [0, 1, 2])
        
    def test_H(self):
        self.plambdaStringEqualTest('(define obj (apply object))', 'obj')
        self.plambdaEqualTest('(setuid obj "adefaultuid")', True)
        self.plambdaEqualTest('(is (fetch "adefaultuid") obj)', True) 
        self.plambdaEqualTest('(is (fetch (getuid obj)) obj)', True) 
        self.plambdaEqualTest('(setuid obj None)', True)
        self.plambdaEqualTest('(fetch "adefaultuid")', None)

    def test_I(self):
        self.plambdaStringEqualTest('(define I (lambda (x) x))', 'I')
        self.plambdaEqualTest('(is (apply I I) I)', True)
        self.plambdaEqualTest('(is (apply (apply I I) (apply I I)) I)', True)


    def test_J(self):
        self.plambdaEqualTest('(import "sys")', True)
        self.plambdaEqualTest('(import "os")', True)
        # make plambda find stuff in the tests directory
        self.plambdaEqualTest('(invoke sys.path "insert" (int 0) (apply os.getcwd))', None)
        self.plambdaEqualTest('(import "tests.kwargs")', True)
        self.plambdaStringEqualTest('(define kwargs tests.kwargs.kwargs)', 'kwargs')
        self.plambdaStringEqualTest('(define l0 (mklist (int 1) (int 2) (int 3)))', 'l0')
        self.plambdaStringEqualTest('(define d0 (mkdict "one" (int 1) "two" (int 2) "three" (int 3)))', 'd0')
        self.plambdaStringEqualTest('(kwapply kwargs l0 d0)', '(1, 2, 3) {one: 1, three: 3, two: 2}')

    def test_K(self):
        self.plambdaStringEqualTest('(define l0 (mklist (int 1) (int 2) (int 3)))', 'l0')
        self.plambdaStringEqualTest('(define d0 (mkdict "one" (int 1) "two" (int 2) "three" (int 3)))', 'd0')
        self.plambdaEqualTest('(modify l0 (int 0) "T")', None)
        self.plambdaStringEqualTest('(get l0 (int 0))', "T")
        self.plambdaEqualTest('(modify d0 "two" "T")', None)
        self.plambdaStringEqualTest('(get d0 "two")', "T")

    def test_L(self):
        self.plambdaEqualTest('(isnone None)', True)
        self.plambdaEqualTest('(isnone "str")', False)
        self.plambdaEqualTest('(isobject "str")', True)
        self.plambdaEqualTest('(isobject None)', False)
        self.plambdaEqualTest('(isobject (int 4))', True)
        self.plambdaEqualTest('(isint (int 4))', True)
        self.plambdaEqualTest('(isint (float 4))', False)
        self.plambdaEqualTest('(isfloat (int 4))', False)
        self.plambdaEqualTest('(isfloat (float 4))', True)


    def test_M(self):
        # hard to read but ...
        self.plambdaStringEqualTest('"23"', "23")
        self.plambdaStringEqualTest("'23'", "23")
        self.plambdaStringEqualTest("'\"'", '"')     # the backslash is for python not plambda
        self.plambdaStringEqualTest('"\'"', "'")     # the backslash is for python not plambda
        self.plambdaStringEqualTest('"\\\\"', "\\")  # the backslash is for python not plambda
        self.plambdaStringEqualTest("'\\\\'", "\\")  # the backslash is for python not plambda

    def test_N(self):
        # examples of how to circumnavigate name clashes
        self.plambdaEqualTest("(apply isinstance (int 21) (global 'int'))", True)
        self.plambdaEqualTest("(apply isinstance (float 21) (global 'float'))", True)


    def test_O(self):
        # examples of tries 'n catches
        self.plambdaEqualTest("(try (int 5) (catch e  (int 6) e))", 5)
        self.plambdaEqualTest("(try (throw (apply Exception)) (catch e  (is e e)))", True)
        self.plambdaEqualTest("(for x (int 7) x)", 6)
        self.plambdaEqualTest("(for x (mklist (int 0) (int 1) (int 2) (int 3) ) x)", 3)

    def test_P(self):
        fact = """
(define fact (n)
  (if (is n (int 0))
      (int 1)
    (* n (apply fact (- n (int 1))))))
        """
        self.plambdaStringEqualTest(fact, 'fact')
        self.plambdaEqualTest('(apply fact (int 10))', 3628800)
        self.plambdaEqualTest('(apply fact (int 15))', 1307674368000)
        self.plambdaEqualTest('(apply fact (int 20))', 2432902008176640000)
        self.plambdaEqualTest('(apply fact (int 30))', 265252859812191058636308480000000)
        self.plambdaEqualTest('(apply fact (int 40))', 815915283247897734345611269596115894272000000000)
        

if __name__ == "__main__":
    unittest.main()



