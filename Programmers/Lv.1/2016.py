def solution(a, b):
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    k = 0
    for i in range(0,a-1):
        k=k+month[i]
    k=k+b

    day=["THU","FRI","SAT","SUN","MON","TUE","WED"]
    idx=k%7
    return day[idx]

print(solution(5,24))