# Devise an experiment to verify that the list index operator is O(1)


from timeit import Timer
import random

for i in range(10000, 1000000, 20000):
    t = Timer("x[(random.randrange(%d))]"%i, "from __main__ import random, x")

    x = list(range(i))
    index_time = t.timeit(number=1000)
    print("%d, %10.4f" % (i, index_time))
    # print(f'{i}, {index_time}')