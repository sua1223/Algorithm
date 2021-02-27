#include <iostream>
#include <stack>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;

	stack<int> coin;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		coin.push(a);
	}

	int sum = 0;
	int count = 0;

	while (true) {
		if (k < coin.top()) {
			coin.pop();
			continue;
		}

		int money = coin.top();
		coin.pop();
		while (true) {
			if (k < money) {
				break;
			}
			count++;
			k -= money;
		}
		
		if (sum == k)
			break;
	}

	cout << count;
}