n, m = map(int, input().split())

result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    min_value = min(arr)
    result = max(min_value, result)
    
print(result)