#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class compare {
public:
	bool operator() (int a, int b)const {
		int a_, b_;

		if (a < 0) a_ = a * -1;
		else a_ = a;
		if (b < 0) b_ = b * -1;
		else b_ = b;

		if (a_ > b_) return true;
		else if (a_ == b_) return a > b;
		else return false;
	}
};

int main() {
	int n;
	cin >> n;
	priority_queue< int, vector<int>, compare > pq;
	queue <int> result;

	int a,b;
	for (int i = 0; i < n; i++) {
		cin >> a;
		if (a != 0) {
			pq.push(a);
		}
		else {
			if (pq.empty())
				result.push(0);
			else {
				result.push(pq.top());
				pq.pop();
			}
		}
	}

	while (!result.empty()) {
		cout << result.front()<< endl;
		result.pop();
	}
}