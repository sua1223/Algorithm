#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool cmp(string a, string b) {
	if (a + b > b + a)
		return true;
	else
		return false;
}

string solution(vector<int> numbers) {
	string answer = "";
	vector <string> num;

	for (int i = 0; i < numbers.size(); i++) {
		num.push_back(to_string(numbers[i]));
	}

	sort(num.begin(), num.end(), cmp);

	for (int i = 0; i < num.size(); i++) {
		answer += num[i];
	}

	if (answer[0] == '0')
		answer = "0";

	return answer;
}

int main() {
	vector<int> numbers = { 3, 30, 34, 5, 9 };
	cout << solution(numbers) << endl;
}