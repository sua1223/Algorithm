# start time 9:49   end time: 10:12  ** 도움 받음
def solution(n):
	n2 = bin(n)[2:]
	answer = '1'
	if len(n2) == n2.count('1'):
		answer += '0'
		for i in range(0, n2.count('1')-1):
			answer += '1'
		return int(answer, 2)

	while True:
		n += 1
		cmp = bin(n)[2:]
		if cmp.count('1') == n2.count('1'):
			return n



print(solution(78))