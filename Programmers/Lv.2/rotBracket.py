# 프로그래머스 괄호 회전하기

def checkRight(s):
	s_list = []
	open_list = ['(', '[', '{']
	close_list = [')', ']', '}']

	if s[0] in close_list:
		return False

	s_list.append(s[0])
	for i in range(1, len(s)):
		if s[i] in open_list:
			s_list.append(s[i])
		else:  # 닫는 괄호일 경우
			if len(s_list) == 0:
				return False
			if close_list.index(s[i]) == open_list.index(s_list[-1]):
				s_list.pop()

	if len(s_list) == 0:  # 짝꿍을 다 찾았을 때
		return True
	return False


def solution(s):
	answer = 0
	for i in range(len(s)):
		tmp = s[i:] + s[:i]
		if checkRight(tmp):
			answer += 1

	return answer