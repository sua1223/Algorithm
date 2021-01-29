def solution(num):
    answer = 0
    while(True):
        if num == 1:
            break
        if answer == 500:
            return -1
        if num%2==0:
            num=num/2
            answer=answer+1
        else:
            num=num*3+1
            answer = answer + 1

    return answer

print(solution(6))
print(solution(16))
print(solution(626331))