def solution(x, n):
    answer = []
    k=x
    for i in range(0, n):
        answer.append(k)
        k+=x
    return answer

print(solution(2,5))
print(solution(4,3))
print(solution(-4,2))