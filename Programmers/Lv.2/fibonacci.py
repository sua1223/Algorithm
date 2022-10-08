def solution(n):
	dp = []
	dp.append(0)  # F(0)
	dp.append(1)  # F(1)
	for i in range(2, n + 2):
		dp.append((dp[i - 1] + dp[i - 2]) % 1234567)

	return dp[n]