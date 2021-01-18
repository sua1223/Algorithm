#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(int brown, int yellow) {
	vector<int> answer;

	for (int i = 1; i < yellow+1; i++) {
		if (yellow%i != 0)
			continue;
		if (i * 2 + yellow/i * 2 + 4 == brown) {
			answer.push_back(yellow / i + 2);
			answer.push_back(i + 2);
			break;
		}
	}

	return answer;
}

int main() {
	for (int i = 0; i < 2; i++) {
		cout << solution(8,1)[i] << " ";
	}
}