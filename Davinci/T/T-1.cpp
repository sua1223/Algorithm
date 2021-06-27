#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, m;
	int a;

	vector <int> request;
	vector <int> store;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a;
		store.push_back(a);
	}
	cin >> m;
	for (int j = 0; j < m; j++) {
		cin >> a;
		request.push_back(a);
	}

	// binary search
	/*sort(store.begin(), store.end());
	for (int i = 0; i < m; i++) {
		int start = 0;
		int end = n - 1;
		int mid;
		int flag = 0;
		while (start <= end) {
			mid = (start + end) / 2;
			if (request[i] == store[mid]) {
				cout << "yes ";
				flag = 1;
				break;
			}
			else if (request[i] < store[mid])
				end = mid - 1;
			else
				start = mid + 1;
		}

		if (flag == 0)
			cout << "no ";
	}*/

	for (int i = 0; i < m; i++) {
		auto it = find(store.begin(), store.end(), request[i]);
		if (it == store.end())
			cout << "no ";
		else
			cout << "yes ";
	}

}