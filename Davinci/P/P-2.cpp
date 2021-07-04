#include <iostream>
#include <algorithm>
using namespace std;

int d[30000];

int dp(int n) {
	for (int i = 2; i <= n; i++) {
		d[i] = d[i - 1] + 1;
		if (i % 2 == 0)
			d[i] = min(d[i / 2] + 1, d[i]);
		if (i % 3 == 0)
			d[i] = min(d[i / 3] + 1, d[i]);
		if (i % 5 == 0)
			d[i] = min(d[i / 5] + 1, d[i]);
	}

	return d[n];
}
int main() {
	int x;
	cin >> x;

	d[1] = 0;
	
	cout << dp(x) << endl;
}