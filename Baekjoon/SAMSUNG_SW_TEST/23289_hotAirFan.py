R, C, K = map(int, input().split())
arr = []
fan = []
todo = []
for r in range(R):
	arr_ = list(map(int, input().split()))
	for c in range(C):
		if arr_[c] != 0 and arr_[c] != 5:
			fan.append([r, c, arr_[c]-1])
			arr_[c] = 0
		if arr_[c] == 5:
			arr_[c] = 0
			todo.append([r, c])
	arr.append(arr_)
W = int(input())
wall = []
for _ in range(W):
	x, y, t = map(int, input().split())
	x -= 1
	y -= 1
	arr_ = [x, y, t]
	wall.append(arr_)


# 상하(0) 좌우(1) -1, 0
def detect_wall(x, y, d):
	for i in range(len(wall)):
		# print(x, y, wall[i][0], wall[i][1], wall[i][2])
		if wall[i][2] == 0:
			if dx[d] == 1:
				if wall[i][0] == x and wall[i][1] == y:
					return False
			if dx[d] == -1:
				if wall[i][0] == x - dx[d] and wall[i][1] == y:
					return False
		if wall[i][2] == 1:
			if dy[d] == 1:
				if wall[i][0] == x and wall[i][1] == y:
					return False
			if dy[d] == -1:
				if wall[i][0] == x and wall[i][1] == y - dy[d]:
					return False
	return True


def wind(x, y, d):
	a = 0
	for k in range(1, 6):
		nx = x + dx[d] * k
		ny = y + dy[d] * k
		if 0 <= nx < R and 0 <= ny < C:
			for i in range(-a, a+1):
				kx = nx + dy[d] * i
				ky = ny + dx[d] * i
				if 0 <= kx < R and 0 <= ky < C and detect_wall(kx, ky, d):
					if arr[kx][ky] >= 0:
						arr[kx][ky] += 6 - k
			a += 1


def control():
	tmp = [[0]*C for _ in range(R)]
	
	# 오른쪽으로 이동하며 가로 인접 온도 조절
	for i in range (R):
		for j in range(C-1):
			if [i, j, 1] not in wall:
				dif = abs(arr[i][j] - arr[i][j+1]) // 4
				if arr[i][j] > arr[i][j+1]:
					tmp[i][j] -= dif
					tmp[i][j+1] += dif
				else:
					tmp[i][j] += dif
					tmp[i][j+1] -= dif

	#아래로 이동하며 세로 인접 온도 조절
	for i in range(R-1):
		for j in range(C):
			if [i, j, 0] not in wall:
				dif = abs(arr[i][j] - arr[i+1][j]) // 4
				if arr[i+1][j] > arr[i][j]:
					tmp[i+1][j] -= dif
					tmp[i][j] += dif
				else:
					tmp[i+1][j] += dif
					tmp[i][j] -= dif

	for i in range(R):
		for j in range(C):
			arr[i][j] += tmp[i][j]
			if i == 0:
				arr[i][j] -= 1
			elif i == R-1:
				arr[i][j] -= 1
			elif j == 0 or j == C-1:
				arr[i][j] -= 1

			if arr[i][j] < 0:
				arr[i][j] = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
answer = 0
while True:
	if answer > 100:
		break
	# 우(0) 좌(1) 상(2) 하(3)
	for k in range(len(fan)):
		x, y, d = fan[k][0], fan[k][1], fan[k][2]
		wind(x, y, d)
	control()
	answer += 1
	print(arr)
	cnt = 0
	for k in range(len(todo)):
		x, y = todo[k][0], todo[k][1]
		if arr[x][y] >= K:
			cnt += 1
	if cnt == len(todo):
		break

print(arr)
print(answer)