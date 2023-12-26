(defun fibonacci (n)
  (if (<= n 1)
      n
      (+ (fibonacci (- n 1))
         (fibonacci (- n 2)))))

; Call the function with an example
(format t "~a~%" (fibonacci 15))