#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(int n) {

	string answer = "";
	string answer_ = "";

	int k = 0;

	while (n > 0) {
		int k = n % 3;
		if (k == 0) {
			n = n / 3 - 1;
			answer_ += "4";
		}
		else {
			answer_ += to_string(k);
			n /= 3;
		}
	}

	for (int i = answer_.size() - 1; i >= 0; i--) {
		answer += answer_[i];
	}

	return answer;
}

int main() {
	cout << solution(19) << endl;
}