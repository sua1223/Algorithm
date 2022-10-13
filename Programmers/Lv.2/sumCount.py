# 프로그래머스 연속 부분 수열 합의 개수
# start time: 08:41

def solution(elements):
	answer = 0
	make_sum = [sum(elements)]

	for i in range(len(elements)):
		k = elements[i]
		make_sum.append(k)
		n = i
		print(n)
		for j in range(len(elements) - 1):
			if n + 1 >= len(elements):
				n = len(elements) - n - 1
			else:
				n += 1
			k += elements[n]
			make_sum.append(k)

	result = set(make_sum)

	return len(result)