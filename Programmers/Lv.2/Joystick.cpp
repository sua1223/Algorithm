#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solution(string name) {
	int answer = 0;

	int len = name.length();
	int right = len - 1;
	int move=right;

	for (int i = 0; i < len; i++) {
		int up = name[i] - 'A';
		int down = 'Z' - name[i] + 1;
		answer += min(up, down);

		int next = i + 1;
		while (next < len&&name[next] == 'A')
			next++;

		int left = i + i+len-next;
		move = min(move, left);
	}

	answer += move;
	return answer;
}

int main() {
	cout << solution("JAN") << endl;
}