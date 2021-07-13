def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ""

    temp = ""
    for i in s:
        if i.isdigit():
            answer += i
        else:
            temp += i
            if temp in num:
                answer += str(num.index(temp))
                temp = ""

    return int(answer)


print(solution("one4seveneight"))
print(solution("23four5six7"))
