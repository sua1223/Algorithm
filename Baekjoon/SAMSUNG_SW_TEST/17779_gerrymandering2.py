N = int(input())
arr = []
total_people = 0
min_people = float('inf')

def solution(x, y, d1, d2):

    global min_people
    loc = [[0] * (N + 1) for _ in range(N + 1)]

    # 경계선 구하기
    for i in range(d1+1):
        loc[x+i][y-i] = 5
    for i in range(d2+1):
        loc[x+i][y+i] = 5
    for i in range(d2+1):
        loc[x+d1+i][y-d1+i] = 5
    for i in range(d1+1):
        loc[x+d2+i][y+d2-i] = 5

    loc_people = [0, 0, 0, 0, 0]

    # 1번 선거구
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if loc[i][j] == 5:
                break
            loc[i][j] = 1
            loc_people[0] += arr[i - 1][j - 1]

    # 2번 선거구
    for i in range(1, x+d2):
        for j in range(N, y, -1):
            if loc[i][j] == 5:
                break
            loc[i][j] = 2
            loc_people[1] += arr[i - 1][j - 1]

    # 3번 선거구
    for i in range(x+d1, N+1):
        for j in range(1, y-d1+d2):
            if loc[i][j] == 5:
                break
            loc[i][j] = 3
            loc_people[2] += arr[i - 1][j - 1]

    # 4번 선거구
    for i in range(x+d2+1, N+1):
        for j in range(N, y-d1+d2-1, -1):
            if loc[i][j] == 5:
                break
            loc[i][j] = 4
            loc_people[3] += arr[i - 1][j - 1]

    loc_people[4] = total_people - sum(loc_people)
    tmp = max(loc_people) - min(loc_people)

    # for i in range(N+1):
    #     if loc[3][5] == 5 and loc[6][4] == 5 and loc[5][5] == 5 :
    #         print(loc[i])
    # print()
    if tmp < min_people:
        min_people = tmp


for _ in range(N):
    arr_ = list(map(int, input().split()))
    total_people += sum(arr_)
    arr.append(arr_)

for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                # d1, d2 설정 (방법 1)
                if x + d1 + d2 > N:
                    continue
                if y - d1 < 1:
                    continue
                if y + d2 > N:
                    continue
                solution(x, y, d1, d2)

print(min_people)