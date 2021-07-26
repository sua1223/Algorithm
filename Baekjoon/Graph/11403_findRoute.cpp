#include <iostream>
using namespace std;

#define MAX 110
int graph[MAX][MAX];
int check[MAX][MAX];
int n;

void dfs(int a, int b) {
	check[a][b] = 1;
	for (int i = 0; i < n; i++) {
		if (graph[b][i] == 1 && check[a][i]==0)
			dfs(a,i);
	}
}

int main() {

	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> graph[i][j];
			check[i][j] = graph[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (graph[i][j])
				dfs(i, j);
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << check[i][j] << " ";
		}
		cout << "\n";
	}
}