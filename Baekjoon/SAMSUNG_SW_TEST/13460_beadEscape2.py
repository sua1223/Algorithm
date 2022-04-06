from collections import deque

N, M = map(int, input().split())
board = [input() for _ in range(N)]
checked_red = [[0]*M for _ in range(N)]
checked_blue = [[0]*M for _ in range(N)]
red_x, red_y, blue_x, blue_y = 0, 0, 0, 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red_x, red_y = i, j
        if board[i][j] == 'B':
            blue_x, blue_y = i, j
            break
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
red_cnt, blue_cnt = 0, 0
q = deque()
q.append((red_x, red_y, red_cnt, blue_x, blue_y, blue_cnt))
answer = 0
while q:
    for _ in range(len(q)):
        qred_x, qred_y, qred_cnt, qblue_x, qblue_y, qblue_cnt = q.popleft()
        checked_red[qred_x][qred_y] = 1       # 빨간 구슬의 방문점(시작점) 체크
        checked_blue[qblue_x][qblue_y] = 1        # 파란 구슬의 방문점(시작점) 체크

        if answer > 10:  # 횟수가 10이 넘는 경우
            print(-1)
            exit()
        if board[qred_x][qred_y] == 'O':    #  구슬이 O에 도착한 경우
            print(answer)
            exit()

        for i in range(4):       # 상,하,좌,우 의 움직임
            # 빨간 구슬
            red_x, red_y, red_cnt = qred_x, qred_y, qred_cnt    # 방향을 틀게되는 지점으로 초기화 하는 효과
            while True:
                red_x += dx[i]
                red_y += dy[i]
                if board[red_x][red_y] == '#':      # 벽에 닿으면 한 칸 뒤로
                    red_x -= dx[i]
                    red_y -= dy[i]
                    break
                elif board[red_x][red_y] == 'O':
                    break
                else:
                    red_cnt += 1
            # 파란 구슬
            blue_x, blue_y, blue_cnt = qblue_x, qblue_y, qblue_cnt
            while True:
                blue_x += dx[i]
                blue_y += dy[i]
                if board[blue_x][blue_y] == '#':
                    blue_x -= dx[i]
                    blue_y -= dy[i]
                    break
                elif board[blue_x][blue_y] == 'O':
                    break
                else:
                    blue_cnt += 1
            if board[blue_x][blue_y] == 'O':    # 파란 구슬이 먼저 들어 가는 경우 무시
                continue
            if red_x == blue_x and red_y == blue_y:     # 움직임 이후 두 구슬이 같은 자리에 있게 되는 경우 (예제 2)
                if red_cnt > blue_cnt:      # 움직인 수를 비교하여 더 많이 움직인 구슬을 한 칸 뒤로
                    red_x -= dx[i]
                    red_y -= dy[i]
                else:
                    blue_x -= dx[i]
                    blue_y -= dy[i]
            if checked_red[red_x][red_y] == 0 or checked_blue[blue_x][blue_y] == 0:     # 방문 안했던 지점
                checked_red[red_x][red_y] = 1
                checked_blue[blue_x][blue_y] = 1
                q.append((red_x, red_y, red_cnt, blue_x, blue_y, blue_cnt))
    answer += 1
print(-1)       # 실패 (예제 7)

