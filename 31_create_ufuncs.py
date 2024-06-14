# ap khud k bhi ufuncs bna skty ho ta k vactorization k zrye ap fastly kaam kr sko

# in functions ko bhi normal python functions ki trah bnana h, or phir un ko add krna h
# numpy ki ufunc library k ander add krna h via frompyfunc()

def my_add(a,b):
    return a+b

# ab is my_add() function ko numpy ki ufunc library m add krna h
import numpy as np
addd=np.frompyfunc(my_add, 2, 1) #is "2" ka matlab y h k asal m 2 arrays input krny hn hm n
# and "1" ka matlab y h k output "1" array ho (yani kehny ka matla y hua k 2 input
# arrays ko add krna h or un ka output "1" array m de do)

print(addd([1,2,3,4],[1,2,3,4])) #y dono input arrays hn jin ko + krna h





# !!!!!!!!!!!!!!!!!!!!  check whether the function is ufunc or not  !!!!!!!!!!!!!!!!!!

print(type(np.add)) # yani "add" function numpy ki ufunc m h ya nhi

print(type(np.concatenate)) #<class 'numpy._ArrayFunctionDispatcher'>  q k y ufunc fun nhi h

# print(type(np.blahblah))  #error



# Use an if statement to check if the function is a ufunc or not:
if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')

