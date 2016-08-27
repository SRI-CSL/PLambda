import sys

from ..util.StringBuffer import StringBuffer

def kwargs(*largs, **kwargs):
    sb = StringBuffer()
    sb.append(str(largs))
    comma = False
    sb.append(' {')
    for key in sorted(kwargs):
        if comma:
            sb.append(', ')
        else:
            comma = True
        sb.append('{0}: {1}'.format(key, kwargs[key]))
    sb.append('}')
    return str(sb)


"""
(import "plambda.util.kwargs")

(define kwargs plambda.util.kwargs.kwargs)

(define l0 (mklist (int 1) (int 2) (int 3)))

(define d0 (mkdict "one" (int 1) "two" (int 2) "three" (int 3)))

(kwapply kwargs l0 d0)



(let ((l0 (mklist (int 1) (int 2) (int 3)))
      (d0 (mkdict "one" (int 1) "two" (int 2) "three" (int 3))))
  (kwapply kwargs l0 d0))

"""


