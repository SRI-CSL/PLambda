#!/usr/bin/env python

import unittest

from plam.visitor.Parser import parseFromString
from plam.plambda.Interpreter import Interpreter
from plam.plambda.PLambdaException import PLambdaException

class dronesTest(unittest.TestCase):
    """Tests using a drone.
    """

    interpreter = Interpreter()
    
    def setUp(self): 
        pass

    def tearDown(self):
        pass

    def testOne(self):
        self.plambdaEqualTest('(import "plam.drones.simple_drone")', True)
        
    def plambdaEqualTest(self, string, value):
        self.assertEqual(self.interpreter.evaluateString(string), value)

        
        

if __name__ == "__main__":
    unittest.main()
