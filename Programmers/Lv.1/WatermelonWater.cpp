#include <iostream>
#include <string>
using namespace std;

string solution(int n) {

	string answer = "";

	for (int i = 0; i < (n / 2); i++)
		answer += "����";

	if (n % 2 == 1)
		answer += "��";
	return answer;
}

int main() {
	cout << solution(3) << endl;
	cout << solution(4) << endl;
}