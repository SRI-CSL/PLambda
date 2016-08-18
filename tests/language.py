#!/usr/bin/env python

# iam: This is needed to stop python from treating 'print' as something special; rather than 
# just a builtin. Wonder how much of this hackery is in our future?
#
from __future__ import print_function

import unittest

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
        self.plambdaEqualTest('(< (float 3.1) (int 3))',  False)
        self.plambdaEqualTest('(== (apply object) (apply object))',  False)

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
        see the edge cases. The commented out cases
        are because of our antrl4 parser. The incantation at the
        top of this file is for the 'print' one to work. 
        """
        for key, value in {'abs'           : abs,
                           'all'           : all,
                           'any'           : any,
                           'basestring'    : basestring,
                           'bin'           : bin,
                           'bool'          : bool,
                           'bytearray'     : bytearray,
                           'callable'      : callable,
                           'chr'           : chr,
                           'classmethod'   : classmethod,
                           'cmp'           : cmp,
                           'compile'       : compile,
                           'complex'       : complex,
                           'delattr'       : delattr,
                           'dict'          : dict,
                           'dir'           : dir,
                           'divmod'        : divmod,
                           'enumerate'     : enumerate,
                           'eval'          : eval,
                           'execfile'      : execfile,
                           'file'          : file,
                           'filter'        : filter,
#                           'float'         : float,
                           'format'        : format,
                           'frozenset'     : frozenset,
#                           'getattr'       : getattr,
                           'globals'       : globals,
                           'hasattr'       : hasattr,
                           'hash'          : hash,
                           'help'          : help,
                           'hex'           : hex,
                           'id'            : id,
                           'input'         : input,
#                           'int'           : int,
                           'isinstance'    : isinstance,
                           'issubclass'    : issubclass,
                           'iter'          : iter,
                           'len'           : len,
                           'locals'        : locals,
                           'long'          : long,
                           'map'           : map,
                           'max'           : max,
                           'memoryview'    : memoryview,
                           'min'           : min,
                           'next'          : next,
                           'object'       : object,
                           'oct'           : oct,
                           'open'          : open,
                           'ord'           : ord,
                           'pow'           : pow,
                           'print'         : print,
                           'property'      : property,
                           'range'         : range,
                           'raw_input'     : raw_input,
                           'reduce'        : reduce,
                           'reload'        : reload,
                           'repr'          : repr,
                           'reversed'      : reversed,
                           'round'         : round,
                           'set'           : set,
#                           'setattr'        : setattr,
                           'slice'         : slice,
                           'sorted'        : sorted,
                           'staticmethod'  : staticmethod,
                           'str'           : str,
                           'sum'           : sum,
                           'super'         : super,
                           'tuple'         : tuple,
                           'type'          : type,
                           'unichr'        : unichr,
                           'unicode'       : unicode,
                           'vars'          : vars,
                           'xrange'        : xrange,
                           'zip'           : zip,
                           '__import__'    : __import__,
        }.iteritems():
            self.plambdaEqualTest(key, value)


    

    def test_F(self):
        """Tests using a drone.
        """
        self.plambdaEqualTest('(import "plambda.drones.simple_drone")', True)
        self.plambdaStringEqualTest('(define SimpleDrone plambda.drones.simple_drone.SimpleDrone) ', 'SimpleDrone')
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
        self.plambdaEqualTest('(import "plambda.util.kwargs")', True)
        self.plambdaStringEqualTest('(define kwargs plambda.util.kwargs.kwargs)', 'kwargs')
        self.plambdaStringEqualTest('(define l0 (mklist (int 1) (int 2) (int 3)))', 'l0')
        self.plambdaStringEqualTest('(define d0 (mkdict "one" (int 1) "two" (int 2) "three" (int 3)))', 'd0')
        self.plambdaEqualTest('(kwapply kwargs l0 d0)', '(1, 2, 3) {one: 1, three: 3, two: 2}')

        
if __name__ == "__main__":
    unittest.main()
