T = int(input())

def dfs(m, cash):
	global min_money
	if m >= 12:
		min_money = min(min_money, cash)
		return
	else:
		dfs(m+1, cash + money[0] * swim[m])
		dfs(m+1, cash + money[1])
		dfs(m+3, cash + money[2])

for test_case in range(1, T + 1):
	money = list(map(int, input().split()))
	swim = list(map(int, input().split()))

	min_money = money[3]
	dfs(0, 0)

	print('#'+str(test_case)+' '+str(min_money))
