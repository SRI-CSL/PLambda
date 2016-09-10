

(try (/ (int 2) (int 0)) (catch e (apply str e)))


(try (/ (int 2) (int 0)) (catch e (int 298)))
