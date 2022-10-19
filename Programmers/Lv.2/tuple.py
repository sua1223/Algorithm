# 프로그래머스 튜플

def solution(s):
	answer = []
	s = s[2:len(s) - 2]

	s_list = s.split('},{')
	for i in range(len(s_list)):
		s_list[i] = s_list[i].split(',')

	s_list.sort(key=lambda x: (len(x)))

	for ss in s_list:
		for i in range(len(ss)):
			if int(ss[i]) not in answer:
				answer.append(int(ss[i]))

	return answer