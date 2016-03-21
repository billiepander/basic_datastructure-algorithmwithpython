def partition(seq, start, mid, stop):
    lst = []
    i = start
    j = mid
    while i < mid and j < stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i+=1
        else:
            lst.append(seq[j])
            j+=1
    while i < mid:
        lst.append(seq[i])
        i+=1
    while j < stop:
        lst.append(seq[j])
        j+=1
    for i in range(len(lst)):
        seq[start+i]=lst[i]

def mergeSortRecursively(seq, start, stop):
    if start >= stop-1:
        return
    mid = (start + stop) // 2
    mergeSortRecursively(seq, start, mid)
    mergeSortRecursively(seq, mid, stop)
    partition(seq, start, mid, stop)

a=[3,4,6,8,2,1,5,9]
mergeSortRecursively(a, 0, len(a))
print(a)