#!/usr/bin/env python

import unittest


from Testing import PLambdaTest


class dronesTest(PLambdaTest):
    """Tests using a drone.
    """

    def testOne(self):
        self.plambdaEqualTest('(import "plam.drones.simple_drone")', True)
        
        

if __name__ == "__main__":
    unittest.main()
