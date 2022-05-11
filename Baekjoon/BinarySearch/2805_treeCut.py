N, M = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, max(arr)

while start < end:
	tree_sum = 0
	height = (start+end) // 2
	for i in range(N):
		if arr[i] > height:
			tree_sum += arr[i] - height
	if start == height or end == height:
		break
	if tree_sum >= M:
		start = height
	else:
		end = height
print(height)