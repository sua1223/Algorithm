# start time 05:31  end time 06:10

def solution(n, left, right):
	answer = []

	for i in range(left, right+1):
		div = i // n
		mod = i % n
		if mod < div:
			answer.append(div+1)
		else:
			answer.append(mod + 1)

	return answer

print(solution(4, 7, 14))