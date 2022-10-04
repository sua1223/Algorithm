# start time 09:17  end time 09:23

def solution(n):
	answer = 1  # 자기 자신
	i = 0
	while i < n // 2:
		i += 1
		i_sum = 0
		k = i
		while True:
			i_sum += k
			k += 1
			if i_sum > n:
				break
			elif i_sum == n:
				answer += 1
				break

	return answer

print(solution(15))