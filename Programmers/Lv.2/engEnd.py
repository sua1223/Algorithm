# start time 11:58  end time 12:20  ** 반례 도움 받음

def calc_answer(n, k):
	k += 1
	if k % n == 0:
		return [n, k // n]
	return [k % n, k // n + 1]

def solution(n, words):
	tmp = []
	k = 0
	while k < len(words):
		# 중복된 경우
		if tmp.count(words[k]) == 1:
			return calc_answer(n, k)
		tmp.append(words[k])
		# 끝말잇기 글자가 잘못된 경우
		if k < len(words) - 1:
			if words[k][len(words[k]) - 1] != words[k + 1][0]:
				return calc_answer(n, k + 1)
		k += 1
	return [0, 0]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))