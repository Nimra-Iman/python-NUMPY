import numpy as np
# accessing 1-D
d=np.array([22,33,44])
# print(d[-2])
# print(d[0])
# print(d[1] + d[2])


#  accessing 2-D 
dd=np.array([[22,33,44], #first row
             [33,44,55]]) #2nd row
# print(dd[0,1]) #0=row,, 1=column  (yani 0th row ka 1st elemnt because 1st elemrnt column1 m
# # lie kr rha h)
# print(dd[1,1]) #yani 1st row 1st column pr jo elemnt pra vo de do


#  accessing 3-D (combing two 2-Ds)
ddd=np.array([[[22,33,44],[21,31,41]], #[22,33,44] is 0th row and [21,31,41] is 1st row of 0th vala 2-D
              [[44,55,66],[77,88,99]]])

print(ddd[0, 0, 1]) #yani 0th vali 2-D m 0th row pr or 1st col pr jo elemnt pra
print(ddd[1,1,1])

