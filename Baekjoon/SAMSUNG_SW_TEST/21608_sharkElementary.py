N = int(input())
student = [[] for _ in range(N*N+1)]
seat = [[0]*N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 입력 받으면서 학생들 앉히기
for k in range(N*N):
    array = list(map(int, input().split()))
    num = array[0]
    student[num] = array[1:]       # 인덱스번호:앉을학생 [좋아하는 친구들 리스트] 형식으로 student 리스트에 담김
    if k == 0:
        seat[1][1] = num  # 첫번쨰 친구는 무조건 1,1
        continue
    # seat 탐색
    seat_info = []  # 각 자리의 정보 (빈자리 수 , 좋아하는 친구 수, 위치)를 담아줄 리스트
    for i in range(N):
        for j in range(N):
            if seat[i][j] != 0:
                continue
            empty_cnt, like_cnt = 0, 0
            for a in range(4):
                x = i + dx[a]
                y = j + dy[a]
                if x < 0 or y < 0 or x > N - 1 or y > N - 1:        # 4방향의 위치가 seat 인덱스를 벗어날 때
                    continue
                if seat[x][y] in student[num]:
                    like_cnt += 1
                if seat[x][y] == 0:
                    empty_cnt += 1
            seat_info.append((like_cnt, empty_cnt, i, j))
    seat_info.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))      # 좋아하는 학생 수(내림차순), 빈 자리 수 (내림차순), 행,열(오름차순) 정렬
    seat[seat_info[0][2]][seat_info[0][3]] = num

# 앉은 학생들의 만족도 구하기
answer = 0
for i in range(N):
    for j in range(N):
        like_cnt = 0
        for a in range(4):
            x = i + dx[a]
            y = j + dy[a]
            if x < 0 or y < 0 or x > N - 1 or y > N - 1:  # 4방향의 위치가 seat 인덱스를 벗어날 때
                continue
            if seat[x][y] in student[seat[i][j]]:
                like_cnt += 1
        if like_cnt > 0:
            answer += 10 ** (like_cnt - 1)
print(answer)
