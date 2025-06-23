# numpy random module provides two meethods:  shuffle() and permutation()

# shuffle() and permutation() dono array ki arrangement ko change krty hn, difference
# y h k shuffle() original array ko chnage kr deti but permutation() always return another
# array without making chnages in the original array 

import numpy as np
d=np.array([1,2,4,7,9])
np.random.shuffle(d)
print(d) #yani original array hi chnage ho gi


dd=np.array([1,4,7,0,3,211])
c=np.random.permutation(dd)
print(c)
print(dd)


