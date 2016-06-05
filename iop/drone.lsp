(import "plambda.drones.simple_drone")

(define SimpleDrone plambda.drones.simple_drone.SimpleDrone)

(define mkdrone (name x y e)
  (let ((drone (apply SimpleDrone name)))
    (invoke drone "initialize" x y e)
    drone))


(define evalOK (sender message)
  (let ((val message))
    (apply send sender (getattr myself "name") (concat "OK " val "\n"))
    )
  )


