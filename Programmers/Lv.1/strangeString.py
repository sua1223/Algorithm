def solution(s):
    answer=''
    a=s.split(" ")
    for i in range (0, len(a)):
        for j in range (0, len(a[i])):
            k = a[i][j]
            if j%2==0:
                k=k.upper()
                answer=answer+k
            else:
                k=k.lower()
                answer=answer+k
        answer=answer+' '
    return answer[:-1]

print(solution("try hello world"))