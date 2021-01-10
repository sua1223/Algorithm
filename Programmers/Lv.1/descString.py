def solution(s):
    l=list(s)
    l.sort(reverse=True)
    answer="".join(l)
    return answer

print(solution("Zbcdefg"))