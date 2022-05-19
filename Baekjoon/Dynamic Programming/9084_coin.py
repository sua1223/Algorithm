T = int(input())

for _ in range(T):
	N = int(input())
	arr = list(map(int, input().split()))
	M = int(input())
	d = [[0]*(M+1) for _ in range(N+1)]

	for i in range(N+1):
		d[i][0] = 1

	# x원 짜리로 y원을 만들 수 있는 가지 수 갱신
	for i in range(1, N+1):
		for j in range(1, M+1):
			d[i][j] = d[i-1][j]
			if j-arr[i-1] >= 0:
				d[i][j] += d[i][j-arr[i-1]]

	print(d[N][M])