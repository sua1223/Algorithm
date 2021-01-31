#include <iostream>
#include <vector>
using namespace std;

#define MAX 1010
vector<int> graph[MAX];
bool checked[MAX];

void dfs(int k) {
	checked[k] = true;
	for (int i = 0; i < graph[k].size(); i++) {
		if (!checked[graph[k][i]])
			dfs(graph[k][i]);
	}
}

int main() {
	int n, m;
	cin >> n >> m;

	int a, b;
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	int count = 0;
	for (int i = 1; i <= n; i++) {
		if (!checked[i]) {
			count++;
			dfs(i);
		}
	}

	cout << count;
}