#This is a basic implement of heap
#完全二叉树使用数组进行存储
#guard是哨兵元素，是list[0]，用来辅助树的调整
#删除过程个人认为教材上有错误，所以按照自己的思路进行了改动。parent指向的是刚刚调整为list[0]的原list[-1]最终要放的位置。
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
    def delete(self):
        if(self.size == 0):
            print("Heap is empty")
            return
        maxitem = self.list[1]
        temp = self.list[-1]
        self.size -= 1

        parent = 1
        while(parent*2<self.size):
            child = 2*parent
            if(child != self.size and (self.list[child] < self.list[child+1])):
                child += 1
            if(temp >= self.list[child]):
               break
            else:
               self.list[parent] =self.list[child]

            parent = child

        if(self.size == 2):
            if(self.list[1] > self.list[2]):
                return
            else:
                parent = 2
        """
        if(self.size == 1):
            parent = 1
        """
        self.list[parent] = temp
        self.list = self.list[0:self.size+1]
            
     
    def output(self):
        print self.list
        
    def buildheap(self):
        print("Please input the series (Seperate with blank)")
        series = raw_input()
        series = series.split()
        if(len(series) > self.capa):
            print("Capacity exceeded")
            return

        for i in range(len(series)):
            self.list.append(int(series[i]))

        self.size = len(series)

        i = self.size/2
        while(i>0):
            self.adjust(i)
            i -= 1

    def adjust(self,i):
        x = self.list[i]
        parent = i
        while(parent*2<self.size):
            child = 2*parent
            if(child != self.size and (self.list[child] < self.list[child+1])):
                child += 1
            if(x >= self.list[child]):
               break
            else:
               self.list[parent] =self.list[child]

            parent = child

        if(parent*2 == self.size):
            if(self.list[parent] > self.list[parent*2]):
                return
            else:
                parent = parent*2

        self.list[parent] = x
