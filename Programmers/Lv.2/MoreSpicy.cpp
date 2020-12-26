#include <string>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

int solution(vector<int> scoville, int K) {
	int answer = 0;

	priority_queue<int, vector<int>, greater<int>> s;

	for (int i = 0; i < scoville.size(); i++) {
		s.push(scoville[i]);
	}

	while (true) {
		if (s.size() < 2)
			return -1;

		int mix_1 = s.top(); s.pop();
		int mix_2 = s.top(); s.pop();

		int mix = mix_1 + mix_2 * 2; s.push(mix);
		answer++;

		if (s.top() >= K)
			break;
	}

	return answer;
}

int main() {
	vector <int> scoville = { 1, 2, 3, 9, 10, 12 };
	int K = 7;

	cout << solution(scoville, K) << endl;
}