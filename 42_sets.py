# sets are always 1D 
import numpy as np
s=np.array([11,2,3,444,5,6,6,3,1,1,1,1,3,4,4])
print("unigue elements are = ", np.unique(s)) #yani saary elemenst ko ek ek dfa show kr de ga

# finding union
s1=np.array([1,2,3])
s2=np.array([1,2,3,5,6,4])
print(np.union1d(s1,s2))

# finding intersection
s1=np.array([1,2,3])
s2=np.array([1,2,3,5,6,4])
print(np.intersect1d(s1,s2, assume_unique=True)) #this takes optional argument
# assume_unique whcih makes computataion fast and it is always considered True in case
# of sets

# find differnce (jo phly m hn but doosry m nhi)
s1=np.array([1,2,3])
s2=np.array([1,2,3,5,6,4])
print(np.setdiff1d(s1,s2, assume_unique=True ))

# finding symmetric difference : elements that are in either sets but not in intersection

s1=np.array([1,2,3])
s2=np.array([1,2,3,5,6,4])
print(np.setxor1d(s1,s2, assume_unique=True))
