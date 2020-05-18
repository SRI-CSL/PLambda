(import "sys")
(import "os.path")

(import "plambda.util.Util")

(define string2error plambda.util.Util.string2error)

(define add2ImportPath (directory)
  (if (apply os.path.exists directory)
      (let ((path (apply os.path.abspath directory)))
        (if (not (in path sys.path))
            (apply sys.path.append path)
          (apply string2error 'Not adding a duplicate entry to sys.path')))
    (apply string2error 'Not adding an non-existant directory to the sys.path')
    )
  )


;;(apply add2ImportPath (apply os.getcwd))
