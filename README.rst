.. image:: https://badge.fury.io/py/PLambda.svg
    :target: https://badge.fury.io/py/PLambda

.. image:: https://travis-ci.org/SRI-CSL/PLambda.svg?branch=master
    :target: https://travis-ci.org/SRI-CSL/PLambda

.. image:: https://img.shields.io/pypi/dm/plambda.svg
    :target: https://pypistats.org/packages/plambda


=======
PLambda
=======

An early prototype of a workable version of JLambda for Python.
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

Guide for JLambda Afficionados
------------------------------

 https://github.com/SRI-CSL/PLambda/blob/master/GUIDE.md

Install
-------

There is a pip package, but that will move along at a lazier pace than developing directly from
the repository.

|
| ``pip install plambda``
|


Dependencies
------------

This master is currently using Python 3.7 but most recent Python 3 versions should work. Travis tests it on 3.5, 3.6, 3.7 and 3.8.
I make no effort to support Python 2, but there is an old branch called 2.7 which might serve your twited purpose.
You will need the antlr4 runtime:

|
| ``pip install antlr4-python3-runtime``
|

Though this is done by doing `make develop` described next.

Develop
-------

Checkout the repository and do:

|
| ``make develop``
|

To run the tests you can do:

|
| ``make check``
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
