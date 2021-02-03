#include <iostream>
#include<string>
#include <stack>
using namespace std;

int solution(string s)
{
	stack<char> str;
	str.push(s[0]);

	for (int i = 1; i < s.length(); i++) {
		if (!str.empty()&&str.top() == s[i])
			str.pop();
		else
			str.push(s[i]);
	}

	if (str.empty())
		return 1;
	else
		return 0;
}

int main() {
	cout << solution("baabaa") << endl;
	cout << solution("cdcd") << endl;
}