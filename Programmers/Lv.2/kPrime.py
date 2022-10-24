import math

def convert_base(n, k):
    res = ''
    while n > 0:
        n, mod = divmod(n, k)
        res += str(mod)
    return res[::-1]

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    cvt = convert_base(n,k)
    zero = cvt.split('0')
    
    for n in zero:
        if len(n) > 0:
            if isPrime(int(n)):
                answer += 1
    return answer