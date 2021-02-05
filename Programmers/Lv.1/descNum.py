def solution(n):
    a=list(str(n))
    a.sort(reverse=True)
    answer=''.join(a)
    return int(answer)

print(solution(118372))