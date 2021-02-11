def solution(s, n):
    a=list(s)
    for i in range (0,len(a)):
        if a[i].isupper():
            a[i]=chr((ord(a[i])-ord('A')+n)%26+ord('A'))
        elif a[i].islower():
            a[i]=chr((ord(a[i])-ord('a')+n)%26+ord('a'))
    answer=(''.join(a))
    return answer

print(solution("AB",1))
print(solution("z",1))
print(solution("a B z",4))