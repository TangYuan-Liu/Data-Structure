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
