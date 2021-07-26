#include <iostream>
using namespace std;

typedef struct node {
	int data;
	struct node* link;
};
node *head = NULL;
node *tail = NULL;

void insertNode(node **head, int data) {
	node* new_node = new node;
	new_node->data = data;
	if (*head == NULL) {
		*head = new_node;
		new_node->link = *head;
	}
	else {
		node* tail = *head;
		while (tail->link != *head)
			tail = tail->link;
		tail->link = new_node;
		new_node->link = *head;
	}
	tail = new_node;
}

void findK(int n,int k) {
	node* find_node = tail;
	node* now_node = NULL;
	cout << "<";
	for (int j = 0; j < n; j++) {
		if (j > 0)
			cout << ", ";
		for (int i = 0; i < k; i++) {
			now_node = find_node;
			find_node = find_node->link;
		}
		now_node->link = find_node->link;
		cout << find_node->data;
	}
	cout<<">";
}

int main() {
	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		insertNode(&head, i);
	}

	int k;
	cin >> k;
	findK(n,k);
}