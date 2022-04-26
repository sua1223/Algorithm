import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr_ = list(map(int, input().split()))
    arr.append(arr_)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[0]*M for _ in range(N)]
max_sum = 0

def dfs(i, j, dsum, cnt):
    global max_sum
    if cnt == 4:
        if dsum > max_sum:
            max_sum = dsum
        return

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if ni < 0 or nj < 0 or ni >= N or nj >= M:
            continue
        if visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj, dsum+arr[ni][nj], cnt+1)
            visited[ni][nj] = 0


# ㅏ, ㅓ, ㅗ, ㅜ
def exception(i, j):
    global max_sum
    for p in range(4):
        dsum = arr[i][j]
        for k in range(4):
            if p == k:
                continue
            if i + dx[k] < 0 or j + dy[k] < 0 or i + dx[k] >= N or j + dy[k] >= M:
                dsum = 0
                break
            dsum += arr[i + dx[k]][j + dy[k]]

        if max_sum < dsum:
            max_sum = dsum


for i in range(N):
    for j in range(M):
        exception(i, j)
        visited[i][j] = 1
        dfs(i, j, arr[i][j], 1)
        visited[i][j] = 0

print(max_sum)






