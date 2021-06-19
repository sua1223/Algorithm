#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solution(vector<int> nums){
	sort(nums.begin(), nums.end());

	int count = 1;
	int a;
	for (int i = 0; i < nums.size()-1; i++) {
		a = nums[i];
		if (a == nums[i + 1])
			continue;
		else
			count++;
	}

	if (count >= nums.size() / 2)
		return nums.size() / 2;
	return count;
}

int main() {

	vector <int> nums = { 3,3,3,2,2,2 };
	cout << solution(nums) << endl;
}