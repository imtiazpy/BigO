def diagonalDifference(arr):
    # Write your code here
    diag1 = arr[0][0] + arr[1][1] + arr[2][2]
    diag2 = arr[0][2] + arr[1][1] + arr[2][0]

    differ = diag1 - diag2
    return abs(differ)
    

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

print(result)
