# 프로그래머스 게임 맵 최단거리

from collections import deque

def solution(maps):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    n, m = 0, 0
    n = len(maps)
    m = len(maps[0])
    visited = []
    for i in range(n):
        v_ = []
        for j in range(m):
            v_.append(0)
        visited.append(v_)
    
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    cnt = 0
    flag = 0
    answer = 0
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[qx][qy] + 1
                    q.append([nx, ny])
                    
            if nx == n-1 and ny == m-1:
                flag = 1
    
    if flag == 0:
        return -1
    
    return visited[n-1][m-1]