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
            retval = self.interpreter.evaluateString(string)

            if str(retval) != str(value):
                print 'str(retval): ', str(retval)
                print 'str(value): ', str(value)
            
            self.assertEqual(str(retval), str(value))
        except Exception as e:
            #traceback.print_exc(file=sys.stderr)
            print 'type(e): ', type(e)
            print 'type(value): ', type(value)
            
            self.assertEqual(type(e), type(value))
            print 'str(e): ', str(e)
            print 'str(value): ', str(value)
            self.assertEqual(str(e), str(value))

