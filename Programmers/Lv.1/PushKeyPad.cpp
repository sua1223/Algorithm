#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;

string solution(vector<int> numbers, string hand) {
	string answer = "";

	map<int, int> loc;
	loc.insert(make_pair(2, 0));
	loc.insert(make_pair(5, 1));
	loc.insert(make_pair(8, 2));
	loc.insert(make_pair(0, 3));

	int left[2] = { 0,3 };
	int right[2] = { 2,3 };

	for (int i = 0; i < numbers.size(); i++) {

		if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) {
			left[0] = 0;
			answer += "L";
			left[1] = numbers[i] / 3;
		}
		else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {
			right[0] = 2;
			answer += "R";
			right[1] = numbers[i] / 3 - 1;
		}
		else {
			int l = (1 - left[0]) + abs(left[1] - (loc.find(numbers[i])->second));
			int r = (right[0] - 1) + abs(right[1] - (loc.find(numbers[i])->second));

			if (l > r) {
				answer += "R";
				right[0] = 1;
				right[1] = loc.find(numbers[i])->second;
			}
			else if (l < r) {
				answer += "L";
				left[0] = 1;
				left[1] = loc.find(numbers[i])->second;
			}
			else {
				if (hand == "right") {
					answer += "R";
					right[0] = 1;
					right[1] = loc.find(numbers[i])->second;
				}
				else {
					answer += "L";
					left[0] = 1;
					left[1] = loc.find(numbers[i])->second;
				}
			}
		}
	}
	return answer;
}

int main() {
	vector<int> numbers = { 1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5 };
	string hand = "right";

	for (int i = 0; i < solution(numbers, hand).size(); i++) {
		cout << solution(numbers, hand)[i] << " ";
	}
}