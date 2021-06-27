#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n;
	cin >> n;
	int a = 1;

	vector <int> num;

	num.push_back(1);
	while (num.size() <= n) {
		if (a % 2 == 0 || a % 3 == 0 || a % 5 == 0) {
			num.push_back(a);
		}
		a++;
	}

	cout << num[n - 1]<<endl;
}