# A discrete difference means subtracting two successive elements.
# E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
# To find the discrete difference, use the diff() function.

import numpy as np
d=np.array([1,2,3,4,5])
difference=(np.diff(d))
print(difference)
difference_2=np.diff(difference)
print(difference_2)

# like above, in order to calculate difference twice, we put n=2
d=np.array([23,34,45,56])
dd=np.diff(d,n=2)
print(dd)