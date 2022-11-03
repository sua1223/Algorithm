# 프로그래머스 단어 변환

from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    q = deque()
    q.append([begin, 0])
    
    while q:
        x, y = q.popleft()
        
        if x == target:
            return y
        
        for w in words:
            diff = 0
            for i in range(len(w)):
                if x[i] != w[i]:
                    diff += 1
            if diff == 1:
                q.append([w, y+1])
    
    return answer