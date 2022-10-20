# 프로그래머스 이진 변환 반복하기

def solution(s):
    trans = 0
    zero = 0
    while s != "1":
        trans += 1
        cnt = s.count('1')
        zero += len(s) - cnt
        binaryNum = format(cnt, 'b')
        s = str(binaryNum)
    
    return [trans, zero]