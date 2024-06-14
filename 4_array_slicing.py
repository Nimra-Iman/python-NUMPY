import numpy as np
x=np.array([11,22,33,44,55,66,77,88,99,100])
# print(x[0:5])  #yani 0th index s le kr (5-1)th yani 4th index tak show kro
# print(x[4:]) #yani 4th index till end
# print(x[:5]) #yani start s le kr 4th index tak

# negative indexing
# print(x[-2:]) #-2 means (length-2) which means 8th index , yani 8th index s end tak
# print(x[:-5]) #yani start s le kr 4th index tak
# print(x[-6:-1]) 
# print(x)

# !!!!!!!!!!!  steps/jumps  !!!!!!!!!!!!!!!!!!!
# print(x[:5:2]) #11 33 55 (yani 2 2 ka jump lo )
# print(x[::2])
# print(x[::-1]) #poori reverse ho gi


#   !!!!!!!!!  slicing 2-D array  !!!!!!!!!!!!!!!
dd=np.array([[1,2,3,4,5],
             [11,21,31,41,51]])
# print(dd[0,1:4]) #yani total two 1-D arrays hn, to 0th vali array ky 1st index s le kr 3rd 
#                   # index tak show kro

# print(dd[1,:-2])

# if i want k mujy 3 and 31 ko show krna h (3 from 0th 1-D array and 31 from 1st 1-D array)

# print(dd[0:2, 2 ])   #comma (,) s phly vala show krta h k kon c 1-D array choose krni h
# yhan , yhan hm keh rhyn hn k 0th vali s le kr 1st vali 1-D array choose ki h hm n or
# us ka 2nd index show kro

# similarly:
# print(dd[0:2, 2:4 ])


#   !!!!!!!!!!!!!  slicing witn 3-D array  !!!!!!!!!!!!!!!!

ddd=np.array([[[1,2,3,4,5],[6,7,8,9,10]],
              [[11,12,13,14,15],[16,17,18,19,20]]])
# print(ddd[1,0,1:4]) # yhan two 2-D arrays hn, hm keh rhy hn k 1st index vali 2-D array ko
# select kro yani is vali ko ( [[11,12,13,14,15],[16,17,18,19,20]] ), ab y ek 2-D array h
# is m mazeed two 1-D arrays hn , ab 0 ka matlab h k 0th index vali 1-D array yani y 
# vali ( [11,12,13,14,15] ) or is ka 1:4 tak show kro

# print(ddd[1,0:2,1:4])
# print(ddd[0:2,0:2,1:4])  # yani 0:2 means k 0th and 1st dono ko select kro

print(ddd[0:2,0:2,1:4])


import numpy as np
d_d_d=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(d_d_d[0:3])   #is m poori array hi ouput m ay gi q k 1st comma s phly valy m hm
# choose krty hn k kon c 2-D array select krni h , to yhan hm keh rhyn h k 0th 2-D array
#  s le kr 2nd 2-D array tak select kr lo, ab yhan h hi sirf ek 2-D array to vhi vali 
# select ho jay gi


