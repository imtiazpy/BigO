import time

t = time.time()
# In this code base we're going to search a particular item from a list using binary search Algorithm

from math import floor

def binary_search(Array, Search_Term):
    n = len(Array)
    Left = 0
    Right = n-1
    
    while Left <= Right:
        mid = floor((Left+Right)/2)
        if Array[mid] < Search_Term:
            Left = mid + 1
        elif Array[mid] > Search_Term:
            Right = mid - 1
        else:
            return mid

    return -1




# Insert your array here
A = [1,2,3,4,7,9,12,14,18]
print("Elements in the list: ", A)
# term to be searched
term = int(input("Enter the element you want: "))

index = binary_search(A, term)
if index >= 0:
    print("{} is at index {}".format(A[index], index))
else:
    print("Search term not found")


print('This code took:', time.time()-t)