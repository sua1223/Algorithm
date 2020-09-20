#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {

	int answer = 0;
	answer += n;
	answer -= lost.size();

	for (int i = 0; i < lost.size(); i++) {
		for (int j = 0; j < reserve.size(); j++) {
			if (lost[i] == reserve[j]) {
				reserve[j] = -1;
				lost[i] = -3;
				answer++;
			}
		}
	}

	for (int i = 0; i < lost.size(); i++) {
		for (int j = 0; j < reserve.size(); j++) {
			if (lost[i] == reserve[j] - 1 || lost[i] == reserve[j] + 1) {
				reserve[j] = -1;
				lost[i] = -3;
				answer++;
				break;
			}
		}
	}
	return answer;
}

int main() {
	int n = 5;
	vector<int> lost = { 2,4 };
	vector<int> reserve = { 1,3,5 };

	cout << solution(n, lost, reserve) << endl;
}