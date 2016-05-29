(import "os")

(invoke os.path "basename" "foo/bar")

(define eleven (let ((x (int 7)) (y (int 9)))  (int 11)))

(define I (lambda (x) x))

(import "sys")

(define stderr sys.stderr)

(invoke stderr "write" "very\n\tinteresting, \"not\"\n")

(for x  (int 7)  (not x))

(try (int 7) (catch eid  eid))

(import "src.drones.simple_drone")

(define SimpleDrone src.drones.simple_drone.SimpleDrone)

(define drone (apply SimpleDrone "mydrone"))

(invoke drone "initialize"  "0" "0" "666")

(invoke drone "mv" "E")

(setattr SimpleDrone "debug" (boolean True))

(getattr SimpleDrone "debug")

(setattr drone "e" (int 1234567890))


