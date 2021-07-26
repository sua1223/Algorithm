#include <iostream>
#include <vector>
using namespace std;

#define MAX 51
int graph[MAX][MAX];
bool checked[MAX][MAX];
int cnt;
int h, w;

void dfs(int a, int b) {
	checked[a][b] = true;
	if (a > 0 && a < h && b < w && graph[a - 1][b] == 1 && checked[a - 1][b] == false)
		dfs(a - 1, b);
	if (b > 0 && a < h && b < w && graph[a][b - 1] == 1 && checked[a][b - 1] == false)
		dfs(a, b - 1);
	if (a < h - 1 && b < w && graph[a + 1][b] == 1 && checked[a + 1][b] == false)
		dfs(a + 1, b);
	if (a < h && b < w - 1 && graph[a][b + 1] == 1 && checked[a][b + 1] == false)
		dfs(a, b + 1);
	if (a > 0 && b > 0 && a < h && b < w && graph[a - 1][b - 1] == 1 && checked[a - 1][b - 1] == false)
		dfs(a - 1, b - 1);
	if (a < h - 1 && b < w - 1 && graph[a + 1][b + 1] == 1 && checked[a + 1][b + 1] == false)
		dfs(a + 1, b + 1);
	if (a > 0 && a < h && b < w - 1 && graph[a - 1][b + 1]==1 && checked[a - 1][b + 1] == false)
		dfs(a - 1, b + 1);
	if (a < h - 1 && b > 0 && b < w && graph[a + 1][b - 1]==1 & checked[a + 1][b - 1] == false)
		dfs(a + 1, b - 1);
}

int main() {
	vector <int> total;
	while (true) {
		cin >> w >> h;
		if (w == 0 && h == 0)
			break;
		int a;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				scanf(" %1d", &a);
				graph[i][j] = a;
				
			}
		}
		int flag = 0;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (!checked[i][j] && graph[i][j] == 1) {
					flag = 1;
					dfs(i, j);
					cnt++;
				}
			}
		}

		if (flag == 0)
			total.push_back(0);
		else {
			total.push_back(cnt);
			cnt = 0;
		}
		for (int i = 0; i < MAX; i++) {
			for (int j = 0; j < MAX; j++) {
				graph[i][j] = 0;
				checked[i][j] = false;
			}
		}
	}

	for (int i = 0; i < total.size(); i++) {
		cout << total[i] << "\n";
	}
}