(invoke foo 666 "123")

(not True)

(isnull None)

(define foo "123")

(define Fun (x) "123")

(for x (apply z y) (apply x y) (apply y x) x)

(+ x y)

(lambda (x y) (apply x y) (apply y x) x)

(let ((x 7) (y 8) (z 9)) (+ x (+ y z)))


(try  (apply x y) (apply y x) (apply z y) (catch e (apply print e)))
