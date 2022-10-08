# 프로그래머스 혼자 놀기의 달인
# start time 01:18

def solution(cards):
	answer = 0

	# 완전 탐색
	for i in range(len(cards)):
		cards[i] -= 1

	answer_list = []
	for i in range(len(cards)):
		visit = [0] * len(cards)
		set = []
		n = i
		cnt = 0
		while visit.count(1) != len(visit):
			flag = 0
			if visit[n] == 0:
				visit[n] = 1
				n = cards[n]
				cnt += 1
				if visit.count(1) == len(visit):
					set.append(cnt)
					break
			elif visit[n] == 1:
				set.append(cnt)
				cnt = 0
				flag = 1

			if flag == 1:
				n = visit.index(0)

		if len(set) <= 1:
			answer_list.append(0)
		else:
			set.sort(reverse=True)
			answer_list.append(set[0] * set[1])

	return max(answer_list)