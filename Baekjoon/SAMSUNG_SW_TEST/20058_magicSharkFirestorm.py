import copy
from collections import deque

N, Q = map(int, input().split())
arr = []
X = 2**N
for _ in range(X):
	arr_ = list(map(int, input().split()))
	arr.append(arr_)
l_list = list(map(int, input().split()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for k in range(len(l_list)):
	arr_len = 2**l_list[k]
	tmp = [[0]*X for _ in range(X)]
	melt = [[0] * X for _ in range(X)]
	for a in range(0, X, arr_len):
		for b in range(0, X, arr_len):
			for i in range(arr_len):
				for j in range(arr_len):
					tmp[a+j][b+arr_len-i-1] = arr[a+i][b+j]
	arr = copy.deepcopy(tmp)
	for i in range(X):
		for j in range(X):
			cnt = 0
			for k in range(4):
				nx = i + dx[k]
				ny = j + dy[k]
				if nx < 0 or ny < 0 or nx >= X or ny >= X:
					cnt += 1
					continue
				if arr[nx][ny] <= 0:
					cnt += 1
			if cnt > 1 and arr[i][j] > 0:
				melt[i][j] -= 1
	for i in range(X):
		for j in range(X):
			arr[i][j] += melt[i][j]

# 얼음 합 구하기
ice_sum = 0
for i in range(X):
	ice_sum += sum(arr[i])
print(ice_sum)

max_ice = 0
for i in range(X):
	for j in range(X):
		if arr[i][j] == 0:
			continue
		q = deque()
		q.append([i, j])
		visited = [[0]*X for _ in range(X)]
		ice_cnt = 1
		while q:
			qx, qy = q.popleft()
			visited[qx][qy] = 1
			for k in range(4):
				nx = qx + dx[k]
				ny = qy + dy[k]
				if nx < 0 or ny < 0 or nx >= X or ny >= X:
					continue
				if arr[nx][ny] > 0 and visited[nx][ny] == 0:
					ice_cnt += 1
					visited[nx][ny] = 1
					q.append([nx, ny])
		if max_ice < ice_cnt:
			max_ice = ice_cnt

print(max_ice)