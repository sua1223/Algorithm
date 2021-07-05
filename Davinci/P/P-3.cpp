#include <iostream>
#include <vector>

using namespace std;

int main() {
	int x, y;
	cin >> x >> y;

	int a;
	vector <vector<int>> arr;
	vector <int> arr_;
	vector <pair<int, int>> two;

	for (int i = 0; i < x; i++) {
		for (int j = 0; j < y; j++) {
			cin >> a;
			arr_.push_back(a);
			if (a == 2)
				two.push_back(make_pair(i, j));
		}
		arr.push_back(arr_);
		arr_.clear();
	}

	int n;
	cin >> n;

	int min = 10000;
	int sum = 0;
	int flag;
	for (int i = 0; i <= x-n; i++) {
		for (int j = 0; j <= y-n; j++) {
			flag = 0;
			for (int z = 0; z < two.size(); z++) {
				if (i <= two[z].first && i + 2 >= two[z].first && j <= two[z].second && j >= two[z].second) {
					flag = 1;
					break;
				}
			}
			if(flag==0){
				int sum = 0;
				for (int a = i; a < i+n; a++) {
					for (int b = j; b < j + n; b++) {
						sum += arr[a][b];
					}
				}
				if (min > sum)
					min = sum;
			}
		}
	}

	if (min == 10000)
		cout << "-1" << endl;
	else
		cout << min << endl;


}