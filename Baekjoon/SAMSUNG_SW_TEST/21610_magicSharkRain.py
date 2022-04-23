N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr_ = list(map(int, input().split()))
    arr.append(arr_)

info = []
for _ in range(M):
    info_ = list(map(int, input().split()))
    info_[0] -= 1
    info.append(info_)

# 8방향 x,y 좌표
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 비바라기 시전
cloud = [[0]*N for _ in range(N)]
cloud[N-1][0] = 1
cloud[N-1][1] = 1
cloud[N-2][0] = 1
cloud[N-2][1] = 1


# 1. 모든 구름이 d 방향으로 s칸 이동
def move_cloud(d, s):
    moved_cloud = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            nx = i + (dx[d] * s)
            ny = j + (dy[d] * s)
            while nx < 0 or ny < 0 or nx >= N or ny >= N:
                if nx < 0:
                    nx += N
                if ny < 0:
                    ny += N
                if nx >= N:
                    nx -= N
                if ny >= N:
                    ny -= N
            moved_cloud[nx][ny] = cloud[i][j]
    return moved_cloud


# 2. 각 구름에서 비가 내림
def raining(cloud):
    for i in range(N):
        for j in range(N):
            if cloud[i][j] == 1:
                arr[i][j] += 1


# 3&4. 구름 삭제 및 물복사버그 마법
def water_copy_bug():
    cloud_tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if cloud[i][j] == 1:
                cnt = 0
                for k in range(1, 8, 2):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    if arr[nx][ny] > 0:
                        cnt += 1
                arr[i][j] += cnt
                cloud[i][j] = 0
                cloud_tmp[i][j] = 1
    return cloud_tmp


# 5. 구름 생기기
def make_cloud(cloud_tmp):
    for i in range(N):
        for j in range(N):
            k = [i, j]
            if arr[i][j] >= 2 and cloud_tmp[i][j] == 0:
                arr[i][j] -= 2
                cloud[i][j] = 1


for i in range(M):
    cloud = move_cloud(info[i][0], info[i][1])
    raining(cloud)
    cloud_loc = water_copy_bug()
    make_cloud(cloud_loc)

answer = 0
for i in range(N):
    answer += sum(arr[i])

print(answer)
