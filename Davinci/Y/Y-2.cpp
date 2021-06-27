#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
	int n, a;
	priority_queue<int, vector<int>, greater<int>> q;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a;
		q.push(a);
	}

	int answer = 0;
	for (int i = 0; i <q.size(); i++) {
		int a = q.top();
		if (q.top() > q.size())
			break;
		answer++;
		for (int j = 0; j < a; j++) {
			if (q.size() > 0) {
				if (q.top() > a)
					a = q.top();
			}
			q.pop();
		}
	}

	cout << answer;
}