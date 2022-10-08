# 프로그래머스 할인 행사
# start time 02:26      end time 02:34

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        new_discount = discount[i:i+10]
        cnt = 0
        for k in range(len(want)):
            if new_discount.count(want[k]) != number[k]:
                break
            cnt += 1
        if cnt == len(want):
            answer += 1
    return answer