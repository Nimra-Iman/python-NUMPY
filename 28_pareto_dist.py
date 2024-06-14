# A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 
# 80% outcome).

# It has two parameter:
# a - shape parameter.
# size - The shape of the returned array.

# "a" describes the shape of the graph.
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
# d=random.pareto(a=20, size=(1000))
# sns.histplot(d,kde=True)
# plt.show()


sns.histplot((random.pareto(a=2, size=1000)),kde=True)
sns.histplot((random.pareto(a=20, size=1000)),kde=True)
plt.show()
