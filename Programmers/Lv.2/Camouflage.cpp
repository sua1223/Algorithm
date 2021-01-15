#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<string> kind;
int find_cloth(string k) {
	for (int i = 0; i < kind.size(); i++) {
		if (kind[i] == k)
			return i;
	}
	return -1;
}
int solution(vector<vector<string>> clothes) {
	vector<int> count;
	for (int i = 0; i < clothes.size(); i++) {
		string k = clothes[i][1];
		int idx = find_cloth(k);
		if (idx == -1) {
			count.push_back(1);
			kind.push_back(k);
		}
		else
			count[idx]++;
	}

	if (count.size() == 1)
		return clothes.size();

	int n = 1;
	for (int i = 0; i < count.size(); i++) {
		n *= count[i]+1;
	}

	return n-1;
}

int main() {
	vector<vector<string>> clothes = { {"yellow_hat", "headgear"},{"blue_sunglasses", "eyewear"},{"green_turban", "headgear"} };

	cout << solution(clothes)<<endl;
}