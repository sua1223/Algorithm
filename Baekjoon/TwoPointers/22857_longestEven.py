S, N = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
max_even_len = 0
while end < S:
	even_len = 0
	odd_len = 0
	for i in range(start, end+1):
		if arr[i] % 2 == 0:       # 짝수 이면
			even_len += 1
		else:
			odd_len += 1
	max_even_len = max(max_even_len, even_len)
	end += 1        # 끝 지점 이동
	if end - start > even_len + N:      # K를 초과하는 경우, 시작 지점 이동
		start += 1

print(max_even_len)