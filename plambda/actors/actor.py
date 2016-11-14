import sys
import inspect

from .actorlib import send, receive

class Actor(object):

    _debug = False

    def __init__(self, name, client):
        """Creates an Actor object with the given name and client."""
        self.client = client
        self.name = name
        # should probably complain if client is not an object...
        self.methods = inspect.getmembers(self.client, callable)
        debug('methods: {0}\n'.format(self.methods))


    def begin(self):
        """Receives and processes messages in an infinite loop. """
        while True:
            incoming = receive()
            if incoming is None:
                return 0
            (sender, msg) = incoming
            send(sender, self.name, self.process_message(sender, msg))


    def process_message(self, sender, msg):
        """The beginnings of a REP for imaude messages.

        Currently processes the message as:

         verb arg0 arg1 ... argN

        and attempts to invoke the 'verb' method on the 'client' object
        with the remaining arguments. I.e.

        client.verb(arg0, arg1, ..., argN)

        If this is kosher it returns the string representation of
        the resulting 'client' object.
        """

        #split the args into verb and rest
        arglist = msg.split()
        verb = arglist[0]
        args = arglist[1:]

        debug('{0} got message with verb = {1} and args = {2}\n'.format(self.name, verb, args))

        # see if we can call the 'verb' on the 'client' with the given 'args'
        success = False
        for (name, value) in self.methods:
            if name == verb:
                argspec = inspect.getargspec(value)
                debug('argspec: {0}'.format(argspec))
                success = True
                if len(argspec.args) - 1 == len(args): # do not count 'self'
                    value(*args)
                else:
                    fmsg = 'Actor arity of msg {0} does not match argsec: {1}'
                    emsg = fmsg.format(args, argspec.args[1:])
                    sys.stderr.write(emsg)
                    success = False
                break

        # return the result to the sender
        if success:
            return str(self.client)
        else:
            return 'unknown command'



def debug(emsg):
    """If the Actor.flag is set to True, then it writes the msg to stderr."""
    if Actor._debug:
        sys.stderr.write(emsg)
