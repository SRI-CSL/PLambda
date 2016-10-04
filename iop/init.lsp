
(import 'sys')
(invoke  sys.stderr 'write' 'Boo!\n')

(define plambda_clones (mklist))
(define plambda_population (int 4))

(import 'plambda.actors.actorlib')

(define cloner (message)
  (let ((tokens (invoke message 'split')))
    (if (> (apply len tokens) (int 1))
	(let ((verb (get tokens (int 0)))
	      (noun (get tokens (int 1))))
	  (if (== verb 'startOK')
	      (seq
	       (invoke clones 'append' noun)
	       (if (< (apply len clones) population)
		   (seq 
		    (invoke  sys.stderr 'write' (concat 'Handled ' noun ' more coming\n'))
		    (apply plambda.actors.actorlib.send 'system' 'plambda' 'start plambda pyactor')
		    )
		 (seq (invoke  sys.stderr 'write' (concat 'Handled ' noun ' enough already\n'))
		      (apply init_clones)
		      )
		 )
	       (boolean true)
	       )
	    (seq
	     (boolean false)
	     )
	    )
	  )
      )
    )
  )


(define make_cloner (prefix executable args clones count)
  (lambda (message)
    (let ((tokens (invoke message 'split')))
      (if (> (apply len tokens) (int 1))
	  (let ((verb (get tokens (int 0)))
		(noun (get tokens (int 1))))
	    (if (and (== verb 'startOK') (invoke noun 'startswith' prefix))
		(seq
		 (invoke clones 'append' noun)
		 (if (< (apply len clones) count)
		     (seq 
		      (invoke  sys.stderr 'write' (concat 'Handled ' noun ' more coming\n'))
		      (apply plambda.actors.actorlib.send 'system' 'plambda' (concat 'start ' prefix ' ' executable ' ' args))
		      )
		   (seq (invoke  sys.stderr 'write' (concat 'Handled ' noun ' enough already\n'))
			(apply init_clones clones prefix)
			)
		   )
		 (boolean true)
		 )
	      (seq
	       (boolean false)
	       )
	      )
	    )
	)
      )
    )
  )



(define init_clones (clones prefix)
  (for clone clones  (invoke  sys.stderr 'write' (concat 'clone: ' clone ' with prefix ' prefix '\n'))))
)


(define catchall (lambda (message)  (invoke  sys.stderr 'write' (concat 'Handled: ' message '\n'))))

(import 'plambda.actors.pyactor')
;;(apply plambda.actors.pyactor.add_handler cloner)
(apply plambda.actors.pyactor.add_handler (apply make_cloner 'plambda' 'pyactor' 'anonymous' plambda_clones plambda_population))

;;start the ball rolling
(apply plambda.actors.actorlib.send 'system' 'plambda' 'start plambda pyactor')


