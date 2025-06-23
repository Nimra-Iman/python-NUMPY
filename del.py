import numpy as np
from numpy import random


# randint, rand, choice

# print(random.randint(100, size = (2,2)))
# print(random.rand(3,2,1))

print(random.choice(random.randint(100,200,size = 5), (2,2) ))
