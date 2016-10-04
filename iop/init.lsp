
(import 'sys')
(invoke  sys.stderr 'write' 'Boo!\n')

(define clones (mklist))
(define population (int 4))

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
		 (invoke  sys.stderr 'write' (concat 'Handled ' noun ' enough already\n'))
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


(define catchall (lambda (message)  (invoke  sys.stderr 'write' (concat 'Handled: ' message '\n'))))

(import 'plambda.actors.pyactor')
(apply plambda.actors.pyactor.add_handler cloner)


