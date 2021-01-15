#include <iostream>
#include <queue>
using namespace std;

int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	int n;
	cin >> n;
	priority_queue< int, vector<int>, greater<int> > pq;

	int a;
	for (int i = 0; i < n*n; i++) {
		cin >> a;
		if (i < n) 
			pq.push(a);
		else if (a > pq.top()) {
			pq.pop();
			pq.push(a);
		}
	}
	
	cout << pq.top();
}