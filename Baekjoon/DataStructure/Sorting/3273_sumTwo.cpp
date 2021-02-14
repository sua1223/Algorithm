#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;

	vector <int> num;
	int a;
	for (int i = 0; i < n; i++) {
		cin >> a;
		num.push_back(a);
	}

	int x;
	cin >> x;
	
	sort(num.begin(), num.end());

	int answer = 0;
	int start = 0;
	int end = num.size() - 1;

	while (start < end) {
		if (num[start] + num[end] == x) {
			answer++;
			start++;
			end--;
		}
		else if (num[start] + num[end] > x)
			end--;
		else
			start++;
	}

	cout << answer;
}