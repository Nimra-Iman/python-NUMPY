# it is used in ML and Datascience in signal processing.
 
# It has two parameters:
# scale - (standard deviation) decides how flat the distribution will be default 1.0).
# size - The shape of the returned array.

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
# d=random.rayleigh(scale=2, size=(1000))
# sns.histplot(d, kde=True)
# plt.show()

# ----------------------
# at Unit scale and 2 df , chi square and rayleigh have sanme graph
sns.histplot((random.chisquare(df=2, size=1000)),kde=True)
sns.histplot((random.rayleigh(scale=1, size=1000)),kde=True)
plt.show()