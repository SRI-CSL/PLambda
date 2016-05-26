
## PLambda

An attempt to produce a workable version of JLambda for Python.
To be used mainly as a part of the IOP imaude system.



## Manuals

The jlambda manual can be found [here](https://github.com/SRI-CSL/iopc/blob/master/doc/jlambda_manual.pdf?raw=true)

The iop manual can be found [here](https://github.com/SRI-CSL/iopc/blob/master/doc/iop_manual.pdf?raw=true)

## Websites

The jlambda webpage lives over [here](http://jlambda.com/~iop/jlambda.html)

The iop webpage lives over [here](http://jlambda.com/~iop/)

The main client of the iop system is [SRI International's Pathway Logic](http://pl.csl.sri.com/)



### Recipe to add an operator

1. Add it to the grammar PLambda.g4

2. Process the grammar with `make antlr4`

3. Add the operator to the `SymbolTable`

4. Add the operator to the `Interpreter`


