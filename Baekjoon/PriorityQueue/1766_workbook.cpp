#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
#define max 32010
vector <int> exist;

int main() {
	int n, m;
	cin >> n >> m;
	priority_queue< int, vector<int>, greater<int> > pq;
	vector <int> num[max];
	vector <int> pr(max,0);

	int a, b;
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		num[a].push_back(b);
		pr[b]++;
	}

	for (int i = 1; i <= n; i++) {
		if (pr[i] == 0 )
			pq.push(i);
	}

	int index, p;
	while(!pq.empty()){
		index = pq.top();
		pq.pop();
		cout << index<<" ";
		for (int i = 0; i < num[index].size(); i++) {
			p= --pr[num[index][i]];
			if (p == 0)
				pq.push(num[index][i]);
		}
	}
}