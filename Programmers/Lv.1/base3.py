# 프로그래머스 3진법 뒤집기

def solution(n):
    answer = 0
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)

    
    return int(rev_base,3)