n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

result = 0

if arr[0] == arr[1]:
    result = arr[0]*m
else:
    div = m // (k+1)
    mod = m % (k+1)
    result = (arr[0] * k + arr[1]) * div + arr[0] * mod

print(result)
