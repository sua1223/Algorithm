import math
def isPrime(n):
    for i in range (2, int(math.sqrt(float(n)))+1):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if isPrime(i):
            answer = answer+1
    return answer

print(solution(5))
