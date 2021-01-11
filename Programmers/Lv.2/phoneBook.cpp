#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

bool compare(string a, string b) {
	return a.length() < b.length();
}

bool solution(vector<string> phone_book) {
	sort(phone_book.begin(), phone_book.end(), compare);

	for (int i = 0; i < phone_book.size(); i++) {
		for (int j = i + 1; j < phone_book.size(); j++) {
			string comp = phone_book[j].substr(0, phone_book[i].size());
			if (phone_book[i]==comp)
				return false;
		}
	}
	return true;
}

int main() {
	vector<string> phone_book = {  "97674223", "1195524421","119"};
	cout << solution(phone_book) << endl;
}