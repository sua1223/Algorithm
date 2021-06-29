#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, a;
	vector <int> A;
	vector <int> B;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> a;
		A.push_back(a);
	} 
	
	int idx;
	for (int i = 0; i < A.size()-1; i++) {
		idx = A.size() - 1;
		for (int j = i; j < A.size(); j++) {
			if (A[i] < A[j]) {
				if (idx > j) {
					idx = j;
				}
			}
		}
		B.push_back(idx);
	}

	for (int i = 0; i < B.size(); i++) {
		cout << B[i] << " ";
	}
}