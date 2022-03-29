N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = N
for i in A:
    if i - B < 0:
        continue
    answer += ((i - B) // C)
    if (i - B) % C != 0:
        answer += 1

print(answer)
