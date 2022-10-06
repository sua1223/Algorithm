def solution(n):
	answer = 0
	while n > 0:
		if n % 2 != 0:
			answer += 1
			n -= 1
		else:
			n /= 2

	return answer

print(solution(6))