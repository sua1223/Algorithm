#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solution(string skill, vector<string> skill_trees) {

	int answer = 0;

	vector<int> s;
	vector<int> sk;

	for (int i = 0; i < skill_trees.size(); i++) {
		string comp = skill_trees[i];
		for (int k = 0; k < skill.length(); k++) {
			for (int j = 0; j < comp.length(); j++) {
				if (skill[k] == comp[j]) {
					s.push_back(j);
					sk.push_back(k);
					break;
				}
			}
		}
		if (sk.size() == 0)
			answer++;
		else if(sk.size() == 1 && sk[0] == 0)
			answer++;
		else if(sk[0]==0){
			int count = 0;
			for(int a = 0; a < sk.size()-1; a++) {
				if (sk[a + 1]-1 == sk[a])
					count++;
			}
			if (count == sk.size() - 1) {
				count = 0;
				for (int b = 0; b < s.size() - 1; b++) {
					if (s[b] > s[b + 1])
						break;
					else
						count++;
				}
			}
			if (count == s.size() - 1)
				answer++;
		}
		s.clear();
		sk.clear();
	}
	return answer;
}

int main() {
	string skill = "CBD";
	vector<string> skill_trees= {  "BDA","AECB", "BACDE" ,"CBADF"};
	cout << solution(skill, skill_trees) << endl;
}