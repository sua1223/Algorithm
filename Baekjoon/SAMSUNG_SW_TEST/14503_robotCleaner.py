N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = []
for i in range(N):
    arr_ = list(map(int, input().split()))
    arr.append(arr_)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr[r][c] = 2      # 로봇의 시작 위치 청소 표시
answer = 1      # 현재 위치 청소 (+)
while True:
    cnt = 0
    while cnt < 4:
        cnt += 1
        # 왼쪽으로 돌기
        if d == 0:
            d = 3
        else:
            d -= 1
        # 인덱스 오류 방지
        if r + dx[d] > N or r + dx[d] < 0 or c + dy[d] > M or c + dy[d] < 0:
            continue
        # 회전 후 전진 시 청소하지 않은 빈공간 일 경우
        if arr[r + dx[d]][c + dy[d]] == 0:
            answer += 1
            r += dx[d]
            c += dy[d]
            arr[r][c] = 2   # 청소해주기
            cnt = 0         # 방향 카운팅 초기화
    # 4번 실행 끝날 경우
    if d < 2 and arr[r + dx[d + 2]][c + dy[d + 2]] == 1 or d >= 2 and arr[r + dx[d - 2]][c + dy[d - 2]] == 1:
        break       # 후진 했을 때 벽
    else:           # 후진 가능한 경우
        if d < 2:
            r += dx[d + 2]
            c += dy[d + 2]
        else:
            r += dx[d - 2]
            c += dy[d - 2]

print(answer)
