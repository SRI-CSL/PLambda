""" This is the python PLambda actor akin to g2d.
"""
import os
import re
import sys
import signal
import time
import threading
import traceback
import psutil

from .actorlib import receive

from ..eval.Interpreter import Interpreter

from ..actors.console import Console

from ..util.Util import string2error

debug = False

def infanticide(pid):
    try:
        parent = psutil.Process(pid)
    except psutil.NoSuchProcess:
        return
    children = parent.children(recursive=True)
    if debug:
        string2error(f'The children of {pid} are {children}')
    for p in children:
        os.kill(p.pid, signal.SIGKILL)
        notify(f'Sent signal {signal.SIGKILL} to {p.pid}')


def sighandler(signum, frame):
    notify(f'Signal handler called with signal {signum} and frame {frame}')
    infanticide(os.getpid())
    sys.exit()


def main():
    if len(sys.argv) == 1:
        launch('noname')
    elif len(sys.argv) == 2:
        launch(sys.argv[1])
    else:
        launch(sys.argv[1], sys.argv[2])
    return 0


class Main:
    """The main class/thread of the python actor."""
    retries = 1

    launchConsole = False

    #iam: must be a better way
    plambda_pattern = re.compile(r'^\s*\(')

    handlers = []

    # a singleton instance
    myself = None

    def __init__(self, name, filename=None):
        """Creates an plambda Actor object with the given name.
        """
        self.name = name
        self.interpreter = Interpreter()
        self.filename = filename
        signal.signal(signal.SIGINT, sighandler)
        if Main.myself is None:
            Main.myself = self
        else:
            raise Exception("plambda.actor.pyactor.Main should have a singleton instance!")
        if self.filename is not None:
            notify(f'Loading {self.filename}\n')
            self.interpreter.load(self.filename)
        self.console = None
        self.oracle = threading.Thread(target=oracle, args=(self, ))
        self.oracle.daemon = True



    def run(self):
        """The main thread ever ready to launch the console.
        """
        self.oracle.start()

        while True:
            time.sleep(1)
            # N.B.: could do this with a message now that we have handlers.
            if Main.launchConsole:
                Main.launchConsole = False
                self.console = Console(self.interpreter)
                self.console.mainloop()


        return 0


def add_handler(closure):
    notify('Adding closure')
    Main.handlers.append(closure)

def remove_handler(closure):
    Main.handlers.remove(closure)


def notify(message):
    if debug:
        string2error(message)


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
            continue
        (sender, msg) = incoming
        thread = threading.Thread(target=pl_eval, args=(actor.interpreter, sender, msg))
        #thread needs to be a daemon so that the actor itself can die in peace.
        thread.daemon = True
        thread.start()



def pl_eval(interpreter, sender, message):
    """Evaluates the message in the given interpreter.

    If the message appears to be an PLambda expression it is simply
    dispatched to the interpreter to evaluate. Otherwise it is processed
    by any custom handlers that have been installed.

    Custom handlers are of the form:

    (define handler (lambda (sender message)  ... ))

    Handlers should return true if they handled the message, and false
    otherwise. They are installed by

    (import 'plambda.actors.pyactor')
    (apply plambda.actors.pyactor.add_handler handler)


    and removed analagously


    (apply plambda.actors.pyactor.remove_handler handler)

    Handlers are stored in a list, and are processed in order,
    until one that handles the incoming message is found.
    Thus the oldest handler that accepts a message will win.



    """
    try:
        if Main.plambda_pattern.match(message):
            val = interpreter.evaluateString(message)
            notify(f'eval: {message} evaluated to {val}')
        else:
            sender = sender.strip()
            message = message.strip()
            notify(f'looking for handlers for: "{message}" from {sender} (we have {len(Main.handlers)} alternatives)')
            for handler in Main.handlers:
                if handler.applyClosure(sender, message):
                    notify(f'found a handler for: "{message}" from sender {sender}')
                    break
                notify('nope')
    except Exception as e:
        string2error(f'plambda.actors.pyactor.Main exception: {e}\nwhile evaluating:\n{message}\nsent by {sender}')
        if debug:
            traceback.print_exc(file=sys.stderr)


def launch(name, plfile=None):
    mainobj = Main(name, plfile)
    mainobj.run()
    return 0
