import numpy as np
import scipy.linalg
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
P,L,U = scipy.linalg.lu(a)
print(L)
print(U)