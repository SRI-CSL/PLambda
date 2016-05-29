#!/usr/bin/env python

import unittest

from src.visitor.Parser import parseFromString
from src.plambda.Interpreter import Interpreter
from src.plambda.PLambdaException import PLambdaException

class dronesTest(unittest.TestCase):
    """Tests using a drone.
    """

    interpreter = Interpreter()
    
    def setUp(self): 
        pass

    def tearDown(self):
        pass

    def testOne(self):
        self.plambdaEqualTest('(import "src.drones.simple_drone")', True)
        
    def plambdaEqualTest(self, string, value):
        self.assertEqual(self.interpreter.evaluateString(string), value)

        
        

if __name__ == "__main__":
    unittest.main()
