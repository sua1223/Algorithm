# start time 03:23  end time 03:40

import itertools
def solution(numbers, target):
	answer = 0
	sum_num = sum(numbers)
	comb = []
	for i in range(len(numbers)):
		comb_ = list(itertools.combinations(numbers, i))
		comb.append(comb_)

	for i in range(len(comb)):
		for j in range(len(comb[i])):
			sum_comb = sum(comb[i][j])
			if sum_num - sum_comb*2 == target:
				# print(comb[i][j])
				answer += 1

	return answer
print(solution([4, 1, 2, 1]	, 4))