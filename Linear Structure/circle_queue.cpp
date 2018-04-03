//环形队列的根本问题在于n中状态去表达n+1种情况，解决方法1)设置一个size计数器 2)空一个
//取模运算(求余)完成环形队列的环形操作
//完成环形队列的顺序与链式存储两种实现
//普通队列
//head->|front|->node1->node2->node3...->noden
//      |rear |----------------------------^
#include<iostream>
using namespace std;

#define maxsize 10
#define ElementType int
/****************************普通队列******************************/
//节点类
struct node{
	ElementType value;
	node* next;
};
//队列指针类
struct Qnode{
	node* front;
	node* rear;
};

Qnode* _init_(Qnode* head){
	head -> rear = NULL;
	head -> front = NULL;
	return head;
}

ElementType delete_queue(Qnode* head){
	node* FrontCell;
	ElementType DeleteValue;
	if(head->front == NULL){
		cout << "队列空\n";
		return 0;
	}
	else{
		FrontCell = head ->front;
		if(head->front == head->rear){
			head->front = head->rear = NULL;
		}
		else{
			head->front = FrontCell->next;
		}
	}
	DeleteValue = FrontCell->value;
	delete(FrontCell);
	return DeleteValue;
}

ElementType join_queue(Qnode* head){
	ElementType tempvalue;
	node* temp;
	cout << "请输入需要入队的值\n";
	cin >> tempvalue;
	temp = new node;
	if(head->rear == NULL){
		head->rear = temp;
		head ->front = temp;
		temp->value = tempvalue;
		temp->next = NULL;
	}
	else{
		temp -> next = NULL;
		temp -> value = tempvalue;
		head -> rear -> next = temp;
		head -> rear = temp;
	}
	
	return tempvalue;
}


void output_queue(Qnode* head){
	node* start;
	start = head -> front;
	if(head->front == NULL){
		return;
	}
	cout << "当前队列为:" << endl;
	while(start != NULL){
		cout << start->value << "->";
		start = start->next;
	}
	cout << "end" << endl;

}



int main(){
	Qnode* qhead;
	qhead = new Qnode;
	qhead = _init_(qhead);

	int flag1;
	int flag2;
	cout << "Queue Approach\n";
	cout << "You want start? yes(1) no(0)\n";
	cin >> flag1;
	while(flag1){
		cout << "Join(1) or Delete(0)?\n";
		cin >> flag2;
		(flag2 == 1) ? (join_queue(qhead)) : (delete_queue(qhead));
		output_queue(qhead);
		cout << "Continue? yes(1) no(0)\n";
		cin >> flag1;
	}
	return 0;
}
/*********************************************************************/
