import time
t = time.time()


def linear_search(myList, item):

    for i in range(len(myList)):
        
        if myList[i] == item:
            return i
    
    return False


myList = [14, 2, 5, 7, 22, 15]
print("Elements in the list: ", myList)

x = int(input("Enter your searching element: "))

result = linear_search(myList, x)

if result == False:
    print("Your element is not found in the list")
else:
    print(f"{x} found at the position {result}")


print("this code took: ", time.time()-t)

