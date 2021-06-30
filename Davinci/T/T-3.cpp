#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;

	vector <int> ddeok;
	int a;
	for (int i = 0; i < n; i++) {
		cin >> a;
		ddeok.push_back(a);
	}

	int height = *max_element(ddeok.begin(), ddeok.end());

	while (true) {
		int sum = 0;
		for (int i = 0; i < n; i++) {
			int sub = ddeok[i] - height;
			if (sub > 0) {
				sum += sub;
			}
		}
		if (sum >= m)
			break;
		else
			height--;
	}

	cout << height;
	
}