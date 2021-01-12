#include <iostream>
#include <string>
#include <queue>
#include <vector>
using namespace std;
#define max 32000
vector <int> exist;

bool isExist(int a) {
	for (int i = 0; i < exist.size(); i++) {
		if (exist[i] == a)
			return false;
	}
	return true;
}
int main() {
	int n, m;
	cin >> n >> m;
	priority_queue< int, vector<int>, greater<int> > pq;
	vector <int> num[max];
	
	int a, b;
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		pq.push(b);
		num[b].push_back(a);
		exist.push_back(a);
	}

	for (int i = 1; i <= n; i++) {
		if (num[i].size() == 0 &&isExist(i))
			pq.push(i);
	}

	int size = pq.size();
	int index;
	for(int j=0; j<size; j++){
		if (j > 0)
			cout << " ";
		index = pq.top();
		pq.pop();
		
		for (int i = 0; i < num[index].size(); i++) {
			cout << num[index][i]<<" ";
		}
		cout << index;
	}
}