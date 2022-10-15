# 프로그래머스 숫자 짝꿍

def solution(X, Y):
	answer = ''
	x_list = list(0 for i in range(10))
	y_list = list(0 for i in range(10))

	len_x = len(X)
	len_y = len(Y)

	bigger = max(len_x, len_y)

	for i in range(bigger):
		if i < len_x:
			x_list[int(X[i])] += 1
		if i < len_y:
			y_list[int(Y[i])] += 1

	couple = []
	cnt = 0
	for i in range(10):
		if x_list[i] != 0 and y_list[i] != 0:
			cnt = min(x_list[i], y_list[i])
			for j in range(cnt):
				couple.append(i)

	couple.sort(reverse=True)

	if len(couple) == 0:
		return "-1"
	if couple[0] == 0:
		return "0"

	for i in range(len(couple)):
		answer += str(couple[i])

	return answer