def solution(land):
	for i in range(1, len(land)):
		for j in range(0, 4):
			cur_max = 0
			for k in range(0, 4):
				if j == k:
					continue
				if land[i][j] + land[i-1][k] > cur_max:
					cur_max = land[i][j] + land[i-1][k]
			land[i][j] = cur_max

	return(max(land[len(land)-1]))


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))