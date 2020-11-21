#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(int n) {

	vector<int> answer;
	vector<vector <int>> array;
	vector<int> array_;

	int max = 0;

	for (int j = 0; j < n; j++) {
		for (int i = 0; i < j + 1; i++) {
			array_.push_back(0);
			max++;
		}
		array.push_back(array_);
		array_.clear();
	}

	int i = 0; int j = 0; int k = 1;

	array[i][j] = k;

	while (true) {
		while (i + 1 < n&& array[i + 1][j] == 0)
			array[++i][j] = ++k;
		while (j + 1 < n&& array[i][j + 1] == 0)
			array[i][++j] = ++k;
		while (i - 1 > 0 && j - 1 > 0 && array[i - 1][j - 1] == 0)
			array[--i][--j] = ++k;

		if (k == max)
			break;
	}

	int num = n + n - 1;
	int a = 1;

	for (int j = 0; j < n; j++) {
		for (int i = 0; i < j + 1; i++) {
			answer.push_back(array[j][i]);
			//cout << array[j][i]<<" ";
		}
		//cout << endl;
	}
	return answer;
}

int main() {
	int n = 6;
	for (int i = 0; i < solution(n).size(); i++) {
		cout << solution(n)[i] << " ";
	}
}