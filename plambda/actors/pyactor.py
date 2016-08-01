import os, sys, threading, signal, subprocess

sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..')))

from actorlib import send, receive

from plambda.eval.Interpreter import Interpreter

from plambda.visitor.Parser import parseFromString

debug = False


def handler(signum, frame):
    subprocess.call(['touch', '/tmp/1234567890'])
    sys.stderr.write('Signal handler called with signal {0}\n'.format(signum))
    sys.exit(0)



def main():
    signal.signal(signal.SIGINT, handler)
    launch(sys.argv[1] if len(sys.argv) == 2 else "noname")
    return 0


class Main(object):

    retries = 1

    # a singleton instance
    myself = None
    
    def __init__(self, name):
        """Creates an plambda Actor object with the given name.
        """
        self.name = name
        self.interpreter = Interpreter()
        if Main.myself is None:
            Main.myself = self
        else:
            raise Exception("plambda.actor.pyactor.Main should have a singleton instance!")
        
    def run(self):
        """The Read Eval Message Loop.
        """
        fails = 0
            
        while True:
            incoming = receive()
            if incoming is None:
                fails += 1
                if fails > Main.retries:
                    return 0
                else:
                    continue
            (sender, msg) = incoming

            threading.Thread(target=eval, args=(self.interpreter, msg)).start()
                
        return 0

def notify(message):
    if debug:
        sys.stderr.write('{0}\n'.format(message))
        sys.stderr.flush()

                
def eval(interpreter, message):
    """Evaluates the message in the given interpreter.
    """
    try:
        val = interpreter.evaluateString(message)
        notify('eval: {0} evaluated to {1}'.format(message, val))
    except Exception as e:
        sys.stderr.write('plambda.actors.pyactor.Main exception: {0}\n'.format(e))


def launch(name):
    main = Main(name)
    main.run()
    return 0
    
