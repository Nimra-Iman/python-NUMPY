# Addition is done between two arguments whereas summation happens over n elements.
#--------------  add
import numpy as np
d1=np.array([1,2,3])
d2=np.array([1,2,3])
dd=np.add(d1,d2)
print(dd)

#------------------ sum
d1=np.array([1,2,3,8])
dd=np.sum([d1])  
print(dd)


d1=np.array([1,2,3,8])
d2=np.array([1,2,3,5])
dd=np.sum([d1,d2])  # it treats the list as a 2D array and sums all the elements
# across both arrays.
print(dd)


# -------------------- summation
d=np.array([1,2,3,4,5])
d1=np.array([1,2,3,4,5])
print(np.sum((d,d1),axis=1))  
# print(np.sum(d,axis=1)) #it will raise error, because sum() dono arrays ko ek 2D array 
# consider krta h, to vo error de ga:  axis 1 is out of bounds for array of dimension 1



#  -----------------  cumsum()
d9=np.array([1,2,3,4,5])
print("sum of all emenets is = ",np.cumsum(d9))
# Cummulative sum means partially adding the elements in array.
# E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].




