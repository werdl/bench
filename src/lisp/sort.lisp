(defun sort-list (lst)
  (sort lst #'<))

; Call the function with an example
(let ((my-list '(9 8 7 6 5 4 3 2 1)))
  (format t "Sorted List: ~a~%" (sort-list my-list)))