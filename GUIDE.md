Construction Zone: please feel free to add questions
----------------------------------------------------

The main differences between Java and Python from the perspective
of PLambda/JLambda are:

0. python is interpreted

1. The `import` mechanism is required, and modules, and classes, are first class objects.

2. The untyped primitive data structures (tuple, list, dictionary) can store objects and numbers etc.

3. There are global functions, which you can just apply. Here is a list of (2.7) built-ins that you can apply: https://docs.python.org/2/library/functions.html
Here are the latest stable, which we should be aiming for:
https://docs.python.org/3.7/library/functions.html

4. There is no `new` operator, just apply the constructor.

5. There are richer forms of argument passing (apply vs kwapply). `(kwapply f l d)` is `f(*l, **d)`.
`f` must be callable (i.e. a python function), our closures do not support `kwapply`.

6. In python things are already attributable (why do we need uids and fetch?)

7. Reflection in python has some holes in it, you cannot get the argspec of a built-in, so some guess work is required.

8. In Python there is no such thing as a character (just a string of length one). So this allows us
to have two types of string literals "these" and 'those', I tried to get """these
working but antrl gave me a hard time, so I gave up in frustration."""

Items 1. and  3. combine to allow us to have a richer use of the '.' in PLambda
than in JLambda, we even combine it with the define mechanism.

After `(import 'sys')`, for example we can either do:
```
(invoke sys.stderr 'write' 'one line at a time\n')
```
or
```
(apply sys.stderr.write 'one line at a time\n')
```

Item 2. makes life very much easier: We have n-ary constructors `mktuple`,
`mklist`, and `mkdict.`


I added `is` since `is` is much more pythonesque and I could never
remember which of `=` and `==` was `eq` not `equal`.
`is` is `eq`. Following JLambda's dubious choice:
The first form, `=`, is related to the Scheme or Lisp equals
predicate, while the second, `==`, is more like `eq`.

`isinstance` is a global so we can do things like:
```
(apply isinstance (mkdict) dict)   -> True
(apply isinstance (mkdict) list)   -> False
(apply isinstance (mklist) list)   -> True
(apply isinstance (mklist) dict)   -> False
(apply isinstance (mktuple) tuple)   -> False
```

lessons:

```
(define f (arg)  (invoke arg "extend" arg)  arg)
```
primitive data: tuple list dict:

mklist mktuple mkdict
```
(define d1 (mkdict (int 0) "a" (int 1) "b" (int 2) "c"))

(define l0 (mklist (int 1) (int 2) (int 3)))

(get l0 (int 2))

(get d1 (int 2))


(modify l0 (int 2) (int 9))
(modify d1 (int 2) (int 9))

(apply isinstance l0 list)
(apply isinstance d1 dict)
```
