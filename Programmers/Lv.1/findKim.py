def solution(seoul):
    loc = seoul.index('Kim')
    answer = f"김서방은 {loc}에 있다"
    return answer

print(solution(["Jane","Kim"]))