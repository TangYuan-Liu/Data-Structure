#冒泡排序
"""
冒泡排序对于以链表形式存储的待排序元素有着很好的处理表现
在冒泡排序添加了flag，可及时中断已排好序的情况
"""

def swap(i,j,a):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp



def bubble_sort(data):

    for i in range(len(data)-1):
        end = len(data)-i
        flag = 0
        for j in range(end-1):
            if(data[j]>data[j+1]):
                flag += 1
                swap(j,j+1,data)

        if(flag == 0):
            break

            
#插入排序
"""
课程视频中的插入排序算法有问题，如下进行了一些修改。
"""
def insert_sort(a):
    length = len(a)
    newlist = a
    for i in range(1,len(a)):
        temp = a[i]
        flag = 0
        for j in range(i):
            if(temp<a[i-j-1]):
               newlist[i-j] = newlist[i-j-1]
               #print newlist
            else:
               flag = 1
               break
        if(flag == 0):
            newlist[i-j-1] = temp
        else:
            newlist[i-j] = temp
    return newlist 
