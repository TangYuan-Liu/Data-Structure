#二叉查找树
#尾递归均可用循环来实现
#搜索任意值、插入、删除、搜索最大值、搜索最小值
#Binary Search Tree
import TreeLayerTraversal as TL

def CreateTree(head):
    flag = None
    print("Start to Create? Yes(1) No(0)")
    flag = raw_input()
    while(flag == '1'):
        print("Please input the value")
        temp = int(raw_input())
        NodePointer = head
        NodePointerParent = head
        if(head.value == None):
            head.value = temp
        else:
            while(NodePointer != None):
                if(NodePointer.value >= temp):
                    NodePointerParent = NodePointer
                    NodePointer = NodePointer.left
                else:
                    NodePointerParent = NodePointer
                    NodePointer = NodePointer.right
                    
            NewNode = TL.tree_node(temp)
            if(NodePointerParent.value >= temp):
                NodePointerParent.left = NewNode
            else:
                NodePointerParent.right = NewNode
        print("Continue? Yes(1) No(0)")
        flag = raw_input()

def FindMin(head):
    if(head.value == None):
        return None
    else:
        temp = head.value
        NodePoint = head
        
        while(NodePoint.left != None):
            NodePoint = NodePoint.left 
        return NodePoint

def DeleteNode(head,value):
    if(head.value == None):
        print("Can't find the node")
        return head
    else:
        if(value > head.value):
            head.right = DeleteNode(head.right,value)
        else:
            if(value < head.value):
                head.left = DeleteNode(head.left,value)
            else:
                if(head.left != None and head.right != None):
                    temp = FindMin(head.right)
                    head.value = temp.value
                    head.right = DeleteNode(head.right,temp.value)
                else:
                    if(head.left == None):
                        head = head.right
                    else:
                        head = head.left
        return head

def RunDelete(head):
    print("Start Delete? Yes(1) No(0)")
    flag = raw_input()
    while(flag == '1'):
        print("Input the node you want delete")
        temp = int(raw_input())
        DeleteNode(head,temp)
        print("Continue? Yes(1) No(0)")
        flag = raw_input()

if __name__ == "__main__":
    head = TL.tree_node(None)
    CreateTree(head)
    TL.output_tree(head)
    RunDelete(head)
    TL.output_tree(head)
