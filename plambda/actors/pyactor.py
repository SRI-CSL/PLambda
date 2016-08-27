import os, sys, time, threading, traceback, signal, subprocess, psutil

from .actorlib import send, receive

from ..eval.Interpreter import Interpreter

from ..visitor.Parser import parseFromString

from ..actors.console import Console

debug = False

def infanticide(pid):
    try:
      parent = psutil.Process(pid)
    except psutil.NoSuchProcess:
      return
    children = parent.children(recursive=True)
    if debug:
        sys.stderr.write('The children of {0} are {1}\n'.format(pid, children))
    for p in children:
        os.kill(p.pid, signal.SIGKILL)
        if debug:
            sys.stderr.write('Sent signal {1} to {0}\n'.format(p.pid, signal.SIGKILL))


def handler(signum, frame):
    if debug:
        sys.stderr.write('Signal handler called with signal {0}\n'.format(signum))
        sys.stderr.flush()
    infanticide(os.getpid())
    sys.exit()


def main():
    launch(sys.argv[1] if len(sys.argv) == 2 else "noname")
    return 0


class Main(object):

    retries = 1

    launchConsole = False

    # a singleton instance
    myself = None
    
    def __init__(self, name):
        """Creates an plambda Actor object with the given name.
        """
        self.name = name
        self.interpreter = Interpreter()
        signal.signal(signal.SIGINT, handler)
        if Main.myself is None:
            Main.myself = self
        else:
            raise Exception("plambda.actor.pyactor.Main should have a singleton instance!")



        
    def run(self):
        """The main thread ever ready to launch the console.
        """
        fails = 0

        self.oracle = threading.Thread(target=oracle, args=(self, ))
        self.oracle.daemon = True
        self.oracle.start()
        
        while True:
            time.sleep(1)
            if Main.launchConsole:
                Main.launchConsole = False
                self.console = Console(self.interpreter)
                self.console.mainloop()

                
        return 0
    
def notify(message):
    if debug:
        sys.stderr.write('{0}\n'.format(message))
        sys.stderr.flush()


def oracle(actor):
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
        thread = threading.Thread(target=eval, args=(actor.interpreter, msg))
        #thread needs to be a daemon so that the actor itself can die in peace.
        thread.daemon = True
        thread.start()
            

        
def eval(interpreter, message):
    """Evaluates the message in the given interpreter.
    """
    try:
        val = interpreter.evaluateString(message)
        notify('eval: {0} evaluated to {1}'.format(message, val))
    except Exception as e:
        sys.stderr.write('plambda.actors.pyactor.Main exception: {0}\n'.format(e))
        if debug:
            traceback.print_exc(file=sys.stderr)


def launch(name):
    main = Main(name)
    main.run()
    return 0
    
