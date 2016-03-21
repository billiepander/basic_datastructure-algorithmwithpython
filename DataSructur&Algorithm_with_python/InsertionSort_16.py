#coding:utf-8
"""
The insertion sort, although still O(n^2), works in a slightly different way. It always maintains
a sorted sublist in the lower positions of the list. Each new item is then “inserted” back into the
previous sublist such that the sorted sublist is one item larger.
"""
def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:        #从目前元素开始向前，若>目前值就后移一位
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(a)
print(a)