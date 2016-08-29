import unittest

from plambda.visitor.Parser import parseFromString
from plambda.eval.Interpreter import Interpreter


class PLambdaTest(unittest.TestCase):

    def setUp(self): 
        self.interpreter = Interpreter()

    def tearDown(self):
        self.interpreter = None
    
    def plambdaEqualTest(self, string, value):
        self.assertEqual(self.interpreter.evaluateString(string), value)

    def plambdaStringEqualTest(self, string, value):
        self.assertEqual(str(self.interpreter.evaluateString(string)), value)

    def cpplambdaEqualTest(self, string, value):
        """Hooks into the CPS interpreter rather than the recursive one.
        """
        self.assertEqual(self.interpreter.cpevaluateString(string), value)

    def cpplambdaStringEqualTest(self, string, value):
        """Hooks into the CPS interpreter rather than the recursive one.
        """
        self.assertEqual(str(self.interpreter.cpevaluateString(string)), value)
