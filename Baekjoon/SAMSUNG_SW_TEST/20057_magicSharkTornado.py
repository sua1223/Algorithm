N = int(input())

arr = []
for _ in range(N):
	arr_ = list(map(int, input().split()))
	arr.append(arr_)

# 시작 지점
x = N // 2
y = N // 2

# 좌하우상 (토네이도 순서)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

answer = 0

# 좌우로 토네이도가 움직일 때의 모래 계산
def LR_torn(x, y, sand, go):
	global answer
	dir = dy[go]

	# 1% 모래 구하기
	per_1 = int(sand * 0.01)
	nx = x - (-1 * dir)
	ny = y + (-1 * dir)
	if 0 <= nx < N and 0 <= ny < N:
		arr[nx][ny] += per_1
	else:
		answer += per_1
	nx = x + (-1 * dir)
	ny = y + (-1 * dir)
	if 0 <= nx < N and 0 <= ny < N:
		arr[nx][ny] += per_1
	else:
		answer += per_1

	# 10% 모래 구하기
	per_10 = int(sand * 0.1)
	nx = x - (-1 * dir)
	ny = y - (-1 * dir)
	if 0 <= nx < N and 0 <= ny < N:
		arr[nx][ny] += per_10
	else:
		answer += per_10
	nx = x + (-1 * dir)
	ny = y - (-1 * dir)
	if 0 <= nx < N and 0 <= ny < N:
		arr[nx][ny] += per_10
	else:
		answer += per_10

	# 7% 모래 구하기 (좌,우 공통)
	per_7 = int(sand * 0.07)
	if x - 1 >= 0:
		arr[x-1][y] += per_7
	else:
		answer += per_7
	if x + 1 < N:
		arr[x+1][y] += per_7
	else:
		answer += per_7

	# 2% 모래 구하기 (좌,우 공통)
	per_2 = int(sand * 0.02)
	if x - 2 >= 0:
		arr[x - 2][y] += per_2
	else:
		answer += per_2
	if x + 2 < N:
		arr[x + 2][y] += per_2
	else:
		answer += per_2

	# 5% 모래 구하기
	per_5 = int(sand * 0.05)
	ny = y - (-2 * dir)
	if 0 <= ny < N:
		arr[x][ny] += per_5
	else:
		answer += per_5

	sand_sum = per_2*2 + per_7*2 + per_10*2 + per_1*2 + per_5
	if 0 <= y + dy[go] < N:
		arr[x][y + dy[go]] += sand - sand_sum
	else:
		answer += sand - sand_sum
	arr[x][y] = 0
	# print(answer)

# 상하로 토네이도가 움직일 때의 모래 계산
def UD_torn(x, y, sand, go):
	global answer
	dir = dx[go]

	# 1% 모래 구하기
	per_1 = int(sand * 0.01)
	nx = x + (-1 * dir)
	ny = y - (-1 * dir)
	if 0 <= nx < N and 0 <= ny < N:
		arr[nx][ny] += per_1
	else:
		answer += per_1
	nx = x + (-1 * dir)
	ny = y + (-1 * dir)
	if 0 <= nx < N and 0 <= ny < N:
		arr[nx][ny] += per_1
	else:
		answer += per_1

	# 10% 모래 구하기
	per_10 = int(sand * 0.1)
	nx = x - (-1 * dir)
	ny = y - (-1 * dir)
	if 0 <= nx < N and 0 <= ny < N:
		arr[nx][ny] += per_10
	else:
		answer += per_10
	nx = x - (-1 * dir)
	ny = y + (-1 * dir)
	if 0 <= nx < N and 0 <= ny < N:
		arr[nx][ny] += per_10
	else:
		answer += per_10

	# 7% 모래 구하기 (상,하 공통)
	per_7 = int(sand * 0.07)
	if y - 1 >= 0:
		arr[x][y-1] += per_7
	else:
		answer += per_7
	if y + 1 < N:
		arr[x][y+1] += per_7
	else:
		answer += per_7

	# 2% 모래 구하기 (좌,우 공통)
	per_2 = int(sand * 0.02)
	if y - 2 >= 0:
		arr[x][y-2] += per_2
	else:
		answer += per_2
	if y + 2 < N:
		arr[x][y+2] += per_2
	else:
		answer += per_2

	# 5% 모래 구하기
	per_5 = int(sand * 0.05)
	nx = x - (-2 * dir)
	if 0 <= nx < N:
		arr[nx][y] += per_5
	else:
		answer += per_5

	sand_sum = per_2*2 + per_7*2 + per_10*2 + per_1*2 + per_5
	if 0 <= x + dx[go] < N:
		arr[x + dx[go]][y] += sand - sand_sum
	else:
		answer += sand - sand_sum
	arr[x][y] = 0
	# print(answer)

k = 0
re = 1
cnt = 0
tmp = 0
while True:
	for _ in range(2):
		for _ in range(re):
			if k % 2 == 0:
				LR_torn(x+dx[k], y+dy[k], arr[x+dx[k]][y+dy[k]], k)
			else:
				UD_torn(x+dx[k], y+dy[k], arr[x+dx[k]][y+dy[k]], k)
			x += dx[k]
			y += dy[k]
			if x == 0 and y == 0:
				break
		if x == 0 and y == 0:
			break
		k += 1
		if k == 4:
			k = 0
	re += 1
	if x == 0 and y == 0:
		break

print(answer)

