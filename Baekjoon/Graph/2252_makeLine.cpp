#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define MAX 32010
int main() {
	int degree[MAX] = { 0, };
	vector <int> line[MAX];
	int n, m;
	cin >> n >> m;

	int a, b;
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		degree[b]++;
		line[a].push_back(b);
	}

	queue <int> q;
	for (int i = 1; i <= n; i++) {
		if (degree[i] == 0)
			q.push(i);
	}

	while (!q.empty()) {
		int k, p;
		k= q.front();
		q.pop();

		cout << k << " ";
		for (int i = 0; i < line[k].size(); i++) {
			p = --degree[line[k][i]];
			if (p == 0)
				q.push(line[k][i]);
		}
	}
}