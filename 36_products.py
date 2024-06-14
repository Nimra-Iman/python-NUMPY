import numpy as np
d=np.array([1,2,3,4,5])
print(np.prod(d))  # find product of all elements


d1=np.array([1,2,3])
d2=np.array([1,2,3])
dd=np.prod([d1,d2])   #it will consider it a 2D array and provide multiplication of all
# elements of both arrays
print(dd)



d1=np.array([1,2,3])
d2=np.array([1,2,3])
dd=np.prod([d1,d2],axis=1)  
print(dd)


# commulative product:
d=np.cumprod([1,2,3,4])
print(d)