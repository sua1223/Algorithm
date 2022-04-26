N = int(input())

dp = [0]*(N+1)
dp[0] = 0
dp[1] = 1

for i in range(2, N+1):
	min_value = float('inf')
	j = 1
	while (j**2) <= i:
		min_value = min(min_value, dp[i-(j**2)])
		j += 1
	dp[i] = min_value + 1

print(dp[N])
