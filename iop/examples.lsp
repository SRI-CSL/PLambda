

(try (/ (int 2) (int 0)) (catch e (apply str e)))


(try (/ (int 2) (int 0)) (catch e (int 298)))

(try foo (catch e (int 666)))

(try (seq foo) (catch e (int 666)))
