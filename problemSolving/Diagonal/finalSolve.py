def diagonalDifference(arr):
    # Write your code here
    diag1Sum = 0
    diag2Sum = 0
    i, j = 0, 0
    while i < len(arr):
        diag1Sum += arr[i][j]
        diag2Sum += arr[i][-(j+1)]
        i += 1
        j += 1
    diff = abs(diag1Sum - diag2Sum)
    
    return diff
