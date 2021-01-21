def solution(n):
    n=str(n)
    answer = list(n);
    answer.reverse()
    answer = list(map(int, answer))
    return answer

print(solution(12345))