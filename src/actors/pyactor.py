#!/usr/bin/env python


import sys

import threading

from actorlib import send, receive

from src.plambda.Interpreter import Interpreter

from src.visitor.Parser import parseFromString

class Main(object):

    _debug = False
    
    def __init__(self, name):
        """Creates an plambda Actor object with the given name."""
        self.name = name
        self.interpreter = Interpreter()

    def run(self):

        fails = 0
            
        while True:
            incoming = receive()
            if incoming is None:
                fails += 1
                if fails > 1:
                    return 0
                else:
                    continue
            (sender, msg) = incoming
            
            threading.Thread(target=eval, args=(self.interpreter, msg)).start()
            
                
        return 0


                
    def process_message(self, sender, msg):
        eval(interpreter, msg)
            
        
def eval(interpreter, string):
    interpreter.evaluateString(string)
        
    
usage = """
Usage: {0} <actor name>
"""
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print usage.format(sys.argv[0])
        sys.exit(1)
    else:
        main = Main(sys.argv[1])
        sys.exit(main.run())

    
