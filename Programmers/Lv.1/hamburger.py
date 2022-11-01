# 프로그래머스 햄버거 만들기

def solution(ingredient):
    answer = 0
    
    s = []
    
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            answer += 1
            for k in range(4):
                s.pop()
    
    return answer