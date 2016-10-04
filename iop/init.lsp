
(import 'sys')
(invoke  sys.stderr 'write' 'Boo!\n')

(define plambda_clones (mklist))
(define plambda_population (int 4))

(define maude_clones (mklist))
(define maude_population (int 4))

(import 'plambda.actors.actorlib')

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
		      (invoke  sys.stderr
			       'write'
			       (concat 'Handled ' noun ' more coming\n'))
		      (apply plambda.actors.actorlib.send
			     'system'
			     'plambda'
			     (concat 'start ' (concat prefix (apply len clones)) ' ' executable ' ' args))
		      )
		   (seq (invoke  sys.stderr
				 'write'
				 (concat 'Handled ' noun ' enough already\n'))
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
  (if (== prefix 'plambda')
      (seq
       (for clone clones
	    (seq 
	     (invoke  sys.stderr 'write' (concat 'clone: ' clone ' with prefix ' prefix '\n'))
	     (apply plambda.actors.actorlib.send clone 'plambda' '(load "hello.lsp")')
	     )
	    )
       (apply plambda.actors.actorlib.send 'system' 'plambda' 'start maude0 iop_maude_wrapper basura')
       )
    )
  (if (== prefix 'maude')
      (for clone clones
	   (seq 
	    (invoke  sys.stderr 'write' (concat 'clone: ' clone ' with prefix ' prefix '\n'))
	    )
	   )
    )
  )


(define catchall (lambda (message)  (invoke  sys.stderr 'write' (concat 'Handled: ' message '\n'))))

(import 'plambda.actors.pyactor')
(apply plambda.actors.pyactor.add_handler (apply make_cloner 'plambda' 'pyactor' 'anonymous' plambda_clones plambda_population))
(apply plambda.actors.pyactor.add_handler (apply make_cloner 'maude' 'iop_maude_wrapper' 'anonymous' maude_clones maude_population))

;;start the ball rolling
(apply plambda.actors.actorlib.send 'system' 'plambda' 'start plambda pyactor')


