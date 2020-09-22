#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {

	vector<string> answer;
	vector<vector<int> > bin1;
	vector<int> bin1_;
	vector<vector<int> > bin2;
	vector<int> bin2_;

	for (int j = 0; j < n; j++) {
		for (int i = n - 1; i >= 0; i--) {
			bin1_.push_back(arr1[j] >> i & 1 ? 1 : 0);
			bin2_.push_back(arr2[j] >> i & 1 ? 1 : 0);
		}
		bin1.push_back(bin1_);
		bin1_.clear();
		bin2.push_back(bin2_);
		bin2_.clear();
	}

	vector<vector<int> > sol;
	vector<int> sol_;
	string line = "";

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (bin1[i][j] == 1 || bin2[i][j] == 1)
				line += "#";
			else
				line += " ";
		}
		answer.push_back(line);
		line = "";
	}

	return answer;
}

int main() {
	int n = 5;
	vector<int> arr1 = { 9, 20, 28, 18, 11 };
	vector<int> arr2 = { 30, 1, 21, 17, 28 };

	for (int i = 0; i < solution(n, arr1, arr2).size(); i++) {
		cout << solution(n, arr1, arr2)[i] << endl;
	}
}