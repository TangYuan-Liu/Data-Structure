#This is a stack

class node:
    def __init__(self,value):
        self.value = value
        self.next_node = None

def push_stack(head,value):
    if(head.next_node == None):
        head.next_node = node(value)
    else:
        pre = head.next_node
        temp = node(value)
        head.next_node = temp
        temp.next_node = pre

def pop_stack(head):
    if(head.next_node == None):
        print("Stack Empty")
        return
    else:
        print("Pop:%d" %head.next_node.value)
        temp = head.next_node.next_node
        head.next_node = temp

def print_stack(head):
    if(head.next_node == None):
        print("Stack empty, cannot print")
    else:
        temp = head.next_node
        while(temp != None):
            print temp.value
            temp = temp.next_node

if __name__ == "__main__":
    print("This is a stack program")
    print("You want start? Yes(1) No(0)")
    flag = raw_input()
    head = node(None)
    while(flag == '1'):
        print("Push or Pop? Push(1) Pop(0)")
        flag = raw_input()
        if(flag == '1'):
            print("Input value you want push")
            value = int(raw_input())
            push_stack(head,value)
        else:
            pop_stack(head)

        print("Current stack is:")
        print_stack(head)
        print("Continue? Yes(1) No(0)")
        flag = raw_input()


            
