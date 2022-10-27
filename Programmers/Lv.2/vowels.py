# 프로그래머스 모음 사전

from itertools import product

def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    tmp = []
    for i in range(1, 6):
        tmp += list(product(alpha, repeat = i))
    
    dict = []
    for k in tmp:
        dict.append(''.join(k))
    
    dict.sort()
    
    return dict.index(word) + 1