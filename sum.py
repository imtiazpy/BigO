import time


def sumOfN(n):
    start = time.time()
    # theSum = 0
    # for i in range(1, n+1):
    #     theSum += i
    theSum = (n*(n+1))/2
    end = time.time()
    return theSum, end - start


print(sumOfN(100))