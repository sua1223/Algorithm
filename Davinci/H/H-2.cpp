#include <iostream>
#include <queue>
#include <cstdio>
using namespace std;

#define MAX 1000
int n, m;
char graph[MAX][MAX];
bool checked[MAX][MAX];

void dfs(int a, int b) {
	checked[a][b] = true;
	if (a > 0 && a < n && b < m && graph[a - 1][b] == '0' && checked[a - 1][b] == false)
		dfs(a - 1, b);
	if (b > 0 && a < n && b < m && graph[a][b - 1] == '0' && checked[a][b - 1] == false)
		dfs(a, b - 1);
	if (a < n - 1 && b < m && graph[a + 1][b] == '0' && checked[a + 1][b] == false)
		dfs(a + 1, b);
	if (a < n && b < m - 1 && graph[a][b + 1] == '0' && checked[a][b + 1] == false)
		dfs(a, b + 1);
}

int main() {
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		scanf("%s", graph[i]);
	}

	int answer = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (!checked[i][j] && graph[i][j]=='0') {
				dfs(i, j);
				answer++;
			}
		}
	}

	cout << answer;
}