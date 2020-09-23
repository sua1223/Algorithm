#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool compare(const pair<double, int>& a, const pair<double, int>& b) {
	if (a.first == b.first)
		return a.second < b.second;
	return a.first > b.first;
}

vector<int> solution(int N, vector<int> stages) {
	vector<int> answer;
	vector<int> stage(N, 0);

	for (int i = 0; i < stages.size(); i++) {
		for (int j = 0; j < N; j++) {
			if (stages[i] == j + 1)
				stage[j]++;
		}
	}

	vector<pair<double, int> > fail;
	int sum = 0;

	for (int i = 0; i < N; i++) {

		if (stages.size() - sum == 0)
			fail.push_back(pair<double, int>(0, i + 1));
		else {
			double x = (double)stage[i] / (double)(stages.size() - sum);
			fail.push_back(pair<double, int>(x, i + 1));
		}
		sum += stage[i];
	}

	sort(fail.begin(), fail.end(), compare);

	for (int i = 0; i < N; i++) {
		answer.push_back(fail[i].second);
	}

	return answer;
}

int main() {

	int N = 4;
	vector<int> stages = { 4,4,4,4,4 };

	for (int i = 0; i < solution(N, stages).size(); i++) {
		cout << solution(N, stages)[i] << " ";
	}
}