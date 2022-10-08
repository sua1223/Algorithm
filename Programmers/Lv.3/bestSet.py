# 프로그래머스 최고의 집합
# start time 11:33       end time 11:45

def solution(n, s):
	answer = []
	if s // n == 0:  # 존재하지 않는 경우
		return [-1]

	list_sum = 0
	while n > 1:
		a = s // n
		s -= a
		answer.append(a)
		n -= 1

	answer.append(s)
	print(answer)

	return answer