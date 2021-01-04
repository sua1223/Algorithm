#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solution(vector<int> citations) {

	int idx = 0;

	sort(citations.begin(), citations.end(), greater<int>());

	while (idx <= citations.size()) {
		if (idx >= citations[idx])
			break;
		idx++;
	}

	return idx;
}

int main() {
	vector<int> citations = { 0,0,0,0,0,0,2,2 };
	cout << solution(citations) << endl;
}