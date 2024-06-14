# ufuncs stands for universal functions
# agar hm n normal 2 lists k elements ko add kr k kisi doosri list m daalny hn to hmy
# ek ek element ko iterate krna ho ga, lekin agar hm vectorization ko use krty hn to
# hm is kaam ko bhhtt fastly kr skty hn

# vactorization: Converting iterative statements into a vector based operation is
# called vectorization.

# using normal way:
a=[1,2,3,4]
b=[1,2,3,4]
z=[]
for i,j in zip(a,b):
    z.append(i+j)
# print(z)

# we will use ufuncs to make this work more fast:
# ufuncs are used to implement vectorization in NumPy which is way faster than 
# iterating over elements
import numpy as np
a=[1,2,3,4]
b=[1,2,3,4]
z=np.add(a,b)
print(z)


# ufuncs also take additional arguments, like:
# where boolean array or condition defining where the operations should take place.
# dtype defining the return type of elements.
# out output array where the return value should be copied.