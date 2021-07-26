#include <iostream>
using namespace std;

typedef struct node {
	int data;
	int num;
	struct node* llink;
	struct node* rlink;
};
node *head = NULL;
int flag = 0;

void insertNode(node **head, int data, int num) {
	node* new_node = new node;
	new_node->data = data;
	new_node->num = num;
	if (*head == NULL) {
		*head = new_node;
		new_node->rlink = *head;
		new_node->llink = *head;
	}
	else {
		node* tail = *head;
		tail->llink = new_node;
		while (tail->rlink != *head)
			tail = tail->rlink;
		tail->rlink = new_node;
		new_node->llink = tail;
		new_node->rlink = *head;
	}
}

void balloon(int n,int num) {
	node* find_node = head;
	for (int j = 0; j < n-1; j++) {
		cout << " ";
		if (flag==1||num < 0) {
			if(flag==0)
				num *= -1;
			flag = 0;
			for (int i = 0; i < num; i++) {
				find_node = find_node->llink;
			}
		}
		else {
			for (int i = 0; i < num; i++) {
				find_node = find_node->rlink;
			}
		}
		cout << find_node->num;
		num = find_node->data;
		find_node->llink->rlink = find_node->rlink;
		find_node->rlink->llink = find_node->llink;
	}
}

int main() {
	int n;
	cin >> n;

	int k,first;
	cin >> first;
	cout << 1;

	for (int i = 2; i <= n; i++) {
		cin >> k;
		insertNode(&head, k, i);
	}

	if (first < 0) {
		first *= -1;
		flag = 1;
	}
	else
		first -= 1;
		
	balloon(n,first);
}