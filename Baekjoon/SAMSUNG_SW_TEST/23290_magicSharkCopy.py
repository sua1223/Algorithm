M, S = map(int, input().split())
fish = []
for _ in range(M):
	fish_ = list(map(int, input().split()))
	for i in range(3):
		fish_[i] -= 1
	fish.append(fish_)
shark_x, shark_y = map(int, input().split())
shark_x -= 1
shark_y -= 1
smell = [[0]*4 for _ in range(4)]
fish_smell_list = []
delete_fish_list = []
move_shark_list = []


def detect_smell(i, j):
	if smell[i][j] == 0:
		return True
	return False


def detect_shark(i, j):
	global shark_x, shark_y
	if i == shark_x and j == shark_y:
		return False
	return True


# 상좌하우 조합 만드는 함수
def make_shark_move():
	for a in range(4):
		for b in range(4):
			for c in range(4):
				move_shark_list.append([a, b, c])


# 냄새 남기고 물고기 없애기
def make_smell(arr):
	for i in range(len(arr)):
		if i < 0:
			continue
		x, y = arr[i][1], arr[i][2]
		smell[x][y] += 1


# 3번 작업 - 상어 이동
def move_shark():
	global shark_x, shark_y
	sx = [-1, 0, 1, 0]
	sy = [0, -1, 0, 1]
	shark_list = []
	for k in range(len(move_shark_list)):
		x, y = shark_x, shark_y
		delete_fish = []
		for z in move_shark_list[k]:
			nx = x + sx[z]
			ny = y + sy[z]
			if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
				break
			for i in range(len(fish)):
				if fish[i][0] == nx and fish[i][1] == ny:
					tmp = [i, nx, ny]
					if tmp not in delete_fish_list:
						if tmp not in delete_fish:
							delete_fish.append(tmp)
			x, y = nx, ny
		shark_list.append([delete_fish, move_shark_list[k][0], move_shark_list[k][1], move_shark_list[k][2], x, y])
	shark_list.sort(key=lambda x: (-len(x[0])))     # 제거된 물고기, 사전 순 정렬
	shark_x, shark_y = shark_list[0][4], shark_list[0][5]       # 글로벌 변수 상어 위치 업데이트
	fish_smell_list.append(shark_list[0][0])        # 냄새 남기는 물고기 리스트
	# 제거된 물고기 리스트
	for p in range(len(shark_list[0][0])):
		delete_fish_list.append(shark_list[0][0][p])
	make_smell(shark_list[0][0])


def delete_smell(cnt):
	if cnt > 2:
		for k in range(len(fish_smell_list[cnt-3])):
			x, y = fish_smell_list[cnt-3][k][1], fish_smell_list[cnt-3][k][2]
			smell[x][y] -= 1


def copy_fish():
	for k in range(len(to_copy)):
		fish.append(to_copy[k])


dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
make_shark_move()
prac = 0
flag = 0
while prac < S:
	to_copy = []
	# 2번 작업 - 물고기 이동
	for k in range(len(fish)):
		x, y, d = fish[k][0], fish[k][1], fish[k][2]
		for p in range(len(delete_fish_list)):
			if k == delete_fish_list[p][0]:
				flag = 1
		if flag == 1:
			flag = 0
			continue
		to_copy.append([x, y, d])
		cnt = 1
		while True:
			nx = x + dx[d]
			ny = y + dy[d]
			# 물고기가 격자 안에 있고, 상어와 냄새가 없는 경우
			if 0 <= nx < 4 and 0 <= ny < 4 and detect_shark(nx, ny) and detect_smell(nx, ny):
				fish[k][0], fish[k][1], fish[k][2] = nx, ny, d
				break
			else:
				cnt += 1
				if cnt == 8:
					break
				d -= 1
				if d == -1:
					d = 7

	move_shark()
	prac += 1
	delete_smell(prac)
	copy_fish()

print(len(fish) - len(delete_fish_list))
