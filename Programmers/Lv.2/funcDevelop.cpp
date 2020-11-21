#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {

	vector<int> answer;
	vector<int> time;

	for (int i = 0; i < progresses.size(); i++) {
		int a = 100 - progresses[i];
		if (a%speeds[i] != 0)
			time.push_back(a / speeds[i] + 1);
		else
			time.push_back(a / speeds[i]);
	}

	int idx = 0;
	int count = 1;
	int day = time[0];

	while (true) {
		idx++;
		if (idx == time.size())
			break;

		if (day >= time[idx]) {
			count++;
			continue;
		}

		answer.push_back(count);
		day = time[idx];
		count = 1;
	}
	answer.push_back(count);

	return answer;
}

int main() {
	vector <int> progresses = { 95, 90, 99, 99, 80, 99 };
	vector <int> speeds = { 1, 1, 1, 1, 1, 1 };

	for (int i = 0; i < solution(progresses, speeds).size(); i++) {
		cout << solution(progresses, speeds)[i] << " ";
	}
}