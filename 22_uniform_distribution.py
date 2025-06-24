#  it is only made for probability, kisi event k hony ki kia probability h
# Used to describe probability where every event has equal chances of occuring.
# E.g. Generation of random numbers, rolling a die(har event ki equal probability h)
# It has three parameters:
# a - lower bound - default 0.0
# b - upper bound - default 1.0
# size - The shape of the returned array.


from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
d=random.uniform(size=(1000))
sns.histplot(d, kde=True)
plt.show()


