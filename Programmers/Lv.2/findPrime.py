from itertools import permutations
import math

global prime
prime=list()

def isPrime(num):
    if(num==0 or num==1):
        return False
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    prime.append(num)
    return True

def solution(numbers):
    answer = 0
    num = list(numbers)
    for i in range(1,len(num)+1):
        a = list(map(''.join,permutations(num,i)))
        for j in a:
            if(prime.count(int(j))==1):
                continue
            if(isPrime(int(j))):
                answer=answer+1
    return answer

print(solution("011"))
print(solution("17"))
