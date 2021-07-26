#include <iostream>
#include <queue>
#include <cstdio>
using namespace std;

#define MAX 110
int n, m;
bool checked[MAX][MAX];
char graph[MAX][MAX];
int dis[MAX][MAX];
int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };

void BFS(int x, int y) {
	checked[x][y] = true;

	queue < pair<int, int>> q;
	q.push(make_pair(x, y));

	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;

		q.pop();

		for (int i = 0; i < 4; i++) {
			int next_x = x + dx[i];
			int next_y = y + dy[i];

			if (0 <= next_x && next_x < n && 0 <= next_y && next_y < m) {
				if (graph[next_x][next_y] == '1' && checked[next_x][next_y] == false) {
					checked[next_x][next_y] = true;
					dis[next_x][next_y] = dis[x][y] + 1;
					q.push(make_pair(next_x, next_y));
				}
			}
		}
	}

}

int main() {
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		scanf("%s", graph[i]);
	}
	BFS(0, 0);
	cout << dis[n - 1][m - 1] + 1;
}