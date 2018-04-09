# -*- coding: utf-8 -*-
"""
This is a layer search achieve using python
"""

class tree_node:
    value = None
    left = None
    right = None
    def __init__(self,item):
        self.value = item
        self.right = None
        self.right = None

def create_tree(head):
    
    print("请按提示构建树")
    print("开始构建树？Yes(1) No(0)")
    flag = raw_input()
    queue = []
    temp = 0
    head.value = None
    while(flag == '1'):
        if(head.value == None):
            print("请输入根节点的值")
            item = raw_input()
            head.value = int(item)
            queue.append(head)
        else:
            print("需要为节点%d添加叶子节点吗？Yes(1) No(0)" % queue[0].value)
            flag = raw_input()
            if(flag == '1'):
                print("需要添加左孩子吗？Yes(1) No(0)")
                flag = raw_input()
                if(flag == '1'):
                    print("输入左孩子的值")
                    temp = int(raw_input())
                    child = tree_node(temp)
                    queue[0].left = child
                    queue.append(child)
                print("需要添加右孩子吗？Yes(1) No(0)")
                flag = raw_input()
                if(flag == '1'):
                    print("输入右孩子的值")
                    temp = int(raw_input())
                    child = tree_node(temp)
                    queue[0].right = child
                    queue.append(child)
                queue = queue[1:]
            else:
                queue = queue[1:]
        print("Continue?Yes(1) No(0)")
        flag = raw_input()

def output_tree(head):
    print("The tree is:")
    queue = []
    queue.append(head)
    while(len(queue) != 0):
        print queue[0].value
        if(queue[0].left != None):
            queue.append(queue[0].left)
        if(queue[0].right != None):
            queue.append(queue[0].right)
        queue = queue[1:]


if __name__ == "__main__":
    head = tree_node(1)
    create_tree(head)
    output_tree(head)
