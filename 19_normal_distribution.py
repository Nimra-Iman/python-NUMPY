from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
# d=random.normal(0.2,0.5,1000)   #ab normal distribution ka data show ho ga wjere 0.2(mean value)
#  0.5 is standard deviation and 1000 is total values in dataset
# loc - (Mean) where the peak of the bell exists. (0.2 in this case)

# scale - (Standard Deviation) how flat the graph distribution should be.(0.5 in this case)

# size - The shape of the returned array.(1000 in this case)
# sns.histplot(d,kde=True)
# plt.show()



# create data that will show normal distribution
data=random.normal(size=(2,3))   #2-D array
print(data)

data=random.normal(loc=1, scale=2,size=(5))   #2-D array
print(data)  # loc=1, scale=2  are default values, agar y cheezy pass nhi kro gy to
# vo by default khud hi y le le ga