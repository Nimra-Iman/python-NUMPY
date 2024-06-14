# poisson distribution y btata h k "on average 2 customers aty hn 1 minute m, to gly 10 minutes
# m customers ki any ki kia probability h, yani kitny ay gy "........
# lekin exponential distribution y btata h k "on average 2 customers aty hn ek time m, to
# kitna time lgy ga agla customer any m kitna time lgy ga "

# Exponential distribution is used for describing time till next event e.g. failure/success etc.

# It has two parameters:
# scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
# size - The shape of the returned array.

from numpy import random
d=random.exponential(scale=2, size=5)
print(d)

# [4.12341838 0.78258345 2.24954811 2.01678284 2.0693296 ] -> if this is output
# then it is showing that: (this is from CHATGPT)
# --> event A k 4.12341838 units of time k baad event B ho ga
# --> event B k 0.78258345 units of time k baad event C ho ga
# ------>if we consoder units of time as seconds and events as customer arrival then it 
# means that customer B will visit shop after 4.12341838 seconds of customer A visit. 

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(random.exponential(size=1000), kde=True)

plt.show()