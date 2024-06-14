# GCD(greatest common diviser) also called HCF(highest common factor) yani vo greatest
#  number jo saary elemnts m common lia ja skta ho or sab pr poora poora divide hota ho
import numpy as np
d=np.gcd(6,9)
print(d)
# 3 because that is the highest number both numbers can be divided by (6/3=2 and 9/3=3).

# calculating HCF of all the elements of array
d=np.array([2,3,4,5,6])
print(np.gcd.reduce(d))

# -----------------  another example
dd=np.array([20, 8, 32, 36, 16])
print(np.gcd.reduce(dd))