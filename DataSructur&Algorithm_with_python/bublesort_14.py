#A bubble sort is often considered the most inefficient sorting method since it must exchange
#items before the final location is known.
def Bublesort(seq):
    i = 0
    j = 0
    while i < len(seq):
        while j < len(seq)-i-1:
            if seq[j] > seq[j+1]:
                seq[j],seq[j+1] = seq[j+1],seq[j]
            else:
                j+=1
        j=0
        i+=1

a=[3,4,6,2,1]
Bublesort(a)
print(a)

