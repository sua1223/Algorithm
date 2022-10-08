def solution(n, a, b):
	answer = 0

	while True:
		if a % 2 == 1:
			a = a // 2 + 1
		else:
			a = a // 2

		if b % 2 == 1:
			b = b // 2 + 1
		else:
			b = b // 2
		answer += 1
		if a == b:
			break

	return answer

print(solution( 8, 4, 7))