def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def solution(n, m):
    answer = []
    if n>m:
        tmp=n
        n=m
        m=tmp
    d=gcd(n,m)
    answer.append(d)
    answer.append(int(n*m/d))
    return answer

print(solution(3,12))
print(solution(2,5))