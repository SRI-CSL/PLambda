(import "sys")

(import "plambda.util.Util")

(define squark (string) (apply plambda.util.Util.string2error string))


(import "plambda.actors.actorlib")

(define send plambda.actors.actorlib.send)

(import "plambda.actors.pyactor")

(define myself (getattr plambda.actors.pyactor.Main "myself"))

(define evalOK (sender message)
  (let ((val message))
    ;;(apply squark val)
    (apply send sender (getattr myself "name") (concat "OK " val "\n"))
    )
  )


(define console ()
  (setattr plambda.actors.pyactor.Main "launchConsole" (boolean True))
  )

;; should be able to do thing like:
;;
;; (import "plambda.actors.pyactor")
;; (define Main plambda.actors.pyactor.Main)
;; (define myself Main.myself)
;; by tweaking glookup a bit, like mlookup.
