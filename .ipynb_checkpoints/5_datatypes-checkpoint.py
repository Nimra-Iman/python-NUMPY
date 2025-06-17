# Python datatypes: integer, string, float, boolean, complex

# Numpy datatypes:
# i for integer 
# b for boolean  
# u for unsigned integer
# f for float
# c for complex float
# m for timedelta  
# M for datetime   
# O for object
# S for string
# U for unicode string
# V - memory

# (ibmM fOcS uUV )

# CHECKING DATATYPE OF NUMPY ARRAY:
import numpy as np
x=np.array([1,2,3,4,5])
print(x.dtype) #yani x ki datatype kia h (output==  int32  yani  each element in the array
# is stored as a 32-bit integer. This means each integer element uses 32 bits (4 bytes)
# of memory.)

y=np.array(['nimra',"iman"])
print(y.dtype)

x=np.array([1,2,3,4,5], dtype="S") #yani is array ka hr element ab integer nhi h, bal k 
# byte string h
print(x)
print(x.dtype) 


x=np.array([1,2,3,4,5], dtype="i4") #yani hr elemnt ka size 4byte h yani, hr element 
                                    # 32 bits ka h
print(x)
print(x.dtype) 


# x=np.array(["apple","banana","mango"], dtype="i4") #error because is string ko int 
#                                                   m convert nhi kr skty
# print(x.dtype)
# print(x)


x=np.array(["1","2","3"], dtype="i4") # is string ko int 
#                                      m convert kr skty
print(x.dtype)
print(x)


#   !!!!!!!!!!!!  astype()  !!!!!!!!!!!!!


# The best way to change the data type of an existing array, is to make a copy of the 
# array with the astype() method.

# The astype() function creates a copy of the array, and allows you to specify the data 
# type as a parameter.
print("neruheuk")
x=np.array([1,2,4])
y=x.astype('f') #agar ap chahty ho k "x" xhange na ho to esa krny s "x" bhi change nhi ho ga
print(y.dtype)
print(y)
print(x) 


