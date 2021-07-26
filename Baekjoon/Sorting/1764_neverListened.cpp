#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;

	vector <string> name;
	string input;
	for (int i = 0; i < n; i++) {
		cin >> input;
		name.push_back(input);
	}

	for (int i = 0; i < m; i++) {
		cin >> input;
		name.push_back(input);
	}

	sort(name.begin(), name.end());
	vector <string> answer;
	for (int i = 0; i < name.size()-1; i++) {
		if (name[i] == name[i + 1]) {
			answer.push_back(name[i]);
			i++;
		}
	}
	
	cout << answer.size()<<"\n";
	for (int i = 0; i < answer.size(); i++) {
		cout << answer[i] << "\n";
	}
}