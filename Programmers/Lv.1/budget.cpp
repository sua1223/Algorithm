#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
	int answer = 0;

	sort(d.begin(), d.end());
	int i = 0;

	while (budget - d[i] >= 0) {
		budget -= d[i];
		answer++;
		i++;

		if (i == d.size())
			break;
	}

	return answer;
}

int main() {
	vector<int> d = { 2,2,3,3 };
	int budget = 10;

	cout << solution(d, budget) << endl;
}