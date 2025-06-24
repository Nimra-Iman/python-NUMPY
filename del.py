import numpy as np

a = np.array([1,2,3,4,5,6])
a1 = np.array([1,2,3,4,5,6])

b= np.array([[1,2,3],[4,5,6]])
b1= np.array([[1,2,3],[4,5,6]])

c = np.array([[[1,2,3],[4,5,6]],
              [[5,4,3],[1,2,3]]])
c1 = np.array([[[1,2,3],[4,5,6]],
              [[5,4,3],[1,2,3]]])

new = np.concatenate((c,c1), axis = 0)
# print(new)
# n = np.stack((b,b1), axis = 0)
n = np.dstack((b,b1))
print(n)

# [[[1,2,3] ,[1,2,3]],[[4,5,6],[4,5,6]]]
