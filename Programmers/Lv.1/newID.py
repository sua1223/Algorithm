def check(a):
    if a.isdigit():
        return True
    if a.isalpha():
        return True
    if a=='.' or a=='-' or a=='_':
        return True
    return False

def solution(new_id):
    answer = ''
    new_id=new_id.lower()
    for i in range (0,len(new_id)):
        if check(new_id[i]):
            answer=answer+new_id[i]

    s=list(answer)

    j=0
    while j<len(s)-1:
        if s[j]=='.' and s[j+1]=='.':
            del s[j]
            j-=1
        j+=1

    if s[0]=='.':
        del s[0]
    if len(s)>0:
        if s[len(s)-1]=='.':
            del s[len(s)-1]

    if len(s)==0:
        return "aaa"
    if len(s)>15:
        del s[15:]
        if s[14]=='.':
            del s[14]
    if len(s)<3:
        while(len(s)<3):
            s.append(s[len(s)-1])

    answer=(''.join(s))
    return answer

print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("abcdefghijklmn.p"))