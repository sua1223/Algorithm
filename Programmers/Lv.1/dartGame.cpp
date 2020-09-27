#include <string>
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int solution(string dartResult) {
	int answer = 0;

	vector<char> input;

	for (int i = 0; i < dartResult.size(); i++) {
		input.push_back(dartResult[i]);
	}

	vector<int> num;
	vector<char>alpha;
	vector<char>option;
	vector<int>opt_idx;

	int k = -1;

	for (int i = 0; i < input.size(); i++) {
		if (isdigit(input[i])) {
			if (input[i] == '1') {
				if (input[i + 1] == '0') {
					num.push_back(10);
					i++;
					continue;
				}
			}
			num.push_back(input[i] - 48);
		}
		else if (isalpha(input[i])) {
			alpha.push_back(input[i]);
			k++;
		}
		else {
			option.push_back(input[i]);
			opt_idx.push_back(k);
		}
	}

	int alpha_num[3] = { 0, };

	for (int i = 0; i < 3; i++) {
		if (alpha[i] == 'S')
			alpha_num[i] = 1;
		else if (alpha[i] == 'D')
			alpha_num[i] = 2;
		else
			alpha_num[i] = 3;
	}

	int opt_num[3] = { 0, };

	for (int i = 0; i < opt_idx.size(); i++) {
		if (option[i] == '*')
			opt_num[opt_idx[i]] = 2;
		else
			opt_num[opt_idx[i]] = -1;
	}

	for (int i = 0; i < 3; i++) {
		if (opt_num[i] == 2) {
			answer += ((int)(pow(num[i], alpha_num[i]))*opt_num[i]);
			if (i > 0) {
				if (opt_num[i - 1] == 2)
					answer += ((int)(pow(num[i - 1], alpha_num[i - 1])))*opt_num[i - 1];
				else if (opt_num[i - 1] == 0)
					answer += ((int)(pow(num[i - 1], alpha_num[i - 1])));
				else
					answer -= ((int)(pow(num[i - 1], alpha_num[i - 1])));
			}
		}
		else if (opt_num[i] == -1)
			answer += ((int)(pow(num[i], alpha_num[i]))*opt_num[i]);
		else
			answer += ((int)(pow(num[i], alpha_num[i])));
	}
	return answer;
}

int main() {
	cout << solution("1D#2S*3S") << endl;
}