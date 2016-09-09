.. image:: https://badge.fury.io/py/PLambda.svg
    :target: https://badge.fury.io/py/PLambda
	     

=======
PLambda
=======

An attempt to produce a workable version of JLambda for Python.
To be used mainly as a part of the IOP imaude system.

JLambda and PLambda are essentially network command and control
languages. JLambda for controlling Java processes, and PLambda for
python processes.  JLambda is over 14 years old, whereas PLambda
is just a pup.

Note that Python is not Java so there will be some differences, but
hopefully the spirit will shine through. 

PLambda, like JLambda,  is a fast, efficient, minimalistic, call-by-value, lexically scoped Lisp or
Scheme like language with closures built upon the underlying data structures of the language it rests upon. 
The interpreter is implemented via CPS (continuation passing style).



Dependencies
------------

Python 2.7 is desired, though it might work on most pythons.
You will need the antlr4 runtime:

|
| ``pip install antlr4-python2-runtime``
|


Develop
-------

Checkout the repository and do:

|
| ``make develop``
|



Install
-------

There is a pip package, but that will move along at a lazier pace than developing directly from 
the repository.

|
| ``pip install plambda``
|



Manuals
-------

The jlambda manual can be found here: https://github.com/SRI-CSL/iopc/blob/master/doc/jlambda_manual.pdf?raw=true

The iop manual can be found here:
https://github.com/SRI-CSL/iopc/blob/master/doc/iop_manual.pdf?raw=true

Websites
--------

The jlambda webpage lives over here: http://jlambda.com/~iop/jlambda.html

The iop webpage lives over here: http://jlambda.com/~iop/

The main client of the iop system is SRI International's Pathway Logic: http://pl.csl.sri.com/



Recipe to add an operator
-------------------------


1. Add it to the grammar ``plambda.antlr4.PLambda.g4``

2. Process the grammar with ``make antlr4``

3. Add the operator to the ``plambda.eval.SymbolTable``

4. Add the operator to the ``plambda.eval.Interpreter``

5. Add some tests to ``tests/language.py``   


