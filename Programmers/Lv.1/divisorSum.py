def solution(n):
    answer = 0
    for i in range (1, n+1):
        if n%i==0:
            answer= answer+i
    return answer

print(solution(12))
print(solution(5))