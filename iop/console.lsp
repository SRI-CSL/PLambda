(import "sys")

(define stderr sys.stderr)

(invoke stderr "write" "very\n\tinteresting, \"not\"\n")

(invoke stderr 'write' 'byeee\n')

(invoke stderr "flush")


(import "plambda.util.Util")
(define string2error plambda.util.Util.string2error)
(apply string2error "This puppy flushes by itself!")
