import numpy as np
arr = np.array([[1,2,3,5,6,7],
                [1,2,3,6,5,4]])

# print(arr.shape)    #2,2,4

# print(arr.reshape(2,3,-1))

# for i in np.nditer(arr[1,3:]):
#     print(i)

dd=np.array([[1,2,3],
            [4,5,6]])

dd1=np.array([[11,12,13],
            [41,51,16]])
dd_new=np.concatenate((dd,dd1),axis=0)  #axis=0 krny s y saari 2-D arrays mil kr ek 2-D
# array bnay gi
print(dd_new)