def diagonalDifference(arr):
    # Write your code here
    differ = 0
    for i in arr:
        for j in i:
           
            differ += arr[j] - arr[-(j+1)]
            
    return differ

# the solution is not correct. it's an attempt
# finalSolve.py has the solution