import numpy as np
# NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and 
# produce the corresponding sinh, cosh and tanh values..


# These functions are analogs of the regular trigonometric functions 
# sin,cos, and tan, but they are defined using exponential functions and have properties 
# related to hyperbolas rather than circles.

print(np.sinh(0))
print(np.sinh(90))

d=np.array([1,2,3,4,5])
print(np.sinh(d))  #calculate sinh of each element of array


# calculating inverse of sin, cos and tan
# arcsin, arccos and arctan are inverse of sin, cos, tan respectively, they take radian
# and calculate the inverses of sin, cos and tan
print(np.arcsin(90))  #nan (not a number)

print(np.arccos(0))

dd=np.array([3,4,5,6,7,8,9])
print(np.arctan(dd))


