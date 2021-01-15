def solution(n):
    a=list(map(int, list(str(n))))
    return sum(a)

print(solution(123))
print(solution(987))