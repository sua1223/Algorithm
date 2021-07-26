#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

bool compare(string a, string b) {
	if (a.length() < b.length())
		return true;
	else if (a.length() > b.length())
		return false;
	else
		return a < b;
}

int main() {
	int n;
	cin >> n;

	vector <string> word;
	string input;
	for (int i = 0; i < n; i++) {
		cin >> input;
		word.push_back(input);
	}

	sort(word.begin(), word.end(),compare);
	
	for (int i = 0; i < n-1; i++) {
		cout << word[i] << "\n";
		if (word[i] == word[i + 1]) {
			while (word[i] == word[i + 1])
				i++;
		}
	}

	if (word[n - 2] != word[n - 1])
		cout << word[n - 1];
}