from collections import deque

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr_ = list(map(int, input().split()))
    arr.append(arr_)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

max_sum = 0
for i in range(N):
    for j in range(M):
        q = deque()
        q.append([i, j])
        cnt = 1
        sum = arr[i][j]
        visited = []
        visited.append([i, j])
        while q:
            x, y = q.popleft()
            for k in range(4):
                if x + dx[k] < 0 or y + dy[k] < 0 or x + dx[k] >= N or y + dy[k] >= M:
                    continue
                loc = [x + dx[k], y + dy[k]]
                if loc in visited:
                    continue
                x += dx[k]
                y += dy[k]
                cnt += 1
                sum += arr[x][y]
                visited.append([x, y])
                q.append([x, y])
                if cnt == 4:
                    break
            if cnt == 4:
                break
        if max_sum < sum:
            max_sum = sum
            print(sum, visited)

print(max_sum)




