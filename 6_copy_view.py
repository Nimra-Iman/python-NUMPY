import numpy as np
#  !!!!!!!!!  copy()  !!!!!!!!
x=np.array([1,2,3,44])
x_new=x.copy() #ab x_new m changes krny s "x" pr koi affect nhi ho ga
x[0]=83892
print(x)
print(x_new) 


#   !!!!!!!!!  view()  !!!!!!!!
a=np.array([22,33,44,45])
a_new=a.view() #ab "a" m changes krny s "a_new" m bhi chnages hon gy and vice virsa
a[0]=342
print(a)
print(a_new)

