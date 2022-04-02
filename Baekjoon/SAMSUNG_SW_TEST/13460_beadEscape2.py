from collections import deque

N, M = map(int, input().split())
board = [input() for _ in range(N)]
# checked_red = [[0]*M for _ in range(N)]
# checked_blue = [[0]*M for _ in range(N)]
print(board)

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red_x = i
            red_y = j
            # checked_red[i][j] = 1
        if board[i][j] == 'B':
            blue_x = i
            blue_y = j
            # checked_blue[i][j] = 1
            break
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()
q.append((red_x, red_y, blue_x, blue_y))
answer = 0
while q:
    red_x, red_y, blue_x, blue_y = q.popleft()
    if answer > 10:     # 횟수가 10이 넘는 경우
        print(-1)
        break

    if board[red_x][red_y] == 'O':      # 빨간색 구슬이 O에 도착한 경우
        print(answer)
        break
    
    for i in range(4):      # 상,하,좌,우 의 움직임
        # 빨간 구슬
        while True:
            red_x += dx[i]
            red_y += dy[i]
            if board[red_x][red_y] == '#':
                red_x -= dx[i]
                red_y -= dy[i]
                break
            elif board[red_x][red_y] == 'O':
                break
        # 파란 구슬
        while True:
            blue_x += dx[i]
            blue_y += dy[i]
            if board[blue_x][blue_y] == '#':
                blue_x -= dx[i]
                blue_y -= dy[i]
                break
            elif board[blue_x][blue_y] == 'O':
                break
        answer += 1
    q.append((red_x, red_y, blue_x, blue_y))
