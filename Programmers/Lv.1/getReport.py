# 프로그래머스 신고 결과 받기 (2022 KAKAO BLIND RECRUITMENT)

def solution(id_list, report, k):
	answer = []

	res = []

	for i in range(len(id_list)):
		res.append([])

	user_list = []
	# res: 각 유저별로 신고한 유저 결과
	for s in report:
		n, m = s.split()
		idx = id_list.index(n)
		if m not in res[idx]:
			res[idx].append(m)
		user_list.append(m)

	# 정지될 유저 찾기
	user_list = list(set(user_list))

	count_user = [0 for i in range(len(user_list))]

	for r in res:
		for n in r:
			idx = user_list.index(n)
			count_user[idx] += 1

	stop_user = []

	for i in range(len(count_user)):
		if count_user[i] >= k:
			stop_user.append(user_list[i])

	# 각 유저별 정지 메일 받기
	for r in res:
		cnt = 0
		for n in r:
			if n in stop_user:
				cnt += 1
		answer.append(cnt)
	return answer