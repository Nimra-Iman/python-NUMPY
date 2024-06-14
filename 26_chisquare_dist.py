# Chi Square distribution is used as a basis to verify the hypothesis.

# It has two parameters:
# df - (degree of freedom).
# size - The shape of the returned array.

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
d=random.chisquare(df=2, size=1000)
sns.histplot(d, kde=True)
plt.show()
