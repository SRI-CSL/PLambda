(import "sys")

(define squark (string)
  (invoke sys.stderr "write" (concat string "\n")))


(import "plambda.actors.actorlib")

(define send plambda.actors.actorlib.send)

(import "plambda.actors.pyactor")

(define myself (getattr plambda.actors.pyactor.Main "myself"))

(define evalOK (sender message)
  (apply squark message)
  (apply send sender (getattr myself "name") "OK\n")
  )


;; should be able to do thing like:
;;
;; (import "plambda.actors.pyactor")
;; (define Main plambda.actors.pyactor.Main)
;; (define myself Main.myself)
;; by tweaking glookup a bit, like mlookup.
