#include <string>
#include <iostream>
using namespace std;

int solution(string s) {
	int answer = 0;
	int min = s.length();
	s += "A";

	for (int i = 1; i < s.length() / 2 + 1; i++) {
		int flag = 0;
		string sen = "";
		int size = i;
		int count = 1;
		for (int j = 0; j < s.length() - size; j += size) {
			string str = "", comp_str = "";

			for (int k = j; k < j + size; k++) {
				str += s[k];
			}
			for (int k = j + size; k < j + size + size; k++) {
				if (s[k] == 'A') {
					flag = 1;
					break;
				}
				comp_str += s[k];
			}

			if (str == comp_str)
				count++;
			else {
				if (count == 1) {
					sen += str;
					if (flag == 1)
						sen += comp_str;
				}
				else {
					sen += to_string(count);
					sen += str;
					count = 1;
					if (flag == 1)
						sen += comp_str;
				}
			}
		}
		cout << sen << endl;
		if (min > sen.length())
			min = sen.length();
	}
	return min;
}

int main() {
	string s = "ababcdcdababcdcd";

	cout << solution(s) << endl;
}