# vesy tu hm predict nhi kr skty k kon ca random number generate ho ga lekin agar
# bht thory c numbers diye gay hun or random number generate krna ho ya sirf ek list m s koi
# digit randomly select krna ho or us list m 2 hi digits hun to hlka ca prediction
# hm kr skty hn k kon ca number repeate ho ga , is ko bolty hn data distribution

# Data Distribution is a list of all possible values, and how often each value occurs.
# Such lists are important when working with statistics and data science.

# agar list m bhhhhhtttt ziada elements ho to of course mushkil ho ga predict krna , isi liye
# kehty hn k password difficult rkho, small, large alphabets, numbers, symbols etc
# sab daalo ta k brute force attack mushkil ho q k vo softwares jo passwords pr
# bruteforce attack krty hn vo isi data distribution ki base pr hi bnty


from numpy import random
import numpy as np

# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

# The probability for the value to be 3 is set to be 0.1

# The probability for the value to be 5 is set to be 0.3

# The probability for the value to be 7 is set to be 0.6

# The probability for the value to be 9 is set to be 0
# ----------- The sum of all probability numbers should be 1.

d=random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(100))
print(d)  #ab is m 9 show hi nhi ho ga q k us ki probability 0.0 h, sab s ziada 7 show
# ho ga , us s kam 5 or 3 bht km show ho ga


d=random.choice([3,5,7,9], p=[0.1,0.3,0.6,0.0], size=(2,5))
# print(d)   #yani agar ap achi research kr k probability nikal lety ho to bht
# chances hn k ap required password crack kr lo 
