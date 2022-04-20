from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

block_groups = []
answer = 0


def bfs(i, j, color):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    block_cnt, rainbow_cnt = 1, 0
    loc = []
    loc.append((i, j))
    rainbow = []
    while q:
        q_x, q_y = q.popleft()
        for a in range(4):
            x = q_x + dx[a]
            y = q_y + dy[a]
            if x < 0 or y < 0 or x > N - 1 or y > N - 1:  # 4방향의 위치가 arr 인덱스를 벗어날 때
                continue
            if (arr[x][y] == color or arr[x][y] == 0) and visited[x][y] == 0:
                if arr[x][y] == 0:
                    rainbow_cnt += 1
                    rainbow.append((x, y))
                else:
                    loc.append((x, y))
                visited[x][y] = 1
                block_cnt += 1
                q.append((x, y))
    loc.sort()
    if block_cnt >= 2:
        block_groups.append((block_cnt, rainbow_cnt, loc+rainbow))


def delete_blocks(loc):
    for i,j in loc:
        arr[i][j] = -2

def gravity(arr):
    for k in range(N):
        for i in range(N-1, 0, -1):
            for j in range(N):
                if i < 0 or j < 0 or i > N - 1 or j > N - 1:  # 4방향의 위치가 arr 인덱스를 벗어날 때
                    continue
                if arr[i][j] == -2 and arr[i-1][j] != -1:
                    arr[i][j] = arr[i-1][j]
                    arr[i-1][j] = -2

def rotate(arr):
    arr_temp = [[0] * N for _ in range(N)]
    x, y = 0, N-1
    for i in range(N):
        for j in range(N):
            arr_temp[i][j] = arr[x][y]
            x += 1
        y -= 1
        x = 0
    return arr_temp

while True:     # 오토플레이
    groups = []
    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            if arr[i][j] > 0 and visited[i][j] == 0:
                bfs(i, j, arr[i][j])        # 가장 큰 블럭 그룹 찾기
    block_groups.sort(reverse=True)
    if len(block_groups) == 0:
        break
    delete_blocks(block_groups[0][2])       # 블럭 제거
    answer += block_groups[0][0] ** 2       # 점수 계산
    gravity(arr)                            # 중력 작용
    arr = rotate(arr)                       # 반시계 회전
    gravity(arr)                            # 중력 작용
    block_groups.clear()

print(answer)


    