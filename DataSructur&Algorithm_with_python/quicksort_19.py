import random
def partition(seq, start, stop):
    pivotIndex = start
    pivot = seq[pivotIndex]
    i = start+1
    j = stop-1 
    while i <= j:
        while pivot > seq[i]:
            i+=1
        while pivot < seq[j]:
            j-=1
        if i < j:
            seq[j],seq[i] = seq[i],seq[j]
            i+=1
            j-=1
    seq[pivotIndex],seq[j] = seq[j],pivot
    return j

def quicksortRecursively(seq, start, stop):
    if start >= stop-1:
        return
    pivotIndex = partition(seq, start, stop)
    quicksortRecursively(seq, start, pivotIndex)
    quicksortRecursively(seq, pivotIndex+1, stop)

def quicksort(seq):
# randomize the sequence first
    for i in range(len(seq)):
        j = random.randint(0,len(seq)-1)
        seq[i],seq[j] = seq[j],seq[i]

    quicksortRecursively(seq, 0, len(seq))

a=[3,4,6,8,2,1,5,9]
quicksort(a)
print(a)