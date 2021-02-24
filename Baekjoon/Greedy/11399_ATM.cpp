#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int n;
	cin >> n;

	vector <int> time;

	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		time.push_back(a);
	}

	sort(time.begin(), time.end());

	int answer = 0;
	int sum = 0;
	for (int i = 0; i < n; i++) {
		sum += time[i];
		answer += sum;
	}

	cout << answer;
}