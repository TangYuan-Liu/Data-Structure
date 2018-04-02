//完成堆栈的操作(单个数组实现双堆栈)
//完成链栈，top为head(1->2->3->4....->n)
//                   ^
//                   |
//                   top(单向链表只能使用头结点作为top)
#include<iostream>
using namespace std;

#define ElementType int	
#define max_size 50
/*******************************************************/
//双栈结构体
struct Dstack{
		ElementType Stack[max_size];
		int top1;
		int top2;
	}s;

void array_pop(struct Dstack *ptr,int tag){
	if(tag == 0){
		if(ptr->top1 == -1){
			cout << "stack1 is empty\n";
			return;
		}
		else{
			ptr->top1 --;
		}
	}
	else{
		if(ptr->top2 == max_size){
			cout << "stack2 is empty\n";
			return;
		}
		else{
			ptr->top2 ++;
		}
	}

}

void array_push(struct Dstack *ptr,ElementType item, int tag){
	if((ptr->top2) - (ptr->top1) == 1){
		cout << "stacks are full\n";
		return;
		}
	if(tag == 0){
		ptr->Stack[++ptr->top1] = item;
	}
	else{
		ptr->Stack[++ptr->top2] = item;
	}
}

void array_approach(){
	
	s.top1 = -1;
	s.top2 = max_size;

	int data=0;
	int stack_num=2;
	int flag=2;
	int tag=2;
	cout << "You want start? Yes(1) No(0)\n";
	cin >> flag;
	while(flag != 0){
		cout << "push(0) or pop(1)?\n";
		cin >> tag;
		if(tag == 0){
			cout << "Input the push number\n";
			cin >> data;
			cout << "Which stack you want push?stack0(0) stack1(1)\n";
			cin >> tag;
			array_push(&s,data,stack_num);
		}
		else{
			cout << "Which stack you want pop?stack0(0) stack1(1)\n";
			cin >> tag;
			array_pop(&s,tag);
		}
		cout << "Continue? No(0) Yes(1)\n";
		cin >> flag;
	}
}
/*************************************************************/


struct SNode{
	ElementType value;
	SNode *Next;
};

SNode* create_stack(){
	SNode* s;
	s = new SNode;
	s -> Next = NULL;
	return s;
}



void chain_push(SNode* head){
	ElementType item;
	cout << "Please input the value\n";
	cin >> item;
	SNode* tmpcell;
	tmpcell = new SNode;
	tmpcell ->Next = head ->Next;
	head -> Next = tmpcell;
	tmpcell -> value = item;
}

void chain_pop(SNode* head){
	if(head->Next == NULL){
		cout << "栈已空\n";
		return;
	}
	else{
		SNode* tmppointer;
		tmppointer = head -> Next;
		head -> Next = head -> Next -> Next;
		delete(tmppointer);
	}

}

int chain_approach(){
	SNode* head;
	head = create_stack();
	int flag = 0;
	cout << "Do you want to start? yes(1) no(0)\n";
	cin >> flag;
	int opt = 2;
	while(flag){
		cout << "Push(1) or Pop(0)?\n ";
		cin >> opt;
		(opt == 1) ? chain_push(head) : chain_pop(head);
		cout << "Continue ? yes(1) no(0)\n";
		cin >> flag;
	}
	return 0;
}


int main(){
	int flag;
	cout << "Array Approach(0) or Chain Approach(1)?\n";
	cin >> flag;
	(flag == 0) ? array_approach() : chain_approach();
	return 0;
}
