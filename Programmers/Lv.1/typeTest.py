# 프로그래머스 성격 유형 검사하기

def calc_score(n):
	if n == 1 or n == 7:
		return 3
	if n == 2 or n == 6:
		return 2
	if n == 3 or n == 5:
		return 1


def solution(survey, choices):
	answer = ''
	survey_list = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

	for i in range(len(survey)):
		if choices[i] == 4:
			continue
		if choices[i] < 4:
			survey_list[survey[i][0]] += calc_score(choices[i])
		else:
			survey_list[survey[i][1]] += calc_score(choices[i])

	list_values = list(survey_list.values())

	type_list = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']

	for i in range(0, len(list_values), 2):
		if list_values[i] > list_values[i + 1]:
			answer += type_list[i]
		elif list_values[i] < list_values[i + 1]:
			answer += type_list[i + 1]
		else:
			answer += min(type_list[i], type_list[i + 1])

	return answer