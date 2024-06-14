# shape of an array is the number of elements in each of dimentions
import numpy as np
x=np.array([[1,2,3,4,5],
            [6,7,8,9,0],
            [2,3,4,6,2]])
# print(x.shape)   #(3,5) 3 rows and each row has 5 columns (jitni diementions ka array
# ho ga utni digits ka output ay ga)


y=np.array([[[1,2,3],[4,5,6]],
            [[7,8,9],[25,43,3]],
            [[343,24,13],[35,34,42]]])
# print(y.ndim)
print(y.shape) #(3,2,3) yani is array k ander total "3" 2_dimentioanl arrays hn, or hr 2_dim 
# array k ander "2" 1_dim arrays hn or he 1_dim array k ander 3 elements hn

z=np.array([22,33,44], ndmin=5)
# print(z.shape)  
# [[[[[22,33,44]]]]]

x=np.array([22,33,44])
print(x.shape) 