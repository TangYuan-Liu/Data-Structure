#分治法的具体应用
"""
机械工业出版社出版的Fundamentals of Data Structure上关于快速排序的算法有错误，具体问题是扫描每个值时，应添加数组越界判断条件。
"""

import os

def QuickSort(seq,left,right):
    if(left > right):
        return
    key = seq[left]
    i = left+1
    j = right
    
    while(i<j):
        #Not only scan the value one by one, but also remember to check the i<=right and j>=left
        while(i<=right and seq[i]<key):
            i+=1
            print i
        while(j>=left and seq[j]>key):
            j-=1
            print j
        if(i<j):
            swap(seq,i,j)
    swap(seq,left,j)
    QuickSort(seq,left,j-1)
    QuickSort(seq,j+1,right)

def swap(seq,num1,num2):
    temp = seq[num1]
    seq[num1] = seq[num2]
    seq[num2] = temp

def char2num(seq):
    numlist = []
    for i in range(len(seq)):
        numlist.append(int(seq[i]))
    return numlist
if __name__ == "__main__":
    print("This is a QuickSort program")
    print("Please input the series:")
    seq = raw_input()
    seq = char2num(seq)
    print seq
    count = len(seq)-1
    QuickSort(seq,0,count)
    print seq
