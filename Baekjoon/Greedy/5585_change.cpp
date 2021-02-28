#include <iostream>

using namespace std;
int main() {
	int n;
	cin >> n;

	int change = 1000 - n;
	int money[6] = { 500,100,50,10,5,1 };
	int count = 0;
	int i = 0;

	while (true) {
		if (change < money[i]) {
			i++;
			continue;
		}
		while (true) {
			if (change < money[i]) {
				i++;
				break;
			}
			count++;
			change -= money[i];
		}
		if (change == 0)
			break;
	}

	cout << count;
}