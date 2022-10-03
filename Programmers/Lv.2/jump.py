# start time 06:34 /

def comb(n, k):
    com = 1
    for i in range(n, n-k, -1):
        com *= i

    mod = 1
    for i in range(1, k+1):
        mod *= i

    return com // mod


def solution(n):
    answer = 1  # 다 한칸 뛰기
    if n % 2 == 0:  # 다 두칸 뛰기
        answer += 1

    cnt_2 = 0
    while True:
        cnt_2 += 1
        if n - cnt_2*2 <= 0:
            break
        k = n - cnt_2 * 2
        answer += comb(k+cnt_2, cnt_2)

    return answer % 1234567

print(solution(3))