n = int(input())

total = 0

for i in range(n):
    row = list(map(int, input().rstrip().split()))
    total += row[i] - row[-(i+1)]
    
print(abs(total))
