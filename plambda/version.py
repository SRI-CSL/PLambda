"""
Feeping Creaturism:

This is the all important version number used by pip.


Version history:

1.0.0   7/1/2016    Paging in the pip process.

1.0.1   8/5/2016    pyactor shuts down (i.e. kills) any children (like SITL etc).

1.0.2   8/18/2016   kwapply added.

1.0.3   8/18/2016   modify added.

1.0.4   8/21/2016   single quote strings added. isint isfloat added. isobject just (not (isnone))

1.0.5   8/23/2016   The read-eval-print loop gets a makeover. Now
                    handles multiline paste and prints definitions.

1.0.6   8/25/2016   PLambda gets a console.

1.0.7   8/27/2016   Updated all relative imports to follow:
                    https://www.python.org/dev/peps/pep-0328/

1.0.8   9/02/2016   CPS (Continuation Passing Style) installed as the default.
                    Can switch to recursive via a mode in plambda.eval.Interpreter

1.0.9   9/10/2016   Various bug fixes in the CPS interpreter.

1.0.10  9/27/2016   Fixed the lookup mechanism in the CPS interpreter.

1.0.11  10/27/2016  Non Sexpression handlers added to pyactor for SoftAgent requirements.

1.0.12  11/05/2016  pylint spots a few mistakes.

1.0.13  11/15/2016  pylintification complete.

1.1.0   05/08/2020  ditch 2.7, dust off the cobwebs, lint the puppy, and forge on.

1.1.1   05/18/2020  add membership tests a la 'in' as a bnary operator, and lots of minor tweaks.

"""

plambda_version = '1.1.1'
