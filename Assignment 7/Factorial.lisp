(defun recursivefact (n)
  (if (= n 1)              
      1                           
      (* n (recursivefact (- n 1))))) 

(write-line "Please enter a number...")  
(setq x  (read))
(format t "~D! is ~D" x (recursivefact x))
(write-line "")  
(defun iterativefact (n)
    (loop for i from 0 to n
          for fact = 1 then (* fact i)
          finally (return fact)))
(write-line "Please enter a number...")  
(setq x  (read))
(format t "~D! is ~D" x (iterativefact x))