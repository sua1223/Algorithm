#include <iostream>
#include <vector>

using namespace std;

int solution(vector<int> priorities, int location) {
	int answer = 0;

	vector<vector<int>> list;
	vector<int> list_;

	for (int i = 0; i < priorities.size(); i++) {
		list_.push_back(i);
		list_.push_back(priorities[i]);

		list.push_back(list_);
		list_.clear();
	}

	int n = (priorities.size()*priorities.size() + 1) / 2;
	int i = 0;

	while (n-- > 0) {
		int k = 0;
		for (int j = i + 1; j < priorities.size(); j++) {
			if (list[i][1] < list[j][1]) {
				list.push_back(list[i]);
				list.erase(list.begin() + i);
				break;
			}
			else {
				k++;
				if (k == priorities.size() - 1 - i) {
					i++;
					break;
				}
			}
		}
	}

	for (int i = 0; i < priorities.size(); i++) {
		if (location == list[i][0])
			answer = i + 1;
	}

	return answer;
}

int main() {
	vector<int> priorities = { 1,2,1,3,2,9,1 };
	int location = 4;

	cout << solution(priorities, location) << endl;

}