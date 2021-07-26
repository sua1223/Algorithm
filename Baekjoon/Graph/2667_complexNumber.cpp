#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

#define MAX 26
int graph[MAX][MAX];
bool checked[MAX][MAX];
int cnt;

void dfs(int a, int b) {
	checked[a][b] = true;
	cnt++;
	if (a > 0 && graph[a - 1][b] == 1&&checked[a-1][b]==false)
		dfs(a - 1, b);
	if (b > 0 && graph[a][b - 1] == 1 && checked[a][b-1] == false)
		dfs(a, b - 1);
	if (graph[a+1][b] == 1 && checked[a+1][b] == false)
		dfs(a+1, b);
	if (graph[a][b + 1] == 1 && checked[a][b+1] == false)
		dfs(a, b + 1);
}

int main() {
	int n;
	cin >> n;
	
	int a;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf(" %1d",&a);
			graph[i][j] = a;
		}
	}

	vector <int> total;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!checked[i][j]&&graph[i][j]==1) {
				dfs(i, j);
				total.push_back(cnt);
				cnt = 0;
			}	
		}
	}

	sort(total.begin(), total.end());
	cout << total.size() << "\n";
	for (int i = 0; i < total.size(); i++) {
		cout << total[i] << "\n";
	}
}