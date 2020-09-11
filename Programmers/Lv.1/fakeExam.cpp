#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {


	vector<int> answer;

	int omr1[5] = { 1, 2, 3, 4, 5 };
	int omr2[8] = { 2, 1, 2, 3, 2, 4, 2, 5 };
	int omr3[10] = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };

	int cnt[3] = { 0,0,0 };

	for (int i = 0; i < answers.size(); i++) {
		if (omr1[i % 5] == answers[i])
			cnt[0]++;
	}

	for (int i = 0; i < answers.size(); i++) {
		if (omr2[i % 8] == answers[i])
			cnt[1]++;
	}

	for (int i = 0; i < answers.size(); i++) {
		if (omr3[i % 10] == answers[i])
			cnt[2]++;
	}

	int max = cnt[0];

	answer.push_back(1);

	for (int i = 1; i < 3; i++) {
		if (max < cnt[i]) {
			max = cnt[i];
			answer.clear();
			answer.push_back(i + 1);
		}
		else if (max == cnt[i]) {
			answer.push_back(i + 1);
		}
	}

	return answer;
}

int main() {

	vector<int> answers = { 1,2,3,4,5 };

	for (auto i : solution(answers))
		cout << i << ' ';

	cout << endl;

	/*vector<int> answers = { 1,3,2,4,2 };
	for (auto i : solution(answers))
		cout << i << ' ';

	cout << endl;*/
}