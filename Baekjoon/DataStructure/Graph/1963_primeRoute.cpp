#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

int prime[10000] = { 0, };
int nextInt(int a) {
	int k;
	for (int i = 0; i < 4; i++) {
		int num[4] = { a / 1000,(a % 1000) / 100,(a % 100) / 10,a % 10 };
		for (int j = 0; j <= 9; j++) {
			if (i == 0 && j == 0)
				continue;
			num[i] = j;
			k = (num[0] * 1000) + (num[1] * 100) + (num[2] * 10) + num[3];
			cout << k << endl;
			if (prime[k]) {
				prime[k] = 0;
				return k;
			}
		}
	}
}

bool isPrime(int k) {
	for (int i = 2; i < sqrt(k); i++) {
		if (k%i == 0)
			return false;
	}
	return true;
}

int main() {
	vector<int> answer;
	
	for (int i = 0; i < 10000; i++) {
		if (isPrime(i)) {
			prime[i] = 1;
		}
	}

	int n;
	cin >> n;

	int a, b;
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		prime[a] = 0;
		int count = 0;
		int pre = a;
		while (true) {
			if (pre== b)
				break;
			pre = nextInt(pre);
			count++;
		}
		answer.push_back(count);
	}
	for (int i = 0; i < n; i++) {
		cout << answer[i] << "\n";
	}
}