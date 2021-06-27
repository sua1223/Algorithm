#include <iostream>
#include <string>
using namespace std;

int main() {

	string s;
	cin >> s;

	int answer = s[0] - '0';

	for (int i = 1; i < s.length(); i++) {
		int a = s[i] - '0';
		
		if (a <= 1 || answer <= 0)
			answer += a;
		else
			answer *= a;
	}

	cout << answer<< "\n";
}