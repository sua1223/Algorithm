# 프로그래머스 야간 전술보행

def solution(distance, scope, times):
    answer = 0
    
    for s in scope:
        s.sort()
    
    idx = 1
    while True:
        for i in range(len(scope)):
            if scope[i][0] <= idx <= scope[i][1]:
                cal = idx % (times[i][0] + times[i][1])
                if 0 < cal <= times[i][0]:
                    return idx
        idx += 1
        if idx == distance:
            return distance
    return answer