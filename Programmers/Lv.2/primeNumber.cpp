#include <vector>
#include <iostream>
using namespace std;

bool isPrime(int n) {
	for (int i = 2; i < n / 2; i++) {
		if (n%i == 0)
			return false;
	}
	return true;
}

int solution(vector<int> nums) {
	int answer = 0;
	vector<int> sum;
	int n, a, b, c;

	for (int i = 0; i < nums.size(); i++) {
		for (int j = i + 1; j < nums.size(); j++) {
			if (i == j)
				break;
			for (int k = j + 1; k < nums.size(); k++) {
				if (i == k || k == j)
					continue;
				a = nums[i];
				b = nums[j];
				c = nums[k];
				n = a + b + c;
				sum.push_back(n);
			}
		}
	}

	for (int i = 0; i < sum.size(); i++) {
		if (isPrime(sum[i]))
			answer++;
	}
	return answer;
}

int main() {
	vector <int> nums = { 1,2,7,6,4 };
	cout << solution(nums) << endl;
}