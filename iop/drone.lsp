(import "plambda.drones.simple_drone")

(define SimpleDrone plambda.drones.simple_drone.SimpleDrone)

(define mkdrone (name x y e)
  (let ((drone (apply SimpleDrone name)))
    (invoke drone "initialize" x y e)
    drone))


