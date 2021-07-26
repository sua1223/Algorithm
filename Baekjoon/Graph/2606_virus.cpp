#include <iostream>
#include <vector>
using namespace std;

#define MAX 110
vector <int> graph[MAX];
bool checked[MAX];
int answer;

void dfs(int k) {
	checked[k] = true;
	answer++;
	for (int i = 0; i < graph[k].size(); i++) {
		if (!checked[graph[k][i]])
			dfs(graph[k][i]);
	}
}

int main() {
	int n;
	cin >> n;
	int m;
	cin >> m;

	int a, b;
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	dfs(1);

	cout << answer-1;
}