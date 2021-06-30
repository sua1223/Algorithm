#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, x;
	cin >> n >> x;

	vector <int> num;
	int a;
	for (int i = 0; i < n; i++) {
		cin >> a;
		num.push_back(a);
	}

	int mid;
	int flag = 0;
	// binary search
	for(int i = 0; i < n; i++) {
		int start = 0;
		int end = n - 1;
		while (start <= end) {
			mid = (start + end) / 2;
			if (x == num[mid]) {
				flag = 1;
				break;
			}
			else if (x < num[mid])
				end = mid - 1;
			else
				start = mid + 1;
		}
		if (flag == 1)
			break;
	}

	int count = 0;
	int i = mid;
	if (flag == 1) {
		count--;
		while (x <= num[i]) {
			count++;
			i--;
		}
		i = mid;
		while (x >= num[i]) {
			count++;
			i++;
		}
	}

	if (flag == 0)
		cout << "-1" << endl;
	else
		cout << count << endl;
}