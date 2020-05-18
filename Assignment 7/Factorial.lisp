(defun recursivefact (n)
  (if (= n 1)              
      1                           
      (* n (recursivefact (- n 1))))) 

(write-line "Please enter a number...")  
(setq x  (read))
(format t "~D! is ~D" x (recursivefact x))
(write-line "")  
(defun iterativefact (n)
    (do
       ((i 1 (+ 1 i))
        (prod 1 (* i prod)))
       ((equal i (+ n 1)) prod)))
(write-line "Please enter a number...")  
(setq x  (read))
(format t "~D! is ~D" x (iterativefact x))