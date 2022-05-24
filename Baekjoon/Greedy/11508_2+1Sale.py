N = int(input())
arr = []
for _ in range(N):
	arr.append(int(input()))

arr.sort(reverse=True)
answer = 0
for i in range(N):
	if i % 3 == 0 or i % 3 == 1:
		answer += arr[i]

print(answer)