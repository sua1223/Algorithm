# 프로그래머스 오픈채팅방

id_name = {}

def solution(record):
	answer = []
	action = []
	action_id = []
	for r in record:
		tmp = r.split(' ')
		action.append(tmp[0])
		action_id.append(tmp[1])

		if tmp[0] != 'Leave':
			id_name[tmp[1]] = tmp[2]

	for i in range(len(action)):
		str = ''
		if action[i] == 'Enter':
			str = id_name[action_id[i]] + "님이 들어왔습니다."
		elif action[i] == 'Leave':
			str = id_name[action_id[i]] + "님이 나갔습니다."
		else:
			continue
		answer.append(str)
	return answer