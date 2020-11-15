#include <string>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int answer = 1;
	int bridge_weight = weight;
	queue<int> wait_truck;
	queue<int> bridge_truck;

	for (int i = 0; i < truck_weights.size(); i++) {
		wait_truck.push(truck_weights[i]);
	}

	vector<int> len;

	bridge_weight -= wait_truck.front();
	len.push_back(bridge_length);
	bridge_truck.push(wait_truck.front());
	wait_truck.pop();

	while (!bridge_truck.empty()) {
		for (int i = 0; i < len.size(); i++) {
			len[i]--;
			if (len[i] == 0) {
				bridge_weight += bridge_truck.front();
				bridge_truck.pop();
				continue;
			}
		}
		if (!wait_truck.empty() && wait_truck.front() <= bridge_weight) {
			bridge_weight -= wait_truck.front();
			len.push_back(bridge_length);
			bridge_truck.push(wait_truck.front());
			wait_truck.pop();
		}
		answer++;
	}

	return answer;
}

int main() {
	int bridge_length = 100;
	int weight = 100;
	vector<int> truck_weights = { 10,10,10,10,10,10,10,10,10,10 };

	cout << solution(bridge_length, weight, truck_weights) << endl;
}