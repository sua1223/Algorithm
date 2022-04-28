from collections import deque

N, L, R = map(int, input().split())
arr = []

for _ in range(N):
	arr_ = list(map(int, input().split()))
	arr.append(arr_)


def bfs(i, j):
	visited[i][j] = 1
	dx = [-1, 0, 1, 0]
	dy = [0, -1, 0, 1]

	q = deque()
	tmp = []
	q.append((i, j))
	people = arr[i][j]
	tmp.append([i, j])
	while q:
		qx, qy = q.popleft()
		for k in range(4):
			nx = qx + dx[k]
			ny = qy + dy[k]
			if nx < 0 or ny < 0 or nx >= N or ny >= N:
				continue
			if visited[nx][ny] == 0 and L <= abs(arr[qx][qy] - arr[nx][ny]) <= R:        # 인구 이동이 가능한 상황
				visited[nx][ny] = 1
				people += arr[nx][ny]
				q.append((nx, ny))
				tmp.append([nx, ny])
	if len(tmp) > 1:        # 열리는 국가 없이 초기 위치만 담길 경우
		open_list.append(tmp)
		open_people.append(people)


answer = 0
while True:
	visited = [[0]*N for _ in range(N)]
	open_list = []
	open_people = []
	for i in range(N):
		for j in range(N):
			if visited[i][j] == 1:
				continue
			bfs(i, j)

	if len(open_people) == 0:
		break

	for k in range(len(open_people)):
		for a in range(len(open_list[k])):
			x = open_list[k][a][0]
			y = open_list[k][a][1]
			arr[x][y] = open_people[k] // len(open_list[k])

	answer += 1

print(answer)



