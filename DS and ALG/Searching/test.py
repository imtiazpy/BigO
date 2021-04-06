def binarySearch(Array, Term):
    n = len(Array)
    left = 0
    right = n -1
    while left <= right:
        mid = (left + right) // 2
        if Array[mid] < Term:
            left = mid + 1
        elif Array[mid] > Term:
            right = mid - 1
        else:
            return mid
    
    return -1


array = [8, 9, 12, 15, 25, 30]

print(array)

term = int(input("which number are you looking for: "))

result = binarySearch(array, term)

if result == -1:
    print("number is not found")
else:
    # print(f"{term} is found at index {result}")
    print('{} is found at index {}'.format(term, result))

