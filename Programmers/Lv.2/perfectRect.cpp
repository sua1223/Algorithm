#include <iostream>

using namespace std;

long long solution(int w, int h) {
	long long answer = 0;

	int min = w;
	int max = h;

	if (min > h) {
		min = h;
		max = w;
	}

	long long n = 0;

	for (int i = 1; i < min; i++) {
		answer += (long long)max / min * i;
		n += (long long)max % min;
		if (n >= min)
			answer += n / min;
	}

	answer *= 2;

	return answer;
}

int main() {
	cout << solution(8, 12) << endl;
}