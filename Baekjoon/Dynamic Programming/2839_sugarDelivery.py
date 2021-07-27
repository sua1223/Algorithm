n = int(input())
d = [0 for i in range(5001)]

d[3] = 1
d[5] = 1

for i in range(6, n+1):
    if i % 5 == 0:
        d[i] = d[i-5]+1
    elif i % 3 == 0:
        d[i] = d[i-3]+1
    else:
        if d[i-3] != 0 or d[i-5] != 0:
            d[i] = min(d[i-3]+1, d[i-5]+1)

if d[n] == 0:
    print(-1)
else:
    print(d[n])
