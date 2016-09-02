import sys, traceback, unittest

from plambda.visitor.Parser import parseFromString
from plambda.eval.Interpreter import Interpreter


class PLambdaTest(unittest.TestCase):

    def setUp(self): 
        self.interpreter = Interpreter()

    def tearDown(self):
        self.interpreter = None
    
    def plambdaClassTest(self, string, cls):
        self.assertEqual(isinstance(self.interpreter.evaluateString(string), cls), True)

    def plambdaEqualTest(self, string, value):
        self.assertEqual(self.interpreter.evaluateString(string), value)

    def plambdaStringEqualTest(self, string, value):
        self.assertEqual(str(self.interpreter.evaluateString(string)), value)

    def plambdaExceptionTest(self, string, value):
        try:
            self.interpreter.evaluateString(string)
        except Exception as e:
            #traceback.print_exc(file=sys.stderr)
            self.assertEqual(type(e), type(value)) 
            self.assertEqual(str(e), str(value))

    def cps_plambdaClassTest(self, string, cls):
        self.assertEqual(isinstance(self.interpreter.cps_evaluateString(string), cls), True)

    def cps_plambdaEqualTest(self, string, value):
        """Hooks into the CPS interpreter rather than the recursive one.
        """
        self.assertEqual(self.interpreter.cps_evaluateString(string), value)

    def cps_plambdaStringEqualTest(self, string, value):
        """Hooks into the CPS interpreter rather than the recursive one.
        """
        self.assertEqual(str(self.interpreter.cps_evaluateString(string)), value)

    def cps_plambdaExceptionTest(self, string, value):
        try:
            self.interpreter.cps_evaluateString(string)
        except Exception as e:
            traceback.print_exc(file=sys.stderr)
            self.assertEqual(type(e), type(value)) 
            self.assertEqual(str(e), str(value))
