(import "sys")

(define squark (string)
  (invoke sys.stderr "write" (concat string "\n")))


(import "plam.actors.actorlib")

(define send plam.actors.actorlib.send)

(import "plam.actors.pyactor")

(define myself (getattr plam.actors.pyactor.Main "myself"))

(define evalOK (sender message)
  (apply squark message)
  (apply send sender (getattr myself "name") "OK\n")
  )


;; should be able to do thing like:
;;
;; (import "plam.actors.pyactor")
;; (define Main plam.actors.pyactor.Main)
;; (define myself Main.myself)
;; by tweaking glookup a bit, like mlookup.
