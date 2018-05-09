#This is a basic implement of heap
#完全二叉树使用数组进行存储
#guard是哨兵元素，是list[0]，用来辅助树的调整
class MaxHeap:
    def __init__(self,capacity,guard):
        self.list = []
        self.size = 0
        self.capa = capacity
        self.list.append(guard)

    def insert(self,value):
        if(self.size == self.capa):
            print("Heap is full")
            return
        self.list.append(value)
        self.size += 1
        current = self.size
        while(self.list[current] > self.list[current/2]):
            self.list[current] = self.list[current/2]
            self.list[current/2] = value
            current = current/2

    def output(self):
        print self.list
