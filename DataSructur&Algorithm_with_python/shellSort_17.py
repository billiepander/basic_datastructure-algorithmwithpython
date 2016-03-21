#coding:utf-8
#http://www.cnblogs.com/huangxincheng/archive/2011/11/20/2255695.html
"""
希尔排序：
增量的取法：
      第一次增量的取法为： d = (count+1)/2;
      第二次增量的取法为:  d = (count/2)/2;
             最后一直到:   d=1;
每次取出来的所有值相当于一个新集合，对这个集合采取insertion sort
"""
def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is",a_list)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list,start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)