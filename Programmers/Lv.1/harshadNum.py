def solution(x):
    a=str(x)
    b=list(a)
    intList=list(map(int,b))
    if x%sum(intList)==0:
        return True
    else:
        return False

print(solution(10))
print(solution(12))
print(solution(11))