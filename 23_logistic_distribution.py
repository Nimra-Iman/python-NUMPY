# Logistic Distribution is used to describe growth.
# Used extensively in machine learning in logistic regression, neural networks etc.
# It has three parameters:
# loc - mean, where the peak is. Default 0.
# scale - standard deviation, the flatness of distribution. Default 1.
# size - The shape of the returned array.

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
d=random.logistic(loc=1, scale= 2, size=(1000))
# sns.histplot(d,kde=True)
# plt.show()

#!!!!!!!!!!!!!   Difference Between Logistic and Normal Distribution
# Both distributions are near identical, but logistic distribution has more area under
# the tails, meaning it represents more possibility of occurrence of an event further away
# from mean.

# For higher value of scale (standard deviation) the normal and logistic distributions 
# are near identical apart from the peak.
sns.histplot((random.normal(scale=2,size=1000)), kde=True)
sns.histplot((random.logistic(size=1000)), kde=True)
plt.show()