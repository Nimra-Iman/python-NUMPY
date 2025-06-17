import numpy as np

arr = np.array(2)
# print(arr)


arr= np.array([[1,2,3,6,4,2,1]])
# print(arr)
print(arr[0,1:3])

print()
print()
print()

a = np.array( [[[ 1,1,1,1,1,1], [2,2,2,2,2,2]], 
               [[3,3,3,3,3,3], [4,4,4,4,4,4]]])

# print(a)
print(a[1,:,1:4])



print()
print()
d_d_d=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(d_d_d[0:3]) 
