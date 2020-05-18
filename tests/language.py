#!/usr/bin/env python

import unittest
import os


from .Testing import PLambdaTest

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
        self.plambdaEqualTest('(= (float 3.0) (int 3))',  True)
        self.plambdaEqualTest('(== (float 3.0) (int 3))',  False)
        self.plambdaEqualTest('(is (float 3.0) (int 3))',  False)
        self.plambdaEqualTest('(< (float 3.1) (int 3))',  False)
        self.plambdaEqualTest('(<= (float 3.1) (int 3))',  False)
        self.plambdaEqualTest('(>= (float 3.1) (int 3))',  True)
        self.plambdaEqualTest('(< (float 3.1) (int 3))',  False)
        self.plambdaEqualTest('(== (apply object) (apply object))',  False)
        self.plambdaEqualTest('(if (boolean True) (int 7) (float 11))',  7)
        self.plambdaEqualTest('(if (boolean False) (int 7) (float 11))',  11.0)
        self.plambdaEqualTest('(if (boolean False) (int 7))',  None)
        self.plambdaExceptionTest('(if (int 11) (int 7))',  PLambdaException('11 is not a boolean in conditional @stdin:1'))
        self.plambdaExceptionTest('(/ (int 4) (int 0))',  PLambdaException('callTernaryOp / @stdin:1 threw division by zero'))


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
        self.plambdaEqualTest('(define l0 (mklist (int 1) (int 2) (int 3)))', 'l0')
        self.plambdaEqualTest('(in (int 4) l0)', False)
        self.plambdaEqualTest('(in (int 3) l0)', True)
        self.plambdaEqualTest('(mkdict "one" (int 1) "two" (int 2) "three" (int 3))', {'one': 1, 'two':2, 'three':3})
        self.plambdaEqualTest('(define d0 (mkdict "one" (int 1) "two" (int 2) "three" (int 3)))', 'd0')
        self.plambdaEqualTest('(in "two" d0)', True)
        self.plambdaEqualTest('(in "seven" d0)', False)
        self.plambdaEqualTest('(get (mktuple (int 1) (int 2) (int 3)) (int 0))', 1)
        self.plambdaEqualTest('(get (mklist (int 1) (int 2) (int 3)) (int 0))', 1)
        self.plambdaEqualTest('(get (mkdict "one" (int 1) "two" (int 2) "three" (int 3)) "three")', 3)
        self.plambdaEqualTest('(mklist)', [])
        self.plambdaEqualTest('(mktuple)', ())
        self.plambdaEqualTest('(mkdict)', {})


    def test_D(self):
        """Checks the availability of builtin functions.
        We are currently just targeting 3.7. Useful to
        see the edge cases. The clashes are because of our antrl4 parser.
        """
        for key in pythonGlobals:
            value = pythonGlobals[key]
            # clashes
            if key not in ('getattr', 'float', 'int', 'setattr', 'apply', '__loader__', 'dict', 'raw_input', 'input', 'oct', 'list', 'round'):
                #import sys
                #sys.stderr.write(f'{key} {value}\n')
                self.plambdaEqualTest(key, value)
            # the global construct allows you to sidestep the clashes
            self.plambdaEqualTest(f'(global "{key}")', value)

        self.plambdaEqualTest('(apply abs (int -7))', 7)
        self.plambdaEqualTest('(apply any (mklist (boolean False) (boolean false)))', False)
        self.plambdaEqualTest('(apply any (mklist (boolean False) (boolean false) (boolean true)))', True)
        self.plambdaEqualTest('(apply all (mklist (boolean False) (boolean true)))', False)
        self.plambdaEqualTest('(apply all (mklist (boolean true) (boolean true) (boolean true)))', True)
        self.plambdaEqualTest("(apply ascii 'this is not a love song')", "'this is not a love song'")
        self.plambdaEqualTest('(apply bin (int 3))', '0b11')
        self.plambdaEqualTest('(apply bin (int -10))', '-0b1010')
        self.plambdaEqualTest('(apply callable callable)', True)
        self.plambdaEqualTest('(apply complex (int 1) (int 7))', (1+7j))
        self.plambdaEqualTest('(apply abs (apply complex (int 1) (int 7)))', 7.0710678118654755)
        self.plambdaEqualTest('(apply divmod (int 10) (int 3))', (3, 1))
        self.plambdaEqualTest('(apply list (apply enumerate (mklist "zero" "one"  "two"   "three")))', [(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three')])
        self.plambdaEqualTest('(apply eval "1 +  2 * 3")', 7)

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
        self.plambdaEqualTest("(try foo (catch e (int 666)))", 666)
        self.plambdaEqualTest("(try (seq foo) (catch e (int 666)))", 666)


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

    def test_Q(self):
        # string buffer test
        self.plambdaEqualTest('(import "plambda.util.StringBuffer")',  True)
        self.plambdaStringEqualTest('(define StringBuilder plambda.util.StringBuffer.StringBuffer)', 'StringBuilder')
        self.plambdaStringEqualTest('(define sb (apply StringBuilder))', 'sb')
        # take care here, without the seq we will actually implicitly call the str method on sb which will
        # among other things, close it.
        self.plambdaEqualTest('(seq (apply sb.append "a") None)', None)
        self.plambdaEqualTest('(seq (apply sb.append "b") None)', None)
        self.plambdaEqualTest('(seq (apply sb.append "c") None)', None)
        self.plambdaStringEqualTest('sb', "abc")

    def test_R(self):
        # string buffer test
        self.plambdaEqualTest('(import "plambda.util.StringBuffer")',  True)
        self.plambdaStringEqualTest('(define StringBuilder plambda.util.StringBuffer.StringBuffer)', 'StringBuilder')
        self.plambdaStringEqualTest('(define sb (apply StringBuilder))', 'sb')
        # the add method is just like append but returns None instead.
        self.plambdaEqualTest('(invoke sb "add" "a1")', None)
        self.plambdaEqualTest('(invoke sb "add" "b2")', None)
        self.plambdaEqualTest('(invoke sb "add" "c3")', None)
        self.plambdaStringEqualTest('sb', "a1b2c3")



if __name__ == "__main__":
    unittest.main()
