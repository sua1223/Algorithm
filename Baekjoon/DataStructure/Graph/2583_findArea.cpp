#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX 110
int graph[MAX][MAX];
bool checked[MAX][MAX];
int cnt;
int m, n;
void dfs(int a, int b) {
	checked[a][b] = true;
	cnt++;
	if (a > 0 && a < m && b < n && graph[a - 1][b] == 0 && checked[a - 1][b] == false)
		dfs(a - 1, b);
	if (b > 0 && a < m && b < n && graph[a][b - 1] == 0 && checked[a][b - 1] == false)
		dfs(a, b - 1);
	if (a < m - 1 && b < n && graph[a + 1][b] == 0 && checked[a + 1][b] == false)
		dfs(a + 1, b);
	if (a < m && b < n - 1 && graph[a][b + 1] == 0 && checked[a][b + 1] == false)
		dfs(a, b + 1);
}

void make_graph(int a, int b, int c, int d) {
	for (int i = b; i < d; i++) {
		for (int j = a; j < c; j++) {
			graph[i][j] = 1;
		}
	}
}

int main() {
	int k;
	cin >> m >> n >> k;

	int a, b, c, d;
	for (int i = 0; i < k; i++) {
		cin >> a >> b >> c >> d;
		make_graph(a, b, c, d);
	}

	vector <int> total;
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (!checked[i][j] && graph[i][j] == 0) {
				dfs(i, j);
				total.push_back(cnt);
				cnt = 0;
			}
		}
	}

	sort(total.begin(), total.end());
	cout << total.size() << "\n";
	for (int i = 0; i < total.size(); i++) {
		cout << total[i] << " ";
	}
}