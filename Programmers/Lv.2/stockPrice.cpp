#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> prices) {
	vector<int> answer;

	for (int i = 0; i < prices.size(); i++) {
		int count = 0;
		for (int j = i + 1; j < prices.size(); j++) {
			if (prices[i] <= prices[j])
				count++;
			else {
				count++;
				break;
			}
		}
		answer.push_back(count);
	}

	return answer;
}

int main() {
	vector<int> prices = { 1, 2, 3, 2, 3 };

	for (int i = 0; i < solution(prices).size(); i++) {
		cout << solution(prices)[i] << " ";
	}
}