#include <iostream>
#include <vector>
using namespace std;

int answer;
vector <int> print;
void move(int n, int start, int end, int middle) {
	answer++;
	if (n == 1) {
		print.push_back(start);
		print.push_back(end);
		return;
	}
	else {
		move(n - 1, start, middle, end);
		print.push_back(start);
		print.push_back(end);
		move(n - 1, middle, end, start);
	}
}

int main() {
	int n;
	cin >> n;
	answer = 0;
	
	move(n, 1,3,2);
	cout << answer << endl;
	for (int i = 0; i < print.size(); i++) {
		cout << print[i++]<<' '<< print[i] << endl;
	}
}