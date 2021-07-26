#include <iostream>
#include <vector>
using namespace std;

#define MAX 100001

vector<int> node[MAX];
int parent[MAX];
bool visited[MAX];
int n;

void findParent(int x) {
	visited[x] = true;
	for (int i = 0; i < node[x].size(); i++) {
		int next = node[x][i];
		if (visited[next] == false) {
			parent[next] = x;
			findParent(next);
		}
	}
}

int main() {
	cin >> n;
	int a, b;
	for (int i = 1; i < n; i++) {
		cin >> a >> b;
		node[a].push_back(b);
		node[b].push_back(a);
	}

	findParent(1);

	for (int i = 2; i <= n; i++)
		cout << parent[i] << '\n';

	return 0;
}