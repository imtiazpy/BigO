def diagonalDifference(arr):
    # Write your code here
    diag1 = 0
    diag2 = 0
    for i in arr:
        for j in i:
           
            diag1 += arr[i][j]
            diag2 += arr[i][-(j+1)]
    diff = abs(diag1 - diag2)

            
    return diff

