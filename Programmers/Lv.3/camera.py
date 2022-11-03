# 프로그래머스 단속카메라

def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x:x[1])
    
    cur = -30001
    for r in routes:
        if r[0] <= cur <= r[1]:
            continue
        else:
            cur = r[1]
            answer += 1
  
    return answer