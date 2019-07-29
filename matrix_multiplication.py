
from numpy import *

matrix_1=matrix('1 2 3 ; 2 3 4 ; 5 6 7')  ### its 3x3 matrix
matrix_2=matrix('2 3 4 ; 8 5 4 ; 2 3 6')  ### its 3x3 matrix

add_matrix=matrix_1*matrix_2

print(f"{matrix_1} \n    * \n {matrix_2} \n    = \n {add_matrix}")
