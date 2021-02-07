import math
def solution(n):
    r=int(math.sqrt(n))

    if r**2==n:
        return (r+1)**2
    else:
        return -1

print(solution(121))
print(solution(3))