# It describes outcomes of multi-nomial scenarios unlike binomial where 
# scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.

# It has three parameters:
# n - number of possible outcomes (e.g. 6 for dice roll).
# pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
# size - The shape of the returned array.

from numpy import random
d=random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(d)
# [1 0 2 1 1 1] if this is output then:
# This means:

# Outcome 1 occurred 1 time.
# Outcome 2 occurred 0 times.
# Outcome 3 occurred 2 times.
# Outcome 4 occurred 1 time.
# Outcome 5 occurred 1 time.
# Outcome 6 occurred 1 time.  (yani 1 dice ko 6 times roll kia or us m "ek dfa 1 aya"),
# ("2 aya hi nhi"), ("do dfa 3 aya") ,(ek dfa 4 aya) ,(ek dfa 5 aya) ,(ek dfa 6 aya).

# Note: As they are generalization of binomial distribution their visual representation
# and similarity of normal distribution is same as that of multiple binomial distributions.