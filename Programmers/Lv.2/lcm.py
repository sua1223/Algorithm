from math import gcd


def solution(arr):
	answer = 0

	if len(arr) == 1:
		return arr[0]

	answer = int(arr[0] * arr[1] / gcd(arr[0], arr[1]))
	if len(arr) > 2:
		for i in range(2, len(arr)):
			answer = int(answer * arr[i] / gcd(answer, arr[i]))

	return answer
