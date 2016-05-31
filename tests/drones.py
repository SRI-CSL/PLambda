#!/usr/bin/env python

import unittest

from plam.visitor.Parser import parseFromString
from plam.plambda.Interpreter import Interpreter
from plam.plambda.PLambdaException import PLambdaException


from Testing import PLambdaTest


class dronesTest(PLambdaTest):
    """Tests using a drone.
    """

    def testOne(self):
        self.plambdaEqualTest('(import "plam.drones.simple_drone")', True)
        
        

if __name__ == "__main__":
    unittest.main()
