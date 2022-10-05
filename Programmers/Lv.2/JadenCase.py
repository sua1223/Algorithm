def solution(s):
    answer = ' '
    flag = 0
    for i in range(0, len(s)):
        if flag == 0 and s[i] != ' ':  # 대문자
            answer += s[i].upper()
            flag = 1
            continue
        if s[i] == ' ':
            flag = 0
            answer += ' '
        if flag == 1:   # 소문자
            answer += s[i].lower()
            continue

    return answer[1:]

print(solution("3people      unFollowed  me"))