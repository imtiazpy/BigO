from timeit import Timer

# 4 different ways we might generate a list
# each has their own time complexity

# for loop and concatenate 
def test1():
    l = []
    for i in range(1000):
        l += [i]
    
# using append()
def test2():
    l = []
    for i in range(1000):
        l.append(i)

# List comprehension
def test3():
    l = [i for i in range(1000)]


# using the range function wrapped by a call to the list constructor
def test4():
    l = list(range(1000))



# to calculate the execution time of each func()

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")


