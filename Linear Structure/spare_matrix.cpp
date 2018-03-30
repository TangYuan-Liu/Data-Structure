/*
完成一个稀疏矩阵的基本操作
*/

#include<iostream>
using namespace std;

#define max_size 100
/*
入口节点和项节点是一致的，头结点结构稍微简单些
*/

typedef enum {head,entry} tagfiled;
typedef struct martrix_node *matrix_pointer;
typedef struct entry_node{
	int col;
	int row;
	int value;
};

typedef struct martrix_node{
	matrix_pointer right;
	matrix_pointer down;
	tagfiled tag;
    /*以上是两种节点相同的地方*/
	union{
		matrix_pointer next;
		entry_node entry;
	} u;
};

matrix_pointer hdnode[max_size];

//获得一个新的节点
matrix_pointer new_node(){
	matrix_pointer temp;
	temp = (matrix_pointer)malloc(sizeof(martrix_node));
	return temp;
}

//读取一个稀疏矩阵
matrix_pointer mread(){
	printf("请在提示下输入一个矩阵\n");
	int num_row, num_col, num_term, num_head;
	matrix_pointer node, temp, last;
	int row, col, value, current_row;
	printf("请输入矩阵行、列、非空节点数");
	scanf("%d%d%d",&num_row, &num_col, &num_term);
	num_head = (num_col > num_row) ? num_col : num_row;
	//为稀疏矩阵添加入口节点，并将矩阵大小存入
	node = new_node();
	node ->u.entry.row = num_row;
	node ->u.entry.col = num_col;
	//初始化所有的head节点
	if(!num_head){
		node ->right = node;
	}
	else{
		for(int i=0; i<num_head; i++){
			temp = new_node();
			hdnode[i] = temp;
			hdnode[i] -> tag = head; 
			hdnode[i] -> right = temp;
			hdnode[i] -> u.next = temp;
		}
		current_row = 0;
		last = hdnode[0];
		for(int i=0; i<num_term;i++){
			printf("请输入行、列、值\n");
			scanf("%d%d%d",&row, &col, &value);
			if(row > current_row){
				last ->right = hdnode[current_row];
				current_row = row;
				last = hdnode[row];
			}
			temp = new_node();
			temp -> tag = entry;
			temp -> u.entry.row = row;
			temp -> u.entry.col = col;
			temp -> u.entry.value = value;
			last -> right = temp;
			last = temp;
			//链入列链表
			hdnode[col] -> u.next ->down = temp;
			hdnode[col] -> u.next = temp;
		}
		//关闭最后一行
		last -> right = hdnode[current_row];
		//关闭所有列
		for(int i=0; i < num_col; i++)
			hdnode[i] ->u.next->down = hdnode[i];
		//将所有节点连起来
			for(int i=0; i<num_head-1; i++)
				hdnode[i] ->u.next = hdnode[i+1];
			hdnode[num_head-1] ->u.next = node;
			node -> right = hdnode[0];
	}
	return node;
}


void main(){
	mread();
}
