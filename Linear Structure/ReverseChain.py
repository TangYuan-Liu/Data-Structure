"""
本程序完成一个朴素的链表反转操作
"""
import chain

def create_chain(head):
    print("Strat create chain? Yes(1) No(0)")
    flag = raw_input()
    while(flag == '1'):
        print("Input value")
        temp = int(raw_input())
        chain.insert(head,temp)
        print("Continue? Yes(1) No(0)")
        flag = raw_input()

def reverse_chain(head):
    pre_head = head.head
    pre_rear = head.rear
    old = head.head
    middle = old.next_node
    new = middle.next_node

    while(new.next_node != None):
        middle.next_node = old
        old = middle
        middle = new
        new = new.next_node

    middle.next_node = old
    new.next_node = middle

    head.head = pre_rear
    head.rear = pre_head
    pre_head.next_node = None

if __name__ == "__main__":
    head = chain.ListHead()
    create_chain(head)
    reverse_chain(head)
    chain.list_print(head)
