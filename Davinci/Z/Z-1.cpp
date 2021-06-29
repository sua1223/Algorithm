#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int n;
	cin >> n;

	int a;
	vector <int> house;
	for (int i = 0; i < n; i++) {
		cin >> a;
		house.push_back(a);
	}

	int min = *min_element(house.begin(), house.end());
	int max = *max_element(house.begin(), house.end());

	int answer = max - min;

	cout << answer;

}