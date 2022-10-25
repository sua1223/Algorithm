# 프로그래머스 피로도
import itertools
def solution(k, dungeons):
    answer = 0
    seq = []
    for i in range(len(dungeons)):
        seq.append(i)
    per = list(itertools.permutations(seq))
    cnt = 0
    for p in per:
        tmp = k
        cnt = 0
        for i in p:
            if dungeons[i][0] <= tmp:
                tmp -= dungeons[i][1]
                cnt += 1
            else:
                break
        
        answer = max(cnt, answer)    
    
    return answer