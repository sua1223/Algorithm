#include <iostream>
#include <vector>

using namespace std;
int main() {
	int cost;
	cin >> cost;

	int n;
	cin >> n;

	int a;
	vector <int> arr;
	for (int i = 0; i < n; i++) {
		cin >> a;
		arr.push_back(a);
	}

	int max = 0;
	for (int i = 0; i < n; i++) {
		int sum = 0;
		for (int j = i; j < n; j++) {
			if (sum + arr[j] > cost) {
				if (max < j - i)
					max = j - i;
				break;
			}
			else
				sum += arr[j];
		}
		if (max > n - i)
			break;
	}
	
	cout << max << endl;
}