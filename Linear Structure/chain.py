#单向链表python实现
"""
Python is totally different compared with C. Without using address, python use
objection.
"""
class node:
    value = None;
    next_node = None;
    def __init__(self, item):
        self.value = item

class ListHead:
    head = None
    rear = None
    size = 0
    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

def insert(self,value):
    temp = node(value)
    if(self.head == None):
        self.head = temp
        self.rear = temp
        self.rear.next_node = None
        self.size += 1
    else:
        self.rear.next_node = temp
        self.rear = temp

def delete(self, value):
    if(self.head == None):
        print("The list is empty so you cannot delete")
        return
    else:
        if(self.head.value == value):
            temp = self.head
            self.head = self.head.next_node
            temp = None
            self.size -= 1
        else:
            temp = self.head
            pre = self.head
            while( temp != None and temp.value != value):
                pre = temp
                temp = temp.next_node
            if(temp == None):
                print("No such value in the list")
            else:
                pre.next_node = temp.next_node
                temp = None
                self.size -= 1

def list_print(self):
    temp = self.head
    if(self.head == None):
        print("List is empty")
    else:
        while(temp != None):
            print (str(temp.value) + "->")
            temp = temp.next_node

    print("END")

if __name__ == '__main__':
    print("You want start? yes(1) no(0)")
    flag = raw_input()
    head = ListHead()
    while(flag == '1'):
        print("Insert(1) or Delete(0)?")
        flag2 = raw_input()
        if(flag2 == '1'):
            print("Input the value you want insert")
            value = raw_input()
            value = int(value)
            insert(head,value)
        else:
            print("Input the value you want delete")
            value = raw_input()
            value = int(value)
            delete(head,value)
        list_print(head)
        print("Continue? yes(1) no(0)")
        flag = raw_input()
