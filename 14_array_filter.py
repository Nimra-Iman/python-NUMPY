# get some elements from existing array and make new array from them
import numpy as np
d=np.array([1,2,3,4,5])
filter=[True,False,True,True,False]  #true valy elements filtered array m show hon gy
# or false valy nhi hon gy
filtered_array=d[filter] 
print(filtered_array)


# make a filtered array with a given condition
d=np.array([1,2,3,4,5])
filter=[]
for i in d:
    if(i>2):
        filter.append(True)
    else:
        filter.append(False)
# print(filter)
filtered_array=d[filter]
print(filtered_array)


# create a filtered array that contain only even elements
d=np.array([1,2,3,4,5])
filter=[]
for i in d:
    if(i%2==0):
        filter.append(True)
    else:
        filter.append(False)

print(filter)
filtered_array=d[filter]
print(filtered_array)


# creating filtered array directly
print(" creating filtered array directly")
d=np.array([2,3,4,5,6])
filtered=d>3
filtered_array=d[filtered]
print(filtered_array)


