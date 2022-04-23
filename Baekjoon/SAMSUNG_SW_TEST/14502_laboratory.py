import copy
from itertools import combinations
from collections import deque

N, M = map(int, input().split())
arr = []
wall_loc = []
virus_loc = []
for i in range(N):
    arr_ = list(map(int, input().split()))
    for j in range(M):
        if arr_[j] == 0:
            wall_loc.append([i, j])
        if arr_[j] == 2:
            virus_loc.append([i, j])
    arr.append(arr_)

# 아래, 오른쪽, 위, 왼쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 벽을 세울 tmp arr 생성
def tmp_wall(arr):
    arr_tmp = copy.deepcopy(arr)
    return arr_tmp

# 생성한 조합에 벽 세우기
def build_wall(arr_wall, wall_list):
    for i in range(len(wall_list)):
        arr_wall[wall_list[i][0]][wall_list[i][1]] = 1
    return arr_wall

# 바이러스 BFS 이후 빈 공간 counting
def bfs(arr_virus):
    q = deque()
    for a in range(len(virus_loc)):
        q.append([virus_loc[a][0], virus_loc[a][1]])
    while q:
        q_x, q_y = q.popleft()
        for i in range(4):
            x = q_x + dx[i]
            y = q_y + dy[i]
            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            if arr_virus[x][y] == 0:
                arr_virus[x][y] = 2
                q.append([x, y])
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr_virus[i][j] == 0:
                cnt += 1
    return cnt


wall_comb = list(combinations(wall_loc, 3))     # 벽이 생길 수 있는 모든 조합
max_safe = 0
for x in range(len(wall_comb)):
    safe_cnt = 0
    arr_wall = tmp_wall(arr)
    arr_virus = build_wall(arr_wall, wall_comb[x])
    safe_cnt = bfs(arr_virus)
    if safe_cnt > max_safe:     # 최대값 구하기
        max_safe = safe_cnt

print(max_safe)

