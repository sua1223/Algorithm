#include <iostream>
#include <map>
using namespace std;

int main() {
	int n;
	cin >> n;
	multimap<int,int> task;

	int a, b;
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		task.insert(pair<int, int>(a, b));
	}

	int ability = 0;
	for (auto iter = task.begin(); iter != task.end(); iter++) {
		if (iter->first > ability)
			break;
		else
			ability += iter->second;
	}

	if (ability == 0)
		cout << "-1";
	else
		cout << ability;
}