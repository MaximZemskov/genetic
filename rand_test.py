import random
from collections import Counter

random_list = []

for i in xrange(10000000):
    random_list.append(random.randint(0, 9))

print Counter(random_list)
