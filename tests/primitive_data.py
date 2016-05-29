#!/usr/bin/env python

import unittest

from src.visitor.Parser import parseFromString
from src.plambda.Interpreter import Interpreter
from src.plambda.PLambdaException import PLambdaException

class primitiveDataTest(unittest.TestCase):
    """Tests for primitive data.
    """

    interpreter = Interpreter()
    
    def setUp(self): 
        pass

    def tearDown(self):
        pass

    def testOne(self):
        self.plambdaEqualTest('(int 666)', 666)
        
    def testTwo(self):
        self.plambdaEqualTest('(boolean False)', False)
        
    def testThree(self):
        self.plambdaEqualTest('(float 3.1459)',  3.1459)


    def plambdaEqualTest(self, string, value):
        self.assertEqual(self.interpreter.evaluateString(string), value)

        
        

if __name__ == "__main__":
    unittest.main()
