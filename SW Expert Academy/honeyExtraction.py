from itertools import combinations

T = int(input())

for test_case in range(1, T+1):
	N, M, C = map(int, input().split())
	arr = []

	for _ in range(N):
		arr_ = list(map(int, input().split()))
		for i in range(N):
			if arr_[i] > C:     # 한 칸의 꿀이 담을 수 있는 양 보다 크면 0으로 생각
				arr_[i] = 0
		arr.append(arr_)

	honey_list = []


	def calc_honey(i, j, m):
		honey = 0
		earn = 0
		tmp = [[i, j]]
		tmp.append([i, j+m-1])
		tmp2 = []
		for k in range(m):
			honey += arr[i][j+k]
			earn += arr[i][j+k]**2
			tmp2.append(arr[i][j+k])

		if honey > C:
			max_earn = 0
			for k in range(1, M):
				a = list(combinations(tmp2, k))
				for b in a:
					sum_honey = sum(b)
					if sum_honey <= C:
						earn = 0
						for c in range(len(b)):
							earn += b[c]**2
						max_earn = max(earn, max_earn)
			tmp.append(max_earn)
		else:
			tmp.append(earn)
		honey_list.append(tmp)


	for i in range(N):
		for j in range(N):
			if j+M > N:        # 인덱스 오류 방지
				continue
			calc_honey(i, j, M)

	make_earn = list(combinations(honey_list, 2))
	make_earn.sort(key=lambda x: -(x[0][2]+x[1][2]))
	for i in range(len(make_earn)):
		# 위치가 겹칠 경우
		if make_earn[i][0][0][0] == make_earn[i][1][0][0] and make_earn[i][0][0][1] <= make_earn[i][1][0][1] <= make_earn[i][0][1][1]:
			continue
		else:
			answer = make_earn[i][0][2] + make_earn[i][1][2]
			break

	print('#'+str(test_case)+' '+str(answer))

