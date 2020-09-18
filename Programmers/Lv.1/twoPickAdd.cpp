#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
	vector<int> answer;

	for (int i = 0; i < numbers.size(); i++) {
		for (int j = i + 1; j < numbers.size(); j++) {
			answer.push_back(numbers[i] + numbers[j]);
			for (int k = 0; k < answer.size() - 1; k++) {
				if (answer[k] == numbers[i] + numbers[j])
					answer.pop_back();
			}
		}
	}
	sort(answer.begin(), answer.end());
	return answer;
}

int main() {
	vector<int> numbers = { 2,1,3,4,1 };

	for (int i = 0; i < solution(numbers).size(); i++) {
		cout << solution(numbers)[i] << " ";
	}
}