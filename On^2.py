# In the following code the number of operation increases quadratically as the number 
# of elements increases. So the time complexity is O(n^2)


nums = ['one', 'two', 'three', 'four', 'five']

for i in range(len(nums)):
    for j in range(len(nums)):
        print(nums[i], nums[j])

