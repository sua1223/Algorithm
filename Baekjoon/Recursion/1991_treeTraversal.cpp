#include <iostream>
#include <string>
#include <vector>

using namespace std;
vector<vector<char>> tree;

void preorder(char parent) {

	if (parent == '.') {
		return;
	}

	cout << tree[parent - 'A'][0];
	preorder(tree[parent - 'A'][1]);
	preorder(tree[parent - 'A'][2]);
}

void inorder(char parent) {

	if (parent == '.') {
		return;
	}

	inorder(tree[parent - 'A'][1]);
	cout << tree[parent - 'A'][0];
	inorder(tree[parent - 'A'][2]);
}

void postorder(char parent) {

	if (parent == '.') {
		return;
	}

	postorder(tree[parent - 'A'][1]);
	postorder(tree[parent - 'A'][2]);
	cout << tree[parent - 'A'][0];
}

int main() {
	
	int n;
	cin >> n;
	tree=vector<vector<char>>(n, vector<char>());

	char a, b, c;

	for (int i = 0; i < n; i++) {
		cin >> a >> b >> c;
		tree[a - 'A'].push_back(a); // parent
		tree[a - 'A'].push_back(b); // left_child
		tree[a - 'A'].push_back(c); // right_child
	}
	char root = 'A';

	preorder(root); cout << endl;
	inorder(root); cout << endl;
	postorder(root); cout << endl;
}